using CsvHelper;
using System.Collections.Generic;
using System.Diagnostics.Metrics;
using System.Globalization;
using System.Runtime.InteropServices;

namespace reading_csvs
{
    public partial class Form1 : Form
    {
        List<Person> personList = new List<Person>();
        string dataLine = string.Empty;

        // CM: Change this to use a local path. The .csv should probs be in the same folder as the .sln. This will allow other people to use the project!
        string filePath = "C:\\Users\\Egglen\\Documents\\person.csv";
        string[] categories = { "FirstName", "Surname", "Age", "Gender" };
        List<Button> listOfEditButtons = new List<Button>();
        List<Button> listOfDeleteButtons = new List<Button>();
        List<string> personDataAsList = new List<string>();
        List<Label> listOfCategoryLabels = new List<Label>();
        //List<TextBox> listOfEntryTextBoxes = new List<TextBox>();
        List<int> listOfMatchIndices = new List<int>();
        List<List<TextBox>> listOfTextBoxGroups = new List<List<TextBox>>();
        bool hasData = false;
        int numberOfMatches = 0;
        int counter = 0;
        int buttonLeftPos = 0;
        [DllImport("user32.dll")]
        static extern bool HideCaret(IntPtr hWnd);

        public Form1()
        {
            InitializeComponent();

            // CM: Space these out to make them more legible.
            // After }; there should always be an empty line.
            // Also after a } there should be an empty line, unless you're opening an else statement.
            getDataButton.Text = "View data";
            checkedListBox1.CheckOnClick = true;
            checkedListBox1.Items.AddRange(categories);
            AddColumn.FlatAppearance.MouseOverBackColor = AddColumn.BackColor;
            AddColumn.BackColorChanged += (s, e) =>
            {
                AddColumn.FlatAppearance.MouseOverBackColor = AddColumn.BackColor;
            };
            AddColumn.FlatAppearance.MouseDownBackColor = AddColumn.BackColor;
            AddColumn.BackColorChanged += (s, e) =>
            {
                AddColumn.FlatAppearance.MouseDownBackColor = AddColumn.BackColor;
            };

            StreamReader reader = new StreamReader(File.OpenRead(filePath));
            while (!reader.EndOfStream)
            {
                var line = reader.ReadLine();
                string[] dataAsList = line.Split(",");

                int ageAsInt = -1;
                bool sucessfullParse = int.TryParse(dataAsList[2], out ageAsInt);

                Person newPerson = new Person(dataAsList[0], dataAsList[1], ageAsInt, dataAsList[3]);
                personList.Add(newPerson);
            }
            reader.Close();
            personList.RemoveAt(0);
            dataGridView2.DataSource = personList;
        }

        // CM: All function names should be capitalised.
        // Search data
        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            textBoxName.Text = $"Enter {comboBox1.Text}";
        }

        // CM: Rename these. What labels are you refering to? Maybe something like DeleteSearchResultLabels
        // Don't worry about variable/function name length, it's more important to be clear!
        private void deleteLabels()
        {
            foreach (Label label in listOfCategoryLabels)
            {
                tabPage1.Controls.Remove(label);
            }
        }
        private void deleteButtons(List<Button> listOfButtons)
        {
            foreach (Button button in listOfButtons)
            {
                tabPage1.Controls.Remove(button);
            }
        }

        private void deleteTextBoxes()
        {
            foreach (List<TextBox> TextBoxGroup in listOfTextBoxGroups)
            {
                foreach (TextBox box in TextBoxGroup)
                {
                    tabPage1.Controls.Remove(box);
                }
            }
        }

        private void getDataButton_Click(object sender, EventArgs e)
        {
            numberOfMatches = 0;
            listOfMatchIndices.Clear();

            deleteLabels();
            deleteTextBoxes();
            deleteButtons(listOfDeleteButtons);
            deleteButtons(listOfEditButtons);

            listOfEditButtons.Clear();
            listOfDeleteButtons.Clear();
            listOfCategoryLabels.Clear();
            listOfTextBoxGroups.Clear();

            hasData = false;

            for (int i = 0; i < personList.Count; i++)
            {
                // CM: It's common practice to use a switch case for something like this.
                // Where you have lots of if cases, all checking the same variable (comboBox1.Text in our case).

                if (comboBox1.Text == "First name")
                {
                    if (personList[i].FirstName.ToLower() == textBoxName.Text.ToLower())
                    {
                        numberOfMatches++;
                        hasData = true;
                        listOfMatchIndices.Add(i);
                    }
                }

                else if (comboBox1.Text == "Surname")
                {
                    if (personList[i].Surname.ToLower() == textBoxName.Text.ToLower())
                    {
                        numberOfMatches++;
                        hasData = true;
                        listOfMatchIndices.Add(i);
                    }
                }

                else if (comboBox1.Text == "Age")
                {
                    numberOfMatches++;
                    int userAgeAsInt = -1;
                    bool successfulAgeParse = int.TryParse(textBoxName.Text, out userAgeAsInt);
                    if (successfulAgeParse == false)
                    {
                        MessageBox.Show("Please enter a number.");
                        hasData = true;
                    }
                    else
                    {
                        if (personList[i].Age == userAgeAsInt)
                        {
                            numberOfMatches++;
                            hasData = true;
                            listOfMatchIndices.Add(i);
                        }
                    }
                }

                else if (comboBox1.Text == "Gender")
                {
                    if (personList[i].Gender.ToLower() == textBoxName.Text.ToLower())
                    {
                        numberOfMatches++;
                        hasData = true;
                        listOfMatchIndices.Add(i);
                    }
                }
            }


            if (hasData == false)
            {
                MessageBox.Show("No entries match your search.");
            }
            else
            {
                PositionSearchResult(40);
            }
        }

        private void CreateTextBoxes(Label newLabel, int categoryIndex)
        {
            TextBox newTextBox = new TextBox();
            string EntryData = personList[listOfMatchIndices[counter]].dataAsList()[categoryIndex];
            newTextBox.Text = $"{EntryData}";
            newTextBox.Top = newLabel.Top;
            newTextBox.Left = newLabel.Right;
            newTextBox.Width = newLabel.Width;
            newTextBox.BorderStyle = BorderStyle.None;
            newTextBox.ReadOnly = true;
            newTextBox.BackColor = Color.White;
            newTextBox.Cursor = System.Windows.Forms.Cursors.Arrow;
            newTextBox.MouseDown += NewTextBox_Click;
            newTextBox.MouseMove += newTextBox_MouseMove;
            tabPage1.Controls.Add(newTextBox);
            buttonLeftPos = newTextBox.Right;
            listOfTextBoxGroups[counter].Add(newTextBox);

        }

        private void NewTextBox_Click(object sender, EventArgs e)
        {
            // Stop blinking cursor before edit button pressed.
            TextBox TextBoxSender = (TextBox)sender;
            HideCaret(TextBoxSender.Handle);

        }
        private void newTextBox_MouseMove(object sender, MouseEventArgs e)
        {
            // Disable selected text.
            TextBox TextBoxSender = (TextBox)sender;
            TextBoxSender.SelectionLength = 0;
        }

        public void PositionSearchResult(int leftIncrement)
        {
            // All the magic numbers here should be put into variables, so people know what the number is and can understand why you are adding it.
            // E.g.:
            // int baseOffsetXInPixels = 20;
            int LabelOffsetY = getDataButton.Top;
            int LabelOffsetX = getDataButton.Right + 20; //baseOffsetXInPixels
            int delButtonOffsetY = getDataButton.Top + 40;
            int editButtonOffsetY = getDataButton.Top + 15;
            int ButtonOffsetX = getDataButton.Right + 140;
            int labelHeight = 20;
            int numberOfLabels = 4;
            int combinedLabelHeight = labelHeight * numberOfLabels; 
            int labelWidth = 70;
            const int labelHorGap = 180;
            const int VertGap = 50;
            counter = -1;
            int horLines = 0;
            double vertLines = Math.Ceiling((double)numberOfMatches / 2d);
            if (listOfMatchIndices.Count() == 1)
            {
                horLines = 1;
            }
            else
            {
                horLines = 2;
            }
            for (int i = 0; i < vertLines; i++)
            {
                for (int j = 0; j < horLines; j++)
                {
                    if (counter+1 < listOfMatchIndices.Count())
                    {
                        counter++;
                        int LabelNewBaseLeft = LabelOffsetX + (labelWidth + labelHorGap) * j;
                        int LabelNewbaseTop = LabelOffsetY + (combinedLabelHeight + VertGap) * i;
                        int delButtonTop = delButtonOffsetY + (combinedLabelHeight + VertGap) * i;
                        int editButtonTop = editButtonOffsetY + (combinedLabelHeight + VertGap) * i;
                        CreateCategoryLabels(LabelNewbaseTop, LabelNewBaseLeft, labelHeight, labelWidth);
                        CreateDeleteButtons(delButtonTop);
                        CreateEditButtons(editButtonTop);
                    }
                }
            }
        }

        private void CreateCategoryLabels(int baseTop, int baseLeft, int labelHeight, int labelWidth)
        {
            listOfTextBoxGroups.Add(new List<TextBox>());
            for (int categoryIndex = 0; categoryIndex < categories.Count(); categoryIndex++)
            {
                Label NewLabel = new Label();
                NewLabel.Text = $"{categories[categoryIndex]}: ";
                NewLabel.Top = baseTop + (labelHeight * categoryIndex);
                NewLabel.Left = baseLeft;
                NewLabel.Width = labelWidth;
                NewLabel.Name = $"label{counter}";
                listOfCategoryLabels.Add(NewLabel);
                tabPage1.Controls.Add(NewLabel);
                CreateTextBoxes(NewLabel, categoryIndex);
            }
            
        }

        private void CreateEditButtons(int editButtonTop)
        {
            Button newButton = new Button();
            newButton.Text = "Edit";
            newButton.Name = $"EditButton{counter}";
            newButton.Top = editButtonTop;
            newButton.Left = buttonLeftPos;
            newButton.Width = 50;
            newButton.Click += editButton_Click;
            listOfEditButtons.Add(newButton);
            tabPage1.Controls.Add(newButton);
            
        }
    
        private void editButton_Click(object sender, EventArgs e)
        {
            Button parsedSender = (Button)sender;
            parsedSender.Click -= editButton_Click;
            parsedSender.Click += saveButton_Click;
            parsedSender.Text = "Save";

        }

        private void saveButton_Click(object sender, EventArgs e)
        {
            Button parsedSender = (Button)sender;
            parsedSender.Click -= saveButton_Click;
            parsedSender.Click += editButton_Click;
            parsedSender.Text = "Edit";
        }

        private void CreateDeleteButtons(int delButtonTop)
        {
            Button newButton = new Button();
            newButton.Text = "Delete";
            newButton.Name = $"DeleteButton{counter}";
            newButton.Top = delButtonTop;
            newButton.Left = buttonLeftPos;
            newButton.Width = 50;
            newButton.Click += deleteButton_Click;
            listOfDeleteButtons.Add(newButton);
            tabPage1.Controls.Add(newButton);
        }
        private void deleteButton_Click(object sender, EventArgs e)
        {
            int personIndexInPersonListToDelete = 0;
            Button parsedSender = (Button)sender;
            string name = parsedSender.Name;
            for (int i = 0; i < listOfDeleteButtons.Count; i++)
            {
                if (listOfDeleteButtons[i].Name == name)
                {
                    personIndexInPersonListToDelete = listOfMatchIndices[i];
                }
            }

            for (int i = 0; i < personList.Count; i++)
            {
                if (personIndexInPersonListToDelete == i)
                {
                    personList.RemoveAt(i);
                }
            }
            WriteCSV();


        }

        public void WriteCSV()
        {
            using (StreamWriter writer = new StreamWriter(filePath))
            {
                using (var csv = new CsvWriter(writer, CultureInfo.InvariantCulture))
                {
                    csv.WriteHeader<Person>();
                    if (personList.Count != 0)
                    {
                    csv.NextRecord();
                    }
                    for (int i = 0; i < personList.Count; i++)
                    {
                        csv.WriteRecord(personList[i]);
                        if (i != personList.Count-1)
                        {
                            csv.NextRecord();
                        }
                    }
                }
                writer.Close();
            }
        }



        private void textBoxName_Click(object sender, EventArgs e)
        {
            textBoxName.Text = string.Empty;
        }


        // Add Data.
        private void addDataButton_Click(object sender, EventArgs e)
        {
            int newAge = -1;
            bool isInt = int.TryParse(addAgeTextBox.Text, out newAge);
            if (!isInt)
            {
                MessageBox.Show("Please enter a valid number in 'Age'.");
            }
            else
            {
                string dataToAdd = $"\n{addFirstNameTextBox.Text},{addSurnameTextBox.Text},{addAgeTextBox.Text},{addGenderTextBox.Text}";
                File.AppendAllText(filePath, dataToAdd);
                Person newPerson = new Person(addFirstNameTextBox.Text, addSurnameTextBox.Text, newAge, addGenderTextBox.Text);
                personList.Add(newPerson);

                printSuccessMessage(addFirstNameTextBox.Text, addSurnameTextBox.Text);

                addFirstNameTextBox.Text = "Enter first name";
                addSurnameTextBox.Text = "Enter surname";
                addAgeTextBox.Text = "Enter age";
                addGenderTextBox.Text = "Enter gender";

            }

        }

        public void printSuccessMessage(string firstName, string surname)
        {

            label1.Text = $"{firstName} {surname} has been successfully added to the database.";
        }


        private void addFirstNameTextBox_Click(object sender, EventArgs e)
        {
            addFirstNameTextBox.Text = string.Empty;
        }
        private void addSurnameTextBox_Click(object sender, EventArgs e)
        {
            addAgeTextBox.Text = string.Empty;
        }
        private void addAgeTextBox_Click(object sender, EventArgs e)
        {
            addSurnameTextBox.Text = string.Empty;
        }
        private void addGenderTextBox_Click(object sender, EventArgs e)
        {
            addGenderTextBox.Text = string.Empty;
        }

        // View all data and make edits.
        private void dgv2CellDoubleClick(object sender, DataGridViewCellEventArgs e)
        {
            dataGridView2.ReadOnly = false;
        }

        private void dvg2_DataError(object sender, DataGridViewDataErrorEventArgs e)
        {
            MessageBox.Show("Please enter a valid number in the 'Age' category.");
        }

        private void dataGridView2_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            dataGridView2.ReadOnly = true;
        }

        private void SaveButton_Click(object sender, EventArgs e)
        {
            WriteCSV();
        }

        private void tabControl2_SelectedIndexChanged(object sender, EventArgs e)
        {
            dataGridView2.DataSource = personList;
            dataGridView2.Update();
            dataGridView2.Refresh();
            label1.Text = string.Empty;
            textBoxName.Text = string.Empty;
            comboBox1.Text = "Search by";
        }

        private void AddColumn_Click(object sender, EventArgs e)
        {
            DataGridViewColumn NewColumn = new DataGridViewColumn();
            NewColumn.Name = $"{NewColumn} {dataGridView2.ColumnCount + 1}";
            NewColumn.HeaderText = string.Empty;
            NewColumn.CellTemplate = new DataGridViewTextBoxCell();
            dataGridView2.Columns.Insert(dataGridView2.ColumnCount, NewColumn);
        }

        //Export data.
        private void button1_Click(object sender, EventArgs e)
        {
            List<object> checkedItems = new List<object>();

            foreach (object itemChecked in checkedListBox1.CheckedItems)
            {
                checkedItems.Add(itemChecked.ToString());
            }
            exportAsCSV(checkedItems);
            MessageBox.Show("Export complete.");
            UncheckAll();
        }

        public void UncheckAll()
        {
            while (checkedListBox1.CheckedIndices.Count > 0)
                checkedListBox1.SetItemChecked(checkedListBox1.CheckedIndices[0], false);
        }

        public void exportAsCSV(List<object> checkedItems)
        {
            string newFilePath = "C:\\Users\\Egglen\\Documents\\exportedPerson.csv";
            string headersToExport = string.Empty;

            foreach (string category in categories)
            {
                if (checkedItems.Contains(category))
                {
                    headersToExport += $"{category},";
                }
            }
            headersToExport = headersToExport.Remove(headersToExport.Length - 1);

            using StreamWriter writer = new StreamWriter(newFilePath);
            {
                writer.WriteLine(headersToExport);
                foreach (Person person in personList)
                {
                    string lineToWrite = string.Empty;
                    if (headersToExport.Contains("FirstName"))
                    {
                        lineToWrite += $"{person.FirstName},";
                    }
                    if (headersToExport.Contains("Surname"))
                    {
                        lineToWrite += $"{person.Surname},";
                    }
                    if (headersToExport.Contains("Age"))
                    {
                        lineToWrite += $"{person.Age},";
                    }
                    if (headersToExport.Contains("Gender"))
                    {
                        lineToWrite += $"{person.Gender},";
                    }
                    lineToWrite = lineToWrite.Remove(lineToWrite.Length - 1);
                    writer.WriteLine(lineToWrite);

                }
            }

        }

        
    }
}

