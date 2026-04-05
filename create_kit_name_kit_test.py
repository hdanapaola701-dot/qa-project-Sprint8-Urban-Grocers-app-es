import data
import sender_stand_request



def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body

def get_new_user_token():
    respose = sender_stand_request.post_new_user(data.user_body)
    return respose.json()["authToken"]

def possitive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 201

def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 400



def test_1_crear_kit_con_1_caracter():
    current_body = get_kit_body("A")
    possitive_assert(current_body)

def test_2_crear_kit_con_511_caracteres():
    current_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    possitive_assert(current_body)

def test_3_crear_kit_vacio():
    current_body = get_kit_body("")
    negative_assert(current_body)


def test_4_crear_kit_con_512_caracteres():
    current_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(current_body)

def test_5_crear_kit_con_caracteres_especiales():
    current_body = get_kit_body("$%@/")
    possitive_assert(current_body)

def test_6_crear_kit_con_espacios():
    current_body = get_kit_body("dana paola")
    possitive_assert(current_body)


def test_7_crear_kit_donde_se_permiten_numeros():
    current_body = get_kit_body("1234")
    possitive_assert(current_body)


def test_8_el_parametro_no_se_pasa_a_la_solicitud():
    current_body = {}
    negative_assert(current_body)

def test_9_crea_kit_con_un_parametro_diferente():
    current_body = {"name": 123}
    negative_assert(current_body)
