
import math
import json

data = [
    {
        "title": "Rick and Morty",
        "alternateTitles": [
            {
                "title": "Rick et Morty",
                "seasonNumber": -1
            },
            {
                "title": "Rick y Morty",
                "seasonNumber": -1
            },
            {
                "title": "Rick és Morty",
                "seasonNumber": -1
            },
            {
                "title": "Rick es Morty",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "rick and morty",
        "status": "continuing",
        "ended": False,
        "overview": "Follows the misadventures of an alcoholic scientist Rick and his overly nervous grandson Morty, who split their time between domestic family life and intergalactic travel. Often finding themselves in a heap of trouble that more often than not is created through their own actions.",
        "previousAiring": "2022-12-12T04:00:00Z",
        "network": "Adult Swim",
        "airTime": "23:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/4/banner.jpg?lastWrite=638059626812633729",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/275274-g8.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/4/poster.jpg?lastWrite=638059626835253481",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/275274-2.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/4/fanart.jpg?lastWrite=638059626866129301",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/275274-10.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 113,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 11,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 4,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 5,
                "monitored": False,
                "statistics": {
                    "previousAiring": "2021-09-06T03:23:00Z",
                    "episodeFileCount": 2,
                    "episodeCount": 2,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 833712954,
                    "releaseGroups": [
                        "BAE"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 6,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-12-12T04:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 5229912634,
                    "releaseGroups": [
                        "BAE",
                        "glhf",
                        "GLHF",
                        "KOGi",
                        "MiNX"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2013,
        "path": "D:/Movies/Series/Rick and Morty",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 23,
        "tvdbId": 275274,
        "tvRageId": 33381,
        "tvMazeId": 216,
        "firstAired": "2013-12-02T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "rickmorty",
        "imdbId": "tt2861424",
        "titleSlug": "rick-and-morty",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Adventure",
            "Animation",
            "Comedy",
            "Science Fiction"
        ],
        "tags": [],
        "added": "2022-12-06T22:31:19.5345583Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 6,
            "episodeFileCount": 12,
            "episodeCount": 12,
            "totalEpisodeCount": 174,
            "sizeOnDisk": 6063625588,
            "releaseGroups": [
                "BAE",
                "glhf",
                "GLHF",
                "KOGi",
                "MiNX"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 4
    },
    {
        "title": "Mr. Robot",
        "alternateTitles": [],
        "sortTitle": "mr robot",
        "status": "ended",
        "ended": True,
        "overview": "Elliot, a young programmer who works as a cyber-security engineer by day and a vigilante hacker by night. Elliot finds himself at a crossroads when the mysterious leader of an underground hacker group recruits him to destroy the corporation.",
        "previousAiring": "2019-12-23T03:50:00Z",
        "network": "USA Network",
        "airTime": "22:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/5/banner.jpg?lastWrite=638108385945934276",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/289590-g8.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/5/poster.jpg?lastWrite=638060068871368205",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/289590-12.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/5/fanart.jpg?lastWrite=638060068880252723",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/289590-18.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 3,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2015-09-03T02:00:00Z",
                    "episodeFileCount": 9,
                    "episodeCount": 9,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 2395793197,
                    "releaseGroups": [
                        "MULVAcoded"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2016-09-22T02:00:00Z",
                    "episodeFileCount": 12,
                    "episodeCount": 12,
                    "totalEpisodeCount": 12,
                    "sizeOnDisk": 3081946723,
                    "releaseGroups": [
                        "MULVAcoded"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2017-12-14T03:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 3164418145,
                    "releaseGroups": [
                        "AVS",
                        "BAMBOOZLE",
                        "GHETTO",
                        "KILLERS"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 4,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2019-12-23T03:50:00Z",
                    "episodeFileCount": 13,
                    "episodeCount": 13,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 3268577746,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2015,
        "path": "D:/Movies/Series/Mr. Robot",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 50,
        "tvdbId": 289590,
        "tvRageId": 42422,
        "tvMazeId": 1871,
        "firstAired": "2015-06-24T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "mrrobot",
        "imdbId": "tt4158110",
        "titleSlug": "mr-robot",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Crime",
            "Drama",
            "Thriller"
        ],
        "tags": [],
        "added": "2022-12-07T10:48:04.9274308Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 4,
            "episodeFileCount": 44,
            "episodeCount": 44,
            "totalEpisodeCount": 48,
            "sizeOnDisk": 11910735811,
            "releaseGroups": [
                "MULVAcoded",
                "AVS",
                "BAMBOOZLE",
                "GHETTO",
                "KILLERS",
                "GalaxyTV"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 5
    },
    {
        "title": "Atlanta",
        "alternateTitles": [],
        "sortTitle": "atlanta",
        "status": "ended",
        "ended": True,
        "overview": "Two cousins, with different views on art versus commerce, on their way up through the Atlanta rap scene; Earnest 'Earn' Marks, an ambitious college dropout and his estranged cousin, who suddenly becomes a star.",
        "previousAiring": "2022-11-11T03:00:00Z",
        "network": "FX",
        "airTime": "22:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/6/banner.jpg?lastWrite=638108385745500253",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/313999-g.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/6/poster.jpg?lastWrite=638060107740267503",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/313999-2.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/6/fanart.jpg?lastWrite=638108385790244115",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/313999-2.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 11,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 4,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-11-11T03:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 10571852903,
                    "releaseGroups": [
                        "cakes",
                        "GOSSIP",
                        "KOGi",
                        "NTb",
                        "plzproper"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2016,
        "path": "D:/Movies/Series/Atlanta",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 29,
        "tvdbId": 313999,
        "tvRageId": 0,
        "tvMazeId": 6508,
        "firstAired": "2016-09-06T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "atlanta",
        "imdbId": "tt4288182",
        "titleSlug": "atlanta",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Comedy",
            "Drama"
        ],
        "tags": [],
        "added": "2022-12-07T11:52:52.4635089Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 4,
            "episodeFileCount": 10,
            "episodeCount": 10,
            "totalEpisodeCount": 41,
            "sizeOnDisk": 10571852903,
            "releaseGroups": [
                "cakes",
                "GOSSIP",
                "KOGi",
                "NTb",
                "plzproper"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 6
    },
    {
        "title": "Halo",
        "alternateTitles": [],
        "sortTitle": "halo",
        "status": "continuing",
        "ended": False,
        "overview": "Depicting an epic 26th-century conflict between humanity and an alien threat known as the Covenant, the series weaves deeply drawn personal stories with action, adventure and a richly imagined vision of the future.",
        "previousAiring": "2022-05-19T07:00:00Z",
        "network": "Paramount+",
        "airTime": "03:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/7/banner.jpg?lastWrite=638060107874896264",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/366524/banners/621bce22c66c8.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/7/poster.jpg?lastWrite=638060107879896546",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/366524/posters/621558d61fc2d.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/7/fanart.jpg?lastWrite=638084606102975247",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/366524/backgrounds/62155bd98aba8.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 18,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-05-19T07:00:00Z",
                    "episodeFileCount": 5,
                    "episodeCount": 5,
                    "totalEpisodeCount": 9,
                    "sizeOnDisk": 1692884301,
                    "releaseGroups": [
                        "TORRENTGALAXY"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2022,
        "path": "D:/Movies/Series/Halo",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 51,
        "tvdbId": 366524,
        "tvRageId": 0,
        "tvMazeId": 35158,
        "firstAired": "2022-03-24T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "halo",
        "imdbId": "tt2934286",
        "titleSlug": "halo",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-14",
        "genres": [
            "Action",
            "Adventure",
            "Science Fiction",
            "Suspense",
            "War"
        ],
        "tags": [],
        "added": "2022-12-07T11:53:06.2324006Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 1,
            "episodeFileCount": 5,
            "episodeCount": 5,
            "totalEpisodeCount": 27,
            "sizeOnDisk": 1692884301,
            "releaseGroups": [
                "TORRENTGALAXY"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 7
    },
    {
        "title": "House of the Dragon",
        "alternateTitles": [
            {
                "title": "La casa del dragon",
                "seasonNumber": -1
            },
            {
                "title": "La Casa del Dragón",
                "seasonNumber": -1
            },
            {
                "title": "Game of Thrones: House of the Dragon",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "house of the dragon",
        "status": "continuing",
        "ended": False,
        "overview": "The story of House Targaryen, 200 years before the events of Game of Thrones.",
        "previousAiring": "2022-10-24T01:00:00Z",
        "network": "HBO",
        "airTime": "21:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/8/banner.jpg?lastWrite=638060108027794873",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/371572/banners/62b3c5840f88d.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/8/poster.jpg?lastWrite=638060108034131307",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/371572/posters/624838567e159.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/8/fanart.jpg?lastWrite=638060108042825934",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/371572/backgrounds/62d27eb474e3c.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 22,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-10-24T01:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 11807163831,
                    "releaseGroups": [
                        "cakes",
                        "EVO",
                        "MeGusta"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2022,
        "path": "D:/Movies/Series/House of the Dragon",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 62,
        "tvdbId": 371572,
        "tvRageId": 0,
        "tvMazeId": 44778,
        "firstAired": "2022-08-21T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "housedragon",
        "imdbId": "tt11198330",
        "titleSlug": "house-of-the-dragon",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Action",
            "Adventure",
            "Drama",
            "Fantasy",
            "War"
        ],
        "tags": [],
        "added": "2022-12-07T11:53:21.806238Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 1,
            "episodeFileCount": 10,
            "episodeCount": 10,
            "totalEpisodeCount": 32,
            "sizeOnDisk": 11807163831,
            "releaseGroups": [
                "cakes",
                "EVO",
                "MeGusta"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 8
    },
    {
        "title": "The Sopranos",
        "alternateTitles": [
            {
                "title": "Die Sopranos",
                "seasonNumber": -1
            },
            {
                "title": "Los Soprano",
                "seasonNumber": -1
            },
            {
                "title": "I Soprano",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "sopranos",
        "status": "ended",
        "ended": True,
        "overview": "New Jersey mob boss Tony Soprano deals with personal and professional issues in his home and business life that affect his mental state, leading him to seek professional psychiatric counseling.",
        "previousAiring": "2007-06-11T01:00:00Z",
        "network": "HBO",
        "airTime": "21:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/9/banner.jpg?lastWrite=638108386004328957",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/75299-g6.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/9/poster.jpg?lastWrite=638060109048723149",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/75299-17.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/9/fanart.jpg?lastWrite=638108386078906614",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/75299-13.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 5,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": False,
                "statistics": {
                    "previousAiring": "1999-04-05T01:00:00Z",
                    "episodeFileCount": 13,
                    "episodeCount": 13,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 6788311040,
                    "releaseGroups": [],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": False,
                "statistics": {
                    "previousAiring": "2000-04-10T01:00:00Z",
                    "episodeFileCount": 13,
                    "episodeCount": 13,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 4756856832,
                    "releaseGroups": [
                        "fucking-oo",
                        "Girl",
                        "Out"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": False,
                "statistics": {
                    "previousAiring": "2001-05-21T01:00:00Z",
                    "episodeFileCount": 13,
                    "episodeCount": 13,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 5012627456,
                    "releaseGroups": [],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 4,
                "monitored": False,
                "statistics": {
                    "previousAiring": "2002-12-09T02:00:00Z",
                    "episodeFileCount": 13,
                    "episodeCount": 13,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 5329412096,
                    "releaseGroups": [
                        "o-My"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 5,
                "monitored": False,
                "statistics": {
                    "previousAiring": "2004-06-07T01:00:00Z",
                    "episodeFileCount": 13,
                    "episodeCount": 13,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 4978919424,
                    "releaseGroups": [],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 6,
                "monitored": False,
                "statistics": {
                    "previousAiring": "2007-06-11T01:00:00Z",
                    "episodeFileCount": 21,
                    "episodeCount": 21,
                    "totalEpisodeCount": 21,
                    "sizeOnDisk": 7709709380,
                    "releaseGroups": [],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 1999,
        "path": "D:/Movies/Series/The Sopranos",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": False,
        "useSceneNumbering": False,
        "runtime": 54,
        "tvdbId": 75299,
        "tvRageId": 6206,
        "tvMazeId": 527,
        "firstAired": "1999-01-10T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "thesopranos",
        "imdbId": "tt0141842",
        "titleSlug": "the-sopranos",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Crime",
            "Drama"
        ],
        "tags": [],
        "added": "2022-12-07T11:55:03.0578805Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 6,
            "episodeFileCount": 86,
            "episodeCount": 86,
            "totalEpisodeCount": 91,
            "sizeOnDisk": 34575836228,
            "releaseGroups": [
                "fucking-oo",
                "Girl",
                "Out",
                "o-My"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 9
    },
    {
        "title": "Arcane",
        "alternateTitles": [
            {
                "title": "Arcane League of Legends",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "arcane",
        "status": "continuing",
        "ended": False,
        "overview": "Amid the stark discord of twin cities Piltover and Zaun, two sisters fight on rival sides of a war between magic technologies and clashing convictions.",
        "previousAiring": "2021-11-20T09:22:00Z",
        "network": "Netflix",
        "airTime": "03:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/10/banner.jpg?lastWrite=638060109225256160",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/371028/banners/615b5c31a0de7.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/10/poster.jpg?lastWrite=638060109240301453",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/371028/posters/617f6a8c59e8f.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/10/fanart.jpg?lastWrite=638060109245322130",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/5da773c1b3db3.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2021-11-20T09:22:00Z",
                    "episodeFileCount": 9,
                    "episodeCount": 9,
                    "totalEpisodeCount": 9,
                    "sizeOnDisk": 4238949757,
                    "releaseGroups": [
                        "HashMiner"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2021,
        "path": "D:/Movies/Series/Arcane",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 41,
        "tvdbId": 371028,
        "tvRageId": 0,
        "tvMazeId": 55138,
        "firstAired": "2021-11-06T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "arcane",
        "imdbId": "tt11126994",
        "titleSlug": "arcane",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-14",
        "genres": [
            "Action",
            "Adventure",
            "Animation",
            "Drama",
            "Fantasy",
            "Science Fiction"
        ],
        "tags": [],
        "added": "2022-12-07T11:55:20.4316985Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 1,
            "episodeFileCount": 9,
            "episodeCount": 9,
            "totalEpisodeCount": 9,
            "sizeOnDisk": 4238949757,
            "releaseGroups": [
                "HashMiner"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 10
    },
    {
        "title": "Baskets",
        "alternateTitles": [],
        "sortTitle": "baskets",
        "status": "ended",
        "ended": True,
        "overview": "In Bakersfield, California, Chip Baskets sets out on following his dream of becoming a professional clown. After failing to get a degree at a prestigious clowning school in Paris, he is stuck with a job at a local rodeo.",
        "previousAiring": "2019-08-23T02:00:00Z",
        "network": "FX",
        "airTime": "22:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/11/banner.jpg?lastWrite=638108385777980543",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/303069-g.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/11/poster.jpg?lastWrite=638060146414684008",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/303069-3.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/11/fanart.jpg?lastWrite=638108385879766607",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/303069-2.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2016-03-25T02:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 980742615,
                    "releaseGroups": [
                        "GWC"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2017-03-24T02:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 1876211213,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2018-03-28T02:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 4,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2019-08-23T02:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            }
        ],
        "year": 2016,
        "path": "D:/Movies/Series/Baskets",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 25,
        "tvdbId": 303069,
        "tvRageId": 0,
        "tvMazeId": 6741,
        "firstAired": "2016-01-21T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "baskets",
        "imdbId": "tt3468798",
        "titleSlug": "baskets",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Comedy",
            "Drama"
        ],
        "tags": [],
        "added": "2022-12-07T12:57:18.8481046Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 4,
            "episodeFileCount": 20,
            "episodeCount": 40,
            "totalEpisodeCount": 40,
            "sizeOnDisk": 2856953828,
            "releaseGroups": [
                "GWC",
                "GalaxyTV"
            ],
            "percentOfEpisodes": 50.0
        },
        "id": 11
    },
    {
        "title": "Breeders",
        "alternateTitles": [
            {
                "title": "Bendita Paciencia",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "breeders",
        "status": "continuing",
        "ended": False,
        "overview": "Paul and Ally juggle full-time careers, aging parents, a mortgage, upheavals in their relationship and the unenviable curveballs of parenting their young children, Luke and Ava — exploring the parental-paradox that it is possible, in the very same moment, to love your child to the horizon of the universe, while being apoplectically angry enough to want to send them there.",
        "previousAiring": "2022-07-12T02:00:00Z",
        "network": "FX",
        "airTime": "22:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/12/banner.jpg?lastWrite=638060146631566605",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/363777/banners/62100839.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/12/poster.jpg?lastWrite=638060146639365050",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/363777/posters/605e07b93c514.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/12/fanart.jpg?lastWrite=638060146672647548",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/363777/backgrounds/605e0703df29b.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2020-04-28T02:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 3227061939,
                    "releaseGroups": [
                        "btx",
                        "hillary",
                        "trump",
                        "xlf"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2021-05-18T02:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 3160571981,
                    "releaseGroups": [
                        "cakes",
                        "ggwp",
                        "MeGusta",
                        "PHOENiX",
                        "plzproper"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-07-12T02:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            }
        ],
        "year": 2020,
        "path": "D:/Movies/Series/Breeders",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 25,
        "tvdbId": 363777,
        "tvRageId": 0,
        "tvMazeId": 39113,
        "firstAired": "2020-03-02T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "breeders",
        "imdbId": "tt8129450",
        "titleSlug": "breeders",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Comedy",
            "Drama"
        ],
        "tags": [],
        "added": "2022-12-07T12:57:41.3013079Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 3,
            "episodeFileCount": 20,
            "episodeCount": 30,
            "totalEpisodeCount": 30,
            "sizeOnDisk": 6387633920,
            "releaseGroups": [
                "btx",
                "hillary",
                "trump",
                "xlf",
                "cakes",
                "ggwp",
                "MeGusta",
                "PHOENiX",
                "plzproper"
            ],
            "percentOfEpisodes": 66.666666666666666666666666670
        },
        "id": 12
    },
    {
        "title": "DAVE",
        "alternateTitles": [],
        "sortTitle": "dave",
        "status": "continuing",
        "ended": False,
        "overview": "A neurotic suburbanite in his mid-20s is convinced he’s destined to be one of the greatest rappers of all time. Now he has to prove it to everyone else.",
        "nextAiring": "2023-04-06T02:00:00Z",
        "previousAiring": "2021-08-12T02:00:00Z",
        "network": "FXX",
        "airTime": "22:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/13/banner.jpg?lastWrite=638060147135413743",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/354905/banners/62090923.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/13/poster.jpg?lastWrite=638093687105105554",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/354905/posters/60a908cd317da.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/13/fanart.jpg?lastWrite=638060147171048560",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/354905/backgrounds/62058282.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2020-04-30T02:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 4570346817,
                    "releaseGroups": [
                        "BTX",
                        "CROOKS",
                        "xlf"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2021-08-12T02:00:00Z",
                    "episodeFileCount": 3,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 616116263,
                    "releaseGroups": [
                        "MeGusta",
                        "MiNX"
                    ],
                    "percentOfEpisodes": 30.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": True,
                "statistics": {
                    "nextAiring": "2023-04-06T02:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 2,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            }
        ],
        "year": 2020,
        "path": "D:/Movies/Series/Dave",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 29,
        "tvdbId": 354905,
        "tvRageId": 0,
        "tvMazeId": 45563,
        "firstAired": "2020-03-04T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "dave",
        "imdbId": "tt8531222",
        "titleSlug": "dave",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Comedy"
        ],
        "tags": [],
        "added": "2022-12-07T12:58:32.2497222Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 3,
            "episodeFileCount": 13,
            "episodeCount": 20,
            "totalEpisodeCount": 22,
            "sizeOnDisk": 5186463080,
            "releaseGroups": [
                "BTX",
                "CROOKS",
                "xlf",
                "MeGusta",
                "MiNX"
            ],
            "percentOfEpisodes": 65.00
        },
        "id": 13
    },
    {
        "title": "The Boys",
        "alternateTitles": [
            {
                "title": "The Boys 2019",
                "seasonNumber": -1
            },
            {
                "title": "Пацаны",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "boys",
        "status": "continuing",
        "ended": False,
        "overview": "In a world where superheroes embrace the darker side of their massive celebrity and fame, a group of vigilantes known informally as \"The Boys\" set out to take down corrupt superheroes with no more than blue collar grit and a willingness to fight dirty.",
        "previousAiring": "2022-07-08T04:00:00Z",
        "network": "Amazon Prime Video",
        "airTime": "00:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/15/banner.jpg?lastWrite=638060152849109773",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/355567/banners/5f208242a5940.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/15/poster.jpg?lastWrite=638060152858736280",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/5c5c402b075cc.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/15/fanart.jpg?lastWrite=638084606075623799",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/5d1200d70e4fe.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 27,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": False,
                "statistics": {
                    "previousAiring": "2019-07-26T04:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": False,
                "statistics": {
                    "previousAiring": "2020-10-09T04:00:00Z",
                    "episodeFileCount": 1,
                    "episodeCount": 1,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 335172470,
                    "releaseGroups": [
                        "MiNX"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-07-08T04:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 8782166662,
                    "releaseGroups": [
                        "cakes",
                        "MeGusta"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2019,
        "path": "D:/Movies/Series/The Boys",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 61,
        "tvdbId": 355567,
        "tvRageId": 0,
        "tvMazeId": 15299,
        "firstAired": "2019-07-26T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "theboys",
        "imdbId": "tt1190634",
        "titleSlug": "the-boys",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Action",
            "Comedy",
            "Crime",
            "Drama",
            "Science Fiction"
        ],
        "tags": [],
        "added": "2022-12-07T13:08:04.1591463Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 3,
            "episodeFileCount": 9,
            "episodeCount": 17,
            "totalEpisodeCount": 51,
            "sizeOnDisk": 9117339132,
            "releaseGroups": [
                "MiNX",
                "cakes",
                "MeGusta"
            ],
            "percentOfEpisodes": 52.941176470588235294117647060
        },
        "id": 15
    },
    {
        "title": "Wu-Tang: An American Saga",
        "alternateTitles": [],
        "sortTitle": "wutang an american saga",
        "status": "continuing",
        "ended": False,
        "overview": "In the early 1990's in New York, during the height of the crack cocaine epidemic, a visionary musician named Bobby Diggs aka The RZA begins to form a super group of a dozen young, black men, who will eventually rise to become one of the unlikeliest success stories in American music history.",
        "nextAiring": "2023-02-15T05:00:00Z",
        "network": "Hulu",
        "airTime": "00:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/16/banner.jpg?lastWrite=638060153201218309",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/5db072ba95bcf.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/16/poster.jpg?lastWrite=638060153203673433",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/5d8b40cf070e2.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/16/fanart.jpg?lastWrite=638085904076125033",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/5d72717c1cfa7.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": True,
                "statistics": {
                    "nextAiring": "2023-02-15T05:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            }
        ],
        "year": 2019,
        "path": "D:/Movies/Series/Wu-Tang - An American Saga",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 50,
        "tvdbId": 354080,
        "tvRageId": 0,
        "tvMazeId": 39048,
        "firstAired": "2019-09-04T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "wutangamericansaga",
        "imdbId": "tt9113406",
        "titleSlug": "wu-tang-an-american-saga",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Drama",
            "Musical"
        ],
        "tags": [],
        "added": "2022-12-07T13:08:37.8633934Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 3,
            "episodeFileCount": 0,
            "episodeCount": 0,
            "totalEpisodeCount": 30,
            "sizeOnDisk": 0,
            "releaseGroups": [],
            "percentOfEpisodes": 0.0
        },
        "id": 16
    },
    {
        "title": "Mob Psycho 100",
        "alternateTitles": [
            {
                "title": "Mob Psycho 100 S2",
                "sceneSeasonNumber": 2
            },
            {
                "title": "Mob Psycho 100 II",
                "sceneSeasonNumber": 2
            },
            {
                "title": "Mob Psycho 100 S3",
                "sceneSeasonNumber": 3
            },
            {
                "title": "Mob Psycho 100 III",
                "sceneSeasonNumber": 3
            }
        ],
        "sortTitle": "mob psycho 100",
        "status": "ended",
        "ended": True,
        "overview": "Kageyama Shigeo (a.k.a. \"Mob\") is a 8th grader with psychic abilities. He could bend spoons and lift objects with his mind from a young age, but he slowly began to withhold from using his abilities in public due to the negative attention he kept receiving. Now, the only thing he wants is to become friends with a girl in his class, Tsubomi. With his psychic \"mentor\" (who has no psychic powers), he continues his daily life, attempting to realize his purpose in life.",
        "previousAiring": "2022-12-21T15:00:00Z",
        "network": "Tokyo MX",
        "airTime": "00:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/17/banner.jpg?lastWrite=638060302351126386",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/307375-g2.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/17/poster.jpg?lastWrite=638085904019721538",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/307375/posters/60aa39f03e5be.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/17/fanart.jpg?lastWrite=638085904027039358",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/307375-5.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2016-09-26T15:00:00Z",
                    "episodeFileCount": 12,
                    "episodeCount": 12,
                    "totalEpisodeCount": 12,
                    "sizeOnDisk": 7957900704,
                    "releaseGroups": [
                        "NanDesuKa"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2019-03-31T15:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 13,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-12-21T15:00:00Z",
                    "episodeFileCount": 6,
                    "episodeCount": 12,
                    "totalEpisodeCount": 12,
                    "sizeOnDisk": 1788893026,
                    "releaseGroups": [
                        "XEN0N",
                        "Yameii"
                    ],
                    "percentOfEpisodes": 50.0
                }
            }
        ],
        "year": 2016,
        "path": "D:/Movies/Anime/Mob Psycho 100",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": True,
        "runtime": 24,
        "tvdbId": 307375,
        "tvRageId": 0,
        "tvMazeId": 18260,
        "firstAired": "2016-07-12T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "mobpsycho100",
        "imdbId": "tt5897304",
        "titleSlug": "mob-psycho-100",
        "rootFolderPath": "D:/Movies/Anime/",
        "certification": "TV-14",
        "genres": [
            "Action",
            "Animation",
            "Anime",
            "Comedy",
            "Science Fiction"
        ],
        "tags": [],
        "added": "2022-12-07T17:17:13.1464296Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 3,
            "episodeFileCount": 18,
            "episodeCount": 37,
            "totalEpisodeCount": 45,
            "sizeOnDisk": 9746793730,
            "releaseGroups": [
                "NanDesuKa",
                "XEN0N",
                "Yameii"
            ],
            "percentOfEpisodes": 48.648648648648648648648648650
        },
        "id": 17
    },
    {
        "title": "The Good Doctor",
        "alternateTitles": [
            {
                "title": "The GD",
                "seasonNumber": -1
            },
            {
                "title": "Good Doctor",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "good doctor",
        "status": "continuing",
        "ended": False,
        "overview": "Shaun Murphy, a young surgeon with autism and savant syndrome, relocates from a quiet country life to join a prestigious hospital surgical unit. Alone in the world and unable to personally connect with those around him, Shaun uses his extraordinary medical gifts to save lives and challenge the skepticism of his colleagues.",
        "nextAiring": "2023-02-07T03:00:00Z",
        "previousAiring": "2023-01-31T03:00:00Z",
        "network": "ABC (US)",
        "airTime": "22:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/18/banner.jpg?lastWrite=638060510229563965",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/328634-g2.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/18/poster.jpg?lastWrite=638060510234418743",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/328634-2.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/18/fanart.jpg?lastWrite=638085038228874468",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/328634-7.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 18,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 18,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 20,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 4,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 20,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 5,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 18,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 6,
                "monitored": True,
                "statistics": {
                    "nextAiring": "2023-02-07T03:00:00Z",
                    "previousAiring": "2023-01-31T03:00:00Z",
                    "episodeFileCount": 4,
                    "episodeCount": 4,
                    "totalEpisodeCount": 15,
                    "sizeOnDisk": 2881489021,
                    "releaseGroups": [
                        "KOGi",
                        "NTb",
                        "SYNCOPY"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2017,
        "path": "D:/Movies/Series/The Good Doctor",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 43,
        "tvdbId": 328634,
        "tvRageId": 0,
        "tvMazeId": 21845,
        "firstAired": "2017-09-25T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "thegooddoctor",
        "imdbId": "tt6470478",
        "titleSlug": "the-good-doctor",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-14",
        "genres": [
            "Drama"
        ],
        "tags": [],
        "added": "2022-12-07T23:03:42.6499643Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 6,
            "episodeFileCount": 4,
            "episodeCount": 4,
            "totalEpisodeCount": 109,
            "sizeOnDisk": 2881489021,
            "releaseGroups": [
                "KOGi",
                "NTb",
                "SYNCOPY"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 18
    },
    {
        "title": "Suits",
        "alternateTitles": [],
        "sortTitle": "suits",
        "status": "ended",
        "ended": True,
        "overview": "College drop-out Mike Ross accidentally lands a job with one of New York's best legal closers, Harvey Specter. They soon become a winning team with Mike's raw talent and photographic memory, and Mike soon reminds Harvey of why he went into the field of law in the first place.",
        "previousAiring": "2013-02-22T02:00:00Z",
        "network": "USA Network",
        "airTime": "21:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/19/banner.jpg?lastWrite=638108386022671586",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/247808-g9.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/19/poster.jpg?lastWrite=638060511386617854",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/247808-6.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/19/fanart.jpg?lastWrite=638108386091358979",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/247808-5.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 30,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2011-09-09T01:00:00Z",
                    "episodeFileCount": 12,
                    "episodeCount": 12,
                    "totalEpisodeCount": 12,
                    "sizeOnDisk": 4086318048,
                    "releaseGroups": [
                        "DeeJayAhmed"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2013-02-22T02:00:00Z",
                    "episodeFileCount": 16,
                    "episodeCount": 16,
                    "totalEpisodeCount": 16,
                    "sizeOnDisk": 5216967944,
                    "releaseGroups": [
                        "DeeJayAhmed"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 16,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 4,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 16,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 5,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 16,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 6,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 16,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 7,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 16,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 8,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 16,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 9,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            }
        ],
        "year": 2011,
        "path": "D:/Movies/Series/Suits",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 43,
        "tvdbId": 247808,
        "tvRageId": 27518,
        "tvMazeId": 172,
        "firstAired": "2011-06-23T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "suits",
        "imdbId": "tt1632701",
        "titleSlug": "suits",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-14",
        "genres": [
            "Comedy",
            "Drama"
        ],
        "tags": [],
        "added": "2022-12-07T23:05:37.888293Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 9,
            "episodeFileCount": 28,
            "episodeCount": 28,
            "totalEpisodeCount": 164,
            "sizeOnDisk": 9303285992,
            "releaseGroups": [
                "DeeJayAhmed"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 19
    },
    {
        "title": "Talentless Nana",
        "alternateTitles": [
            {
                "title": "Munou na Nana",
                "sceneSeasonNumber": -1
            },
            {
                "title": "Munou na Nana (Talentless Nana)",
                "sceneSeasonNumber": -1
            }
        ],
        "sortTitle": "talentless nana",
        "status": "ended",
        "ended": True,
        "overview": "It is the year 20XX. Earth was assaulted by monsters that would come to be known as \"the Enemy of Humanity.\" In order to deal with this threat, special schools composed of teenagers with extraordinary abilities were formed. These people, who came to be known as \"the Talented,\" had abilities that could defy the rules of reality.\r\nAmong these people with supernatural powers was an outlier, an individual who was sent to one of these schools despite having no innate special abilities whatsoever. This is the story of our protagonist, who attempts to defeat the Enemies of Humanity through the use of intelligence and manipulation alone.",
        "previousAiring": "2020-12-27T12:30:00Z",
        "network": "AT-X",
        "airTime": "21:30",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/20/banner.jpg?lastWrite=638076447614496598",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/386714/banners/5f88a6e49cb56.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/20/poster.jpg?lastWrite=638076447709347473",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/386714/posters/5f75cfe47ba46.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/20/fanart.jpg?lastWrite=638076447814992963",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/386714/backgrounds/5f75d199883f0.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2020-12-27T12:30:00Z",
                    "episodeFileCount": 13,
                    "episodeCount": 13,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 7517961801,
                    "releaseGroups": [
                        "SubsPlease"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2020,
        "path": "D:/Movies/Anime/Talentless Nana",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": True,
        "runtime": 24,
        "tvdbId": 386714,
        "tvRageId": 0,
        "tvMazeId": 50387,
        "firstAired": "2020-10-04T00:00:00Z",
        "seriesType": "anime",
        "cleanTitle": "talentlessnana",
        "imdbId": "tt12312018",
        "titleSlug": "talentless-nana",
        "rootFolderPath": "D:/Movies/Anime/",
        "certification": "TV-14",
        "genres": [
            "Action",
            "Animation",
            "Anime",
            "Fantasy",
            "Horror",
            "Mystery",
            "Science Fiction",
            "Thriller"
        ],
        "tags": [],
        "added": "2022-12-26T09:45:32.3661162Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 1,
            "episodeFileCount": 13,
            "episodeCount": 13,
            "totalEpisodeCount": 26,
            "sizeOnDisk": 7517961801,
            "releaseGroups": [
                "SubsPlease"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 20
    },
    {
        "title": "Dirty Money (2018)",
        "alternateTitles": [
            {
                "title": "Dirty Money",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "dirty money 2018",
        "status": "ended",
        "ended": True,
        "overview": "From rigged cars to wildly inflated drug prices, this documentary series lifts the lid on shocking acts of corporate greed and corruption.",
        "previousAiring": "2020-03-11T07:00:00Z",
        "network": "Netflix",
        "airTime": "03:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/22/banner.jpg?lastWrite=638108385835821152",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/339925-g.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/22/poster.jpg?lastWrite=638080786790029667",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/339925/posters/1260834.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/22/fanart.jpg?lastWrite=638080786815718484",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/339925-2.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2018-01-26T08:00:00Z",
                    "episodeFileCount": 6,
                    "episodeCount": 6,
                    "totalEpisodeCount": 6,
                    "sizeOnDisk": 9418255762,
                    "releaseGroups": [
                        "STRiFE"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2020-03-11T07:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 6,
                    "totalEpisodeCount": 6,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            }
        ],
        "year": 2018,
        "path": "D:/Movies/Series/Dirty Money (2018)",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 61,
        "tvdbId": 339925,
        "tvRageId": 0,
        "tvMazeId": 34584,
        "firstAired": "2018-01-26T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "dirtymoney2018",
        "imdbId": "tt7889220",
        "titleSlug": "dirty-money-2018",
        "rootFolderPath": "D:/Movies/Series/",
        "genres": [
            "Crime",
            "Documentary"
        ],
        "tags": [],
        "added": "2022-12-31T10:17:52.6032033Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 2,
            "episodeFileCount": 6,
            "episodeCount": 12,
            "totalEpisodeCount": 12,
            "sizeOnDisk": 9418255762,
            "releaseGroups": [
                "STRiFE"
            ],
            "percentOfEpisodes": 50.0
        },
        "id": 22
    },
    {
        "title": "Wednesday",
        "alternateTitles": [
            {
                "title": "Mercoledì",
                "seasonNumber": -1
            },
            {
                "title": "Miércoles",
                "seasonNumber": -1
            },
            {
                "title": "Mercredi",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "wednesday",
        "status": "continuing",
        "ended": False,
        "overview": "Smart, sarcastic and a little dead inside, Wednesday Addams investigates a murder spree while making new friends — and foes — at Nevermore Academy.",
        "previousAiring": "2022-11-23T08:00:00Z",
        "network": "Netflix",
        "airTime": "03:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/23/banner.jpg?lastWrite=638084227078329671",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/397060/banners/639e548836035.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/23/poster.jpg?lastWrite=638084227081669247",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/397060/posters/632dbd876738d.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/23/fanart.jpg?lastWrite=638084227085957908",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/397060/backgrounds/638872658fa2b.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-11-23T08:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 10891243840,
                    "releaseGroups": [
                        "SMURF"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2022,
        "path": "D:/Movies/Series/Wednesday",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 51,
        "tvdbId": 397060,
        "tvRageId": 0,
        "tvMazeId": 53647,
        "firstAired": "2022-11-23T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "wednesday",
        "imdbId": "tt13443470",
        "titleSlug": "wednesday",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-14",
        "genres": [
            "Family",
            "Fantasy",
            "Horror",
            "Mystery"
        ],
        "tags": [],
        "added": "2023-01-04T09:51:47.4031691Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 1,
            "episodeFileCount": 8,
            "episodeCount": 8,
            "totalEpisodeCount": 8,
            "sizeOnDisk": 10891243840,
            "releaseGroups": [
                "SMURF"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 23
    },
    {
        "title": "The Wire",
        "alternateTitles": [],
        "sortTitle": "wire",
        "status": "ended",
        "ended": True,
        "overview": "Follows one single drug and homicide investigation throughout the length of an entire season. Centered on the drug culture of inner-city Baltimore, the series' storyline unfolds from the points of view of both the criminals lording the streets and the police officers determined to bring them down.",
        "previousAiring": "2003-08-25T01:00:00Z",
        "network": "HBO",
        "airTime": "21:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/24/banner.jpg?lastWrite=638110547547848026",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/79126-g19.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/24/poster.jpg?lastWrite=638084427660243633",
                "remoteUrl": "https://artworks.thetvdb.com/banners/posters/79126-2.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/24/fanart.jpg?lastWrite=638110547575495630",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/79126-3.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 26,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2002-09-09T01:00:00Z",
                    "episodeFileCount": 13,
                    "episodeCount": 13,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 7192627518,
                    "releaseGroups": [],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2003-08-25T01:00:00Z",
                    "episodeFileCount": 12,
                    "episodeCount": 12,
                    "totalEpisodeCount": 12,
                    "sizeOnDisk": 6589787190,
                    "releaseGroups": [],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 12,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 4,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 13,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 5,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            }
        ],
        "year": 2002,
        "path": "D:/Movies/Series/The Wire",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 60,
        "tvdbId": 79126,
        "tvRageId": 6296,
        "tvMazeId": 179,
        "firstAired": "2002-06-02T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "thewire",
        "imdbId": "tt0306414",
        "titleSlug": "the-wire",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Crime",
            "Drama",
            "Thriller"
        ],
        "tags": [],
        "added": "2023-01-04T15:26:01.6766651Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 5,
            "episodeFileCount": 25,
            "episodeCount": 25,
            "totalEpisodeCount": 86,
            "sizeOnDisk": 13782414708,
            "releaseGroups": [],
            "percentOfEpisodes": 100.0
        },
        "id": 24
    },
    {
        "title": "Kaleidoscope (2023)",
        "alternateTitles": [
            {
                "title": "Kaleidoscope (2023)",
                "seasonNumber": -1,
                "sceneSeasonNumber": -1,
                "sceneOrigin": "mixed",
                "comment": "Netflix randomises episodes"
            },
            {
                "title": "Kaleidoscope",
                "seasonNumber": -1,
                "sceneSeasonNumber": -1,
                "sceneOrigin": "mixed",
                "comment": "Netflix randomises episodes"
            },
            {
                "title": "Kaleidoskop",
                "seasonNumber": -1,
                "sceneSeasonNumber": -1,
                "sceneOrigin": "mixed",
                "comment": "Netflix randomises episodes"
            },
            {
                "title": "Caleidoscopio",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "kaleidoscope 2023",
        "status": "ended",
        "ended": True,
        "overview": "A master thief and his crew attempt an epic and elaborate heist worth $7 billion dollars — but betrayal, greed and other threats undermine their plans.",
        "previousAiring": "2023-01-01T08:00:00Z",
        "network": "Netflix",
        "airTime": "03:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/29/banner.jpg?lastWrite=638090618371426219",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/410092/banners/639ca76ca9d99.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/29/poster.jpg?lastWrite=638090618373707655",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/410092/posters/639ca6160df19.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/29/fanart.jpg?lastWrite=638090618382809771",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/410092/backgrounds/639ca7db189db.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 1,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2023-01-01T08:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 2207943222,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2023,
        "path": "D:/Movies/Series/Kaleidoscope (2023)",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": False,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 47,
        "tvdbId": 410092,
        "tvRageId": 0,
        "tvMazeId": 57680,
        "firstAired": "2023-01-01T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "kaleidoscope2023",
        "imdbId": "tt15438246",
        "titleSlug": "kaleidoscope-2023",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Action",
            "Crime",
            "Drama",
            "Mini-Series",
            "Thriller"
        ],
        "tags": [],
        "added": "2023-01-11T19:23:56.6291158Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 1,
            "episodeFileCount": 8,
            "episodeCount": 8,
            "totalEpisodeCount": 9,
            "sizeOnDisk": 2207943222,
            "releaseGroups": [
                "GalaxyTV"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 29
    },
    {
        "title": "Only Murders in the Building",
        "alternateTitles": [
            {
                "title": "Solo asesinatos en el edificio",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "only murders in the building",
        "status": "continuing",
        "ended": False,
        "overview": "Three strangers who share an obsession with True crime suddenly find themselves wrapped up in one.",
        "previousAiring": "2022-08-23T04:00:00Z",
        "network": "Hulu",
        "airTime": "00:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/30/banner.jpg?lastWrite=638098879551716225",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/399959/banners/60d5cd5481a3e.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/30/poster.jpg?lastWrite=638098879559103113",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/399959/posters/60d5e4a9214e7.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/30/fanart.jpg?lastWrite=638098879583438740",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/399959/backgrounds/6117b25e49195.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2021-10-19T04:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 1926493138,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-08-23T04:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 4731962694,
                    "releaseGroups": [
                        "NTb"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2021,
        "path": "D:/Movies/Series/Only Murders in the Building",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 33,
        "tvdbId": 399959,
        "tvRageId": 0,
        "tvMazeId": 48830,
        "firstAired": "2021-08-31T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "onlymurdersinbuilding",
        "imdbId": "tt12851524",
        "titleSlug": "only-murders-in-the-building",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Comedy",
            "Crime",
            "Drama",
            "Mystery",
            "Thriller"
        ],
        "tags": [],
        "added": "2023-01-21T08:52:24.7261825Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 2,
            "episodeFileCount": 20,
            "episodeCount": 20,
            "totalEpisodeCount": 30,
            "sizeOnDisk": 6658455832,
            "releaseGroups": [
                "GalaxyTV",
                "NTb"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 30
    },
    {
        "title": "The Sinner",
        "alternateTitles": [],
        "sortTitle": "sinner",
        "status": "ended",
        "ended": True,
        "overview": "In a small New York town, a haunted detective hunts for answers about perplexing crimes while wrestling with his own demons.",
        "previousAiring": "2021-12-02T03:00:00Z",
        "network": "USA Network",
        "airTime": "22:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/31/banner.jpg?lastWrite=638098880072483046",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/326866/banners/62046601.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/31/poster.jpg?lastWrite=638098880076249158",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/326866/posters/614e221101549.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/31/fanart.jpg?lastWrite=638098880088908509",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/326866/backgrounds/62045029.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2017-09-21T02:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 1933109393,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2018-09-20T02:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 1889831858,
                    "releaseGroups": [
                        "HETeam"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2020-03-27T02:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 1552181104,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 4,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2021-12-02T03:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 1977368592,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2017,
        "path": "D:/Movies/Series/The Sinner",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 46,
        "tvdbId": 326866,
        "tvRageId": 0,
        "tvMazeId": 20895,
        "firstAired": "2017-08-02T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "thesinner",
        "imdbId": "tt6048596",
        "titleSlug": "the-sinner",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Crime",
            "Drama",
            "Mystery",
            "Suspense",
            "Thriller"
        ],
        "tags": [],
        "added": "2023-01-21T08:53:25.4115795Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 4,
            "episodeFileCount": 32,
            "episodeCount": 32,
            "totalEpisodeCount": 32,
            "sizeOnDisk": 7352490947,
            "releaseGroups": [
                "GalaxyTV",
                "HETeam"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 31
    },
    {
        "title": "See",
        "alternateTitles": [
            {
                "title": "See - Reich der Blinden",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "see",
        "status": "ended",
        "ended": True,
        "overview": "A virus has decimated humankind. Those who survived emerged blind. Centuries later when twins are born with the mythic ability to see, their father must protect his tribe against a threatened queen.",
        "previousAiring": "2022-10-14T04:00:00Z",
        "network": "Apple TV+",
        "airTime": "00:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/32/banner.jpg?lastWrite=638098880193932788",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/5d7d7464cc1a6.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/32/poster.jpg?lastWrite=638098880201785149",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/361565/posters/61126bd10a396.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/32/fanart.jpg?lastWrite=638098880213080447",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/5d7d736c44c80.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2019-12-06T05:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2021-10-14T04:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 2503865923,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 3,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-10-14T04:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 9827873904,
                    "releaseGroups": [
                        "ggez",
                        "glhf",
                        "KOGi",
                        "MiNX"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2019,
        "path": "D:/Movies/Series/See",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 53,
        "tvdbId": 361565,
        "tvRageId": 0,
        "tvMazeId": 34345,
        "firstAired": "2019-11-01T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "see",
        "imdbId": "tt7949218",
        "titleSlug": "see",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Action",
            "Drama",
            "Science Fiction"
        ],
        "tags": [],
        "added": "2023-01-21T08:53:38.4497305Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 3,
            "episodeFileCount": 16,
            "episodeCount": 24,
            "totalEpisodeCount": 24,
            "sizeOnDisk": 12331739827,
            "releaseGroups": [
                "GalaxyTV",
                "ggez",
                "glhf",
                "KOGi",
                "MiNX"
            ],
            "percentOfEpisodes": 66.666666666666666666666666670
        },
        "id": 32
    },
    {
        "title": "Warrior Nun",
        "alternateTitles": [
            {
                "title": "La monja guerrera",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "warrior nun",
        "status": "ended",
        "ended": True,
        "overview": "After waking up in a morgue, an orphaned teen discovers she now possesses superpowers as the chosen Halo-Bearer for a secret sect of demon-hunting nuns.",
        "previousAiring": "2022-11-10T08:00:00Z",
        "network": "Netflix",
        "airTime": "03:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/33/banner.jpg?lastWrite=638098880950866780",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/382544/banners/5ef06b00d7a6c.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/33/poster.jpg?lastWrite=638098880969025605",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/382544/posters/5efd834cc0d28.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/33/fanart.jpg?lastWrite=638098880992439859",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/382544/backgrounds/5eed0a0d9ac4f.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2020-07-02T07:00:00Z",
                    "episodeFileCount": 10,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 2087665643,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2022-11-10T08:00:00Z",
                    "episodeFileCount": 8,
                    "episodeCount": 8,
                    "totalEpisodeCount": 8,
                    "sizeOnDisk": 1754229669,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2020,
        "path": "D:/Movies/Series/Warrior Nun",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 43,
        "tvdbId": 382544,
        "tvRageId": 0,
        "tvMazeId": 38913,
        "firstAired": "2020-07-02T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "warriornun",
        "imdbId": "tt9059350",
        "titleSlug": "warrior-nun",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Action",
            "Drama",
            "Fantasy",
            "Science Fiction"
        ],
        "tags": [],
        "added": "2023-01-21T08:54:52.6918889Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 2,
            "episodeFileCount": 18,
            "episodeCount": 18,
            "totalEpisodeCount": 18,
            "sizeOnDisk": 3841895312,
            "releaseGroups": [
                "GalaxyTV"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 33
    },
    {
        "title": "Fleabag",
        "alternateTitles": [],
        "sortTitle": "fleabag",
        "status": "ended",
        "ended": True,
        "overview": "Meet Fleabag. She’s not talking to all of us; she’s talking to YOU. So why don’t you pop your top off and come right in?\r\n\r\nFleabag is a hilarious and poignant window into the mind of a dry-witted, sexual, angry, porn-watching, grief-riddled woman trying to make sense of the world.",
        "previousAiring": "2019-04-08T21:30:00Z",
        "network": "BBC Three",
        "airTime": "22:30",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/36/banner.jpg?lastWrite=638111380641485079",
                "remoteUrl": "https://artworks.thetvdb.com/banners/graphical/314614-g6.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/36/poster.jpg?lastWrite=638111380645084428",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/314614/posters/601feb0c8a666.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/36/fanart.jpg?lastWrite=638111380662057613",
                "remoteUrl": "https://artworks.thetvdb.com/banners/fanart/original/314614-1.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2016-08-25T21:30:00Z",
                    "episodeFileCount": 6,
                    "episodeCount": 6,
                    "totalEpisodeCount": 6,
                    "sizeOnDisk": 828725226,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            },
            {
                "seasonNumber": 2,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2019-04-08T21:30:00Z",
                    "episodeFileCount": 6,
                    "episodeCount": 6,
                    "totalEpisodeCount": 6,
                    "sizeOnDisk": 699917288,
                    "releaseGroups": [
                        "GalaxyTV"
                    ],
                    "percentOfEpisodes": 100.0
                }
            }
        ],
        "year": 2016,
        "path": "D:/Movies/Series/Fleabag",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": False,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 25,
        "tvdbId": 314614,
        "tvRageId": 0,
        "tvMazeId": 16149,
        "firstAired": "2016-07-21T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "fleabag",
        "imdbId": "tt5687612",
        "titleSlug": "fleabag",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Comedy",
            "Drama"
        ],
        "tags": [],
        "added": "2023-02-04T20:07:41.8131595Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 2,
            "episodeFileCount": 12,
            "episodeCount": 12,
            "totalEpisodeCount": 12,
            "sizeOnDisk": 1528642514,
            "releaseGroups": [
                "GalaxyTV"
            ],
            "percentOfEpisodes": 100.0
        },
        "id": 36
    },
    {
        "title": "The Underground Railroad",
        "alternateTitles": [
            {
                "title": "La ferrovia sotterranea",
                "seasonNumber": -1
            }
        ],
        "sortTitle": "underground railroad",
        "status": "ended",
        "ended": True,
        "overview": "Follow young Cora’s journey as she makes a desperate bid for freedom in the antebellum South. After escaping her Georgia plantation for the rumored Underground Railroad, Cora discovers no mere metaphor, but an actual railroad full of engineers and conductors, and a secret network of tracks and tunnels beneath the Southern soil.",
        "previousAiring": "2021-05-14T04:00:00Z",
        "network": "Amazon Prime Video",
        "airTime": "00:00",
        "images": [
            {
                "coverType": "banner",
                "url": "/MediaCover/37/banner.jpg?lastWrite=638111928491296322",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/373877/banners/6095e519b13fa.jpg"
            },
            {
                "coverType": "poster",
                "url": "/MediaCover/37/poster.jpg?lastWrite=638111928496028686",
                "remoteUrl": "https://artworks.thetvdb.com/banners/v4/series/373877/posters/609dff571df0f.jpg"
            },
            {
                "coverType": "fanart",
                "url": "/MediaCover/37/fanart.jpg?lastWrite=638111928517839903",
                "remoteUrl": "https://artworks.thetvdb.com/banners/series/373877/panels/60389f15c5c00.jpg"
            }
        ],
        "seasons": [
            {
                "seasonNumber": 0,
                "monitored": False,
                "statistics": {
                    "episodeFileCount": 0,
                    "episodeCount": 0,
                    "totalEpisodeCount": 1,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            },
            {
                "seasonNumber": 1,
                "monitored": True,
                "statistics": {
                    "previousAiring": "2021-05-14T04:00:00Z",
                    "episodeFileCount": 0,
                    "episodeCount": 10,
                    "totalEpisodeCount": 10,
                    "sizeOnDisk": 0,
                    "releaseGroups": [],
                    "percentOfEpisodes": 0.0
                }
            }
        ],
        "year": 2021,
        "path": "D:/Movies/Series/The Underground Railroad",
        "qualityProfileId": 7,
        "languageProfileId": 1,
        "seasonFolder": True,
        "monitored": True,
        "useSceneNumbering": False,
        "runtime": 59,
        "tvdbId": 373877,
        "tvRageId": 0,
        "tvMazeId": 26481,
        "firstAired": "2021-05-14T00:00:00Z",
        "seriesType": "standard",
        "cleanTitle": "theundergroundrailroad",
        "imdbId": "tt6704972",
        "titleSlug": "the-underground-railroad",
        "rootFolderPath": "D:/Movies/Series/",
        "certification": "TV-MA",
        "genres": [
            "Drama",
            "Fantasy",
            "History",
            "Mini-Series",
            "War"
        ],
        "tags": [],
        "added": "2023-02-05T11:20:47.2740359Z",
        "ratings": {
            "votes": 0,
            "value": 0.0
        },
        "statistics": {
            "seasonCount": 1,
            "episodeFileCount": 0,
            "episodeCount": 10,
            "totalEpisodeCount": 11,
            "sizeOnDisk": 0,
            "releaseGroups": [],
            "percentOfEpisodes": 0.0
        },
        "id": 37
    }
]

def pprint(object: list|dict|set) -> None:
    print(json.dumps(object, indent=2))

msg_str = ""
for i, show in enumerate(data):
    # pprint(show)
    if "Boys" not in show['title']: continue

    status = ""
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

    msg_str += f"{i+1:02}) {show['title']} {status}\n"
    pprint(msg_str)
    break
