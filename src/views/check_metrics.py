import matplotlib.pyplot as plt


def check_metrics(div, df):
    cols = div.columns(3)
    cols[0].scatter_chart(data=df, x="size_x", y="rate")
    cols[1].bar_chart(df.sort_values("rate", ascending=False), x="name", y="rate")
    df_count = df["status"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(list(df_count.values), labels=list(df_count.index))
    cols[2].pyplot(fig)
