# DON`T CHANGE THIS FILE (path of pc-stat-bot)
#   official translate by Agzes (developer)
#             version: 4.0.0 


language_name = "en"
language_full_name = "English"
translations = {
    "user": {
        "greeting": "Hello, {UserName}"
    },
    "tab_bar": {
        "home": "  Home  ",
        "terminal": "Terminal",
        "statistics": "Statistics",
        "plugins": "Plugins",
        "dark": ' "Dark" ',
        "panel": "Panel*",
        "settings": "Settings",
    },
    "home_tab": {
        "feedback": "Feedback",
        "license_agreement": "License Agreement",
        "project_page": "Project Page"
    },
    "terminal_tab": {
        "label": "Terminal",
    },
    "statistics_tab": {
        "label": "Statistics",
        "cpu": "CPU: ",
        "GPU_Cores": "CPU cores: ",
        "ram_occupied": "Occupied RAM:",
        "free_ram": "Free RAM: ",
        "total_ram": "Total RAM:",
        "gpu": "GPU: ",
        "other": "Other: ",
        "total_online": "Total online: ",
        "time": "Time: ",
        "auto_stat_update": "automatic statistics update",
        "save": "save",
        "update": "update",
    },
    "plugins_tab": {
        "label": "Plugins",
        "for_dark": 'For "Dark"',
        "more": "More",
        "ai_functions_dark": "AI Functions*",
        "for_telegram_bot": "For Telegram Bot",
        "mouse_control": "Mouse Control",
        "keyboard_control": "Keyboard Control",
        "ai_functions": "AI Functions*",
        "files_control": "Files Control",
        "other": "Other",
        "pc_monitoring": "PC Monitoring",
    },
    "dark_tab": {
        "settings": "Set\ntin\ngs",
        "info": """# Warning!\n**dark is now in alpha (+_+)**""",
    },
    "panel_tab": {
        "label": "v4 | Pc-Stat-Bot | Panel",
        "in_dev": "# In development",
        "soon_ver410": """<font color="(155, 155, 155)">soon, in version 4.1.0</font>""",
    },
    "settings_tab": {
        "label": "Settings",
        "main": "## Main:",
        "name": "Name (what to call you)",
        "token": "Token",
        "telegram_id": "Telegram ID",
        "additionally": "## Additionally:",
        "web_hook": "Web-hook",
        "discord_token": "Discord token",
        "functions": "## Functions:",
        "auto_screen": "auto-screen",
        "auto_info": "auto-info",
        "security": "## Security:",
        "login": "Login",
        "password": "Password",
        "interface": "## Interface:",
        "theme": "Theme",
        "save": "Save",
    },
    "dark_assistant": {
        "done": "**[Dark]:** done!",
        "think": "**[Dark]:** Think...",
        "msg": "**[Dark]:** {mesage}",
        "command_not_recognized": "Command or speech is not recognized :c",
        "you_voice": "[You][Voice]:** {dark_recognize}",
        "you": "**[You]:** {temp_msg}",
        "error_speech_recognize": "Error with recognize Voice",
        "error_with_response": "Error with response to recognize Voice",
        "hi": "",
        "bye": "",
    },
    "ui_tools": {
        "close": "close",
        "more": "[more]",
        "error_name": "Error: Name is null!",
        "error_token": "Error: No token!",
        "error_token_incorrect": "Error: The token is not in the right format!",
        "error_id": "Error: id not entered!",
        "error_auto-screen_time": "Error: The time in Auto-Screenshots is not correct!\nUse values from 1 to 999",
        "error_auto-information_time": "Error: The time in Auto-Statistics is not correct!\nUse values from 1 to 999",
        "error_time": "Mistake!\nThe time for the update should be from 1 to 999",
        "saved": "Saved!",
        "new_update": "A new version is available! Latest version: {file_content}, your version: {version}",
        "error_check_update": "Error with check for update. Response from server: {data}",
        "ui_notification": "Notification!",
        "ui_information": "Information",
    },
    "statistics": {
        "cpu": "CPU: {info}%",
        "cpu_core": "CPU cores: {data}",
        "cpu_core_i": "{i} core: {percent}%",
        "memory_occupied": "Occupied RAM: {data} GB",
        "memory_free": "Free RAM: {data} GB",
        "memory_total": "{data} GB",
        "gpu": "GPU: {data}",
        "time": "Time: {data}",
        "program_on": "Total online: {data}",
    },
    "ui_back": {
        "info_about_ai_functions_dark": """AI Functions (for “Dark”) \nVersion: 1.1.0 | Type: Add-on for "Dark" \nAdds AI functions for "Dark" """,
        "info_about_mouse_control": "Mouse control \nVersion: 1.1.0 | Type: plugin for telegram bot \nAdds Mouse Control Function to Telegram Bot",
        "info_about_keyboard_control": "Keyboard Control\nVersion: 2.0 | Type: Add-on for Telegram\nAdds keyboard control functions for Telegram bot",
        "info_about_ai_functions": """AI Functions (for Telegram bot)\nVersion: 1.1.0 | Type: Add-on for Telegram\nAdds AI functions for Telegram bot""",
        "info_about_data_functions": """Version: 1.1.0 | Type: Add-on for Telegram\nAdds files control for Telegram bot""",
        "info_about_monitoring_pc": """PC Monitoring\nVersion: 1.0.0 | Type: Other\nPC Monitoring and all""",
        "dark_have_no_settings": """At the moment, "Dark" has no settings""",
    },
}

telegram_bot = {
    "main": {
        "pc-stat-bot": "| Pc-Stat-Bot | beta 4.0 |",
        "initialization": "[Telegram BOT][Status]: Initialization",
        "checking_data": "[Telegram BOT][Information]: Checking your settings",
        "entering_data": "[Telegram BOT][Information]: Entering data for the bot",
        "init_keyboard0": "[Telegram BOT][Information]: Initializing the keyboard [0/]",
        "init_keyboard1": "[Telegram BOT][Information]: Initializing the keyboard: music management [1/4]",
        "init_keyboard2": "[Telegram BOT][Information]: Initializing the keyboard: video management [2/4]",
        "init_keyboard3": "[Telegram BOT][Information]: Initializing the keyboard: volume management [3/4]",
        "init_keyboard4": "[Telegram BOT][Information]: Initializing the keyboard: PC management [4/4]",
        "init_keyboard5": "[Telegram BOT][Information]: Initializing the keyboard: [Plugin] KeyBoard management [5/8]",
        "init_keyboard6": "[Telegram BOT][Information]: Initializing the keyboard: [Plugin] Mouse management [6/8]",
        "init_keyboard7": "[Telegram BOT][Information]: Initializing the keyboard: [Plugin] Data management [7/8]",
        "init_keyboard8": "[Telegram BOT][Information]: Initializing the keyboard: [Plugin] AI [8/8]",
        "greetings": "| Pc-Stat-Bot | beta 4.0 |\nHello, {name}.",
        "initialized": "[Telegram BOT][Status]: KeyBoard initialized",
        "initialization_command": "[Telegram BOT][Status]: Initializing the commands",
        "user_greetings": "",
        "log_in": "| Pc-Stat-Bot | beta 4.0 |\n🔐 Log in using /login {login} {password}",
        "warning": "[Telegram BOT][Warning]: {id} pressed a button in the menu or entered something",
        "already_login": "| Pc-Stat-Bot | beta 4.0 |\nYou already authorized!",
        "checking_data_from_user": "[Telegram BOT][Status]: {id} wants to log in, checking his data",
        "successful_login": "| Pc-Stat-Bot | beta 4.0 |\nAuthorization is successful!\n Welcome to Panel!\n⚠️ When restarting the bot , you will not be logged in ⚠️",
        "successful_login_terminal": "[Telegram BOT][Status]: {id} successfully logged in",
        "incorrect_data": "[Telegram BOT][Warning]: {id} gave incorrect data",
        "incorrect_pass_or_login": "| Pc-Stat-Bot | beta 4.0 |\nYou have given an incorrect username or password!",
        "incorrect_no_data": "| Pc-Stat-Bot | beta 4.0 |\nThere is not enough data!\nUse /login {login} {password}",
        "any_write_terminal": "[Telegram BOT][Warning]: {id} pressed a button in the menu or entered something",
        "any_write": "",
        "command_initialized": "[Telegram BOT][Status]: The commands are initialized",
        "interacting_processing": "[Telegram BOT][Information]: {id} was interacting with something, processing information",
        "bot_start": "[Telegram BOT][Status]: The bot is running!",
        "pc_stat_bot_label": "| Pc-Stat-Bot | beta 4.0 |",
        "sure_to_turn_off": "| Pc-Stat-Bot | beta 4.0 |\nAre you sure you want to turn off the bot?\nUse the /off_bot command to turn off",
        "successful": "| Pc-Stat-Bot | beta 4.0 | ✅",
        "sure_to_hibernate": "| Pc-Stat-Bot | beta 4.0 |\nAre you sure you want to put your PC into hibernation mode?\nUse the /hibernation command to switch to hibernation mode",
        "sure_to_reboot": "| Pc-Stat-Bot | beta 4.0 |\nAre you sure you want to restart your PC?\n Use the /reboot command to reboot",
        "sure_to_shutdown": "| Pc-Stat-Bot | beta 4.0 |\nAre you sure you want to turn off your PC?\n Use the /shutdown command to turn off",
        "battery_connected": "| Pc-Stat-Bot | beta 4.0 |\nBattery is connected!\ncheck if the charger is connected",
        "power_connected": "| Pc-Stat-Bot | beta 4.0 |\nThe charger is connected! \Charge: {data}",
        "power_not_connected": "| Pc-Stat-Bot | beta 4.0 |\nThe charger is not connected!\Charge: {data}",
        "battery_not_connected": "| Pc-Stat-Bot | beta 4.0 |\nBattery is not connected!",
        "emptying_trash": "| Pc-Stat-Bot | beta 4.0 |\nI'm emptying the trash...",
        "write_text": "| Pc-Stat-Bot | beta 4.0 | Write: {data}",
        "write_under": "| Pc-Stat-Bot | beta 4.0 | Write⤵️",
        "select_disk": "| Pc-Stat-Bot | beta 4.0 |\n| Select disk:",
        "write_path_to_file": "| Pc-Stat-Bot | beta 4.0 |\nWrite path to file",
        "send_need_file": "| Pc-Stat-Bot | beta 4.0 |\nSend file",
        "file_downloading": "| Pc-Stat-Bot | beta 4.0 |\nYour file is being uploaded, wait.",
        "incorrect_path_to_file": "| Pc-Stat-Bot | beta 4.0 |\nMistake: the path is incorrect or the file does not exist",
        "successful_download_file_in_pc_stat_bot": "| Pc-Stat-Bot | beta 4.0 |\nSuccessfully. The file will be in the folder with the bot",
        "error_send_file_as_doc": "| Pc-Stat-Bot | beta 4.0 |\nError: Send the file as a document",
        "send_your_request": "| Pc-Stat-Bot | beta 4.0 |\nSend your request",
        "processed_the_request": "| Pc-Stat-Bot | beta 4.0 |\n{data}",
        "successful_with_key":  "| Pc-Stat-Bot | beta 4.0 |\n {tmp_status} ✅",
        "worked": "[Telegram BOT][Information]: Processed the request from {id}",
    },
    "data_plugin": {
        "decided_download": "[Telegram BOT][Information]: {id} decided to download the file, uploading it",
        "decided_not_download_terminal": "[Telegram BOT][Information]: {id} decided not to download the file",
        "decided_not_download": "| Pc-Stat-Bot | beta 4.0 | 🆗",
        "walks_in_directories": "[Telegram BOT][Information]: {id} walks through the directories",
        "click_to_file": "[Telegram BOT][Information]: {id} clicked on the file, ask for further actions",
        "click_to_file_terminal": "| Pc-Stat-Bot | beta 4.0 | Do you want to download this file?",

    },
    "keyboards": {
        "keyboard_need": {
            "back": "| 🔙 Back 🔙 |",
            "back_to_main": "| 🔚 Back 🔚 |",
        },
        "main_keyboard": {
            "bot_management": "| 🕹️ Bot Management 🤖 |",
            "music_management": "| 🕹️ Music Management 🎵 |",
            "video_management": "| 🕹️ Video Management 📼 |",
            "sound_management": "| 🕹️ Sound Management 🔈|",
            "pc_management": "| 🕹️ PC Management 🖥️ |",
            "plugins": "| ➕ Plugins ➕ |",
        },
        "bot_control_keyboard": {
            "information": "| ℹ️ Information ℹ️ |",
            "shutdown": "| 🔴 Shutdown 🔴 |",
        },
        "music_keyboard": {
            "prev": "⏮️",
            "play": "⏯️",
            "next": "⏭️",
        },
        "video_keyboard": {
            "prev": "⏪",
            "play": "⏸▶️",
            "next": "⏩",
        },
        "volume_keyboard": {
            "minus": "🔉",
            "off": "🔇",
            "plus": "🔊",
        },
        "pc_keyboard": {
            "hibernation": "⚪Hibernation⚪",
            "shutdown": "🔴Shutdown🔴",
            "reboot": "⭕Reboot⭕",
            "lock": "🔒Lock🔒",
            "statistics": "📊Statistics📊",
            "explorer": "📁Explorer📁",
            "close_window": "❌Close window❌",
            "screenshot": "🎦Screenshot🎦",
            "collapse_all": "⬛Collapse all⬛",
            "enter": "⏭Enter⏭",
            "battery": "🔋Battery🔋",
            "clear_cart": "🗑️Clear cart🗑️",
            "list_of_program": "📃List of programs📃",
        },
        "plugin_keyboard": {
            "keyboard": "| ⌨️ KeyBoard management ⌨️ |",
            "mouse": "| 🖱️ Mouse management 🖱️ |",
            "data": "| 💻️ Data management 💻️ |",
            "ai": "| 🧑‍💻 AI 🧑‍💻 |",
        },
        "mouse_keyboard": {
            "left": "⬅️",
            "left_top": "↖️",
            "top": "⬆️",
            "right_top": "↗️",
            "right": "➡️",
            "right_bottom": "↘️",
            "bottom": "⬇️",
            "left_bottom": "↙️",
            "click": "⏺️",
            "screenshot": "🎦Screenshot🎦",
            "click_left": "⏺ RB ⏺",
            "click_right": "⏺ LB ⏺",
        },
        "plugin_keyboard_keyboard": {
            "write": "⌨️ Write ⌨️",
            "screenshot": "🎦Screenshot🎦",
            "change_language": "Change Language",
        },
        "data_keyboards": {
            "files": "📂 Files 📂",
            "download": "⬆️Download from PC⬆️",
            "upload": "⬇️Upload on PC⬇️",
        },
        "ai_keyboards": {
            "ask": "❓ Ask ❓",
        },
    }
}


dark_translate = {
    "hi": "Hi!",
    "bye": "Bye!",
    "not_recognized": "Command or speech is not recognized :c",  
}

parameters = {
    "tab_weight": {
        "home": 0,
        "terminal": 78,
        "statistics": 149,
        "plugins": 234,
        "dark": 298,
        "panel": 369,
        "settings": 426,
    }
}