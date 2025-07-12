import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from web_function import preprocess_dataframe, load_data  # Pastikan fungsi ini tersedia dan benar

# Descriptive names for the climate indicators in both languages
indicator_names_en = {
    'TS': 'Average Air Temperature at surface (°C)',
    'PRECTOTCORR': 'Rainfall (mm)',
    'WS10M': 'Average Wind Speed at 10 Meters Height (m/s)'
}

indicator_names_id = {
    'TS': 'Suhu Udara Rata-Rata pada permukaan (°C)',
    'PRECTOTCORR': 'Curah Hujan (mm)',
    'WS10M': 'Kecepatan Angin Rata-Rata pada Ketinggian 10 Meter (m/s)'
}

def plot_climate_indicator(df, indicator, lang):
    indicator_names = indicator_names_en if lang == "English" else indicator_names_id
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df[indicator], mode='lines', name=indicator))
    fig.update_layout(title=indicator_names[indicator],
                      xaxis_title='Date' if lang == 'English' else 'Tanggal',
                      yaxis_title=indicator_names[indicator],
                      template='plotly_dark')
    return fig

def app():
    lang = st.selectbox("Pilih Bahasa / Select Language", ["Bahasa Indonesia", "English"])

    if lang == "Bahasa Indonesia":
        st.title("Dashboard Pemantauan dan Prediksi Upwelling Berbasis Indikator Iklim di Danau Maninjau")
        st.markdown("""
            Selamat datang di Dashboard Pemantauan dan Prediksi Upwelling berbasis indikator iklim Danau Maninjau!
            Dengan menggabungkan data dalam setahun, potensi produksi ikan di Danau Maninjau dapat mencapai 196 ton. 
            Namun, perubahan iklim yang tidak menentu mengganggu kestabilan produksi ikan di Danau Maninjau.
        """)
        column_header = 'Deskripsi Kolom dari Tabel'
        tampilan_header = 'Tampilan Data Historis'
        column_description = """
        1. DATE         : Tanggal indikator iklim
        2. TS           : Suhu udara rata-rata pada permukaan (°C)
        3. PRECTOTCORR  : Curah hujan (mm)
        4. WS10M        : Kecepatan angin rata-rata pada ketinggian 10 meter (m/s)
        5. Cluster      : Potensi Kejadian Upwelling
        """
    else:
        st.title("Climate Indicator-Based Upwelling Monitoring and Prediction Dashboard in Danau Maninjau")
        st.markdown("""
            Welcome to the Lake Maninjau climate indicator-based Upwelling Monitoring and Prediction Dashboard!
            By combining the data in a year, the potential fish production in Danau Maninjau can reach 196 tons.
            However, erratic climate change is destabilizing fish production in Danau Maninjau.
        """)
        column_header = 'Column descriptions of the table'
        tampilan_header = 'Historical Data Display'
        column_description = """
        1. DATE         : Date of the climate indicator
        2. TS           : Average air temperature at surface (°C)
        3. PRECTOTCORR  : Rainfall (mm)
        4. WS10M        : Average wind speed at 10 meters height (m/s)
        5. Cluster      : Potential Upwelling Event
        """

    # Load Dataset
    df = load_data("Dashboard/data/HASIL_CLUSTERING.csv")
    df['DATE'] = pd.to_datetime(df['DATE'])

    # Untuk display tabel
    df_table = df.copy()
    df_plot = df.copy()

    df_table['DATE_STR'] = df_table['DATE'].dt.strftime('%d-%m-%Y')
    df_table.set_index('DATE_STR', inplace=True)

    min_date = pd.to_datetime("2025-01-01")
    max_date = pd.to_datetime("2027-12-31")
    date_range = st.date_input("Pilih Rentang Waktu" if lang == "Bahasa Indonesia" else "Select Date Range", 
                               [min_date, max_date], 
                               min_value=min_date, max_value=max_date, key="date_range")
    
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df_table = df_table[(df_table['DATE'] >= start_date) & (df_table['DATE'] <= end_date)]
    df_plot = df_plot[(df_plot['DATE'] >= start_date) & (df_plot['DATE'] <= end_date)]

    # Display historical data table
    st.write(df_table[['TS', 'PRECTOTCORR', 'WS10M', 'Cluster']])

    st.header(column_header)
    st.text(column_description)

    # Scatter plot PRECTOTCORR vs DATE with color based on Cluster
    st.header(tampilan_header)
    fig = go.Figure()
    for status, color in zip(df_plot['Cluster'].unique(), ['red', 'green']):
        filtered_df = df_plot[df_plot['Cluster'] == status]
        fig.add_trace(go.Scatter(
            x=filtered_df['DATE'], y=filtered_df['PRECTOTCORR'],
            mode='markers', marker=dict(color=color),
            name=status
        ))
    fig.update_layout(title='Potential Upwelling vs Non-Upwelling Events' if lang == "English" 
                      else 'Potensi Upwelling vs Tidak Berpotensi Upwelling',
                      xaxis_title='Date' if lang == "English" else 'Tanggal',
                      yaxis_title='Rainfall (PRECTOTCORR)' if lang == "English" else 'Curah Hujan (PRECTOTCORR)',
                      template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

    # Indicator Plot Options (optional advanced visualization)
    st.header("Select Climate Indicators" if lang == "English" else "Pilih Indikator Iklim")
    with st.expander("Choose Climate Indicators to Display:" if lang == "English" else "Pilih Indikator Iklim yang Ingin Ditampilkan:"):
        select_all = st.checkbox('Select All Indicators' if lang == "English" else 'Tampilkan Semua Indikator')
        ts = st.checkbox('TS - Temperature' if lang == "English" else 'TS - Suhu', value=select_all)
        prectotcorr = st.checkbox('PRECTOTCORR - Rainfall' if lang == "English" else 'PRECTOTCORR - Curah Hujan', value=select_all)
        ws10m = st.checkbox('WS10M - Wind Speed' if lang == "English" else 'WS10M - Kecepatan Angin', value=select_all)

    if ts:
        fig_indicator = plot_climate_indicator(df_plot.set_index('DATE'), 'TS', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)

    if prectotcorr:
        fig_indicator = plot_climate_indicator(df_plot.set_index('DATE'), 'PRECTOTCORR', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)

    if ws10m:
        fig_indicator = plot_climate_indicator(df_plot.set_index('DATE'), 'WS10M', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)

if __name__ == "__main__":
    app()
