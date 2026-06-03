"""
Sci-ImageMiner Annotation Tool

Installation:
    pip install -r requirements.txt

Running:
    streamlit app app.py
"""

import os
import io
import re
import json
import time
from pprint import pprint

import pathlib
import pandas as pd
import uuid
import shutil
import bcrypt
import datetime
import timedelta
# from datetime import datetime
import zipfile

import streamlit as st
# import clipboard
# import pyperclip
# from st_copy import copy_button
# from streamlit_quill import st_quill
# from streamlit_markdown import st_markdown

# ---------- CONSTANTS ----------

DATA_DIR_PAPERS = "data"
DATA_URL_GITHUB = "https://github.com/sciknoworg/ALD-E-ImageMiner/tree/main/data"
MARKDOWN_EDITOR_URL = "https://markdowncheatsheet.com/editor"
# OUTPUT_DIR = "outputs"
# INPUT_PAPER_DIST_DIR = os.path.join(OUTPUT_DIR, "user_paper_dists")
# OUTPUT_JSON_DIR = os.path.join(OUTPUT_DIR, "user_annotations")
# os.makedirs(OUTPUT_JSON_DIR, exist_ok=True)

LOGO_SIDEBAR = "assets/logo-github-small.png"
LOGO_MAIN = "assets/logo-github.png"
LOGO_PAGE_ICON = "assets/logo-github-icon.png"

USERS_CSV = "users.csv"
DATA_DIR_USERS = "data"
DATA_TEMPLATE = "data_template.json"
LOG_DIR = "logs"


####################################
# DEBUG MODE
####################################
DEBUG_MODE = False
if st.session_state and ("last_name" in st.session_state) and (st.session_state["last_name"] == "Admin"):
    DEBUG_MODE = True


# if DEBUG_MODE:
CLASS_OPTIONS = [
    "-- Quantitative Plots (General) --",
    "area chart", "bar chart", "3d bar chart", 
    "grouped bar chart", "stacked bar chart", "box plot", 
    "bubble chart", "donut chart", "funnel chart", 
    "heatmap", "line chart", "multiple line chart", 
    "multi-axis chart", "pie chart", "polar chart (rose chart)", 
    "radar chart (spider chart)", "3d scatter plot", "scatter plot", "multiple scatter plot"
    "treemap",
    # -- domain-specific quantitative -- #
    "-- Quantitative Plots (Domain-specific) --",
    "spectra chart", "stacked spectra chart", "multi spectra chart", "phase diagram", 
    "band diagram", "adsorption isotherm", "process timing diagram", "contour heatmap",
    # -- domain-specific -- #
    "-- Domain-specific --",
    "image panel", "map/geo chart",
    # -- scientific schematic -- #
    "-- Scientific Schematics --",
    "molecular structure diagram", "reaction scheme", "reaction energy profile diagram", "process flow diagram",
    "apparatus diagram", "conceptual diagram", "device structure", "chromaticity diagram"
    # -- matrix layout -- #
    "-- Matrix Layouts --",
    "periodic table map", "element-property matrix",
    "network diagram", "tree diagram",
    # -- others -- #
     "-- Others --",
    "workflow diagram", "timeline chart", "comparison table",
    "formula", "table",
    "unknown",
    ]
# else:
#     CLASS_OPTIONS = [
#         # -- general quantitative -- #
#         "area chart", "bar chart", "3d bar chart", 
#         "grouped bar chart", "stacked bar chart", "box plot", 
#         "bubble chart", "donut chart", "funnel chart", 
#         "heatmap", "line chart", "multiple line chart", 
#         "multi-axis chart", "pie chart", "polar chart (rose chart)", 
#         "radar chart (spider chart)", "3d scatter plot", "scatter plot", 
#         "treemap",
#         # -- domain-specific quantitative -- #
#         "spectra chart", "phase diagram", 
#         "band diagram", "adsorption isotherm", "process timing diagram",
#         # # -- domain-specific -- #
#         # "image panel", "map/geo chart",
#         # # -- scientific schematic -- #
#         # "molecular structure diagram", "reaction scheme", "process flow diagram",
#         # "apparatus diagram", "conceptual diagram",
#         # # -- matrix layout -- #
#         # "periodic table map", "element-property matrix",
#         # "network diagram", "tree diagram",
#         # # -- others -- #
#         # "workflow diagram", "timeline chart", "comparison table",
#         # "formula", "table",
#         "unknown",
#     ]

CLASS_OPTION_DESC = {
        # -- quantitative general -- #
        "area chart": "Filled area under a line to show cumulative values or trends",
        "bar chart": "Rectangular bars to compare quantities across categories",
        "3d bar chart": "Bar chart displayed in three dimensions", 
        "grouped bar chart": "Bars grouped by categories for side-by-side comparison",
        "stacked bar chart": "Bars stacked to show part-to-whole relationships",
        "box plot": "Statistical distribution showing median, quartiles, and outliers", 
        "bubble chart": "Scatter plot with variable marker size representing a third dimension",
        "donut chart": "Pie chart with a central hole to show proportions",
        "funnel chart": "Progressive reduction across stages of a process",
        "heatmap": "Matrix of values represented with colors",
        "line chart": "Continuous line showing trends over intervals",
        "multiple line chart": "Several lines showing multiple series of trends",
        "multi-axis chart": "Plot with multiple axes to compare different scales",
        "pie chart": "Circular chart divided into slices to show proportions",
        "polar chart (rose chart)": "Circular chart plotting values by angle", 
        "radar chart (spider chart)": "Multivariate data represented in a radial layout",
        "3d scatter plot": "Scatter plot displayed in three dimensions",
        "scatter plot": "Points plotted on two axes to show correlations", 
        "treemap": "Nested rectangles sized by values to show hierarchy",

        # -- quantitative domain-specific -- #
        "spectra chart": "Specialized single line chart used in scientific spectroscopy/diffraction contexts (NMR, IR, Raman, UV-vis, MS, XRD)",
        "multi spectra chart": "Specialized multiple line chart used in scientific spectroscopy/diffraction contexts (NMR, IR, Raman, UV-vis, MS, XRD)",
        "stacked spectra chart": "Specialized multiple-line chart used in scientific spectroscopy/diffraction contexts (NMR, IR, Raman, UV-vis, MS, XRD). Used to visualize multiple spectra in a single plot, allowing for easy comparison of peak shifts, changes in peak splittings, and signal intensities.",
        "phase diagram": "Specialized chart showing equilibrium phase boundaries in temperature-pressure-composition space", 
        "band diagram": "Specialized chart plotting electronic energy levels vs. momentum (k) or position, showing band gaps and Fermi levels",
        "adsorption isotherm": "Specialized line/scatter plot showing gas uptake vs. pressure (or relative pressure), used to derive Henry constants and capacity values",
        "process timing diagram": "Time-axis plot showing one or more process variables (e.g., gas flows, pressure, power, valve states) as step-like or pulsed functions over a cycle or sequence of steps.",
        "countour heatmap":	"Profile mapping of pressure/temperature or any relevant parameter of study",

        # -- domain-specific -- #
        "image panel": "Collection of microscopy or spectroscopy images",
        "map/geo chart": "Geographic or spatial distribution visualization",

        # -- scientific schematic -- #
        "molecular structure diagram": "Chemical structure drawings of molecules or precursors",
        "reaction scheme": "Arrows and molecules showing chemical reactions",
        "process flow diagram": "Schematic showing sequential or cyclic steps in a scientific or technical process",
        "apparatus diagram": "Diagram of experimental or laboratory setups",
        "conceptual diagram": "Illustration of theoretical models or mechanisms",
        "device structure diagram": "",

        # -- matrix layout -- #
        "periodic table map": "Property overlay aligned to the full periodic table layout (rows, groups, blocks), typically showing trends across all or most elements",
        "element-property matrix": "Matrix-style visualization linking a subset of elements (e.g. lanthanides) with categorical or binary properties (e.g. precursor availability)",
        "network diagram": "Nodes and edges showing relationships or interactions",
        "tree diagram": "Hierarchical branching structure (taxonomy, phylogeny, decision)",

        # -- unknown -- #
        "workflow diagram": "Diagram showing pipeline or methodological steps",
        "timeline chart": "Chronological sequence of events or steps",
        "comparison table": "Structured tabular comparison of properties or studies",
        "formula": "Mathematical or chemical expression typeset as formula",
        "table": "General tabular data representation",
        "unknown": "Unclassified or unclear figure type"
    }

Q_TYPES = [
    "Process-Oriented",
    "Comparative/Trend",
    "Structure-Property",
    "Application/Performance"
]
A_TYPES = ["Yes/No", "Factoid", "List", "Paragraph"]


# st.logo(
#     LOGO_SIDEBAR,
#     # link="https://streamlit.io/gallery",
#     icon_image=LOGO_MAIN,
# )


# ---------- UTILS ----------

def get_current_time_string():
    """
    Returns the current time as a string in the format 'YYYY-MM-DD-H:M:S'
    """
    #  return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

def read_timestamp_from_string(timestamp_str):
    return datetime.datetime.strptime(timestamp_str, "%Y-%m-%d-%H:%M:%S")

def create_timestamp_string():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

def check_time_status(start_timestamp, days_limit):
    """
    Determines if the time is up based on a start timestamp and day limit
    
    Args:
        start_timestamp (str): The starting timestamp in 'YYYY-MM-DD-HH-MM-SS' format
        days_limit (int/float): Number of days after which time is considered up
    
    Returns:
        dict: Dictionary containing:
            - is_time_up (bool): True if time is up, False otherwise
            - days_passed (float): Number of days that have passed
            - days_remaining (float): Number of days remaining (negative if time is up)
            - deadline (str): The calculated deadline timestamp
    """
    days_limit = int(days_limit)

    # Convert start timestamp to datetime object
    start_dt = read_timestamp_from_string(start_timestamp)
    
    # Get current time
    current_dt = datetime.datetime.now()
    # timedelta.difference()
    # Calculate deadline by adding days to start timestamp
    deadline_dt = start_dt + timedelta.Timedelta(days=days_limit)
    deadline = deadline_dt.strftime("%Y-%m-%d-%H:%M:%S")
    
    # Calculate time difference
    time_passed = current_dt - start_dt
    days_passed = time_passed.total_seconds() / (24 * 3600)  # Convert to days
    
    # Calculate days remaining
    time_remaining = deadline_dt - current_dt
    days_remaining = time_remaining.total_seconds() / (24 * 3600)
    
    # Determine if time is up
    time_is_up = current_dt >= deadline_dt
    
    return {
        'is_time_up': time_is_up,
        'days_passed': round(days_passed, 2),
        'days_remaining': round(days_remaining, 2),
        'deadline': deadline,
        'start_time': start_timestamp,
        'current_time': create_timestamp_string()
    }

def check_time_status_adv(start_timestamp, days_limit, buffer_hours=0):
    """
    Advanced time checking with buffer hours and detailed status
    
    Args:
        start_timestamp (str): Starting timestamp
        days_limit (float): Number of days allowed
        buffer_hours (float): Buffer hours before considering time as 'almost up'
    
    Returns:
        dict: Detailed status information
    """
    days_limit = int(days_limit)

    start_dt = read_timestamp_from_string(start_timestamp)
    current_dt = datetime.now()
    deadline_dt = start_dt + timedelta.Timedelta(days=days_limit)
    
    # Calculate time differences
    total_time_passed = current_dt - start_dt
    time_remaining = deadline_dt - current_dt
    
    days_passed = total_time_passed.total_seconds() / (24 * 3600)
    days_remaining = time_remaining.total_seconds() / (24 * 3600)
    hours_remaining = days_remaining * 24
    
    # Determine status
    if current_dt >= deadline_dt:
        status = "TIME_UP"
    elif hours_remaining <= buffer_hours:
        status = "ALMOST_UP"
    else:
        status = "TIME_REMAINING"
    
    return {
        'status': status,
        'is_time_up': status == "TIME_UP",
        'is_almost_up': status == "ALMOST_UP",
        'days_passed': round(days_passed, 2),
        'days_remaining': round(days_remaining, 2),
        'hours_remaining': round(hours_remaining, 2),
        'deadline': deadline_dt.strftime("%Y-%m-%d-%H:%M:%S"),
        'start_time': start_timestamp,
        'current_time': current_dt.strftime("%Y-%m-%d-%H:%M:%S")
    }


def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)


def zip_and_download_folder(folder_path: str, zip_name: str = "archive.zip"):
    """
    Create a temporary ZIP of `folder_path` and show a Streamlit download button.
    The ZIP is kept in memory (no temp file written to disk).
    """
    # Check folder existence
    if not os.path.isdir(folder_path):
        st.error(f"Folder not found: {folder_path}")
        return

    # Create in-memory ZIP
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname=rel_path)

    zip_buffer.seek(0)

    # Streamlit download button
    st.download_button(
        label=f"📦 Download {zip_name}",
        data=zip_buffer,
        file_name=zip_name,
        mime="application/zip",
    )

# def on_copy_click(text):
#     if "copied" not in st.session_state: 
#         st.session_state.copied = []

#     st.session_state.copied.append(text)
#     clipboard.copy(text)
#     # clipboard.paste()


def to_os_free_path(path_str):
    """Convert a path string to a POSIX-style path."""
    return pathlib.Path(path_str).as_posix()

def from_os_free_path(path_str):
    """Convert a POSIX-style path string back to a platform-specific path."""
    return pathlib.Path(path_str)

def log_error(message: str):
    """Log runtime exceptions to logs/YYYYMMDD-errors.log"""
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, f"{datetime.date.today():%Y%m%d}-errors.log")
    with open(log_path, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")


def to_python_int(x):
    return int(x) if x != '' else None

def to_python_float(x):
    return float(x) if x != '' else None

def read_users_df():
    if not os.path.exists(USERS_CSV):
        # df = pd.DataFrame(columns=["uuid","first_name","last_name","email","password_hash","user_folder"])
        # df = pd.DataFrame(columns=["annotator_id", "is_admin", "first_name", "last_name", "email", "is_first_login", "time_started", "time_given_days", "user_folder"])
        df = pd.DataFrame(columns=["annotator_id", "is_admin", "first_name", "last_name", "email", "is_first_login", "time_started", "time_given_days", "user_folder"])
        df.to_csv(USERS_CSV, index=False)
        return df
    else:
        return pd.read_csv(USERS_CSV,
                           dtype={
                               "annotator_id": int,
                               "is_admin": bool,
                               "first_name": str,
                               "last_name": str,
                               "email": str,
                               "is_first_login": bool,
                               "time_started": str,
                               "time_given_days": int,
                               "user_folder": str
                            },
                        #    converters={
                        #    'integer_column': to_python_int,
                        #    'float_column': to_python_float
                        #}
                        )


def write_users_df(df):
    df.to_csv(USERS_CSV, index=False)

def append_user_row(first_name, last_name, email, password_hash, user_folder, uuid_str):
    df = read_users_df()
    new_row = {
        "uuid": uuid_str,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password_hash": password_hash,
        "user_folder": user_folder
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    write_users_df(df)

def sanitize_email(email: str):
    return email.replace("@", "_at_").replace(".", "_dot_")

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    # return False

def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    # return ""

def backup_json(path):
    backup_path = os.path.join(os.path.dirname(path), "annotations.backup.json")
    if os.path.exists(path):
        shutil.copyfile(path, backup_path)

def load_json(path):
    if not os.path.exists(path):
        return {"pdf_documents": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    backup_json(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def check_password_strength(password):
    length_criteria = len(password) >= 8
    lower_case = bool(re.search(r"[a-z]", password))
    upper_case = bool(re.search(r"[A-Z]", password))
    digit = bool(re.search(r"\d", password))
    special_char = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    strength = sum([length_criteria, lower_case, upper_case, digit, special_char])

    suggestions = []
    if not length_criteria:
        suggestions.append("🔹 Use at least 8 characters.")
    if not lower_case:
        suggestions.append("🔹 Add lowercase letters (a-z).")
    if not upper_case:
        suggestions.append("🔹 Add uppercase letters (A-Z).")
    if not digit:
        suggestions.append("🔹 Include numbers (0-9).")
    if not special_char:
        suggestions.append("🔹 Use special characters (!@#$%^&*).")

    if strength == 5:
        return "🟢 Strong", suggestions
    elif strength >= 3:
        return "🟡 Medium", suggestions
    else:
        return "🔴 Weak", suggestions


def validate_email(email):
    """
    Validate email format using regex pattern
    
    Args:
        email (str): Email address to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # Comprehensive email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


def validate_name(name):
    if not str(name).strip():
        return False
    else:
        return True

# ---------- NAVIGATION ----------
def set_view(view_name: str):
    st.session_state["view"] = view_name

def get_view():
    return st.session_state.get("view", "login")

def back_button(label, target_view):
    if st.button(label):
        # Clear the temporary storage when the form is submitted
        if "temp_new_manual_classes" in st.session_state:
            del st.session_state['temp_new_manual_classes'] 

        set_view(target_view)
        st.rerun()
        
        


# ---------- AUTH VIEWS ----------

def register_view():
    st.header("📝 Register New User")
    with st.form("register_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Register")

    if st.button("🔙 Back to Login"):
        set_view("login")
        st.rerun()

    
    if submitted:
        try:

            # trim inputs
            first_name = first_name.strip()
            last_name = last_name.strip()
            email = email.strip()

            if not first_name:
                st.error("Please enter your first name.", icon="❌")
                return
            
            if not last_name:
                st.error("Please enter your last name.", icon="❌")
                return

            # if not email:
            if not validate_email(email):
                st.error("Please enter a valid email address.", icon="❌")
                return

            # validate email
            df = read_users_df()
            if email in df["email"].values:
                st.error("User is already registered.", icon="❌")
                # st.toast("User is already registered.", icon="❌")

                # return from here
                return
            
            # validate password strength
            # if password:
            strength, suggestions = check_password_strength(password)
            st.markdown(f"Password Strength: {strength}", unsafe_allow_html=True)

            if suggestions:
                st.markdown("**💡 Suggestions to Improve Your Password:**")
                for suggestion in suggestions:
                    st.markdown(f"- {suggestion}")
                
                # return from here
                return

            
            # create UUID
            user_uuid = str(uuid.uuid4())

            # create user folder
            user_folder = os.path.join(DATA_DIR_USERS, sanitize_email(email))
            os.makedirs(user_folder, exist_ok=True)

            # Copy template JSON
            if os.path.exists(DATA_TEMPLATE):
                shutil.copy(DATA_TEMPLATE, os.path.join(user_folder, "annotations.json"))

            # encrypt password
            password_hash = hash_password(password)

            append_user_row(first_name, last_name, email, password_hash, user_folder, user_uuid)
            st.success("Registration successful! Please log in.")

            # Redirect to login after 5 seconds
            with st.spinner("Redirecting to login view...", show_time=True):
                time.sleep(1)
                set_view("login")
                st.rerun()


        except Exception as e:
            log_error(str(e))
            st.error(f"Registration failed: {e}", icon="❌")
            # st.toast(f"Registration failed: {e}", icon="❌")

    # if st.button("🔙 Back to Login"):
    #     set_view("login")
    #     st.rerun()

def login_view():

    st.header("🔐 Login")
    with st.form("login_form"):
        email = st.text_input("Email").strip().lower()
        # password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
    
    # -- Register button --
    # if st.button("🆕 Register New User"):
    #     set_view("register")
    #     st.rerun()

    if submitted:
        try:
            df = read_users_df()
            
            # output = df.to_string()
            # # st.text_area("OUTPUT", "\n".join(df["email"].values))
            # st.text_area("OUTPUT", output)

            if email not in df["email"].values:
                st.error("User not found.", icon="❌")
                # st.toast("User not found.", icon="❌")
                return
            
            row = df[df["email"] == email].iloc[0] # find and get matching the row

            # if verify_password(password, row["password_hash"]):
            #     st.session_state["user_email"] = email
            #     st.session_state["user_folder"] = row["user_folder"]
            #     st.session_state["user_uuid"] = row["uuid"]
            #     st.success("Login successful!")
            #     set_view("all_pdfs")
            #     st.rerun()
            # else:
            #     st.error("Incorrect password.", icon="❌")
            #     # st.toast("Incorrect password.", icon="❌")

            # -- Show the PDFs view -- #
            st.session_state["user_email"] = email
            st.session_state["user_folder"] = row["user_folder"]
            st.session_state["first_name"] = row["first_name"]
            st.session_state["last_name"] = row["last_name"]
            st.session_state["is_admin"] = row["is_admin"]
            # st.session_state["is_first_login"] = row["is_first_login"]
            
            # -- first time login, start the time -- #
            if row["is_first_login"] == True:
                # st.subheader("❤️ First Time Visit")

                row["is_first_login"] = False
                row["time_started"] = get_current_time_string() # 2025-10-14-15-48-00

                # -- update CSV record only when the user logs in for the first time -- #
                # update user record by reading CSV file again and only updating current users record
                df_curr = read_users_df() # read most recent
                df_curr.loc[df_curr["email"] == email, "time_started"] = row["time_started"]
                df_curr.loc[df_curr["email"] == email, "is_first_login"] = row["is_first_login"]
                write_users_df(df=df_curr)


            # -- update session state -- #
            #     st.session_state["is_first_login"] = row["is_first_login"]
            #     st.session_state["time_started"] = row["time_started"]

            #     # st.subheader(f"❤️ Time Started: {row["time_started"]}")
            # else:
            #     # st.subheader("💀 Old User")
            #     st.session_state["is_first_login"] = row["is_first_login"]
            #     st.session_state["time_started"] = row["time_started"]

            st.session_state["is_first_login"] = row["is_first_login"]
            st.session_state["time_started"] = row["time_started"]
            st.session_state["time_given_days"] = row["time_given_days"]

            

            # st.session_state[""] = row[""]
            
            
            # output = df_curr.to_string()
            # # st.text_area("OUTPUT", "\n".join(df["email"].values))
            # st.text_area("OUTPUT NEW", output)
            
            st.success("Login successful!")
            time.sleep(1)
            set_view("all_pdfs")
            st.rerun()
        except Exception as e:
            log_error(str(e))
            st.error(f"Login failed: {e}", icon="❌")
            # st.toast(f"Login failed: {e}", icon="❌")

    # if st.button("🆕 Register New User"):
    #     set_view("register")
    #     st.rerun()

# ---------- APP VIEWS ----------

@st.dialog("View PDF")
def view_pdf(path_to_pdf_file):
    st.pdf(path_to_pdf_file, height=600)


def admin_view():
    if st.session_state.get('is_admin',False) == True:
        st.header("Admin View")
        
        # st.subheader("Download Data")
        # with st.container(border=True):
        #     for dir_name in os.listdir("data/"):
        #         # Display download button
        #         st.download_button(
        #             label=f"Download: {dir_name}",
        #             data="",
        #             file_name="{dir_name}.json",
        #             mime="text/json"
        #         )
        # zip_folder('path/to/folder', 'output.zip')

        zip_and_download_folder("data/", f"annotations_backup_{get_current_time_string()}.zip")
    
    back_button("⬅️ Back to All Papers", "all_pdfs")


def all_pdfs_view():
    st.header(f"Welcome, {st.session_state.get('first_name','')} {st.session_state.get('last_name','')}!")

    #------------------------------------
    # Progress tracker view
    #------------------------------------

    st.subheader("Progress Tracker ⏱")
    with st.container(border=True):
        time_started = st.session_state.get('time_started','')
        time_given_days = st.session_state.get('time_given_days','')

        deadline_results = check_time_status(time_started, time_given_days)

        st.markdown(f"""                                      
##### Days passed: {int(round(deadline_results["days_passed"], 0))}

##### Days remaining: {int(round(deadline_results["days_remaining"], 0))}

##### Started on: {time_started}

##### Ends on: {deadline_results["deadline"]}

""")
        
        # if deadline has passed let the user know and no longer show papers to annotate and NON ADMIN USER
        if deadline_results["is_time_up"] and (st.session_state.get('is_admin',False) == False):
            # st.markdown(f"""#### Time Remaining: {"❌" if deadline_results["is_time_up"] else "✅"}""")
            st.markdown("""#### 🚨 Your time has ended and you can no longer perform annotation. 🚨""")

            return


# 'status': status,
#         'is_time_up': status == "TIME_UP",
#         'is_almost_up': status == "ALMOST_UP",
#         'days_passed': round(days_passed, 2),
#         'days_remaining': round(days_remaining, 2),
#         'hours_remaining': round(hours_remaining, 2),
#         'deadline': deadline_dt.strftime("%Y-%m-%d-%H-%M-%S"),
#         'start_time': start_timestamp,
#         'current_time': current_dt.strftime("%Y-%m-%d-%H-%M-%S")


    # st.session_state.get('','')
    # st.session_state.get('','')
    # st.session_state.get('','')
    
    # st.session_state["is_first_login"] = row["is_first_login"]
    # st.session_state["time_started"] = row["time_started"]
    # st.session_state["time_given_days"] = row["time_given_days"]

    st.divider()
    
    
    if st.session_state.get('is_admin',False) == True:
        if st.button("🤖 Admin View", help="Show Admin view"):
                # st.session_state["selected_pdf_index"] = idx
                set_view("admin_view")
                st.rerun()

        # st.subheader("Admin Tool")
        
        # with st.container(border=True):
        #     for dir_name in os.listdir("data/"):
        #         # Display download button
        #         st.download_button(
        #             label=f"Download: {dir_name}",
        #             data="",
        #             file_name="{dir_name}.json",
        #             mime="text/json"
        #         )
        # zip_folder('path/to/folder', 'output.zip')

        st.divider()

    st.subheader("📄 All Research Papers")
    
    user_folder = st.session_state["user_folder"]
    data_path = os.path.join(user_folder, "annotations.json")
    data = load_json(data_path)

    pdfs = data.get("pdf_documents", [])
    if not pdfs:
        st.info("No PDFs found for this user.")
        # return
    else:
        cols = st.columns(3)
        for idx, pdf in enumerate(pdfs):
            col = cols[idx % 3]
            with col:
                disabled = not pdf.get("active", True)
                completed = pdf.get("completed", False)
                dataset_folder_name = pdf.get("dataset_folder_name", "")
                button_label = f"📘 {idx + 1} - (Paper {dataset_folder_name})" + ("✅" if completed else "⚠️")
                # help_text = "Click to view and annotate" if not completed else "The paper has been marked as completed"
                help_text = "Click to view and annotate"
                if disabled:
                    help_text += " (inactive)"
                
                if completed:
                    help_text += " (completed)"
                
                if st.button(button_label, key=f"pdf_{idx}", help=help_text, disabled=disabled):
                    st.session_state["selected_pdf_index"] = idx
                    set_view("pdf_view")
                    st.rerun()

    if st.button("🚪 Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        
        st.success("Logout successful!")
        # st.toast("Loguot successful!")
        time.sleep(1)
        set_view("login")
        st.rerun()


def pdf_view():
    st.header("📘 Paper View")
    user_folder = st.session_state["user_folder"]
    data_path = os.path.join(user_folder, "annotations.json")
    data = load_json(data_path)

    pdf_index = st.session_state.get("selected_pdf_index")
    if pdf_index is None or pdf_index >= len(data["pdf_documents"]):
        st.error("Invalid PDF selection.", icon="❌")
        # st.toast("Invalid PDF selection.", icon="❌")
        back_button("⬅️ Back to All Papers", "all_pdfs")
        return

    pdf_doc = data["pdf_documents"][pdf_index]

    # Read-only PDF info
    dataset_folder_name = pdf_doc.get("dataset_folder_name", "")
    # st.subheader(f"Paper {pdf_index + 1}")
    st.subheader(f"{pdf_index + 1} - Paper {dataset_folder_name}")
    # st.subheader(f"Paper {dataset_folder_name}")

    col1, col2 = st.columns(2)
    with col1:
        # st.text_input("Main Category", pdf_doc.get("dataset_main_category", ""), disabled=True)
        st.markdown(f"**Main Category:** {pdf_doc.get("dataset_main_category", "")}")
    with col2:
        # st.text_input("Sub Category", pdf_doc.get("dataset_sub_category", ""), disabled=True)
        st.markdown(f"**Sub Category:** {pdf_doc.get("dataset_sub_category", "")}")
        # st.text_input("Dataset Folder Name", pdf_doc.get("dataset_folder_name", ""), disabled=True)
        # st.text_input("PDF Path", pdf_doc.get("pdf_path", ""), disabled=True)
        # st.text_input("File Name", pdf_doc.get("file_name", ""), disabled=True)

    # if st.button("👁️ View PDF"):
    #     path_to_pdf_file = os.path.join(DATA_DIR_PAPERS, pdf_doc.get("pdf_path", ""), pdf_doc.get("file_name", ""))
    #     if os.path.exists(path_to_pdf_file):
    #         view_pdf(path_to_pdf_file)
    #     else:
    #         st.error(f"PDF file does not exists: {path_to_pdf_file}", icon="❌")
    #         # st.toast(f"PDF file does not exists: {path_to_pdf_file}", icon="❌")

    # view pdf in new tab
    # if st.button("🌐 View PDF"):
    github_url_to_pdf_file = DATA_URL_GITHUB + "/" + pdf_doc.get("dataset_main_category", "") + "/" +  pdf_doc.get("dataset_sub_category", "") + "/" + pdf_doc.get("dataset_folder_name", "") + "/" + pdf_doc.get("file_name", "")
    # st.link_button(label, url, *, help=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")
    st.link_button("View PDF (Github)", github_url_to_pdf_file, help="View PDF in a new browser tab on Github", type="secondary", icon="🌐", disabled=False, use_container_width=None, width="content")

    figures = pdf_doc.get("figure_annotations", [])
    st.write(f"### Figures ({len(figures)})")
    cols = st.columns(3)
    for i, fig in enumerate(figures):
        col = cols[i % 3]
        with col:
            path_to_figure_file = os.path.join(DATA_DIR_PAPERS, fig.get("figure_path", ""))
            if fig.get("figure_path") and os.path.exists(path_to_figure_file):
                st.image(path_to_figure_file, width=250, use_container_width=False)

            completed = fig.get("completed", False)
            button_label = f"Figure {i + 1}" + ("✅" if completed else "⚠️")
            # help_text = "Click to view and annotate" if not completed else "The paper has been marked as completed"
            help_text = "Click to view and annotate"
            
            if completed:
                help_text += " (completed)"
            
            if st.button(button_label, help=help_text, key=f"fig_{i}"):
                st.session_state["selected_figure_index"] = i
                set_view("annotation_view")
                st.rerun()


    with st.form("pdf_form"):
         # fig["completed"] = st.toggle("Completed", value=fig.get("completed", False), disabled=disable_rest)
        pdf_doc["completed"] = st.toggle("Completed", value=pdf_doc.get("completed", False))

        submitted = st.form_submit_button("💾 Save")
        if submitted:
            try:
                save_json(data_path, data)
                st.success("Saved successfully!")
            except Exception as e:
                log_error(str(e))
                # st.error(f"Failed to save annotation: {e}", icon="❌")
                st.toast(f"Failed to save: {e}", icon="❌")

    back_button("⬅️ Back to All Papers", "all_pdfs")


def get_qa_type_index(field_name, types):
    if field_name in types:
        return types.index(field_name)
    else:
        return 0 # default


def annotation_view():
    st.header("🖊️ Annotation View")
    user_folder = st.session_state["user_folder"]
    data_path = os.path.join(user_folder, "annotations.json")
    data = load_json(data_path)

    pdf_index = st.session_state.get("selected_pdf_index")
    fig_index = st.session_state.get("selected_figure_index")
    if pdf_index is None or fig_index is None:
        # st.error("Invalid figure selection.", icon="❌")
        st.toast("Invalid figure selection.", icon="❌")
        back_button("⬅️ Back to Paper View", "pdf_view")
        return

    pdf_doc = data["pdf_documents"][pdf_index]
    # fig = data["pdf_documents"][pdf_index]["figure_annotations"][fig_index]
    fig = pdf_doc["figure_annotations"][fig_index]
    # st.subheader(f"Figure {fig_index + 1}: {fig.get('figure_label','')}")
    st.subheader(f"Figure {fig_index + 1}")


    # print()
    # print("-- annotation_view --")
    # print(f"Figure {fig_index + 1}")
    # pprint(fig)
    # print()
    # with open("logs/debug_annotation_view.log", "w", encoding="utf-8") as debug_f:
    #     debug_f.write(f"-- annotation_view --\n")
    #     debug_f.write(f"Figure {fig_index + 1}\n")
    #     pprint(fig, stream=debug_f)
    #     debug_f.write("\n")

    # -- FORM -- #
    with st.form("annotation_form"):


        with st.container(border=True):
            path_to_figure_file = os.path.join(DATA_DIR_PAPERS, fig.get("figure_path", ""))
            if fig.get("figure_path") and os.path.exists(path_to_figure_file):
                st.image(path_to_figure_file, width=250, use_container_width=False)

            # view pdf in new tab
            # if st.button("🌐 View PDF"):
            github_url_to_pdf_file = DATA_URL_GITHUB + "/" + pdf_doc.get("dataset_main_category", "") + "/" +  pdf_doc.get("dataset_sub_category", "") + "/" + pdf_doc.get("dataset_folder_name", "") + "/" + "images/figures" + "/" + fig.get("file_name", "")
            # st.link_button(label, url, *, help=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")
            st.link_button("View Figure (Github)", github_url_to_pdf_file, help="View in a new browser tab on Github", type="secondary", icon="🌐", disabled=False, use_container_width=None, width="content")



            # -- rejected checkbox -- #
            # if DEBUG_MODE:
            fig["rejected"] = fig.get("rejected", False)
            fig["rejected"] = st.checkbox("Figure is rejected (anything which is not a figure in the paper. e.g. a cover page of a journal, an advertisement, author's photograph, icon etc.)", value=fig["rejected"])

            fig["non_quantitative_or_mixed_subfigures"] = fig.get("non_quantitative_or_mixed_subfigures", False)
            fig["non_quantitative_or_mixed_subfigures"] = st.checkbox("Figure contains either all non-quantitative or mixed sub-figures (Should follow the next step rule)", value=fig["non_quantitative_or_mixed_subfigures"])


            submitted = st.form_submit_button("💾 Save and ⬅️ Back", help="⚠️ Warning: This will not save any changes to the following form fields.")
            if submitted:
                try:
                    save_json(data_path, data)

                    del st.session_state['temp_new_manual_class'] # clear session var
                    
                    st.success("Annotation saved successfully!")

                    # go back to PDF view
                    set_view(view_name="pdf_view")
                    st.rerun()

                except Exception as e:
                    log_error(str(e))
                    # st.error(f"Failed to save annotation: {e}", icon="❌")
                    st.toast(f"Failed to save annotation: {e}", icon="❌")
            
            # back_button("⬅️ Back", "pdf_view")



    
        # fig["figure_label"] = st.text_input("Figure Label", fig.get("figure_label", ""), disabled=True)
        # fig["figure_caption"] = st.text_area("Figure Caption", fig.get("figure_caption", ""), disabled=True)
        st.text("Figure Caption:")
        # st.code(fig.get("figure_caption", ""), language=None)
        st.markdown(fig.get("figure_caption", ""))

        st.markdown("#### Classification")
        # fig["auto_class"] = st.selectbox("Auto Class", [""] + ["A", "B", "C"], index=0)
        # fig["manual_class"] = st.selectbox("Manual Class", [""] + ["A", "B", "C", "unknown"], index=0)
        # auto_class_value = fig.get("auto_class", None)
        # manual_class_value = fig.get("manual_class", None)

        # with st.container(border=True):
        #     st.title("Copy Paste in streamlit")
        #     pathinput = st.text_input("Enter your Path:")
        #     #you can place your path instead
        #     Path = f'''{pathinput}'''
        #     st.code(Path, language="python")
        #     st.markdown("Now you get option to copy")


        with st.container(border=True):
            # fig["auto_class"] = st.selectbox("Auto Class", CLASS_OPTIONS, index=CLASS_OPTIONS.index(auto_class_value) if auto_class_value in CLASS_OPTIONS else None, disabled=True)
            # fig["manual_class"] = st.selectbox("Manual Class", CLASS_OPTIONS, index=CLASS_OPTIONS.index(manual_class_value) if manual_class_value in CLASS_OPTIONS else None)
            st.text("Auto Class:")
            st.code(fig.get("auto_class",""), language=None)
            # fig["auto_class"] = st.text_area("Auto Class", fig.get("auto_class",""), disabled=True)
            # copy_button(
            #     fig["auto_class"],
            #     tooltip="Copy to Clipboard",
            #     copied_label="Copied!",
            #     icon="st",
            # )
            # -- correct auto_class checkbox -- #
            fig["auto_class_data_is_correct"] = fig.get("auto_class_data_is_correct", False)
            # ( ⚠️ Warning: this overwrites the existing data in the manual class field )
            fig["auto_class_data_is_correct"] = st.checkbox("Auto class data is correct", value=fig["auto_class_data_is_correct"])
                
                
                # if 'auto_class_data_is_correct' not in st.session_state:
                #     st.session_state['auto_class_data_is_correct'] = ""
                
                # if fig["auto_class_data_is_correct"] == True:
                #     fig["manual_class"] = fig.get("auto_class","")
                #     fig.set("manual_class", fig.get("auto_class",""))
                # if (fig.get("auto_class_data_is_correct", False)):
                # if fig["auto_class_data_is_correct"]:
                #     st.success('This is correct', icon="✅")
                # else:
                #     st.success('This is incorrect', icon="⛔")
                # st.text(f"{fig["auto_class_data_is_correct"]} = {type(fig['auto_class_data_is_correct'])}")


            with st.container(border=True):
                # Initialize text area content in session_state if not already there
                if 'temp_new_manual_class' not in st.session_state:
                    st.session_state['temp_new_manual_class'] = "" # fig.get("manual_class", "")
                
                # new_manual_class = st.selectbox("➕ Add New Class", CLASS_OPTIONS, index=None, on_change="on_change_add_new_class")
                # fig.get("manual_class", None)
                new_manual_class = st.selectbox("Figure Classes", CLASS_OPTIONS, index=None)

                # TODO: filter out categorical list items
                # new_manual_class = new_manual_class
                
                # Button to append selectbox value to text area
                if st.form_submit_button("➕ Append") and (not str(new_manual_class).startswith("--")):
                    st.session_state['temp_new_manual_class'] += f"label\t{new_manual_class}\n"
                    # fig["manual_class"] = fig.get("manual_class","") + str(st.session_state['temp_new_manual_class'])

                # TODO: figure description field
                fig_class_desc = CLASS_OPTION_DESC[new_manual_class] if (new_manual_class in CLASS_OPTION_DESC) else ""
                if fig_class_desc:
                    st.text("Class description:")
                    st.markdown(fig_class_desc)

                # st.session_state['temp_new_manual_class'] += 

                # manual_class_value = fig.get("manual_class", "")

                # manual_class_value += f"{manual_class_value}\nnew_label\t{new_manual_class}"
                # new_manual_class = f"\nnew_label\t{new_manual_class}"
                # st.session_state.get("view", "login")
                # st.session_state.set("temp_new_manual_classes", manual_class_value + new_manual_class)
                # new_manual_class = st.session_state['temp_new_manual_classes']

                # fig["manual_class"] = st.text_area("Manual Class", manual_class_value)

                # prepend previously saved saved manual_calss value to current session data
                # st.session_state['temp_new_manual_class'] = fig.get("manual_class","") + st.session_state['temp_new_manual_class']
                fig["manual_class"] = fig.get("manual_class","") + str(st.session_state['temp_new_manual_class'])
                
                
                # set manual_class field values
                # if (fig.get("auto_class_data_is_correct", False)):
                    # fig["manual_class"] = fig.get("auto_class","")
                    # fig.set("manual_class", fig.get("auto_class",""))
                    # fig["manual_class"] = st.text_area("-Manual Class", value=fig.get("auto_class",""))
                # else:
                fig["manual_class"] = st.text_area("Manual Class", value=fig.get("manual_class",""))
                
                # def on_change_add_new_class():
                #     fig["manual_class"] = fig["manual_class"] + f"\nnew_label\t{new_manual_class}"

                # st.session_state['temp_new_manual_classes'] = ""

                # # Clear the temporary storage when the form is submitted
                # del st.session_state['temp_new_manual_class'] # BUG: does not save manual_class
                # st.session_state['temp_new_manual_class'] = "" # BUG: manually enter data in manual_class field workd, using append button doesn't update data in this field when saved.

                
                
             
            
            # disable rest of the form if manual_class is "unknown"
            # disable_rest = (fig["manual_class"] == "unknown") # BUG: even if it is True, the fields are not disabled, perhaps a refresh is needed
            disable_rest = False

            fig["comment_auto_class"] = st.text_area("Comment on Auto Class", fig.get("comment_auto_class",""), disabled=disable_rest)
        
        # # disable rest of the form if manual_class is "unknown"
        # disable_rest = (fig["manual_class"] == "unknown")
        

        st.markdown("#### Data")
        with st.container(border=True):#, horizontal_alignment="right"):
            # fig["auto_data"] = st.text_area("Auto Data", fig.get("auto_data",""), disabled=True)
            # copy_button(
            #     fig["auto_data"],
            #     tooltip="Copy to Clipboard",
            #     copied_label="Copied!",
            #     icon="st",
            # )
            st.text("Auto Data:")
            st.code(fig.get("auto_data",""), language=None)

            fig["auto_data_is_correct"] = fig.get("auto_data_is_correct", False)
            fig["auto_data_is_correct"] = st.checkbox("Auto data is correct", value=fig["auto_data_is_correct"])


        with st.container(border=True):#, horizontal_alignment="right"):
            fig["manual_data"] = st.text_area("Manual Data", fig.get("manual_data",""), disabled=disable_rest)
            # view pdf in new tab
            # st.link_button(label, url, *, help=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")
            st.link_button("Online Markdown Editor", MARKDOWN_EDITOR_URL, help="Edit Markdown in a new browser tab", type="secondary", icon="🌐", disabled=False, use_container_width=None, width="content")
            # copy_button(
            #     fig["manual_data"],
            #     tooltip="Copy to Clipboard",
            #     copied_label="Copied!",
            #     icon="st",
            # )

        

        # fig["auto_data"] = st.markdown(fig.get("auto_data",""))
        # fig["manual_data"] = st_quill(value=fig.get("manual_data","")) if not disable_rest else "" # BUG: quill
        # if not disable_rest:
        #     manual_data_val = fig.get("manual_data", "")
        #     # quill_value = st_quill(value=manual_data_val, key=f"manual_data_{pdf_index}_{fig_index}")
        #     quill_value = st_markdown(manual_data_val, key=f"manual_data_{pdf_index}_{fig_index}")

        #     # st_quill returns dict or None; convert to plain string
        #     if isinstance(quill_value, dict) and "text" in quill_value:
        #         fig["manual_data"] = quill_value["text"]
        #     elif isinstance(quill_value, str):
        #         fig["manual_data"] = quill_value
        #     else:
        #         fig["manual_data"] = ""
        # else:
        #     fig["manual_data"] = ""

        

        st.markdown("#### Summaries")
        with st.container(border=True):
            # fig["auto_summary"] = st.text_area("Auto Summary", fig.get("auto_summary",""), disabled=True)
            # copy_button(
            #     fig["auto_summary"],
            #     tooltip="Copy to Clipboard",
            #     copied_label="Copied!",
            #     icon="st",
            # )
            st.text("Auto Summary:")
            st.code(fig.get("auto_summary",""), language=None)
            
            fig["manual_summary"] = st.text_area("Manual Summary", fig.get("manual_summary",""), disabled=disable_rest)
            fig["comment_on_auto_summary"] = st.text_area("Comment on Auto Summary", fig.get("comment_on_auto_summary",""), disabled=disable_rest)

        st.markdown("#### Questions / Answers")
        # fetch indexes of saved question and answer types
        q1_type_index = get_qa_type_index(fig.get("q1_type",""), Q_TYPES)
        q2_type_index = get_qa_type_index(fig.get("q2_type",""), Q_TYPES)
        q3_type_index = get_qa_type_index(fig.get("q3_type",""), Q_TYPES)
        q4_type_index = get_qa_type_index(fig.get("q4_type",""), Q_TYPES)

        a1_type_index = get_qa_type_index(fig.get("a1_type",""), A_TYPES)
        a2_type_index = get_qa_type_index(fig.get("a2_type",""), A_TYPES)
        a3_type_index = get_qa_type_index(fig.get("a3_type",""), A_TYPES)
        a4_type_index = get_qa_type_index(fig.get("a4_type","",), A_TYPES)
        
        for i in range(1,5):
            with st.container(border=True):
                
                # eval value from named variable
                q_index = eval(f"q{i}_type_index")
                a_index = eval(f"a{i}_type_index")

                st.markdown(f"**Q{i}/A{i}**")
                fig[f"q{i}_type"] = st.selectbox(f"Q{i} Type", Q_TYPES, index=q_index, disabled=disable_rest)
                fig[f"q{i}"] = st.text_area(f"Q{i}", fig.get(f"q{i}",""), disabled=disable_rest)
                fig[f"a{i}_type"] = st.selectbox(f"A{i} Type", A_TYPES, index=a_index, disabled=disable_rest)
                fig[f"a{i}"] = st.text_area(f"A{i}", fig.get(f"a{i}",""), disabled=disable_rest)

        fig["overall_comments"] = st.text_area("Overall Comments", fig.get("overall_comments",""), disabled=disable_rest)


        with st.container(border=True, horizontal_alignment="right"):
            # fig["completed"] = st.toggle("Completed", value=fig.get("completed", False), disabled=disable_rest)
            fig["completed"] = st.toggle("Completed", value=fig.get("completed", False))

            submitted = st.form_submit_button("💾 Save")
            if submitted:
                try:
                    save_json(data_path, data)
                    del st.session_state['temp_new_manual_class'] # clear session var
                    st.success("Annotation saved successfully!")
                except Exception as e:
                    log_error(str(e))
                    # st.error(f"Failed to save annotation: {e}", icon="❌")
                    st.toast(f"Failed to save annotation: {e}", icon="❌")

    back_button("⬅️ Back to Paper View", "pdf_view")


# ---------- MAIN ----------

def main():
    st.set_page_config(page_title="ALD-E ImageMiner Annotation Tool", layout="wide", page_icon=LOGO_PAGE_ICON)
    st.logo(
        LOGO_SIDEBAR,
        icon_image=LOGO_MAIN,
        # link=""
    )

    # Create three columns
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(LOGO_MAIN, width=400)

    # st.title("📚 ALD-E ImageMiner Annotation Tool")
    # st.title("ALD-E ImageMiner Annotation Tool")
    st.markdown("<center><h1>Annotation Tool</h1></center>", unsafe_allow_html=True)

    view = get_view()
    if view == "login":
        login_view()
    elif view == "register":
        register_view()
    elif view == "all_pdfs":
        all_pdfs_view()
    elif view == "pdf_view":
        pdf_view()
    elif view == "annotation_view":
        annotation_view()
    elif view == "admin_view":
        admin_view()
    else:
        set_view("login")
        st.rerun()

if __name__ == "__main__":
    main()
