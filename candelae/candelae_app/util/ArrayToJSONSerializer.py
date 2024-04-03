from enum import Enum

from ..my_models.Candle import Candle

"""
Этот файл позволяет легко создавать map для любого массива. Это фактически самодельный сериализитор из массива в JSON
Сперва создаем Enum тип в RecordType, затем пишем статический метод в классе JSONRecordGetter, 
в котором возвращаем нужный json. Смотри пример в функции get_candle_record

"""


class RecordType(Enum):
    CANDLE = 1
    # ETC


class ArrayToJSONSerializer:

    @classmethod
    def __get_record_by_type(cls, record_type, object_to_json):
        json_type_to_record_map = {
            RecordType.CANDLE: ArrayToJSONSerializer.__get_candle_record(object_to_json)
        }
        return json_type_to_record_map[record_type]

    @staticmethod
    def __get_candle_record(candle: Candle) -> dict:
        return {"uid": candle.id, "name": candle.name, "story_id": candle.story_id}

    @staticmethod
    def get_dict_from_obj_list(objs_array, record_type, name_for_array_in_json) -> dict:
        objs_dict = {}
        objs_records = []
        for obj in objs_array:
            record = ArrayToJSONSerializer.__get_record_by_type(record_type, obj)
            objs_records.append(record)
        objs_dict[name_for_array_in_json] = objs_records
        return objs_dict
