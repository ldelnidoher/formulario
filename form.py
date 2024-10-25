formbtn = st.button("Form")

if "formbtn_state" not in st.session_state:
    st.session_state.formbtn_state = False

if formbtn or st.session_state.formbtn_state:
    st.session_state.formbtn_state = True
    
    st.subheader("User Info Form")
    # name = st.text_input("Name")
    with st.form(key = 'user_info'):
        st.write('User Information')
    
        name = st.text_input(label="Name 📛")
        age = st.number_input(label="Age 🔢", value=0)
        email = st.text_input(label="Email 📧")
        phone = st.text_input(label="Phone 📱")
        gender = st.radio("Gender 🧑", ("Male", "Female", "Prefer Not To Say"))
    
        submit_form = st.form_submit_button(label="Register", help="Click to register!")
    
        # Checking if all the fields are non empty
        if submit_form:
            st.write(submit_form)
    
            if name and age and email and phone and gender:
                # add_user_info(id, name, age, email, phone, gender)
                st.success(
                            f"ID:  \n Name: {name}  \n Age: {age}  \n Email: {email}  \n Phone: {phone}  \n Gender: {gender}"
                        )
            else:
                st.warning("Please fill all the fields")
