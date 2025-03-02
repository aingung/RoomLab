import streamlit as st
import os
import sys
from pathlib import Path

# Add the parent directory to the Python path to import the engine module
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Import classes from engine.py
try:
    from engine import (
        CustomerInformation, Config, Preferences, 
        TokenPayment, GenerateDesign, DesignWorkflow
    )
except ImportError:
    # If engine.py is in the same directory
    try:
        from .engine import (
            CustomerInformation, Config, Preferences, 
            TokenPayment, GenerateDesign, DesignWorkflow
        )
    except ImportError:
        # Fallback if imports don't work
        st.error("Could not import engine.py. Make sure it's in the correct location.")
        # Define placeholder classes for development/testing
        class CustomerInformation:
            def __init__(self, name="", lastname="", email="", phone_number="", billing_address=""):
                self.name = name
                self.lastname = lastname
                self.email = email
                self.phone_number = phone_number
                self.billing_address = billing_address

        class DesignWorkflow:
            def __init__(self):
                self.current_state = "Login"
            
            def process_login(self, customer):
                self.current_state = "PropertySetup"
                return True


def main():
    # Page configuration
    st.set_page_config(
        page_title="RoomLab",
        page_icon="🏠",
        layout="centered"
    )

    # Custom CSS to style the app
    st.markdown(""" 
    <style>
    .main {
        max-width: 480px !important;
        margin: 0 auto;
        padding: 2rem 0;
    }
    .title {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .input-container {
        margin-bottom: 10px;
    }
    .button-primary {
        background-color: #4169E1;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px;
        width: 100%;
        cursor: pointer;
        margin-bottom: 10px;
    }
    .login-option {
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 8px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }
    .login-option img {
        margin-right: 10px;
    }
    .divider {
        display: flex;
        align-items: center;
        text-align: center;
        margin: 15px 0;
    }
    .divider::before, .divider::after {
        content: '';
        flex: 1;
        border-bottom: 1px solid #ddd;
    }
    .divider span {
        padding: 0 10px;
        color: #666;
        font-size: 14px;
    }
    .signup-text {
        text-align: center;
        margin-bottom: 10px;
        font-size: 14px;
    }
    .footer {
        text-align: center;
        margin-top: 100px;
        font-size: 12px;
        color: #666;
    }
    .footer a {
        color: #666;
        text-decoration: none;
    }
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session states if they don't exist
    if "workflow" not in st.session_state:
        st.session_state.workflow = DesignWorkflow()
    
    if "customer" not in st.session_state:
        st.session_state.customer = None
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"
    
    # Main application flow based on current page
    if st.session_state.current_page == "login":
        show_login_page()
    elif st.session_state.current_page == "property_setup":
        show_property_setup()
    elif st.session_state.current_page == "preferences":
        show_preferences()
    elif st.session_state.current_page == "design":
        show_design_page()

def show_login_page():
    # Adding some vertical space at the top
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Title
    st.markdown('<div class="title">RoomLab</div>', unsafe_allow_html=True)

    # Login form
    with st.container():
        # Email/phone input
        email = st.text_input("", placeholder="Email address or phone number", key="login_email")
        
        # Continue button
        if st.button('Continue'):
            if email:
                # Create a basic customer object with email
                st.session_state.customer = CustomerInformation(
                    name="",
                    lastname="",
                    email=email,
                    phone_number="",
                    billing_address=""
                )
                
                # Process login in the workflow
                if hasattr(st.session_state.workflow, 'process_login'):
                    st.session_state.workflow.process_login(st.session_state.customer)
                
                # Move to property setup page
                st.session_state.current_page = "property_setup"
                st.rerun()
        
        # Sign up text
        st.markdown('<div class="signup-text">Don\'t have an account? <a href="#" style="color: #4169E1; text-decoration: none;">Sign Up</a></div>', unsafe_allow_html=True)
        
        # Divider
        st.markdown('<div class="divider"><span>OR</span></div>', unsafe_allow_html=True)
        
        # Social login options
        google_btn = """
        <div class="login-option">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 48 48" style="margin-right: 10px">
                <path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"/>
                <path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"/>
                <path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"/>
                <path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"/>
            </svg>
            Continue with Google
        </div>
        """
        facebook_btn = """
        <div class="login-option">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 16 16" style="margin-right: 10px; fill: #1877F2;">
                <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>
            </svg>
            Continue with Facebook
        </div>
        """
        line_btn = """
        <div class="login-option">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="margin-right: 10px">
                <path fill="#06C755" d="M19.952,12.24c0-4.102-4.111-7.445-9.162-7.445c-5.052,0-9.162,3.342-9.162,7.445c0,3.679,3.267,6.76,7.677,7.344c0.328,0.071,0.775,0.217,0.889,0.498c0.101,0.256,0.066,0.655,0.032,0.913c0,0-0.117,0.706-0.145,0.856c-0.044,0.256-0.202,1.001,0.873,0.545c1.076-0.457,5.814-3.425,7.935-5.862h0.001C19.454,14.695,19.952,13.514,19.952,12.24z M8.891,14.722H6.588c-0.303,0-0.548-0.246-0.548-0.548V9.73c0-0.303,0.246-0.548,0.548-0.548c0.303,0,0.548,0.246,0.548,0.548v3.894h1.754c0.303,0,0.548,0.246,0.548,0.548C9.44,14.476,9.194,14.722,8.891,14.722z M10.089,14.174c0,0.302-0.246,0.548-0.548,0.548c-0.303,0-0.548-0.246-0.548-0.548V9.73c0-0.303,0.246-0.548,0.548-0.548c0.303,0,0.548,0.246,0.548,0.548V14.174z M14.307,14.174c0,0.302-0.246,0.548-0.548,0.548c-0.149,0-0.284-0.06-0.383-0.157c-0.021-0.021-0.041-0.043-0.059-0.066l-2.434-3.293v3.516c0,0.302-0.246,0.548-0.548,0.548c-0.303,0-0.548-0.246-0.548-0.548V9.73c0-0.303,0.246-0.548,0.548-0.548c0.147,0,0.28,0.058,0.378,0.153l0.04,0.043l2.458,3.33V9.73c0-0.303,0.246-0.548,0.548-0.548c0.303,0,0.548,0.246,0.548,0.548V14.174z M17.698,11.303c0.303,0,0.548,0.246,0.548,0.548c0,0.303-0.246,0.548-0.548,0.548h-1.754v1.228h1.754c0.303,0,0.548,0.246,0.548,0.548c0,0.303-0.246,0.548-0.548,0.548h-2.303c-0.303,0-0.548-0.246-0.548-0.548V9.73c0-0.303,0.246-0.548,0.548-0.548h2.303c0.303,0,0.548,0.246,0.548,0.548c0,0.303-0.246,0.548-0.548,0.548h-1.754v1.228H17.698z"/>
            </svg>
            Continue with LINE
        </div>
        """
        
        st.markdown(google_btn, unsafe_allow_html=True)
        st.markdown(facebook_btn, unsafe_allow_html=True)
        st.markdown(line_btn, unsafe_allow_html=True)
    
    # Footer
    st.markdown('<div class="footer">RoomLab | <a href="#">Terms of Service</a> | <a href="#">Privacy Policy</a></div>', unsafe_allow_html=True)

def show_property_setup():
    st.markdown('<div class="title">Set Up Your Property</div>', unsafe_allow_html=True)
    
    # Property setup form
    with st.form("property_setup_form"):
        real_estate_type = st.selectbox(
            "Property Type",
            ["Apartment", "House", "Condo", "Studio", "Office"]
        )
        
        floor = st.number_input("Floor Number", min_value=0, value=1)
        
        room_type = st.selectbox(
            "Room Type",
            ["Living Room", "Bedroom", "Kitchen", "Bathroom", "Office", "Dining Room"]
        )
        
        col1, col2 = st.columns(2)
        with col1:
            length = st.number_input("Length (m)", min_value=1.0, value=4.0)
            width = st.number_input("Width (m)", min_value=1.0, value=3.0)
        
        with col2:
            height = st.number_input("Height (m)", min_value=1.0, value=2.4)
            space = st.number_input("Total Area (m²)", min_value=1.0, value=length * width)
        
        # Submit button
        submit_button = st.form_submit_button("Continue to Preferences")
        
        if submit_button:
            # Create Config object
            config = Config(
                real_estate_type=real_estate_type,
                floor=floor,
                room_type=room_type,
                space=space,
                length=length,
                width=width,
                height=height
            )
            
            # Store in session state
            st.session_state.config = config
            
            # Update workflow if method exists
            if hasattr(st.session_state.workflow, 'setup_property'):
                st.session_state.workflow.setup_property(config)
            
            # Move to preferences page
            st.session_state.current_page = "preferences"
            st.rerun()

def show_preferences():
    st.markdown('<div class="title">Your Design Preferences</div>', unsafe_allow_html=True)
    
    # Preferences form
    with st.form("preferences_form"):
        style = st.selectbox(
            "Design Style",
            ["Modern", "Minimalist", "Contemporary", "Traditional", "Industrial", "Scandinavian", "Bohemian"]
        )
        
        family = st.selectbox(
            "Household Type",
            ["Single", "Couple", "Small Family", "Large Family", "Shared Space"]
        )
        
        budget = st.slider("Budget ($)", 5000, 100000, 25000, 1000)
        
        # Submit button
        submit_button = st.form_submit_button("Generate Design")
        
        if submit_button:
            # Create Preferences object
            preferences = Preferences(
                style=style,
                family=family,
                budget=float(budget)
            )
            
            # Store in session state
            st.session_state.preferences = preferences
            
            # Update workflow if method exists
            if hasattr(st.session_state.workflow, 'setup_preferences'):
                st.session_state.workflow.setup_preferences(preferences)
            
            # Move to design page
            st.session_state.current_page = "design"
            st.rerun()

def show_design_page():
    st.markdown('<div class="title">Your Design</div>', unsafe_allow_html=True)
    
    # Check if we have the necessary data to generate a design
    if all(key in st.session_state for key in ["customer", "config", "preferences"]):
        # Create a prompt based on the collected data
        prompt = f"Generate a {st.session_state.preferences.style} design for a {st.session_state.config.room_type} " \
                f"in a {st.session_state.config.real_estate_type} for a {st.session_state.preferences.family} " \
                f"with a budget of ${st.session_state.preferences.budget}"
        
        # Display the generated prompt
        st.write("Design Prompt:")
        st.info(prompt)
        
        # Create GenerateDesign object
        generate_design = GenerateDesign(
            prompt=prompt,
            config=st.session_state.config,
            preferences=st.session_state.preferences,
            customer=st.session_state.customer
        )
        
        # Store in session state
        st.session_state.generate_design = generate_design
        
        # Generate design if the workflow has the method
        if hasattr(st.session_state.workflow, 'generate_initial_design'):
            try:
                st.session_state.workflow.generate_initial_design(generate_design)
                st.success("Design generated successfully!")
            except Exception as e:
                st.error(f"Error generating design: {str(e)}")
                # For demonstration, show a placeholder
                st.image("https://via.placeholder.com/800x600?text=Your+Room+Design", 
                        caption="Design Preview (Placeholder)")
        else:
            # For demonstration purposes when the actual method isn't available
            st.image("https://via.placeholder.com/800x600?text=Your+Room+Design", 
                    caption="Design Preview (Placeholder)")
        
        # Design modification options
        st.subheader("Modify Your Design")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Update Wallpaper"):
                st.session_state.modification = "UpdateWallpaper"
        
        with col2:
            if st.button("Update Flooring"):
                st.session_state.modification = "UpdateFlooring"
        
        col3, col4 = st.columns(2)
        with col3:
            if st.button("Update Colors"):
                st.session_state.modification = "UpdateColors"
        
        with col4:
            if st.button("Update Furniture"):
                st.session_state.modification = "UpdateFurniture"
        
        # Purchase section
        st.subheader("Purchase Options")
        if st.button("Purchase Design"):
            # Show payment form
            st.session_state.show_payment = True
        
        # Show payment form if requested
        if st.session_state.get("show_payment", False):
            with st.form("payment_form"):
                st.write("Payment Information")
                credit_card = st.text_input("Credit Card Number", placeholder="XXXX-XXXX-XXXX-XXXX")
                
                col1, col2 = st.columns(2)
                with col1:
                    card_name = st.text_input("Name on Card")
                
                with col2:
                    card_date = st.text_input("Expiration Date (MM/YY)")
                
                ccv = st.text_input("Security Code (CCV)", max_chars=3)
                
                submit_payment = st.form_submit_button("Complete Purchase")
                
                if submit_payment:
                    # Process payment
                    token_payment = TokenPayment(st.session_state.customer.customer_id)
                    token_payment.credit_card = credit_card
                    token_payment.card_name = card_name
                    token_payment.card_date = card_date
                    token_payment.ccv = ccv
                    
                    # Process payment if workflow has the method
                    if hasattr(st.session_state.workflow, 'process_purchase'):
                        try:
                            st.session_state.workflow.process_purchase(token_payment)
                            st.success("Payment successful! Your design has been purchased.")
                        except Exception as e:
                            st.error(f"Payment error: {str(e)}")
                    else:
                        # For demonstration
                        st.success("Payment successful! Your design has been purchased.")
    else:
        st.error("Missing required information. Please complete the previous steps.")
        if st.button("Return to Login"):
            st.session_state.clear()
            st.session_state.current_page = "login"
            st.rerun()

if __name__ == "__main__":
    main()
