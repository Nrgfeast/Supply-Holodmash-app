import streamlit as st

st.set_page_config(page_title="Запрос на материал", page_icon="📦")

st.title("Форма запроса на материал")

# Ввод данных
material = st.text_input("Материал")
quantity = st.text_input("Количество")
unit = st.selectbox("Единица измерения", ["шт", "кг", "л", "м", "другое"])
requirements = st.text_area("Дополнительные требования")

# Кнопка отправки
if st.button("Отправить запрос"):
    if material and quantity:
        st.success(f"Запрос на **{material}** в количестве **{quantity} {unit}** успешно создан!")
        st.info("Дальнейшие шаги (например, отправка письма) будут добавлены в следующих версиях.")
    else:
        st.warning("Пожалуйста, заполните поля 'Материал' и 'Количество'.")
