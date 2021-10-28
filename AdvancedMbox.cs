// Advanced message box [Required: System.Windows.Forms reference
using System.Windows.Forms;

DialogResult result = MessageBox.Show(text: "Text",
                                      caption: "Title", buttons: MessageBoxButtons.YesNo,
                                      icon: MessageBoxIcon.Information,
                                      MessageBoxDefaultButton.Button1);
if (result == DialogResult.Yes) {
  // if pressed on yes
}
