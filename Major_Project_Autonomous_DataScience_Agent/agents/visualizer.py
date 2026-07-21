import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


class VisualizationAgent:

    def show_charts(self, df):

        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) == 0:
            st.warning("No numeric columns found.")
            return


        # Histogram
        st.subheader("Histogram")

        column = st.selectbox(
            "Choose a numeric column",
            numeric_cols
        )

        fig, ax = plt.subplots(figsize=(6,4))
        ax.hist(df[column], bins=20)
        ax.set_title(f"Histogram of {column}")
        st.pyplot(fig)

        # Box Plot
        st.subheader("Box Plot")

        fig, ax = plt.subplots(figsize=(6,4))
        sns.boxplot(y=df[column], ax=ax)
        st.pyplot(fig)

        # Correlation Heatmap
        st.subheader("Correlation Heatmap")

        fig, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(
            df[numeric_cols].corr(),
            annot=True,
            cmap="coolwarm",
            ax=ax
        )
        st.pyplot(fig)

        # Scatter Plot
        if len(numeric_cols) >= 2:

            st.subheader("Scatter Plot")

            x = st.selectbox(
                "X-axis",
                numeric_cols,
                key="x"
            )

            y = st.selectbox(
                "Y-axis",
                numeric_cols,
                index=1,
                key="y"
            )

            fig, ax = plt.subplots(figsize=(6,4))
            sns.scatterplot(
                data=df,
                x=x,
                y=y,
                ax=ax
            )

            st.pyplot(fig)
            