import common.util as util

def get_features(features):
  val_features = util.LBL_EMPTY
  if features == util.ACCESS_FREE:
    val_features += "License: Free\n"
    val_features += "Price: Free\n"
    val_features += "\n"
    val_features += "Dungeons:\n"
    val_features += "Hazardous Valley (Awakened)\n"
    val_features += "Hazardous Valley (Hard)\n"
    val_features += "Hazardous Valley (Medium)\n"
    val_features += "Hazardous Valley (Easy)\n"
    val_features += "\n"
    val_features += "Setups:\n"
    val_features += "Buffs\n"
    val_features += "Range\n"
    val_features += "\n"
    val_features += "For license upgrade, please contact the page.\n"
    val_features += "https://www.facebook.com/TheTeamAei\n"
  elif features == util.ACCESS_PRO:
    val_features += "License: Pro\n"
    val_features += "Price: $6.00 (30 days subscription)\n"
    val_features += "\n"
    val_features += "Dungeons:\n"
    val_features += "Hazardous Valley (Awakened)\n"
    val_features += "Hazardous Valley (Hard)\n"
    val_features += "Hazardous Valley (Medium)\n"
    val_features += "Hazardous Valley (Easy)\n"
    val_features += "Steamer Crazy (Awakened)\n"
    val_features += "Catacomb Frost (Awakened)\n"
    val_features += "Lava Hellfire (Awakened)\n"
    val_features += "\n"
    val_features += "Setups:\n"
    val_features += "Mode II\n"
    val_features += "Buffs\n"
    val_features += "Shorts\n"
    val_features += "Range\n"
    val_features += "\n"
    val_features += "Others:\n"
    val_features += "All features\n"
    val_features += "\n"
    val_features += "For license upgrade, please contact the page.\n"
    val_features += "https://www.facebook.com/TheTeamAei\n"
  elif features == util.ACCESS_PREMIUM:
    val_features += "License: Premium\n"
    val_features += "Price: $10.00 (40 days subscription)\n"
    val_features += "\n"
    val_features += "Dungeons:\n"
    val_features += "Hazardous Valley (Awakened)\n"
    val_features += "Hazardous Valley (Hard)\n"
    val_features += "Hazardous Valley (Medium)\n"
    val_features += "Hazardous Valley (Easy)\n"
    val_features += "Steamer Crazy (Awakened)\n"
    val_features += "Catacomb Frost (Awakened)\n"
    val_features += "Lava Hellfire (Awakened)\n"
    val_features += "Holy Windmill\n"
    val_features += "Holy Keldrasil\n"
    val_features += "\n"
    val_features += "Setups:\n"
    val_features += "Mode II\n"
    val_features += "Buffs\n"
    val_features += "Shorts\n"
    val_features += "Range\n"
    val_features += "Veradrix\n"
    val_features += "\n"
    val_features += "Others:\n"
    val_features += "All features\n"
    val_features += "\n"
    val_features += "Connection:\n"
    val_features += "All features\n"
    val_features += "\n"
    val_features += "For license upgrade, please contact the page.\n"
    val_features += "https://www.facebook.com/TheTeamAei\n"

  return val_features
