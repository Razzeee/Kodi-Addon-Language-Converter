#!/usr/bin/env python3

import os
import sys
import xml.etree.ElementTree as etree

LANGUAGE_LIST = [{'iso_code': 'af', 'locale': 'af_ZA', 'name': 'Afrikaans'}
                 , {'iso_code': 'AM', 'locale': 'am_ET', 'name': 'Amharic'}
                 , {'iso_code': 'ar', 'locale': 'ar_SA', 'name': 'Arabic'}
                 , {'iso_code': 'ast', 'locale': 'ast', 'name': 'Asturian'}
                 , {'iso_code': 'az', 'locale': 'az_AZ', 'name': 'Azerbaijani'}
                 , {'iso_code': 'be', 'locale': 'be_BY', 'name': 'Belarusian'}
                 , {'iso_code': 'bg', 'locale': 'bg_BG', 'name': 'Bulgarian'}
                 , {'iso_code': 'bs', 'locale': 'bs_BA', 'name': 'Bosnian'}
                 , {'iso_code': 'ca', 'locale': 'ca_ES', 'name': 'Catalan'}
                 , {'iso_code': 'cs', 'locale': 'cs_CZ', 'name': 'Czech'}
                 , {'iso_code': 'cy', 'locale': 'cy_GB', 'name': 'Welsh'}
                 , {'iso_code': 'da', 'locale': 'da_DK', 'name': 'Danish'}
                 , {'iso_code': 'de', 'locale': 'de_DE', 'name': 'German'}
                 , {'iso_code': 'ee', 'locale': 'ee_EE', 'name': 'Ewe'}
                 , {'iso_code': 'el', 'locale': 'el_GR', 'name': 'Greek'}
                 , {'iso_code': 'en', 'locale': 'en_GB', 'name': 'English'}
                 , {'iso_code': 'en', 'locale': 'en_GB', 'name': 'English (Great Britain)'}
                 , {'iso_code': 'en', 'locale': 'en_AU', 'name': 'English (Australia)'}
                 , {'iso_code': 'en', 'locale': 'en_NZ', 'name': 'English (New Zealand)'}
                 , {'iso_code': 'en', 'locale': 'en_US', 'name': 'English (United States)'}
                 , {'iso_code': 'en', 'locale': 'en_US', 'name': 'English (US)'}
                 , {'iso_code': 'es', 'locale': 'es_ES', 'name': 'Spanish'}
                 , {'iso_code': 'es', 'locale': 'es_AR', 'name': 'Spanish (Argentina)'}
                 , {'iso_code': 'es', 'locale': 'es_MX', 'name': 'Spanish (Mexico)'}
                 , {'iso_code': 'et', 'locale': 'et_EE', 'name': 'Estonian'}
                 , {'iso_code': 'eo', 'locale': 'eo', 'name': 'Esperanto'}
                 , {'iso_code': 'eu', 'locale': 'eu_ES', 'name': 'Basque'}
                 , {'iso_code': 'fa', 'locale': 'fa_AF', 'name': 'Persian'}
                 , {'iso_code': 'fa', 'locale': 'fa_AF', 'name': 'Persian (Afghanistan)'}
                 , {'iso_code': 'fa', 'locale': 'fa_IR', 'name': 'Persian (Iran)'}
                 , {'iso_code': 'fi', 'locale': 'fi_FI', 'name': 'Finnish'}
                 , {'iso_code': 'fo', 'locale': 'fo_FO', 'name': 'Faroese'}
                 , {'iso_code': 'fr', 'locale': 'fr_FR', 'name': 'French'}
                 , {'iso_code': 'fr', 'locale': 'fr_CA', 'name': 'French (Canadian)'}
                 , {'iso_code': 'fr', 'locale': 'fr_CA', 'name': 'French (Canada)'}
                 , {'iso_code': 'fy', 'locale': 'fy_DE', 'name': 'Western Frisian'}
                 , {'iso_code': 'gl', 'locale': 'gl_ES', 'name': 'Galician'}
                 , {'iso_code': 'gl', 'locale': 'gl_ES', 'name': 'Gallego'}
                 , {'iso_code': 'he', 'locale': 'he_IL', 'name': 'Hebrew'}
                 , {'iso_code': 'hi', 'locale': 'hi_IN', 'name': 'Hindi (India)'}
                 , {'iso_code': 'hi', 'locale': 'hi_IN', 'name': 'Hindi (Devanagiri)'}
                 , {'iso_code': 'hr', 'locale': 'hr_HR', 'name': 'Croatian'}
                 , {'iso_code': 'ht', 'locale': 'ht_HT', 'name': 'Haitian (Haitian Creole)'}
                 , {'iso_code': 'hu', 'locale': 'hu_HU', 'name': 'Hungarian'}
                 , {'iso_code': 'hy', 'locale': 'hy_AM', 'name': 'Armenian'}
                 , {'iso_code': 'id', 'locale': 'id_ID', 'name': 'Indonesian'}
                 , {'iso_code': 'is', 'locale': 'is_IS', 'name': 'Icelandic'}
                 , {'iso_code': 'it', 'locale': 'it_IT', 'name': 'Italian'}
                 , {'iso_code': 'ja', 'locale': 'ja_JP', 'name': 'Japanese'}
                 , {'iso_code': 'ka', 'locale': 'ka_GE', 'name': 'Georgian'}
                 , {'iso_code': 'ko', 'locale': 'ko_KR', 'name': 'Korean'}
                 , {'iso_code': 'lt', 'locale': 'lt_LT', 'name': 'Lithuanian'}
                 , {'iso_code': 'lv', 'locale': 'lv_LV', 'name': 'Latvian'}
                 , {'iso_code': 'mi', 'locale': 'mi', 'name': 'Maori'}
                 , {'iso_code': 'mk', 'locale': 'mk_MK', 'name': 'Macedonian'}
                 , {'iso_code': 'ml', 'locale': 'ml_IN', 'name': 'Malayalam'}
                 , {'iso_code': 'ml', 'locale': 'ml_IN', 'name': 'Malayalam (India)'}
                 , {'iso_code': 'mn', 'locale': 'mn_MN', 'name': 'Mongolian (Mongolia)'}
                 , {'iso_code': 'ms', 'locale': 'ms_MY', 'name': 'Malaysian'}
                 , {'iso_code': 'ms', 'locale': 'ms_MY', 'name': 'Malay'}
                 , {'iso_code': 'mt', 'locale': 'mt_MT', 'name': 'Maltese'}
                 , {'iso_code': 'my', 'locale': 'my_MM', 'name': 'Burmese'}
                 , {'iso_code': 'my', 'locale': 'my_MM', 'name': 'Burmese (Myanmar)'}
                 , {'iso_code': 'nl', 'locale': 'nl_NL', 'name': 'Dutch'}
                 , {'iso_code': 'no', 'locale': 'nb_NO', 'name': 'Norwegian'}
                 , {'iso_code': 'pl', 'locale': 'pl_PL', 'name': 'Polish'}
                 , {'iso_code': 'pt', 'locale': 'pt_PT', 'name': 'Portuguese'}
                 , {'iso_code': 'pt', 'locale': 'pt_BR', 'name': 'Portuguese (Brazillian)'}
                 , {'iso_code': 'pt', 'locale': 'pt_BR', 'name': 'Portuguese (Brazil)'}
                 , {'iso_code': 'ro', 'locale': 'ro_RO', 'name': 'Romanian'}
                 , {'iso_code': 'ru', 'locale': 'ru_RU', 'name': 'Russian'}
                 , {'iso_code': 'se', 'locale': 'se_SE', 'name': 'Northern Sami'}
                 , {'iso_code': 'sk', 'locale': 'sk_SK', 'name': 'Slovak'}
                 , {'iso_code': 'sl', 'locale': 'sl_SI', 'name': 'Slovenian'}
                 , {'iso_code': 'sl', 'locale': 'sl_SI', 'name': 'Slovenian (Slovenia)'}
                 , {'iso_code': 'sq', 'locale': 'sq_AL', 'name': 'Albanian'}
                 , {'iso_code': 'sr', 'locale': 'sr_RS', 'name': 'Serbian'}
                 , {'iso_code': 'sr', 'locale': 'sr_RS', 'name': 'Serbian (Cyrillic)'}
                 , {'iso_code': 'sr', 'locale': 'sr_RS@latin', 'name': 'Serbian (latin)'}
                 , {'iso_code': 'sv', 'locale': 'sv_SE', 'name': 'Swedish'}
                 , {'iso_code': 'szl', 'locale': 'szl', 'name': 'Silesian'}
                 , {'iso_code': 'ta', 'locale': 'ta_IN', 'name': 'Tamil (India)'}
                 , {'iso_code': 'te', 'locale': 'te_IN', 'name': 'Telugu (India)'}
                 , {'iso_code': 'tg', 'locale': 'tg_tj', 'name': 'Tajik'}
                 , {'iso_code': 'th', 'locale': 'th_TH', 'name': 'Thai'}
                 , {'iso_code': 'tr', 'locale': 'tr_TR', 'name': 'Turkish'}
                 , {'iso_code': 'tt', 'locale': 'tt', 'name': 'Tatar'}
                 , {'iso_code': 'uk', 'locale': 'uk_UA', 'name': 'Ukrainian'}
                 , {'iso_code': 'uz', 'locale': 'uz_UZ', 'name': 'Uzbek'}
                 , {'iso_code': 'vi', 'locale': 'vi_VN', 'name': 'Vietnamese'}
                 , {'iso_code': 'vi', 'locale': 'vi_VN', 'name': 'Vietnamese (Viet Nam)'}
                 , {'iso_code': 'zh', 'locale': 'zh_CN', 'name': 'Chinese (China)'}
                 , {'iso_code': 'zh', 'locale': 'zh_CN', 'name': 'Chinese (Simple)'}
                 , {'iso_code': 'zh', 'locale': 'zh_TW', 'name': 'Chinese (Taiwan)'}
                 , {'iso_code': 'zh', 'locale': 'zh_TW', 'name': 'Chinese (Traditional)'}
                 ]

if len(sys.argv) != 2:
    print("Too many or to few arguments. Exitting.")
    exit(1)

TARGET_FOLDER = sys.argv[1]

if not os.path.isdir(TARGET_FOLDER):
    print("%s is not a folder. Exitting." % TARGET_FOLDER)
    exit(1)
else:
    # Addon.xml conversion
    for item in LANGUAGE_LIST:
        fileToSearch = os.path.join(TARGET_FOLDER, "addon.xml")
        textToSearch = "\"%s\"" % item["iso_code"]
        textToReplace = "\"%s\"" % item["locale"]

        # Read in the file
        with open(fileToSearch, 'r', encoding="utf8") as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(textToSearch, textToReplace)

        # Write the file out again
        with open(fileToSearch, 'w', encoding="utf8") as file:
            file.write(filedata)

    # Find language folders
    data = etree.parse(fileToSearch).getroot()
    addonid = data.get('id')

    if addonid.startswith('skin.'):
        LANGUAGE_FOLDER = os.path.join(TARGET_FOLDER, "language")
    else:
        LANGUAGE_FOLDER = os.path.join(TARGET_FOLDER, "resources", "language")
    if os.path.isdir(LANGUAGE_FOLDER):
        SUBFOLDERS = next(os.walk(LANGUAGE_FOLDER))[1]
    else:
        print("Done converting.")
        exit(0)

    # Language file conversion
    engFile = os.path.join(LANGUAGE_FOLDER, "English", "strings.xml")
    if os.path.exists(engFile):
        root = etree.parse(engFile).getroot()
        strings = root.findall('string')
        engDict = {}
        for string in strings:
          sid = string.get("id")
          text = string.text
          engDict[sid] = text

        # Update english language file
        newText = 'msgid ""\nmsgstr ""\n\n'
        for k,v in engDict.items():
           newText = newText + 'msgctxt "' + k + '"\n' + 'msgid "' + v + '"\nmsgstr ""\n\n'

        newFile = os.path.join(LANGUAGE_FOLDER, "English", "strings.po")
        with open(newFile, 'w', encoding="utf8") as file:
            file.write(newText)

        os.remove(engFile)

        # Update other language files
        for folder in SUBFOLDERS:
            if folder != 'English':
                langFile = os.path.join(LANGUAGE_FOLDER, folder, "strings.xml")
                root = etree.parse(langFile).getroot()
                strings = root.findall('string')
                strDict = {}

                for string in strings:
                    sid = string.get("id")
                    text = string.text
                    strDict[sid] = text

                # Update the language file
                newText = 'msgid ""\nmsgstr ""\n\n'
                for k,v in strDict.items():
                    if k in engDict:
                        newText = newText + 'msgctxt "' + k + '"\n' + 'msgid "' + engDict[k] + '"\nmsgstr "' + v + '"\n\n'

                newFile = os.path.join(LANGUAGE_FOLDER, folder, "strings.po")
                with open(newFile, 'w', encoding="utf8") as file:
                    file.write(newText)

                os.remove(langFile)

    # Language folder conversion
    for folder in SUBFOLDERS:
        try:
            match = next(
                language for language in LANGUAGE_LIST if language["name"] == folder)
            print("Matching %s to %s" % (folder, match['locale']))
            old_folder_path = os.path.join(LANGUAGE_FOLDER, folder)
            new_folder_path = os.path.join(LANGUAGE_FOLDER, "resource.language." + match['locale'])
            try:
                os.rename(old_folder_path, new_folder_path)
            except FileExistsError:
                print("'%s' already exists. Might have been converted wrongly." % new_folder_path)

        except StopIteration:
            print("Can't find match for '%s'" % folder)

    print("Done converting.")
    exit(0)
