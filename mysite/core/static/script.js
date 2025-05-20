document.addEventListener('click', function() {
  document.getElementById('input').focus(); // Refocus on the input box on any click
});

document.getElementById('input').addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    const command = this.value;
    processCommand(command);
    this.value = ''; // Clear input after command processing
    scrollToBottom(); // Ensure the terminal scrolls to the latest output
  }
});

function processCommand(command) {
  const output = document.getElementById('output');
  const commandLower = command.trim().toLowerCase(); // Normalize command input

  switch (commandLower) {
    case 'help':
      output.innerHTML += `
        <div>Available commands:</div>
        <ul>
          <li>help - Show this help message</li>
          <li>whoami - Display the user information</li>
          <li>projects - List of projects</li>
          <li>links - Useful links</li>
          <li>clear - Clear the screen</li>
        </ul>
      `;
      break;
    case 'whoami':
      output.innerHTML += `<div>$ I'm Chad and I'm learning programming and software development. I hope you enjoy my site!</div>`;
      break;
    case 'projects':
      output.innerHTML += `<div>$ Visit my GitHub in the "links" section. </div>`;
      break;
    case 'links':
      output.innerHTML += `
        <div>Useful Links:</div>
        <ul>
          <li><a href="https://github.com/cdoors" target="_blank">GitHub</a></li>
          <!-- Correctly format your HTML comments within JavaScript strings -->
        </ul>
      `;
      break;
    case 'clear':
      output.innerHTML = '';
      break;
    default:
      output.innerHTML += `<div>$ ${command} - Command not recognized.</div>`;
  }
}

function scrollToBottom() {
  const terminal = document.getElementById('terminal');
  terminal.scrollTop = terminal.scrollHeight; // Adjust scrolling to the terminal container
}
