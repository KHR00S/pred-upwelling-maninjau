import streamlit as st
from st_social_media_links import SocialMediaIcons

def app():

    # Language selection
    lang = st.selectbox("Select Language / Pilih Bahasa", ["Bahasa Indonesia", "English"])

    if lang == "Bahasa Indonesia":
        # Indonesian content
        st.title("Tentang Kami")
        st.header("Deskripsi Projek")
        st.markdown("""
            Pembuatan dashboard ini merupakan salah satu luaran dari Pogram Kreativitas Mahasiswa – Riset Eksakta (PKM - RE) yang dikerjakan oleh Mahasiswa Universitas Syiah Kuala. Projek ini disusun untuk tujuan membantu Pembudidaya Keramba Jaring Apung (KJA) Danau Maninjau untuk mengambil Keputusan dalam membudidayakan ikan.
        """)
        st.image('Artboard 1.png', use_column_width=True)

        # Visi, Misi, and Tujuan (Vision, Mission, and Goals)
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.header("Visi")
            st.markdown("""
            Menjadi penyedia solusi inovatif dalam mengatasi risiko upwelling dan memberikan informasi yang akurat untuk pengambilan keputusan oleh Pembudidaya KJA Danau Maninjau
            """)
        with col_2:
            st.header("Misi")
            st.markdown("""
            1. Mengumpulkan dan menganalisis data kejadian upwelling dan indikator iklim dengan akurat.
            2. Mengembangkan model prediksi upwelling yang handal berdasarkan data historis.
            3. Menyediakan dashboard interaktif untuk memantau dan meramalkan risiko upwelling.
            4. Menyebarkan informasi mengenai risiko upwelling kepada Pembudidaya KJA secara efektif.
            """)
        with col_3:
            st.header("Tujuan")
            st.markdown("""
            1. Menyediakan sumber informasi yang terpercaya terkait risiko upwelling di Danau Maninjau.
            2. Meningkatkan kewaspadaan dan kesiapsiagaan pembudidaya KJA Danau Maninjau terhadap potensi risiko upwelling.
            3. Mendukung upaya mitigasi dan penanggulangan risiko upwelling di Danau Maninjau.
            """)

        # Dataset Section
        st.header("Dataset yang Digunakan")
        st.markdown("""
            Kami menggunakan beberapa dataset dalam projek ini. Berikut adalah beberapa di antaranya:
            1. Data Kejadian upwelling di Danau Maninjau
            2. Data iklim Danau Maninjau   : [NASA Prediction Of Worldwide Energy Resources](https://power.larc.nasa.gov/)
        """)

        # Model Section
        st.header("Model yang Digunakan")
        st.markdown("""
            ### Model Forecast ( Vector Autoregresive)
            Kami menggunakan Vector Autoregresive untuk meramalkan indikator iklim pada berbagai interval waktu
        """)

        # Tools and Technologies
        st.header("Teknologi / Tools yang Digunakan")
        st.markdown("""
            - **Streamlit**              : Untuk pembuatan antarmuka pengguna.
            - **Pandas & R**             : Untuk manipulasi dan analisis data.
            - **Joblib**                 : Untuk menyimpan dan memuat model pembelajaran mesin.
            - **Plotly Express**         : Library untuk membuat visualisasi data interaktif.
        """)

        # Social Media
        st.header("Sosial Media")
        st.markdown("""
            <a href="https://www.instagram.com/pkmre_upwelling?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width:30px;height:30px;">
            @pkmre_upwelling
            </a>
            """, unsafe_allow_html=True)
        st.markdown("""
            <a href="https://www.tiktok.com/@pkmre_upwelling?_t=8n8OhzhoUsr&_r=1">
            <img src="https://upload.wikimedia.org/wikipedia/en/a/a9/TikTok_logo.svg" alt="TikTok" style="width:30px;height:10px;background-color:white;">
            @pkmre_upwelling
            </a>
            """, unsafe_allow_html=True)

        # Contact
        st.header("Kontak")
        st.markdown("""
            Jika Anda memiliki pertanyaan atau umpan balik, silakan hubungi kami:
        """)
            st.markdown("""
                - ##### Fakhrus Syakir
                """)
            st.image('s.png')
            st.markdown("""
                    - Email   : [fakhroosyakir@gmail.com](mailto:fakhroosyakir@gmail.com) 
                    - LinkedIn: [Fakhrus Syakir](https://www.linkedin.com/in/fakhrus-syakir-65bb72205/) 
                    """)

    else:
        # English content
        st.title("About Us")
        st.header("Project Description")
        st.markdown("""
            This dashboard is part of the output from the Program Kreatifitas Mahasiswa – Riset Eksakta (PKM - RE) conducted by students of Syiah Kuala University. This project is designed to help Floating Net Cage farmers in Danau Maninjau make decisions in fish farming.
        """)
        st.image('Artboard 1.png', use_column_width=True)

        # Vision, Mission, and Goals
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.header("Vision")
            st.markdown("""
            To be an innovative solution provider in mitigating upwelling risks and providing accurate information for decision-making by Danau Maninjau KJA farmers.
            """)
        with col_2:
            st.header("Mission")
            st.markdown("""
            1. Accurately collect and analyze upwelling events and climate indicators.
            2. Develop reliable upwelling prediction models based on historical data.
            3. Provide an interactive dashboard to monitor and forecast upwelling risks.
            4. Effectively disseminate information on upwelling risks to KJA farmers.
            """)
        with col_3:
            st.header("Goals")
            st.markdown("""
            1. Provide a reliable source of information related to upwelling risks in Danau Maninjau.
            2. Increase awareness and preparedness of Danau Maninjau KJA farmers against potential upwelling risks.
            3. Support mitigation and countermeasures against upwelling risks in Danau Maninjau.
            """)

        # Dataset Section
        st.header("Datasets Used")
        st.markdown("""
            We use several datasets in this project. Here are some of them:
            1. Upwelling events data in Danau Maninjau.
            2. Danau Maninjau climate data   : [NASA Prediction Of Worldwide Energy Resources](https://power.larc.nasa.gov/)
        """)

        # Model Section
        st.header("Models Used")
        st.markdown("""
            #### Forecas Vector Autoregressive)
            We use Vector Autoregressive, to forecast climate indicators at various time intervals:
        """)

        # Tools and Technologies
        st.header("Technologies / Tools Used")
        st.markdown("""
            - **Streamlit**              : For building the user interface.
            - **Pandas & R**             : For data manipulation and analysis.
            - **Joblib**                 : For saving and loading machine learning models.
            - **Plotly Express**         : Libraries for creating interactive data visualizations.
        """)

        # Social Media
        st.header("Sosial Media")
        st.markdown("""
            <a href="https://www.instagram.com/pkmre_upwelling?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width:30px;height:30px;">
            @pkmre_upwelling
            </a>
            """, unsafe_allow_html=True)
        st.markdown("""
            <a href="https://www.tiktok.com/@pkmre_upwelling?_t=8n8OhzhoUsr&_r=1">
            <img src="https://upload.wikimedia.org/wikipedia/en/a/a9/TikTok_logo.svg" alt="TikTok" style="width:30px;height:10px;background-color:white;">
            @pkmre_upwelling
            </a>
            """, unsafe_allow_html=True)

        # Contact
        st.header("Kontak")
        st.markdown("""
            If you have any questions or feedback, please contact us:
        """)
            st.markdown("""
                - ##### Fakhrus Syakir
                """)
            st.image('s.png')
            st.markdown("""
                    - Email   : [fakhroosyakir@gmail.com](mailto:fakhroosyakir@gmail.com) 
                    - LinkedIn: [Fakhrus Syakir](https://www.linkedin.com/in/fakhrus-syakir-65bb72205/) 
                    """)
