import json
import pickle


class Airplane:

    def __init__(self, model: str, seats: int, _range: int):
        self.__model = model
        self.__seats = seats
        self.__range = _range

    def get_model(self):
        return self.__model

    def get_seats(self):
        return self.__seats

    def get_range(self):
        return self.__range

    def print_airplane_props(self):
        print(
            f"airplane model: {self.__model} has {self.__seats} available "
            f"seats and has {self.__range} km max distance flight"
        )


def pickle_object(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


def unpikle_object(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


class JSONDataAdapter:

    @classmethod
    def to_json(cls, obj):
        if isinstance(obj, Airplane):
            return json.dumps({
                'model': obj.get_model(),
                'seats': obj.get_seats(),
                'range': obj.get_range(),
                'class': obj.__class__.__name__,
                'methods': {
                    'get_model': obj.get_model(),
                    'get_seats': obj.get_seats(),
                    'get_range': obj.get_range(),
                    'print_airplane_props':
                        f'printed data:{[f'airplane model: {obj.get_model()} has {obj.get_seats()} available', 
                                                             f'seats and has {obj.get_range()} km max distance flight']} ',
                }
            }, ensure_ascii=False, indent=2)

    @classmethod
    def from_json(cls, obj):
        obj = json.loads(obj)

        try:
            model = obj['model']
            seats = obj['seats']
            _range = obj['range']
            plane = Airplane(model, int(seats), int(_range))
            return plane
        except AttributeError:
            print('Неверная структура!')


if __name__ == '__main__':
    plane = Airplane('Boeing 737-200', 110, 4000)
    plane_json = JSONDataAdapter.to_json(plane)
    print(plane_json)
    plane_obj = JSONDataAdapter.from_json(plane_json)
    plane_obj.print_airplane_props()
