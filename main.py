import streamlit as st
import pandas as pd
import pylightxl as xl
import numpy as np

# set page config
st.set_page_config(
    page_title="Laravel CRUD Generator | FERDYHAPE",
    page_icon=":gear:",
    layout="centered",
    initial_sidebar_state="auto", menu_items=None
)

# sidebar for author introduction
st.sidebar.markdown("""

<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"
        integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
    <div class="profile_picture">
        <img src="https://github.com/ferdyhape.png" alt="Profile_Picture" srcset="">
    </div>
    <p class ="html" style='text-align: center;'>Connect with me!</p>
    <div class="group-icon">
        <a href="https://github.com/ferdyhape" target="_blank"><i class="fa-brands fa-github"></i></a>
        <a href="https://instagram.com/ferdyhape" target="_blank"><i class="fa-brands fa-instagram"></i></a>
        <a href="https://www.linkedin.com/in/ferdy-hahan-pradana/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
    </div> 
    <footer>
        <p class="copyright">©2023<br> Copyright By <a href="https://github.com/ferdyhape">FERDYHAPE</a></p>
    </footer>
    <style>
    .profile_picture {
        text-align:center;
    }
    .profile_picture img{
      border-radius: 50%;
      width: 65%;
    }
    .group-icon {
        margin: 10px 20px;
        padding: 0;
        border-radius: 25px;
        background-color: #F6F6F6;
        text-align: center;
        font-size: 25px;
    } 
    .group-icon:hover {
        background-color: #F9F9F9;
        cursor: pointer;
    }
    .fa-github {
        color: #333;
    }
    .fa-instagram {
        color: #833AB4;
    }
    .fa-linkedin {
        color: #0e76a8;
    }
    .author {
        margin: 0px 10px;;
        font-size: 20px;
        font-weight: bold;
    }
    .html {
        margin: 10px 10px;
        padding: 0;
    }
    footer {
        position: static;
        height: 240px;
        width: 100%;
    }
    .copyright{
        position: absolute;
        width: 100%;
        color: #fff;
        line-height: 20px;
        font-size: 1em;
        text-align: center;
        bottom:0;
    }
    .copyright a {
        margin: 0;
        text-decoration: none;
    }
    footer p {
        margin: 0;
    }
    a {
        font-weight: bolder;
        margin: 0 10px;
    }
    </style>
</body>

""", unsafe_allow_html=True)

# set the title of page


def title_template(title):
    st.title(f"""
    {title}
    """)


def CRUDGenerator():

    atribute_name_list = []
    atribute_name_list.clear()

    atribute_datatype_list = []
    atribute_datatype_list.clear()

    generate_field = []
    generate_field.clear()

    title = "Laravel CRUD Generator"
    title_template(title)
    table_name = st.text_input(
        "Input Table Name, then enter")
    if table_name:

        attribute_data = {
            'Attribute': [
                'Integer', 'String']}

        df = pd.DataFrame(data=attribute_data)
        st.table(df)

        input_atribute_name = st.text_input(
            "Input Field ")
        input_atribute_name = input_atribute_name.replace(" ", "").lower()
        atribute_name_list = input_atribute_name.split(",")
        atribute_name_list.pop()

        input_atribute_datatype = st.text_input(
            'Input Datatype')
        input_atribute_datatype = input_atribute_datatype.replace(
            " ", "").lower()
        atribute_datatype_list = input_atribute_datatype.split(",")
        atribute_datatype_list.pop()

        if (len(atribute_datatype_list) == 0 and len(atribute_name_list) == 0):
            st.write("")
        elif ((len(atribute_datatype_list) == len(atribute_name_list)) and atribute_datatype_list and atribute_name_list):

            for (field_datatype, field_name) in zip(atribute_datatype_list, atribute_name_list):
                dump_generate_field = f"$table->{field_datatype}('{field_name}')"
                generate_field.append(dump_generate_field)
            final_field_for_migration = ';\n'.join(generate_field)

            d = {'Field': atribute_name_list,
                 'Datatype': atribute_datatype_list}
            df = pd.DataFrame(data=d)
            st.markdown('---------------------------------------')
            st.write("""
                Table Preview
                """)
            st.table(df)

            st.markdown("""
            1. Open the terminal, paste this command and enter
            """)
            st.markdown(f"""
                    ```shell
                    php artisan make:model {table_name} -mcr;
                    """)

            st.markdown("""
                <style>
                .small-text {
                    font-size:15px;
                    margin-bottom: 15px;
                    font-style:italic;
                }
                </style>
                2. <div class="label-text">Find and open your migration file with name <b>'... create_(yourTables)_table.php'</b></div>
                   <div class="small-text">(Example: '2014_10_12_000000_create_users_table.php')</div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
                    ```shell
                    {final_field_for_migration};
                    """)
        else:
            st.error('Length of Field and Datatype must be the same!', icon="⚠️")


CRUDGenerator()
