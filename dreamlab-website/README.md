# DreamLab AI Consulting Website

A world-class website for DreamLab AI Consulting, showcasing executive training programs and premium Lake District accommodation.

## 🚀 Features

- **Modern Design**: Clean, professional design with DreamLab brand colors
- **Responsive Layout**: Optimized for all devices and screen sizes
- **Interactive Elements**: Smooth animations and engaging user interactions
- **Training Programs**: Detailed showcase of AI and VR training offerings
- **Luxury Accommodation**: Premium Lake District retreat presentation
- **Contact Forms**: Professional inquiry and booking forms
- **Performance Optimized**: Fast loading with lazy loading and optimizations
- **SEO Ready**: Structured data and meta tags for search engines
- **Accessibility**: WCAG compliant with keyboard navigation support

## 🛠 Technology Stack

- **HTML5**: Semantic markup with accessibility features
- **CSS3**: Modern styling with CSS Grid and Flexbox
- **JavaScript (ES6+)**: Interactive functionality and form handling
- **Alpine.js**: Lightweight reactive framework for components
- **AOS**: Animate On Scroll library for smooth animations
- **Vite**: Modern build tool for development and production

## 📦 Project Structure

```
dreamlab-website/
├── src/
│   ├── components/          # Reusable components
│   ├── pages/              # Individual page files
│   ├── styles/             # CSS stylesheets
│   │   └── main.css        # Main stylesheet
│   ├── scripts/            # JavaScript files
│   │   └── main.js         # Main application logic
│   └── assets/             # Static assets
│       ├── images/         # Image files
│       ├── fonts/          # Custom fonts
│       └── icons/          # Icon files
├── public/                 # Public assets
├── dist/                   # Built files (generated)
├── index.html              # Main HTML file
├── package.json            # Dependencies and scripts
├── vite.config.js          # Vite configuration
└── README.md              # Project documentation
```

## 🎨 Design System

### Brand Colors
- **Primary**: #6633ff (DreamLab Purple)
- **Secondary**: #00d9ff (Cyan Blue)
- **Accent**: #ff6b35 (Orange)
- **Success**: #27ae60 (Green)
- **Dark**: #1a1a1a
- **Light**: #f8f9fa

### Typography
- **Primary Font**: Inter (body text)
- **Display Font**: Space Grotesk (headings)

### Spacing Scale
- xs: 0.25rem (4px)
- sm: 0.5rem (8px)
- md: 1rem (16px)
- lg: 1.5rem (24px)
- xl: 2rem (32px)
- 2xl: 3rem (48px)
- 3xl: 4rem (64px)
- 4xl: 6rem (96px)
- 5xl: 8rem (128px)

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dreamlab-website
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open in browser**
   Navigate to `http://localhost:3000`

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run serve` - Serve built files with Python

## 🏗 Building for Production

1. **Build the project**
   ```bash
   npm run build
   ```

2. **Preview the build**
   ```bash
   npm run preview
   ```

3. **Deploy the `dist` folder** to your web server

## 📱 Sections Overview

### 1. Hero Section
- Compelling headline with gradient text
- Key statistics and metrics
- Call-to-action buttons
- Background video with fallback

### 2. Features Section
- Technology highlights
- Equipment specifications
- Sustainability features
- Interactive cards with hover effects

### 3. Training Programs
- Three main training packages
- Detailed pricing and duration
- Module breakdowns
- Featured program highlighting

### 4. Accommodation
- Luxury facility showcase
- Image gallery
- Pricing information
- Feature highlights

### 5. About Section
- Company mission and vision
- Industry statistics
- Facility diagram
- Team information

### 6. Contact Section
- Multiple contact methods
- Professional contact form
- Location information
- Form validation and submission

## 🎯 Key Business Metrics

The website prominently displays these key metrics:
- **68.5% IRR** - Investment return rate
- **£3M** - Annual revenue target
- **51,000+** - Sellafield ecosystem size
- **£16.1B** - UK nuclear industry value
- **211,500** - 2050 workforce target

## 📧 Contact Form Features

- Real-time validation
- Multiple inquiry types
- Newsletter subscription option
- Success/error notifications
- Accessibility compliant
- Mobile-optimized

## 🔧 Customization

### Colors
Update CSS variables in `src/styles/main.css`:
```css
:root {
  --color-primary: #6633ff;
  --color-secondary: #00d9ff;
  /* ... other variables */
}
```

### Content
Edit sections in `index.html` or create separate page files.

### Images
Add images to `src/assets/images/` and update references in HTML/CSS.

## 📈 Performance Features

- **Lazy Loading**: Images load as needed
- **Critical Resource Preloading**: Important assets load first
- **Optimized Assets**: Minified CSS/JS in production
- **Efficient Animations**: Hardware-accelerated transitions
- **Mobile Optimization**: Reduced content for mobile devices

## ♿ Accessibility Features

- **Semantic HTML**: Proper heading structure and landmarks
- **Keyboard Navigation**: Full keyboard accessibility
- **Screen Reader Support**: ARIA labels and descriptions
- **Color Contrast**: WCAG AA compliant contrast ratios
- **Focus Management**: Visible focus indicators
- **Skip Links**: Quick navigation for assistive technology

## 🔍 SEO Optimization

- **Meta Tags**: Comprehensive meta descriptions and keywords
- **Open Graph**: Social media sharing optimization
- **Structured Data**: JSON-LD for rich snippets
- **Semantic HTML**: Proper document structure
- **Fast Loading**: Optimized for Core Web Vitals

## 🌐 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 Content Management

To update content:

1. **Text Content**: Edit directly in `index.html`
2. **Images**: Replace files in `src/assets/images/`
3. **Styling**: Modify `src/styles/main.css`
4. **Functionality**: Update `src/scripts/main.js`

## 🚀 Deployment Options

### Static Hosting
- Netlify
- Vercel
- GitHub Pages
- AWS S3 + CloudFront

### Traditional Hosting
- Upload `dist` folder contents
- Configure web server
- Set up SSL certificate

## 📞 Support

For technical support or customization requests:
- Email: dev@dreamlab-ai.co.uk
- Documentation: See inline comments in code
- Issues: Create GitHub issues for bugs

## 📄 License

Copyright © 2025 DreamLab AI Consulting. All rights reserved.

---

**Built with ❤️ for DreamLab AI Consulting**