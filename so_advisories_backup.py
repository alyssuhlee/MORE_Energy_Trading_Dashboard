import streamlit as st
import pandas as pd

# Load your Excel file
excel_file = r"C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\SO_ADVISORIES.xlsx"

# Function to fetch latest 10 entries
def fetch_latest_10_entries():
    df = pd.read_excel(excel_file)

    # Convert TIME_MESSAGE to datetime format (if it's not already)
    df['TIME_MESSAGE'] = pd.to_datetime(df['TIME_MESSAGE'], errors='coerce')

    # Drop rows where TIME_MESSAGE couldn't be converted to datetime (if needed)
    df = df.dropna(subset=['TIME_MESSAGE'])

    # Sort dataframe by TIME_MESSAGE in descending order
    df = df.sort_values(by='TIME_MESSAGE', ascending=False)

    # Get latest 10 entries
    latest_10_entries = df.head(10)
    return latest_10_entries

# Render the scrolling content using HTML and JavaScript
st.markdown(
    """
    <style>
    .scrolling-container {
        white-space: nowrap;
        overflow: hidden;
        box-sizing: border-box;
        width: 100%;
        height: 120px; /* Adjust height as needed */
        border: 1px solid #ccc;
        border-radius: 5px;
        position: relative;
    }
    .scrolling-content {
        display: inline-block;
        padding: 10px;
        margin-right: 20px; /* Adjust margin between entries */
        background-color: #f0f0f0;
        border-radius: 5px;
    }
    .scrolling-wrapper {
        display: inline-block;
        white-space: nowrap;
        animation: marquee 240s linear infinite; 
    }
    @keyframes marquee {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    </style>
    """
    , unsafe_allow_html=True)

# Function to generate scrolling content
def generate_scrolling_content(entries):
    # list containing the advisories
    content = []
    for _, row in entries.iterrows():
        time_message = row['TIME_MESSAGE'].strftime('%m/%d/%Y %H:%M')
        message = row['MESSAGE']
        # format of showing the advisories
        entry_text = f"{time_message} - {message}"
        # store the advisories in a list
        content.append(entry_text)
    return content

# Display the scrolling container
scrolling_container = st.empty()

# Initial fetch and display
latest_entries = fetch_latest_10_entries()
scrollable_content = generate_scrolling_content(latest_entries)
if scrollable_content:
    scrolling_container.markdown(
        f"""
        <div class="scrolling-container">
            <div class="scrolling-wrapper">
                {' '.join(f'<div class="scrolling-content">{entry}</div>' for entry in scrollable_content)}
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )
else:
    st.markdown("No data available.")

# JavaScript for scrolling animation
st.markdown(
    """
    <script>
    // Function to update scrolling content
    function updateScrollContent() {
        const newContent = streamlit_component_func_fetch_latest_10_entries();

        // Generate new HTML content
        let htmlContent = '';
        newContent.forEach(entry => {
            const timeMessage = entry['TIME_MESSAGE'];
            const message = entry['MESSAGE'];
            const entryText = `${timeMessage} - ${message}`;
            htmlContent += `<div class="scrolling-content">${entryText}</div>`;
        });

        // Update scrolling container
        const container = document.querySelector('.scrolling-wrapper');
        container.innerHTML = htmlContent;

        // Reset animation duration based on updated content
        const contentWidth = container.scrollWidth;
        const containerWidth = container.clientWidth;
        const duration = (contentWidth + containerWidth) * 100; // Adjust speed as needed
        container.style.animationDuration = duration + 'ms';
    }

    setInterval(function() {
        updateScrollContent();
    }, 30); // Adjust refresh interval as needed (in milliseconds)
    </script>
    """
    , unsafe_allow_html=True)