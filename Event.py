
class event:
    _event = []

    def add(self, datetime, message):
        self._event.append({'datetime': datetime, 'message': message})

    