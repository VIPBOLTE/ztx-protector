class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6257270528"
    sudo_users = "6257270528", "6574393060", "5562647760", "6092692622", "6708020976", "6140108968", "6242774437", "6281473623", "6849434647"
    GROUP_ID = -1002140753266
    TOKEN = "7126535078:AAGCzeFY5MGDhhPtgupdv9HTixUSfraNgg8"
    mongo_url = "mongodb+srv://ztx:ztxwaifu@cluster0.dpny5vq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/a75e0d1a655943665b662.jpg", "https://telegra.ph/file/bee112f781897c3447515.jpg", "https://telegra.ph/file/a0123f958a26695bd9e14.jpg"]
    SUPPORT_CHAT = "Ɓ ʟ ᴀ ᴅ ᴇ メ ƈ ᴏ ᴍ ᴍ ᴜ ɴ ɪ ᴛ ʏ"
    UPDATE_CHAT = "Nᴀʀᴜᴛᴏ Uᴘᴅᴀᴛᴇs"
    BOT_USERNAME = "Seal_Your_Waifu_Bot"
    CHARA_CHANNEL_ID = "-1002140753266"
    api_id = 22792918
    api_hash = "ff10095d2bb96d43d6eb7a7d9fc85f81"
    
    STRICT_GBAN = True
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True