// Function to open a new window and display the Python code file
function openCodeWindow() {
    // Fetch the Python code file from the specified path
    fetch('FinalAIVA.py')
      .then(response => response.text()) // Get the response text (code content)
      .then(code => {
        // Open a new window
        const codeWindow = window.open('', '_blank');
  
        // Write HTML content to the new window
        codeWindow.document.write(`
          <!DOCTYPE html>
          <html>
            <head>
              <title>AIVA Code</title>
              <link rel="stylesheet" href="style.css"> <!-- Link to the external CSS file -->
            </head>
            <body>
              <pre class="code-window">${code}</pre> <!-- Apply the CSS class for code formatting -->
            </body>
          </html>
        `);
  
        // Close the document stream for the new window
        codeWindow.document.close();
      })
      .catch(error => console.error('Error fetching the code file:', error)); // Handle any errors that occurred during the fetch
  }
