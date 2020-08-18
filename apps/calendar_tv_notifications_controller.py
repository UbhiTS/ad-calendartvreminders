import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, time

#
# TV Calendar Notifications Controller App
#
# Args:
# tv_calendar_notifications:
#  module: calendar_tv_notifications_controller
#  class: CalendarTVNotificationsController
#  tv: media_player.tv_living_room
#  calendars:
#    - calendar.important_dates
#    - calendar.holidays_in_united_states
#  notifications:
#    service: notify/tv_living_room
#    triggers:
#      - 5
#  debug: false

class TVCalendarNotificationsController(hass.Hass):

  def initialize(self):

    self.debug = True
    
    self.tv = self.args["tv"]
    self.calendars = self.args["calendars"]
    self.service = self.args["notifications"]["service"]
    self.triggers = self.args["notifications"]["triggers"]
    
    self.debug = bool(self.args["debug"]) if "debug" in self.args else self.debug
    
    self.listen_state(self.tv_switched_on, self.tv, attribute = "state", old = "off", new = "on")
    
    if self.debug: self.show_notification(None)


  def tv_switched_on(self, entity, attribute, old, new, kwargs):
    
      for trigger in self.triggers:
        self.run_in(self.show_notification, trigger)


  def show_notification(self, kwargs):
    
    delay = 0
    for event in self.calendar_events():
      self.run_in(self.notify_tv, delay, event = event)
      delay = delay + 5
      
      
  def calendar_events(self):
    
    messages = []
    
    for calendar in self.calendars:
      event = self.get_state(calendar, attribute="all")
      event_message = event["attributes"]["message"]
      event_date_str = event["attributes"]["start_time"]
      event_date = datetime.strptime(event_date_str, '%Y-%m-%d %H:%M:%S')
      current_date = datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
      event_days_remaining = event_date - current_date
      
      event_message = event_message.replace("&","&amp;")
      event_message = event_message.replace("<","&lt;")
      event_message = event_message.replace(">","&gt;")
      
      if event_days_remaining.days == 0:
        messages += [ event_message + '<br/>Today' ]
      elif event_days_remaining.days == 1:
        messages += [ event_message + '<br/>Tomorrow' ]
      elif event_days_remaining.days <= 15:
        messages += [ event_message + '<br/>' + str(event_days_remaining.days) + ' days<br/>' + event_date.strftime("%d %b %Y") ]
      
    return messages


  def notify_tv(self, kwargs):
    
    event = kwargs['event']
    if self.debug: self.log("TV NOTIFY: " + event)

    self.call_service(self.service, message = event)
