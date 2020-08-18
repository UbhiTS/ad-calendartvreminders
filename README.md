# :tv::calendar: Calendar TV Notifications :chicken:

If you're like me :sleeping:, who forgets important days in the year, like a friends birthday :birthday:, anniversary :gift:, and insurance due date :motorcycle: etc; say hello to the HA Calendar TV Notifications :tv::calendar: App. This app will (like a faithful assistant) keep reminding you **every time you turn on your TV** about the upcoming events in the next 15 days. I'm sure you turn on your TV atleast once a day, so there is absolutly no chance that you will ever forget an important day of the year, if your TV is the one reminding you about it :stuck_out_tongue_winking_eye:

This app has been a lifesaver. My family and friends are now plesantly surprised at how good I am at remembering birthdays. Little do they know ;)

Please ⭐ this repo if you like my work and also check out my other repos like
- [Home Assistant 'STEROIDS' Configuration](https://github.com/UbhiTS/ha-config-ataraxis)
- [Alexa (& Friends) Talking Clock](https://github.com/UbhiTS/ad-alexatalkingclock)
- [Alexa (& Friends) Doorbell](https://github.com/UbhiTS/ad-alexadoorbell)
- [Alexa (& Friends) Door/Window Announce](https://github.com/UbhiTS/ad-alexadoorwindowannounce)
- [Alexa (& Friends) Smart Talking Thermostat](https://github.com/UbhiTS/ad-alexasmarttalkingthermostat)
- [Auto 'Crappy Internet' Rebooter](https://github.com/UbhiTS/ad-autointernetrebooter)

Also, if you want to see a walkthrough of my Home Assistant configuration, I have my video walkthrough on youtube below
- [Home Automation on 'STEROIDS' : Video Walkthrough](https://youtu.be/qqktLE9_45A)

## Installation
**Needs the following integrations to work**
- [Google Calendar](https://www.home-assistant.io/integrations/calendar.google/)
- [LG WebOS Smart TV](https://www.home-assistant.io/integrations/webostv/)

Use [HACS](https://github.com/custom-components/hacs) or [download](https://github.com/UbhiTS/ad-tvcalendarnotifications) the `tv_calendar_notifications_controller.py` from inside the `apps` directory to your local `apps` directory, and add the configuration to enable the app.

### Configuration (config/appdaemon/apps/apps.yaml)
```yaml
tv_calendar_notifications:
  module: tv_calendar_notifications_controller
  class: TVCalendarNotificationsController
  tv: media_player.tv_living_room
  calendars:
    - calendar.important_dates
    - calendar.holidays_in_united_states
  notifications:
    service: notify/tv_living_room
    triggers:
      - 5
      - 300
  debug: false
```

key | description
-- | --
`module` | The module name of the app
`class` | The name of the Class
`tv` | The TV (media_player) to send the notification to. **Currently tested with only LG WebOS Smart TVs**
`calendars` | The Google Calendars (list, one or multiple) to query
`notifications/service` | The TV Notifications Service to be called for your TV. Normally it's "notify/<your tv name>"
`notifications/triggers` | From the moment the TV turns on, after how many seconds to send the notifications to the TV. You may define multiple triggers, e.g. 5 seconds, 5 minutes (300 seconds)
`debug` | if True, outputs messages to the AppDaemon Log

## Thank you! :raised_hands:
If you like my work and feel gracious, you can buy me a beer below ;)

Currently tested and working with LG WebOS Smart TVs, but hopefully it will work with other Smart TVs. If your TV does not work, feel free to log a bug or CR to the repo and I'll try to get it working at the earliest.

<a href="https://www.buymeacoffee.com/ubhits" target="_blank">
<img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"
     alt="Buy Me A Beer" 
     style="height:41px !important; width:174px !important;" />
</a>

# License
[Apache-2.0](LICENSE). By providing a contribution, you agree the contribution is licensed under Apache-2.0. This is required for Home Assistant contributions.
