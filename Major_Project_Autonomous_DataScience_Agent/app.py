import streamlit as st
from agents.file_reader import FileReaderAgent
from agents.profiler import DataProfiler
from agents.data_cleaner import DataCleaner
from agents.visualizer import VisualizationAgent
from agents.llm_agent import LLMAnalysisAgent
from agents.code_generator import CodeGeneratorAgent
from agents.code_executor import CodeExecutorAgent
from agents.error_fixer import ErrorFixAgent

st.set_page_config(
    page_title="Autonomous Data Science Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Autonomous Data Science Agent")

st.sidebar.title("🤖 Autonomous Data Science Agent")

st.sidebar.markdown("---")

st.sidebar.info(
    """
### Features

- 📂 Upload Dataset
- 📊 Data Profiling
- 🧹 Data Cleaning
- 📈 Data Visualization
- 🤖 AI Data Analysis
- 💻 AI Code Generator
- ⚡ Code Execution
- 🔧 Self-Healing AI
"""
)

st.sidebar.markdown("---")

st.sidebar.markdown("---")

st.sidebar.subheader("About")

st.sidebar.write("""
This application uses multiple AI agents to:

- Analyze datasets
- Generate Python code
- Execute code
- Automatically repair execution errors

Powered by Streamlit + LangChain + Groq.
""")

st.sidebar.success("Version 1.0")

if "generated_code" not in st.session_state:
    st.session_state.generated_code = ""

uploaded_file = st.file_uploader(
    "Upload a dataset",
    type=["csv", "xlsx", "xls", "json"]
)

if uploaded_file is not None:

    reader = FileReaderAgent()

    try:
        df = reader.load_file(uploaded_file)

        # Create profiler
        profiler = DataProfiler()
        profile = profiler.profile(df)

        cleaner = DataCleaner()
        cleaned_df = cleaner.clean(df)

        visualizer = VisualizationAgent()

        llm = LLMAnalysisAgent()
        
        code_generator = CodeGeneratorAgent()
        code_executor = CodeExecutorAgent()
        error_fixer = ErrorFixAgent()

        st.success("File loaded successfully!")

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📂 Dataset",
            "📊 Profile",
            "📈 Visualizations",
            "🤖 AI Analyst",
            "💻 Code Lab"
        ])

        st.divider()
    
        with tab1:
            
            st.header("📂 Dataset Information")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Rows", df.shape[0])

            with col2:
                st.metric("Columns", df.shape[1])

            st.write("### Column Names")
            st.write(list(df.columns))

            st.write("### Data Types")
            st.dataframe(
                df.dtypes.astype(str).reset_index().rename(
                    columns={"index": "Column", 0: "Data Type"}
                )
            )

            st.write("### Dataset Preview")
            st.dataframe(df.head())

        # ---------------- Data Profile ----------------
        st.divider()

        with tab2:
            st.header("📊 Data Profile")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Missing Values",
                    int(profile["missing_values"].sum())
                )

            with col2:
                st.metric(
                    "Duplicate Rows",
                    int(profile["duplicate_rows"])
                )

            st.write("### Missing Values Per Column")
            st.dataframe(
                profile["missing_values"]
                .reset_index()
                .rename(columns={"index": "Column", 0: "Missing Values"})
            )

            st.write("### Summary Statistics")
            st.dataframe(profile["summary"])

            st.divider()

        with tab3:
                st.header("🧹 Cleaned Dataset")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Original Rows", df.shape[0])

                with col2:
                    st.metric("Cleaned Rows", cleaned_df.shape[0])

                st.write("### Cleaned Dataset Preview")
                st.dataframe(cleaned_df.head())


                st.divider()

                st.header("📈 Data Visualizations")
                visualizer.show_charts(cleaned_df)

                st.divider()
        
        with tab4:
            st.header("🤖 AI Data Analyst")

            question = st.text_area(
                "Ask a question about your dataset",
                placeholder="Example: Summarize this dataset and identify important insights."
            )

            if st.button("🔍 Analyze Dataset"):

                dataframe_info = f"""
            Rows: {cleaned_df.shape[0]}
            Columns: {cleaned_df.shape[1]}

            Column Names:
            {list(cleaned_df.columns)}

            Data Types:
            {cleaned_df.dtypes}

            Summary:
            {cleaned_df.describe(include='all').to_string()}
            """

                with st.spinner("Analyzing dataset..."):

                    answer = llm.analyze(
                        dataframe_info,
                        question
                    )

                st.subheader("AI Analysis")
                st.write(answer)

                st.divider()

        st.divider()
        with tab5:
            st.header("💻 AI Code Lab")
            st.subheader("🐍 AI Code Generator")

            task = st.text_input(
                "Describe the Python task",
                placeholder="Example: Plot a histogram of Age"
            )

            if st.button("Generate Python Code"):

                dataframe_info = f"""
            Rows: {cleaned_df.shape[0]}
            Columns: {cleaned_df.shape[1]}

            Columns:
            {list(cleaned_df.columns)}

            Data Types:
            {cleaned_df.dtypes}
            """

                with st.spinner("Generating code..."):
                    st.session_state.generated_code = code_generator.generate_code(
                        dataframe_info,
                        task
                    )

            # ---------- ALWAYS SHOW THE EDITOR ----------

            if st.session_state.generated_code:

                st.subheader("⚙ Generated Code")

                st.session_state.generated_code = st.text_area(
                    "Edit Generated Code",
                    value=st.session_state.generated_code,
                    height=250,
                    key="code_editor"
                )

            if st.session_state.generated_code:

                if st.button("▶ Execute Code"):

                    with st.spinner("Executing code..."):

                        st.subheader("Code Being Executed")
                        st.code(st.session_state.generated_code)

                        result = code_executor.execute(
                            st.session_state.generated_code,
                            cleaned_df
                        )

                    # ---------------- SUCCESS ---------------- #

                    if result["success"]:

                        st.success("✅ Code executed successfully!")

                        if result["output"]:
                            st.subheader("Execution Output")
                            st.code(result["output"])

                        if "figure" in result and result["figure"] is not None:
                            st.pyplot(result["figure"])

                    # ---------------- ERROR ---------------- #

                    else:

                        st.warning("⚠ Error detected")

                        st.code(result["error"])

                        with st.spinner("AI is fixing the code..."):

                            fixed_code = error_fixer.fix_code(
                                st.session_state.generated_code,
                                result["error"]
                            )

                        st.subheader("AI Corrected Code")

                        st.code(fixed_code, language="python")

                        retry = code_executor.execute(
                            fixed_code,
                            cleaned_df
                        )

                        if retry["success"]:

                            st.success("🎉 Fixed automatically!")

                            if retry["output"]:
                                st.subheader("Execution Output")
                                st.code(retry["output"])

                            if "figure" in retry and retry["figure"] is not None:
                                st.pyplot(retry["figure"])

                        else:

                            st.error("AI could not fix the code.")

                            st.code(retry["error"])

        st.divider()

        st.caption(
            "🚀 Autonomous Data Science Agent | Built using Streamlit, Pandas, Matplotlib, LangChain & Groq"
        )
    
    except Exception as e:
        st.error(str(e))