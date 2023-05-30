from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, CallbackQueryHandler, MessageHandler, filters
import telegram
from telegram.constants import ParseMode
import os
import json
from dotenv import load_dotenv
from datetime import datetime
import time
import requests
import string
import asyncio

telegram.InlineKeyboardButton.MAX_CALLBACK_DATA = 128
# print(telegram.InlineKeyboardButton.MAX_CALLBACK_DATA)
load_dotenv()
ROOT_DIR = f'{os.sep}'.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep))
BOT_TOKEN = os.environ["BOT_TOKEN"]
RECIPIENTS = os.environ["RECIPIENTS"]
VISITOR_FILE = os.path.join(ROOT_DIR, 'src', 'visitors.json')
interactions_ids = {}
TITLE_ROUTES, MOVIE_TITLE, SELECTION, SHOW_TITLE, TV_SELECTION = range(5)
RADARR_KEY = "33addebd9a994a7eb70b71ef128aa6bd"
SONARR_KEY = "33a3824e00884aac92b5ed0d3e991229"
DELIMITER = 'AND'

## Validate if visitor file if there
if not os.path.isfile(VISITOR_FILE):
    print("CREATING VISITOR FILE...")
    with open(VISITOR_FILE, 'w') as fo:
        json.dump({}, fo, indent=2)


## Telegram Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user(update)
    await update.message.reply_text("Movie Manager Bot.\nUse /help to see available commands.")


async def _help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user(update)
    
    help_str = f"""
    /start -> Start interaction with the bot.
    /help -> Show this help message.

    /add_title -> Add a Movie/Tv-Shows to the queue.
    
    /list_movies -> List all the movies available.
    /movies_queue -> List the movies queue.
    
    /list_shows -> List all the Tv-Shows available.
    /shows_queue -> List the Tv-Shows queue.

    /misc_use
    """
    
    help_str = '\n'.join([s.strip() for s in help_str.split('\n')])
    help_str = "AVAILABE COMMANDS: \n" + help_str
    
    await update.message.reply_text(help_str)


async def list_movies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user(update)

    msg_str = ""

    await update.message.reply_text("Geting the movie list...")

    ## Get movies list
    try:
        url = f"http://localhost:7878/api/v3/movie?apikey={RADARR_KEY}"
        r = requests.get(url)
    except Exception as e:
        msg_str = f"REQUEST ERROR: {e}"
        await update.message.reply_text(msg_str)
        return 

    ## Check responce
    if r.status_code != 200:
        msg_str = f"RESPONCE ERROR: <{r.status_code}>"
        await update.message.reply_text(msg_str)
        return 
    
    ## Purse the movies
    movies = []
    for movie in r.json():
        movie_data = {}
        movie_data['title'] = movie['title']
        movie_data['available'] = movie['hasFile']
        movies.append(movie_data)
    
    ## Create the message string
    for i, movie in enumerate(movies):
        msg_str += f"{i+1:02}) {'✅' if movie['available'] else '❌'} {movie['title']}\n"
    
    msg_str = '\n'.join([s.strip() for s in msg_str.split('\n')])
    msg_str = "AVAILABE MOVIES: \n" + msg_str
    msg_str += "\n\n/help"

    await update.message.reply_text(msg_str)

async def movies_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user(update)

    msg_str = ""

    ## Get movies list
    try:
        url = f"http://localhost:7878/api/v3/queue?includeUnknownMovieItems=false&includeMovie=false&apikey={RADARR_KEY}&pageSize=100"
        r = requests.get(url)
    except Exception as e:
        msg_str = f"REQUEST ERROR: {e}"
        await update.message.reply_text(msg_str)
        return 

    ## Check responce
    if r.status_code != 200:
        msg_str = f"RESPONCE ERROR: <{r.status_code}>"
        await update.message.reply_text(msg_str)
        return 

    ## Purse the movies
    movies = []
    for movie in r.json()['records']:
        movie_data = {}
        movie_data['title'] = movie['title']
        movie_data['timeleft'] = movie['timeleft']
        movie_data['status'] = movie['status']
        movie_data['indexer'] = movie['indexer']
        movies.append(movie_data)
    
    ## Create the message string
    for i, movie in enumerate(movies):
        msg_str += f"{i+1}) {movie['title']} - ETA: {movie['timeleft']} ({movie['status']} :: {movie['indexer']})\n"
    
    msg_str = '\n\n'.join([s.strip() for s in msg_str.split('\n')])
    msg_str = "MOVIES DOWNLOAD QUEUE: \n" + msg_str
    msg_str += "\n/help"

    await update.message.reply_text(msg_str)


async def list_shows(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user(update)

    msg_str = ""

    await update.message.reply_text("Geting the shows list...")

    ## Get movies list
    try:
        url = f"http://localhost:8989/api/v3/series?apikey={SONARR_KEY}"
        r = requests.get(url)

        ## Check responce
        if r.status_code != 200:
            msg_str = f"RESPONCE ERROR: <{r.status_code}>"
            await update.message.reply_text(msg_str)
            return ConversationHandler.END

    except Exception as e:
        msg_str = f"REQUEST ERROR: {e}"
        await update.message.reply_text(msg_str)
        return ConversationHandler.END

    
    ## Purse the shows
    shows = r.json()
    # for show in r.json():
    #     show_data = {}
    #     show_data['title'] = show['title']
    #     # show_data['available'] = show['seasons']
    #     shows.append(show_data)
    
    ## Create the message string
    for i, show in enumerate(shows):

        status = ""
        # print(show)
        for season in show['seasons']:
            if season['seasonNumber'] != 0:
                if season['statistics']['episodeFileCount'] == season['statistics']['episodeCount']:
                    status += "✅"
                elif season['statistics']['episodeFileCount'] < season['statistics']['episodeCount'] and season['monitored']:
                    status += "⏳"
                elif not season['monitored']:
                    status += "🙅🏿‍♂️"
                else:
                    status += "🤷‍♂️"

        # msg_str += f"{i+1:02}) {'✅' if show['available'] else '❌'} {show['title']}\n"
        msg_str += f"{i+1:02}) {show['title']} {status}\n"
        # msg_str += f"{i+1:02}) {show['title']}\n"
    
    msg_str = '\n'.join([s.strip() for s in msg_str.split('\n')])
    msg_str = "AVAILABE TV SHOWS: \n" + msg_str
    msg_str += "\n\n/help"

    await update.message.reply_text(msg_str)

async def shows_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user(update)

    msg_str = ""

    ## Get shows list
    try:
        url = f"http://localhost:8989/api/v3/queue?includeUnknownSeriesItems=false&includeSeries=true&includeEpisode=true&apikey={SONARR_KEY}&pageSize=100"
        r = requests.get(url)

        ## Check responce
        if r.status_code != 200:
            msg_str = f"RESPONCE ERROR: <{r.status_code}>"
            await update.message.reply_text(msg_str)
            return ConversationHandler.END

    except Exception as e:
        msg_str = f"REQUEST ERROR: {e}"
        await update.message.reply_text(msg_str)
        return ConversationHandler.END

    ## Purse the shows
    shows = []
    for show in r.json()['records']:
        # print(json.dumps(show, indent=2))
        show_data = {}
        show_data['title'] = f"{show['series']['title']} S{show['episode']['seasonNumber']}E{show['episode']['episodeNumber']}"
        show_data['timeleft'] = "NA" if show.get('timeleft') is None else show.get('timeleft')
        show_data['status'] = show['status']
        show_data['indexer'] = show['indexer']
        shows.append(show_data)
    
    ## Create the message string
    for i, show in enumerate(shows):
        msg_str += f"{i+1}) {show['title']} - ETA: {show['timeleft']} ({show['status']} :: {show['indexer']})\n"
    
    msg_str = '\n\n'.join([s.strip() for s in msg_str.split('\n')])
    msg_str = "TV SHOWS DOWNLOAD QUEUE: \n\n" + msg_str
    msg_str += "\n/help"

    await update.message.reply_text(msg_str)


async def add_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user(update)

    keyboard = [
        [
            InlineKeyboardButton("Movie", callback_data=str("MOVIE")),
            InlineKeyboardButton("Tv-Show", callback_data=str("SHOW")),
            InlineKeyboardButton("Exit", callback_data=str("EXIT")),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text="What do you want to download?", reply_markup=reply_markup)
    return TITLE_ROUTES


async def ask_movie_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("ASK MOVIE TITLE")
    # log_user(update)

    query = update.callback_query
    await query.answer()
    
    await query.message.reply_text("Enter the title for the movie search... \n/exit")
    return MOVIE_TITLE

async def movie_search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    search_term = update.message.text
    await update.message.reply_text(
        text=f"⏳ Searching for {search_term}...", 
    )
    
    ## Search for the movie...
    try:
        url = f"http://localhost:7878/api/v3/movie/lookup?term={search_term}&apikey={RADARR_KEY}"
        r = requests.get(url)

        ## Check responce
        if r.status_code != 200:
            msg_str = f"SEARCH RESPONCE ERROR: <{r.status_code}>. Try Again\n/help"
            await update.message.reply_text(msg_str)
            return ConversationHandler.END

    except Exception as e:
        msg_str = f"SEARCH REQUEST ERROR: {e}. Try Again\n/help"
        await update.message.reply_text(msg_str)
        return ConversationHandler.END

    
    ## Purse the movies
    results = r.json()
    await update.message.reply_text(
        text=f"😀 Found {len(results)} results...", 
    )

    # print(json.dumps(r.json()))
    movies = []
    for movie in r.json():
        movie_data = {}
        movie_data['title'] = str(movie['title']).title()
        movie_data['year'] = movie['year']
        movie_data['hasFile'] = movie['hasFile']
        movie_data['tmdbId'] = movie['tmdbId']
        movie_data['imdbId'] = movie.get('imdbId')
        
        if movie_data['imdbId'] is not None:
            movies.append(movie_data)

        print(movie_data['title'])
    

    ## Create buttons with the titles
    keyboard = []
    for movie in movies:
        buttons = []
        str_data = f"{movie['tmdbId']} {DELIMITER} {movie['imdbId']}"
        x = InlineKeyboardButton(f"{'✅' if movie['hasFile'] else ''} {movie['title']} ({ movie['year']})", callback_data=str_data)
        buttons.append(x)
        keyboard.append(buttons)
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text="Choose The title you want to download. \n/exit", reply_markup=reply_markup)
    return SELECTION

async def confirfm_movie_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Confirm Selection")
    # log_user(update)

    query = update.callback_query
    await query.answer()

    tmdb_id, imdb_id = str(query.data).split(DELIMITER)
    tmdb_id = str(tmdb_id).strip()
    imdb_id = str(imdb_id).strip()
    
    ## Get the data from tvdb api
    await query.message.reply_text("Getting movie info...")
    try:
        end_point = f"https://imdb-api.com/en/API/Title/k_f01i69si/{imdb_id}"
        r = requests.get(end_point)
        print(f"Getting movie info: {end_point}")
        
        ## Check responce
        if r.status_code != 200:
            msg_str = f"RESPONCE ERROR: <{r.status_code}>\n\n/help"
            await query.message.reply_text(msg_str)
            return
        
        movie_data = r.json()

    except Exception as e:
        msg_str = f"REQUEST ERROR: {e}\n/help"
        await query.message.reply_text(msg_str)
        return 
    
    
    movie_title = movie_data['title']
    movie_id = int(tmdb_id)
    

    await query.message.reply_text(text=f"👍 Processing {movie_title} download...")
    print(movie_title, movie_id)

    ## Get movie info
    payload = {
        "QualityProfileId": 7,
        "tmdbId": movie_id,
        "Title": movie_title,
        "RootFolderPath": "D:\\Movies\\Movies",
        "Path": f"D:\\Movies\\Movies\\{movie_title}",
        "monitored": True,
        "addOptions": {
            "monitor": "movieOnly",
            "searchForMovie": True
        }
    }

    ## Send the post request
    try:
        end_point = f"http://localhost:7878/api/v3/movie?apikey={RADARR_KEY}"
        r = requests.post(end_point, json=payload)

        ## Check responce
        if r.status_code == 400:
            msg_str = f"SEND POST RESPONCE ERROR: <{r.status_code}> {r.json()[0]['errorMessage']}\n\n/help"
            await query.message.reply_text(msg_str)
            return
        
        elif r.status_code != 201:
            msg_str = f"SEND POST RESPONCE ERROR: <{r.status_code}>\n\n/help"
            await query.message.reply_text(msg_str)
            return

    except Exception as e:
        msg_str = f"SEND POST REQUEST EXCEPTION: {e}\n/help"
        await query.message.reply_text(msg_str)
        return 
    
    added_movie_data = r.json()
    reply_msg = f""" ✅ Successfully added: {added_movie_data['title']} ({added_movie_data['images'][0]['remoteUrl']})\n\n/help"""
    
    await send_alert(f"Started new download of {added_movie_data['title']}")
    await query.message.reply_text(reply_msg)
    return ConversationHandler.END


async def ask_show_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("ASK SHOW TITLE")
    # log_user(update)

    query = update.callback_query
    await query.answer()
    
    await query.message.reply_text("Enter the title for the tv show to search...")
    return SHOW_TITLE

async def show_search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    search_term = update.message.text
    await update.message.reply_text(
        text=f"⏳ Searching for {search_term}...", 
    )
    
    ## Search for the movie...
    try:
        url = f"http://localhost:8989/api/v3/series/lookup?term={search_term}&apikey={SONARR_KEY}"
        r = requests.get(url)
    except Exception as e:
        msg_str = f"REQUEST ERROR: {e}. Try Again\n/help"
        await update.message.reply_text(msg_str)
        return ConversationHandler.END

    ## Check responce
    if r.status_code != 200:
        msg_str = f"RESPONCE ERROR: <{r.status_code}>. Try Again\n/help"
        await update.message.reply_text(msg_str)
        return ConversationHandler.END
    
    ## Purse the shows
    results = r.json()
    await update.message.reply_text(
        text=f"😀 Found {len(results)} shows...",
    )

    # print(json.dumps(r.json()))
    shows = []
    for movie in r.json():
        show_data = {}
        show_data['title'] = str(movie['title']).translate(str.maketrans('', '', string.punctuation)).title()
        show_data['year'] = movie['year']
        show_data['hasFile'] = True if movie.get('id') else False
        show_data['tvdbId'] = movie['tvdbId']
        shows.append(show_data)

        print(show_data['title'], show_data['hasFile'])
    

    ## Create buttons with the titles
    keyboard = []
    for show in shows:
        buttons = []
        str_data = f"{show['tvdbId']}"
        x = InlineKeyboardButton(f"{'✅' if show['hasFile'] else ''} {show['title']} ({ show['year']})", callback_data=str_data)
        buttons.append(x)
        keyboard.append(buttons)
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text="Choose The title you want to download.", reply_markup=reply_markup)
    return TV_SELECTION

async def confirfm_tv_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Confirm show Selection")
    # log_user(update)

    query = update.callback_query
    await query.answer()

    show_id = int(query.data)
    msg_str = ""
    show_data = {}
    
    ## Get the data from tvdb api
    await query.message.reply_text("Getting show info...")
    try:
        end_point = f"https://api.thetvdb.com/series/{show_id}"
        r = requests.get(end_point)
        
        ## Check responce
        if r.status_code != 200:
            msg_str = f"RESPONCE ERROR: <{r.status_code}>\n\n/help"
            await query.message.reply_text(msg_str)
            return
        
        show_data = r.json()

    except Exception as e:
        msg_str = f"REQUEST ERROR: {e}\n/help"
        await query.message.reply_text(msg_str)
        return 
    
    
    show_title = show_data['data']['seriesName']
    show_id = show_data['data']['id']


    await query.message.reply_text(text=f"👍 Processing {show_title} download...")
    print(show_title, show_id)

    ## Get movie info
    payload = {
        "tvdbId": show_id,
        "Title": f"{show_title}",
        "QualityProfileId": 7,
        "LanguageProfileId": 1,
        "Path": f"D:\\Movies\\Series\\{show_title}",
        "RootFolderPath": "D:\\Movies\\Series",
        "monitored": True,
        "addOptions": {
            "monitor": "all",
            "searchForMissingEpisodes": True,
            "searchForCutoffUnmetEpisodes": True,
            "ignoreEpisodesWithFiles": False,
            "ignoreEpisodesWithoutFiles": False
        }
    }

    ## Send the post request
    try:
        end_point = f"http://localhost:8989/api/v3/series?apikey={SONARR_KEY}"
        r = requests.post(end_point, json=payload)

        ## Check responce
        if r.status_code != 201:
            msg_str = f"RESPONCE ERROR: <{r.status_code}>\n\n/help"
            await query.message.reply_text(msg_str)
            return

    except Exception as e:
        msg_str = f"REQUEST ERROR: {e}\n/help"
        await query.message.reply_text(msg_str)
        return 
    
    
    added_movie_data = r.json()
    reply_msg = f""" ✅ Successfully added: {added_movie_data['title']} ({added_movie_data['images'][0]['remoteUrl']})\n\n/help"""
    
    await send_alert(f"Started new download of {added_movie_data['title']}")
    await query.message.reply_text(reply_msg)
    return ConversationHandler.END


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


async def list_visitors(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user(update)

    with open(VISITOR_FILE) as fo: visitor_data = dict(json.load(fo))
    msg_str = ""
    i = 1
    for visitor_id, visitor in visitor_data.items():
        msg_str += f"{i}) {visitor['user_name']} on {datetime.fromtimestamp(visitor['timestamp']).strftime('%a, %b %d %Y @ %I:%M %p')} [ID: {visitor_id}]"
        i += 1
    
    msg_str = "VISITORS LIST: \n\n" + msg_str

    if update.message.from_user.id in json.loads(RECIPIENTS):
        await update.message.reply_text(text=msg_str)
    else:
        await update.message.reply_text(text="TEST OK")


async def send_alert(message):

    for user_id in json.loads(RECIPIENTS):
        print(f"SENDING TEXT TO : {user_id}")
        await telegram.Bot(BOT_TOKEN).send_message(chat_id=user_id, text=message)


## Utility Commands
def log_user(update: Update):
    
    interactions_ids[update.message.from_user.id] = {
        'user_name': update.message.from_user.username,
        'timestamp': time.time()
    }
    
    print(f"[{datetime.now()}] Interaction with bot from user: {update.message.from_user.username}")
    
    with open(os.path.join(ROOT_DIR, 'src', 'visitors.json'), 'w') as fo: json.dump(interactions_ids, fo, indent=2)



def run_bot():
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", _help))
    
    app.add_handler(CommandHandler("list_movies", list_movies))
    app.add_handler(CommandHandler("movies_queue", movies_queue))

    app.add_handler(CommandHandler("list_shows", list_shows))
    app.add_handler(CommandHandler("shows_queue", shows_queue))

    app.add_handler(CommandHandler("misc_use", list_visitors))


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("add_title", add_title)],
        states={
            TITLE_ROUTES: [
                CallbackQueryHandler(ask_movie_title, pattern="^" + "MOVIE" + "$"),
                CallbackQueryHandler(ask_show_title, pattern="^" + "SHOW" + "$"),
                CallbackQueryHandler(end, pattern="^" + "EXIT" + "$"),
                CommandHandler("exit", end)
            ],
            MOVIE_TITLE: [
                MessageHandler(filters.TEXT, movie_search),
                CommandHandler("exit", end)
            ],
            SELECTION: [
                CallbackQueryHandler(confirfm_movie_selection, pattern=".*"),
                # MessageHandler(filters.TEXT, confirfm_selection),
                CommandHandler("exit", end)
            ],
            SHOW_TITLE: [
                MessageHandler(filters.TEXT, show_search),
                CommandHandler("exit", end)
            ],
            TV_SELECTION: [
                CallbackQueryHandler(confirfm_tv_selection, pattern=".*"),
                CommandHandler("exit", end)
            ],
        },
        fallbacks=[CommandHandler("help", _help)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    app.add_handler(conv_handler)
    
    app.run_polling()
    



if __name__ == '__main__':
    run_bot()
    

