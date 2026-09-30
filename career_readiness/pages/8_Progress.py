import streamlit as st
import pandas as pd
from repositories.database import activities
st.title("Progress")
rows=activities()
if not rows: st.info("No activities recorded yet. Complete a learning item, save an opportunity, or practice an interview.")
else:
    frame=pd.DataFrame(rows,columns=["Type","Activity","Completed (UTC)"])
    st.metric("Recorded activities",len(frame))
    st.dataframe(frame,hide_index=True,use_container_width=True)
    st.caption("This is an activity timeline, not a universal employability score.")
