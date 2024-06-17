def add_data(div):
    columns_ = div.columns([2, 3])
    columns_[0].subheader("Upload")
    add_files(columns_[0])
    add_csv(columns_[0])
    add_row(columns_[1])


def add_row(div):
    div.subheader("Add Data")

    cols1 = div.columns(3)
    cols1[0].text_input("ID (optional)", key="1")
    cols1[1].text_input("Name", key="2")
    cols1[2].text_input("Type", key="3")

    cols2 = div.columns(3)
    cols2[0].number_input("Size 1", value=None)
    cols2[1].number_input("Size 2", value=None)
    cols2[2].number_input("Size 3", value=None)

    div.text_input("Remarks (optional)", "")

    div.button("Add data")


def add_files(div):
    div.file_uploader("Files")
    div.button("Upload Files")


def add_csv(div):
    div.file_uploader("CSV", type="csv")
    div.button("Upload CSV")
