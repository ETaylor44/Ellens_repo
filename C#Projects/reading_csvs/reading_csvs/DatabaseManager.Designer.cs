namespace reading_csvs
{
    partial class DatabaseManager
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            getDataButton = new Button();
            textBoxName = new TextBox();
            DropDownBox = new ComboBox();
            label1 = new Label();
            addDataButton = new Button();
            addGenderTextBox = new TextBox();
            addAgeTextBox = new TextBox();
            addSurnameTextBox = new TextBox();
            addFirstNameTextBox = new TextBox();
            tabControl2 = new TabControl();
            tabPage1 = new TabPage();
            displayDataLabelRight = new Label();
            displayDataLabelLeft = new Label();
            tabPage2 = new TabPage();
            tabPage3 = new TabPage();
            AddRowButton = new Button();
            SaveButton = new Button();
            ViewAllDataTable = new DataGridView();
            firstNameDataGridViewTextBoxColumn = new DataGridViewTextBoxColumn();
            surnameDataGridViewTextBoxColumn = new DataGridViewTextBoxColumn();
            ageDataGridViewTextBoxColumn = new DataGridViewTextBoxColumn();
            genderDataGridViewTextBoxColumn = new DataGridViewTextBoxColumn();
            personBindingSource = new BindingSource(components);
            tabPage4 = new TabPage();
            ExportButton = new Button();
            checkedListBox1 = new CheckedListBox();
            tabControl2.SuspendLayout();
            tabPage1.SuspendLayout();
            tabPage2.SuspendLayout();
            tabPage3.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)ViewAllDataTable).BeginInit();
            ((System.ComponentModel.ISupportInitialize)personBindingSource).BeginInit();
            tabPage4.SuspendLayout();
            SuspendLayout();

            // 
            // getDataButton
            // 
            getDataButton.Location = new Point(169, 44);
            getDataButton.Name = "getDataButton";
            getDataButton.Size = new Size(123, 67);
            getDataButton.TabIndex = 1;
            getDataButton.Text = "Get data";
            getDataButton.UseVisualStyleBackColor = true;
            getDataButton.Click += GetDataButton_Click;
            // 
            // textBoxName
            // 
            textBoxName.Location = new Point(32, 94);
            textBoxName.Name = "textBoxName";
            textBoxName.Size = new Size(100, 23);
            textBoxName.TabIndex = 2;
            textBoxName.Click += TextBoxName_Click;
            // 
            // DropDownBox
            // 
            DropDownBox.FormattingEnabled = true;
            DropDownBox.Items.AddRange(new object[] { "First name", "Surname", "Age", "Gender" });
            DropDownBox.Location = new Point(32, 44);
            DropDownBox.Name = "DropDownBox";
            DropDownBox.Size = new Size(121, 23);
            DropDownBox.TabIndex = 3;
            DropDownBox.Text = "Search by";
            DropDownBox.SelectedIndexChanged += DropDownBox_SelectedIndexChanged;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(186, 139);
            label1.Name = "label1";
            label1.Size = new Size(38, 15);
            label1.TabIndex = 6;
            label1.Text = "label1";
            // 
            // addDataButton
            // 
            addDataButton.Location = new Point(186, 42);
            addDataButton.Name = "addDataButton";
            addDataButton.Size = new Size(140, 70);
            addDataButton.TabIndex = 4;
            addDataButton.Text = "Add to database";
            addDataButton.UseVisualStyleBackColor = true;
            addDataButton.Click += AddDataButton_Click;
            // 
            // addGenderTextBox
            // 
            addGenderTextBox.Location = new Point(39, 218);
            addGenderTextBox.Name = "addGenderTextBox";
            addGenderTextBox.Size = new Size(100, 23);
            addGenderTextBox.TabIndex = 3;
            addGenderTextBox.Text = "Enter gender";
            addGenderTextBox.Click += AddGenderTextBox_Click;
            // 
            // addAgeTextBox
            // 
            addAgeTextBox.Location = new Point(39, 155);
            addAgeTextBox.Name = "addAgeTextBox";
            addAgeTextBox.Size = new Size(100, 23);
            addAgeTextBox.TabIndex = 2;
            addAgeTextBox.Text = "Enter age";
            addAgeTextBox.Click += AddSurnameTextBox_Click;
            // 
            // addSurnameTextBox
            // 
            addSurnameTextBox.Location = new Point(39, 97);
            addSurnameTextBox.Name = "addSurnameTextBox";
            addSurnameTextBox.Size = new Size(100, 23);
            addSurnameTextBox.TabIndex = 1;
            addSurnameTextBox.Text = "Enter surname";
            addSurnameTextBox.Click += AddAgeTextBox_Click;
            // 
            // addFirstNameTextBox
            // 
            addFirstNameTextBox.Location = new Point(39, 42);
            addFirstNameTextBox.Name = "addFirstNameTextBox";
            addFirstNameTextBox.Size = new Size(100, 23);
            addFirstNameTextBox.TabIndex = 0;
            addFirstNameTextBox.Text = "Enter first name";
            addFirstNameTextBox.Click += AddFirstNameTextBox_Click;
            // 
            // tabControl2
            // 
            tabControl2.Controls.Add(tabPage1);
            tabControl2.Controls.Add(tabPage2);
            tabControl2.Controls.Add(tabPage3);
            tabControl2.Controls.Add(tabPage4);
            tabControl2.Location = new Point(-4, -2);
            tabControl2.Name = "tabControl2";
            tabControl2.SelectedIndex = 0;
            tabControl2.Size = new Size(805, 450);
            tabControl2.TabIndex = 7;
            tabControl2.SelectedIndexChanged += TabControl2_SelectedIndexChanged;
            // 
            // tabPage1
            // 
            tabPage1.Controls.Add(displayDataLabelRight);
            tabPage1.Controls.Add(displayDataLabelLeft);
            tabPage1.Controls.Add(getDataButton);
            tabPage1.Controls.Add(DropDownBox);
            tabPage1.Controls.Add(textBoxName);
            tabPage1.Location = new Point(4, 24);
            tabPage1.Name = "tabPage1";
            tabPage1.Padding = new Padding(3);
            tabPage1.Size = new Size(797, 422);
            tabPage1.TabIndex = 0;
            tabPage1.Text = "Search Data";
            tabPage1.UseVisualStyleBackColor = true;
            // 
            // displayDataLabelRight
            // 
            displayDataLabelRight.AutoSize = true;
            displayDataLabelRight.Location = new Point(571, 27);
            displayDataLabelRight.Name = "displayDataLabelRight";
            displayDataLabelRight.Size = new Size(0, 15);
            displayDataLabelRight.TabIndex = 5;
            // 
            // displayDataLabelLeft
            // 
            displayDataLabelLeft.AutoSize = true;
            displayDataLabelLeft.Location = new Point(351, 27);
            displayDataLabelLeft.Name = "displayDataLabelLeft";
            displayDataLabelLeft.Size = new Size(0, 15);
            displayDataLabelLeft.TabIndex = 4;
            // 
            // tabPage2
            // 
            tabPage2.Controls.Add(addDataButton);
            tabPage2.Controls.Add(label1);
            tabPage2.Controls.Add(addGenderTextBox);
            tabPage2.Controls.Add(addFirstNameTextBox);
            tabPage2.Controls.Add(addAgeTextBox);
            tabPage2.Controls.Add(addSurnameTextBox);
            tabPage2.Location = new Point(4, 24);
            tabPage2.Name = "tabPage2";
            tabPage2.Padding = new Padding(3);
            tabPage2.Size = new Size(797, 422);
            tabPage2.TabIndex = 1;
            tabPage2.Text = "Add data";
            tabPage2.UseVisualStyleBackColor = true;
            // 
            // tabPage3
            // 
            tabPage3.Controls.Add(AddRowButton);
            tabPage3.Controls.Add(SaveButton);
            tabPage3.Controls.Add(ViewAllDataTable);
            tabPage3.Location = new Point(4, 24);
            tabPage3.Name = "tabPage3";
            tabPage3.Padding = new Padding(3);
            tabPage3.Size = new Size(797, 422);
            tabPage3.TabIndex = 2;
            tabPage3.Text = "View All Data";
            tabPage3.UseVisualStyleBackColor = true;
            // 
            // AddRowButton
            // 
            AddRowButton.BackgroundImageLayout = ImageLayout.None;
            AddRowButton.FlatAppearance.BorderSize = 0;
            AddRowButton.FlatStyle = FlatStyle.Flat;
            AddRowButton.Font = new Font("Segoe UI", 14F);
            AddRowButton.Location = new Point(753, 264);
            AddRowButton.Name = "AddRowButton";
            AddRowButton.Size = new Size(35, 40);
            AddRowButton.TabIndex = 2;
            AddRowButton.Text = "+";
            AddRowButton.UseVisualStyleBackColor = true;
            AddRowButton.Click += AddRowButton_Click;
            // 
            // SaveButton
            // 
            SaveButton.Location = new Point(632, 367);
            SaveButton.Name = "SaveButton";
            SaveButton.Size = new Size(115, 39);
            SaveButton.TabIndex = 1;
            SaveButton.Text = "Save";
            SaveButton.UseVisualStyleBackColor = true;
            SaveButton.Click += DataTableSaveButton_Click;
            // 
            // ViewAllDataTable
            // 
            ViewAllDataTable.AllowUserToResizeColumns = false;
            ViewAllDataTable.AllowUserToResizeRows = false;
            ViewAllDataTable.AutoGenerateColumns = false;
            ViewAllDataTable.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            ViewAllDataTable.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            ViewAllDataTable.Columns.AddRange(new DataGridViewColumn[] { firstNameDataGridViewTextBoxColumn, surnameDataGridViewTextBoxColumn, ageDataGridViewTextBoxColumn, genderDataGridViewTextBoxColumn });
            ViewAllDataTable.DataSource = personBindingSource;
            ViewAllDataTable.Location = new Point(6, 6);
            ViewAllDataTable.Name = "ViewAllDataTable";
            ViewAllDataTable.Size = new Size(741, 298);
            ViewAllDataTable.TabIndex = 0;
            ViewAllDataTable.CellClick += DataTable_CellClick;
            ViewAllDataTable.CellDoubleClick += DataTableCellDoubleClick;
            ViewAllDataTable.DataError += DataTable_DataError;
            // 
            // firstNameDataGridViewTextBoxColumn
            // 
            firstNameDataGridViewTextBoxColumn.DataPropertyName = "FirstName";
            firstNameDataGridViewTextBoxColumn.HeaderText = "FirstName";
            firstNameDataGridViewTextBoxColumn.Name = "firstNameDataGridViewTextBoxColumn";
            // 
            // surnameDataGridViewTextBoxColumn
            // 
            surnameDataGridViewTextBoxColumn.DataPropertyName = "Surname";
            surnameDataGridViewTextBoxColumn.HeaderText = "Surname";
            surnameDataGridViewTextBoxColumn.Name = "surnameDataGridViewTextBoxColumn";
            // 
            // ageDataGridViewTextBoxColumn
            // 
            ageDataGridViewTextBoxColumn.DataPropertyName = "Age";
            ageDataGridViewTextBoxColumn.HeaderText = "Age";
            ageDataGridViewTextBoxColumn.Name = "ageDataGridViewTextBoxColumn";
            // 
            // genderDataGridViewTextBoxColumn
            // 
            genderDataGridViewTextBoxColumn.DataPropertyName = "Gender";
            genderDataGridViewTextBoxColumn.HeaderText = "Gender";
            genderDataGridViewTextBoxColumn.Name = "genderDataGridViewTextBoxColumn";
            // 
            // personBindingSource
            // 
            personBindingSource.DataSource = typeof(Person);
            // 
            // tabPage4
            // 
            tabPage4.Controls.Add(ExportButton);
            tabPage4.Controls.Add(checkedListBox1);
            tabPage4.Location = new Point(4, 24);
            tabPage4.Name = "tabPage4";
            tabPage4.Padding = new Padding(3);
            tabPage4.Size = new Size(797, 422);
            tabPage4.TabIndex = 3;
            tabPage4.Text = "Export Data";
            tabPage4.UseVisualStyleBackColor = true;
            // 
            // ExportButton
            // 
            ExportButton.Location = new Point(36, 158);
            ExportButton.Name = "ExportButton";
            ExportButton.Size = new Size(75, 23);
            ExportButton.TabIndex = 1;
            ExportButton.Text = "Export";
            ExportButton.UseVisualStyleBackColor = true;
            ExportButton.Click += ExportButton_Click;
            // 
            // checkedListBox1
            // 
            checkedListBox1.BorderStyle = BorderStyle.None;
            checkedListBox1.CheckOnClick = true;
            checkedListBox1.FormattingEnabled = true;
            checkedListBox1.Location = new Point(36, 43);
            checkedListBox1.Name = "checkedListBox1";
            checkedListBox1.Size = new Size(120, 90);
            checkedListBox1.TabIndex = 0;
            // 
            // DatabaseManager
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(tabControl2);
            Name = "DatabaseManager";
            Text = "Database Manager";
            tabControl2.ResumeLayout(false);
            tabPage1.ResumeLayout(false);
            tabPage1.PerformLayout();
            tabPage2.ResumeLayout(false);
            tabPage2.PerformLayout();
            tabPage3.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)ViewAllDataTable).EndInit();
            ((System.ComponentModel.ISupportInitialize)personBindingSource).EndInit();
            tabPage4.ResumeLayout(false);
            ResumeLayout(false);
        }

        #endregion
        private Button getDataButton;
        private TextBox textBoxName;
        private ComboBox DropDownBox;
        private Button addDataButton;
        private TextBox addGenderTextBox;
        private TextBox addAgeTextBox;
        private TextBox addSurnameTextBox;
        private TextBox addFirstNameTextBox;
        private Label label1;
        private TabControl tabControl2;
        private TabPage tabPage1;
        private TabPage tabPage2;
        private Label displayDataLabelLeft;
        private Label displayDataLabelRight;
        private TabPage tabPage3;
        private DataGridView ViewAllDataTable;
        private Button SaveButton;
        private TabPage tabPage4;
        private CheckedListBox checkedListBox1;
        private Button ExportButton;
        private Button AddRowButton;
        private DataGridViewTextBoxColumn firstNameDataGridViewTextBoxColumn;
        private DataGridViewTextBoxColumn surnameDataGridViewTextBoxColumn;
        private DataGridViewTextBoxColumn ageDataGridViewTextBoxColumn;
        private DataGridViewTextBoxColumn genderDataGridViewTextBoxColumn;
        private BindingSource personBindingSource;
    }
}
