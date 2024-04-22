"""Model for aircraft flights"""

class Flight:
    def __init__(self, number, aircraft) -> None:
        # could optionally add checks that first two chars are uppercase letters followed by a 4-digit number
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]



    def aircraft_model(self):
        return self._aircraft.model()


    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]
    
    

class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row) -> None:
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1,self._num_rows+1), 
                "ABCDEFGHJKLM"[:self._num_seats_per_row])
    
