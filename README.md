# 🔍 EmojiFind

**Find any emoji instantly** - A beautiful, fast, and intuitive emoji search tool with a modern interface.

🌐 **[Try it live at emojifind.dumbprojects.com](https://emojifind.dumbprojects.com/)**

![EmojiFind Preview](https://raw.githubusercontent.com/jeremehancock/EmojiFind/main/images/screenshot.png "EmojiFind Preview")

## ✨ Features

- **⚡ Instant Search** - Lightning-fast emoji search with keyword matching
- **🌙 Dark/Light Themes** - Beautiful themes that automatically save your preference
- **📋 One-Click Copy** - Click any emoji to instantly copy it to your clipboard
- **🕐 Recent History** - Quick access to your recently copied emojis
- **📱 Mobile Optimized** - Responsive design that works perfectly on all devices
- **🔄 Offline Ready** - Works with fallback emoji database if external resources fail
- **♿ Accessible** - Keyboard navigation and screen reader friendly
- **🚀 Fast Loading** - Optimized performance with smooth animations

## 📁 Project Structure

```
emojifind/
├── index.html              # Main application file
├── images/
│   └── og-image.svg        # Social media preview image
├── data/
│   ├── emojis.json         # Emoji database (see format below)
│   └── generate-emoji-json.py # Script to generate emoji database
└── README.md               # This file
```

## 🗃️ Generating Emoji Database

To create your emoji database, use the included Python script:

```bash
cd data
python generate-emoji-json.py
```

This will create the `emojis.json` file with a comprehensive emoji database including keywords for searching.

> **⚠️ Important:** The `generate-emoji-json.py` script is for local development only. Do not include this file when deploying to a web server for security reasons. Only deploy the generated `emojis.json` file along with your HTML, CSS, and other web assets.

## 🛠️ Technical Details

### Technologies Used
- **HTML5** - Semantic markup with modern features
- **CSS3** - Advanced styling with gradients, backdrop-filter, and animations
- **Vanilla JavaScript** - No dependencies, modern ES6+ features
- **SVG** - Scalable icons and graphics

### Browser Support
- ✅ Chrome 88+
- ✅ Firefox 84+
- ✅ Safari 14+
- ✅ Edge 88+

### Performance Features
- Efficient emoji filtering with keyword matching
- Debounced search for smooth typing
- CSS transforms for smooth animations
- Backdrop-filter for modern glass effects
- Optimized mobile touch interactions

## 📱 Mobile Features

- **PWA Ready** - Add to home screen capabilities
- **Touch Optimized** - Proper touch targets and feedback
- **Keyboard Handling** - Smart mobile keyboard management
- **Safe Areas** - Respects iPhone notches and Android navigation
- **iOS Styling** - Native-feeling bounce effects and interactions

## License

[MIT License](LICENSE)

## AI Disclosure

This project was created with the help of AI.
