#login page
import streamlit as st

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
    
    # Adding some vertical space at the top
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Title
    st.markdown('<div class="title">RoomLab</div>', unsafe_allow_html=True)
    
    # Login form
    with st.container():
        # Email/phone input
        st.text_input("", placeholder="Email address or phone number", key="email")
        
        # Continue button
        st.markdown('<button class="button-primary">Continue</button>', unsafe_allow_html=True)
        
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
    st.markdown("""
    <div class="footer">
        <a href="#">Terms of Use</a> | <a href="#">Privacy Policy</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
