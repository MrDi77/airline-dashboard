import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Настройка страницы
st.set_page_config(layout="wide", page_title="Airline Dashboard")

# Стили (можно добавить CSS для точного копирования дизайна)
st.markdown("""
<style>
    .sidebar .sidebar-content {
        background-color: #34495e;
        color: white;
    }
    .stButton button {
        background-color: #f39c12;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Боковое меню
with st.sidebar:
    st.image("https://via.placeholder.com/80", width=80)  # Замените на реальный аватар
    st.title("ALEX JOHNSON")
    st.write("alex.johnson@gmail.com")
    st.markdown("---")

    menu = ["Dashboard", "Flights", "Wallet", "Reports", "Statistics", "Settings"]
    choice = st.radio("📌 Меню", menu, index=0)

    st.markdown("---")
    st.subheader("🟢 Active Users")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.image("https://via.placeholder.com/40", width=40)
    with col2: st.image("https://via.placeholder.com/40", width=40)
    with col3: st.image("https://via.placeholder.com/40", width=40)
    with col4: st.image("https://via.placeholder.com/40", width=40)
    st.markdown("**+70**")
    st.image("https://via.placeholder.com/150x80?text=World+Map", use_column_width=True)

# Основной контент
if choice == "Dashboard":
    st.title("📊 Dashboard")

    # Карточки сверху
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: #e6b800; padding: 15px; border-radius: 10px; color: white;">
            <h4>Boeing 787</h4>
            <h2>$548</h2>
            <img src="https://via.placeholder.com/100x50?text=Boeing" style="float:right;">
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: #34495e; padding: 15px; border-radius: 10px; color: white;">
            <h4>Airbus 811</h4>
            <h2>$620</h2>
            <img src="https://via.placeholder.com/100x50?text=Airbus" style="float:right;">
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Последние поездки
    st.subheader("✈️ Last Trips")
    st.caption("Overview of latest month")

    data_trips = pd.DataFrame({
        'Name': ['John Doe', 'Martin Loiness'],
        'Email': ['john@gmail.com', 'martin_loi@gmail.com'],
        'Flight': ['Qatar', 'Emirates'],
        'Total Members': [5, 2],
        'Ticket Price': ['$56k', '$56k']
    })

    for _, row in data_trips.iterrows():
        col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 1, 1])
        with col1:
            st.image("https://via.placeholder.com/40", width=40)
        with col2:
            st.write(f"**{row['Name']}**")
            st.write(row['Email'])
        with col3:
            st.write(row['Flight'])
        with col4:
            st.markdown(f"<div style='background:#e6b800; padding:5px; border-radius:10px; text-align:center;'>{row['Total Members']}</div>", unsafe_allow_html=True)
        with col5:
            st.write(row['Ticket Price'])

    st.markdown("---")

    # Графики
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Flights Share")
        fig_donut = px.pie(
            values=[30, 25, 20, 25], 
            names=['Boeing', 'Airbus', 'Other', 'Charter'], 
            hole=0.5,
            color_discrete_sequence=["#e6b800", "#34495e", "#27ae60", "#2980b9"]
        )
        fig_donut.update_layout(showlegend=False)
        st.plotly_chart(fig_donut, use_container_width=True)

    with col2:
        st.subheader("Flights Schedule")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        data_schedule = pd.DataFrame({
            'Month': months,
            'Flights': [3, 5, 2, 4, 3]
        })
        fig_line = px.line(data_schedule, x='Month', y='Flights', markers=True)
        fig_line.update_traces(line_color='#e6b800')
        st.plotly_chart(fig_line, use_container_width=True)

elif choice == "Flights":
    st.title("✈️ Flights")
    st.write("Здесь будет информация о рейсах, расписании, загрузке самолётов.")

elif choice == "Wallet":
    st.title("💳 Wallet")
    st.write("Баланс, транзакции, оплаты.")

elif choice == "Reports":
    st.title("📈 Reports")
    st.write("Отчёты по доходам, расходам, эффективности.")

elif choice == "Statistics":
    st.title("📊 Statistics")
    st.write("Статистика по месяцам, маршрутам, авиакомпаниям.")

elif choice == "Settings":
    st.title("⚙️ Settings")
    st.write("Настройки аккаунта, уведомлений, интеграций.")