import streamlit as st
import time


# progress bar example
st.title("welcome to Streamlit! 👋" )
st.write("Progress bar example")

my_counter = st.empty()
my_bar = st.progress(0)
"let's start a long computation...!!!"
for percent_complete in range(100):
    my_counter.text(f"Progress: {percent_complete + 1}%")
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
st.write("Task completed!")
# loading spinner example
st.write("----------------------------------------------------")
st.write("Loading spinner example")
with st.spinner("Loading..."):
    time.sleep(3)
st.success("Loading complete!")
st.write("This is after the loading spinner.")
# status message example
st.write("----------------------------------------------------")
st.write("Status message example")
st.info("This is an info message.")
st.warning("This is a warning message.")
st.error("This is an error message.")
st.success("This is a success message.")
st.write("This is a normal message after the status messages.")
st.write("----------------------------------------------------")
st.write("End of progress bar examples.")




