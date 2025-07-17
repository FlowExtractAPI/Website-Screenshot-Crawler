# 📸 Website Screenshot Crawler 🌐

Capture high-quality screenshots of any website with advanced scrolling capabilities and cookie support. Perfect for web monitoring, documentation, testing, and content archival.

## ✨ Key Features

### 📷 Advanced Screenshot Capture
- **Full-Page Screenshots**: Capture entire webpage length, not just viewport
- **Custom Viewport**: Set any browser window dimensions
- **High-Quality PNG**: Lossless image format for professional results
- **Configurable Delays**: Control timing for dynamic content loading

### 🔄 Smart Scrolling System
- **Smooth Scrolling**: Gradual page scrolling with configurable distance
- **Adaptive Delays**: Customizable wait times between scroll actions
- **Dynamic Content**: Perfect for lazy-loaded content and infinite scroll pages
- **Bottom Detection**: Automatically stops at page bottom

### 🍪 Session Management
- **Cookie Support**: Import cookies for authenticated sessions
- **Persistent Sessions**: Maintain login states across captures
- **Paywall Bypass**: Access restricted content with proper authentication
- **Custom Headers**: Support for various authentication methods

### 🌐 Network Optimization
- **Network Idle Detection**: Multiple wait conditions for page loading
- **Timeout Control**: Configurable page load timeouts
- **Image Optimization**: Optional image loading control for faster processing
- **Resource Management**: Efficient memory usage with headless browsing

## 🚀 Quick Start

### Basic Screenshot
```json
{
  "link_urls": ["https://example.com"],
  "fullPage": true,
  "Sleep": 5
}
```

### Full-Page with Scrolling
```json
{
  "link_urls": ["https://example.com"],
  "fullPage": true,
  "scrollToBottom": true,
  "distance": 200,
  "delay": 150
}
```

### Custom Viewport
```json
{
  "link_urls": ["https://example.com"],
  "window_Width": 1366,
  "window_Height": 768,
  "waitUntil": "networkidle0"
}
```

### With Authentication
```json
{
  "link_urls": ["https://secure-site.com/dashboard"],
  "cookies": [
    {
      "name": "session_token",
      "value": "abc123xyz",
      "domain": ".secure-site.com"
    }
  ],
  "Sleep": 10
}
```

## 📋 Input Configuration

### 🎯 Basic Settings

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `link_urls` | Array | `["https://apify.com"]` | List of URLs to capture screenshots from |
| `fullPage` | Boolean | `false` | Capture entire page height vs viewport only |
| `Sleep` | Integer | `10` | Wait duration (seconds) after page load |
| `waitUntil` | String | `"networkidle0"` | Page load completion condition |

### 📱 Viewport Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `window_Width` | Integer | `1920` | Browser window width in pixels |
| `window_Height` | Integer | `1080` | Browser window height in pixels |

### 🔄 Scrolling Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `scrollToBottom` | Boolean | `false` | Enable automatic scrolling to page bottom |
| `distance` | Integer | `100` | Scroll distance per step (pixels) |
| `delay` | Integer | `100` | Wait time between scroll actions (milliseconds) |

### 🍪 Authentication

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `cookies` | Array | `[]` | Cookie objects for authenticated sessions |

### 🌐 Network Settings

| Parameter | Type | Options | Description |
|-----------|------|---------|-------------|
| `waitUntil` | String | `load`, `domcontentloaded`, `networkidle0`, `networkidle2` | Navigation completion condition |

#### Wait Conditions Explained:
- **`load`**: Wait until all resources are loaded
- **`domcontentloaded`**: Wait until HTML is parsed
- **`networkidle0`**: Wait until no network connections for 500ms
- **`networkidle2`**: Wait until ≤2 network connections for 500ms

## 📊 Output Data

Each successful capture returns:

```json
{
  "screenshot_url": "https://api.apify.com/v2/key-value-stores/txdAB1M5FomDeUwQH/records/k36q82evyv7pqtgl.png",
  "linkUrl": "https://codex.wordpress.org/Theme_Development"
}
```

### Output Details:
- **`screenshot_url`**: Direct download link to the captured PNG image
- **`linkUrl`**: Original URL that was captured
- **File Format**: PNG with random 16-character filename
- **Storage**: Apify Key-Value Store with permanent URLs

## 🎯 Use Cases

### 📈 Business & Monitoring
- **Website Monitoring**: Track visual changes and updates
- **Competitor Analysis**: Regular captures of competitor pages
- **Documentation**: Create visual records of web states
- **Archival**: Preserve webpage appearances over time

### 🧪 Development & Testing
- **Responsive Testing**: Verify layouts at different viewport sizes
- **Cross-Browser Testing**: Ensure consistent appearance
- **Bug Documentation**: Capture error states and issues
- **CI/CD Integration**: Automated screenshot testing

### 📚 Content & Research
- **Tutorial Creation**: Generate step-by-step visual guides
- **Academic Research**: Capture web-based data and layouts
- **Social Media**: Create engaging visual content
- **Portfolio**: Showcase web development projects

### 🔍 E-commerce & Marketing
- **Price Monitoring**: Track product pages and pricing
- **Ad Campaign Tracking**: Monitor landing pages
- **A/B Testing**: Compare different page versions
- **SEO Analysis**: Document search result pages

## ⚙️ Advanced Configuration Examples

### High-Resolution Capture
```json
{
  "link_urls": ["https://example.com"],
  "window_Width": 2560,
  "window_Height": 1440,
  "fullPage": true,
  "Sleep": 15,
  "waitUntil": "networkidle0"
}
```

### Slow-Loading Content
```json
{
  "link_urls": ["https://slow-site.com"],
  "scrollToBottom": true,
  "distance": 150,
  "delay": 300,
  "Sleep": 20,
  "waitUntil": "networkidle2"
}
```

### Mobile Viewport Simulation
```json
{
  "link_urls": ["https://mobile-site.com"],
  "window_Width": 375,
  "window_Height": 812,
  "fullPage": true,
  "Sleep": 8
}
```

### Authenticated Session
```json
{
  "link_urls": ["https://dashboard.example.com"],
  "cookies": [
    {
      "name": "auth_token",
      "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "domain": ".example.com",
      "path": "/",
      "secure": true,
      "httpOnly": true
    }
  ],
  "Sleep": 12,
  "waitUntil": "networkidle0"
}
```

## 🔧 Technical Details

### Browser Configuration
- **Engine**: Pyppeteer (Chrome/Chromium)
- **Mode**: Headless for optimal performance
- **Security**: Sandbox disabled for containerized environments
- **Memory**: Optimized shared memory usage
- **Images**: Optional image loading for faster processing

### Performance Optimization
- **Async Processing**: Non-blocking operations for multiple URLs
- **Memory Management**: Efficient resource cleanup
- **Network Optimization**: Configurable network idle detection
- **Error Handling**: Robust error recovery and logging

### File Management
- **Naming**: Random 16-character filenames to prevent conflicts
- **Storage**: Apify Key-Value Store with permanent URLs
- **Format**: PNG for lossless quality
- **Cleanup**: Automatic temporary file removal

## 🛠️ Installation & Usage

### Running the Actor

1. **Input Configuration**: Set your parameters using JSON or the visual editor
2. **Execute**: Run the actor and monitor progress
3. **Results**: Access screenshots via the generated dataset
4. **Download**: Use the provided URLs to download images

### Integration Options

- **Apify API**: Programmatic access via REST API
- **Webhooks**: Automated notifications on completion
- **Scheduling**: Run captures at regular intervals
- **Zapier Integration**: Connect with other tools and services

## 🔍 Troubleshooting

### Common Issues

**Screenshots are blank or incomplete?**
- Increase `Sleep` duration for dynamic content
- Try `waitUntil: "networkidle2"` for slower sites
- Enable `scrollToBottom` for lazy-loaded content
- Check if site blocks automation tools

**Page won't load properly?**
- Increase timeout values
- Verify URL accessibility
- Check for required cookies/authentication
- Try different `waitUntil` conditions

**Scrolling not working correctly?**
- Adjust `distance` for smaller/larger scroll steps
- Increase `delay` for slower content loading
- Verify page has scrollable content
- Check for fixed/sticky elements interfering

**Cookie authentication failing?**
- Verify cookie format and values
- Check domain and path settings
- Ensure cookies are not expired
- Test with browser developer tools first

## 📄 API Reference

### Input Schema Validation
The actor validates all input parameters according to the JSON Schema specification. Invalid inputs will result in clear error messages.

### Output Format
Results are stored in Apify Dataset with consistent structure:
- **URL**: `screenshot_url` for direct image access
- **Source**: `linkUrl` for reference tracking
- **Storage**: Permanent Key-Value Store links

### Error Handling
- **Network Errors**: Automatic retry mechanisms
- **Timeout Handling**: Graceful failure with logging
- **Invalid URLs**: Clear error messages
- **Memory Issues**: Efficient cleanup and recovery

## 🏆 Best Practices

### Configuration Tips
1. **Test First**: Start with default settings and adjust gradually
2. **Monitor Performance**: Balance quality vs speed based on needs
3. **Handle Failures**: Implement retry logic for critical captures
4. **Optimize Timing**: Adjust `Sleep` and `delay` for your target sites
5. **Use Appropriate Viewports**: Match your analysis requirements

### Performance Optimization
- Use `networkidle0` for fast, static sites
- Use `networkidle2` for dynamic, interactive sites
- Disable images loading for faster processing when not needed
- Adjust scroll parameters based on content type
- Monitor memory usage for large batch operations

### Security Considerations
- Store cookies securely when using authentication
- Validate URLs before processing
- Respect robots.txt and rate limits
- Use proper authentication methods
- Monitor for sensitive data in screenshots

## 📈 Performance Metrics

### Speed Benchmarks
- **Simple Page**: ~5-10 seconds per screenshot
- **Complex Page**: ~15-30 seconds with scrolling
- **Full Page**: Additional 2-5 seconds for scrolling
- **Authenticated**: +2-3 seconds for cookie setup

### Resource Usage
- **Memory**: ~50-100MB per browser instance
- **CPU**: Moderate usage during capture
- **Network**: Depends on page size and resources
- **Storage**: PNG files typically 100KB-5MB

## 🤝 Support & Maintenance

### Getting Help
- Review this documentation thoroughly
- Check common issues and solutions
- Test with simple examples first
- Monitor actor logs for detailed error information

### Updates & Improvements
- Regular updates for browser compatibility
- Performance optimizations based on usage patterns
- New features based on user feedback
- Security updates and bug fixes
