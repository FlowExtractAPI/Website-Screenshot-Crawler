# 📸 Website Screenshot Crawler 🌐

Capture high-quality screenshots of any website with advanced scrolling capabilities and cookie support. Perfect for web monitoring, documentation, testing, and content archival.

## ✨ Key Features

### 📷 Advanced Screenshot Capture
- **Full-Page Screenshots**: Capture entire webpage length, not just viewport
- **Custom Viewport**: Set any browser window dimensions
- **High-Quality PNG**: Lossless image format for professional results
- **Smart Wait Conditions**: Multiple options for page load completion

### 🍪 Session Management
- **Cookie Support**: Import cookies for authenticated sessions
- **Persistent Sessions**: Maintain login states across captures
- **Paywall Bypass**: Access restricted content with proper authentication
- **Custom Headers**: Support for various authentication methods

### 🌐 Network Optimization
- **Network Idle Detection**: Multiple wait conditions for page loading
- **Timeout Control**: Configurable page load timeouts
- **Resource Management**: Efficient memory usage with headless browsing

## 💰 Pricing Structure

This actor uses a **30-second interval** charging system for optimal cost efficiency:

### 🧮 Interactive Cost Calculator
**Plan your budget with precision!** Use our interactive cost calculator to estimate your exact costs before running the actor:

🔗 **[Launch Cost Calculator](https://script.google.com/macros/s/AKfycbw3sBQ4KOnXk91-eUDADAl1EDeooRkVubBAHBBrSpqQX_l-vbmmc2ID1M92JmB1YZyN/exec)**

Features:
- ⚡ **Real-time calculations** as you adjust parameters
- 📊 **Visual cost breakdown** by component (initialization, memory, screenshots)
- 🎯 **Scenario planning** with different configurations
- 💡 **Cost optimization suggestions** for better efficiency
- 📱 **Mobile-friendly** interface for on-the-go planning

### 📊 How Pricing Works

#### 🔧 Three Types of Charges:

1. **Actor Initialization** - One-time startup fee
2. **Memory Usage** - Based on memory allocation and runtime
3. **Screenshot Capture** - Per successful screenshot

#### ⏱️ 30-Second Interval System:
- Every **30 seconds** of runtime = **1 interval**
- **1 minute** = 2 intervals | **1 hour** = 120 intervals
- **Total operations** = Memory (GB) × Number of intervals

### 💵 Pricing Tiers

| Component | FREE | BRONZE | SILVER | GOLD |
|-----------|------|--------|--------|------|
| **Initialization** | $0.05 | $0.03 | $0.02 | $0.01 |
| **Memory (per operation)** | $0.0033 | $0.0020 | $0.0015 | $0.0005 |
| **Screenshot** | $0.01 | $0.007 | $0.006 | $0.005 |

### 📝 Pricing Examples

#### Example 1: Quick Single Screenshot
- **Scenario**: 1 screenshot, 1GB memory, 30 seconds runtime
- **Calculation**: 
  - Initialization: $0.05
  - Memory: 1GB × 1 interval × $0.0033 = $0.0033
  - Screenshots: 1 × $0.01 = $0.01
- **Total**: **$0.0633** (FREE tier)

#### Example 2: Multiple Screenshots
- **Scenario**: 10 screenshots, 2GB memory, 5 minutes runtime
- **Calculation**:
  - Initialization: $0.05
  - Memory: 2GB × 10 intervals × $0.0033 = $0.066
  - Screenshots: 10 × $0.01 = $0.10
- **Total**: **$0.216** (FREE tier)

#### Example 3: Long Running Task
- **Scenario**: 50 screenshots, 4GB memory, 30 minutes runtime
- **Calculation**:
  - Initialization: $0.05
  - Memory: 4GB × 60 intervals × $0.0033 = $0.792
  - Screenshots: 50 × $0.01 = $0.50
- **Total**: **$1.342** (FREE tier)

### 💡 Cost Optimization Tips

1. **Choose Right Memory**: Use minimum required memory allocation
2. **Optimize Runtime**: Reduce unnecessary wait times
3. **Batch Processing**: Process multiple URLs in single run
4. **Upgrade Tier**: Higher tiers offer significant savings for heavy usage
5. **Use the Calculator**: Plan your runs with our cost calculator tool

### 🔍 Understanding Your Bill

Your Apify dashboard will show:
- **Operations count**: Memory (GB) × 30-second intervals
- **Example**: 2GB memory running for 5 minutes = 2 × 10 = 20 operations
- **Cost calculation**: 20 operations × $0.0033 = $0.066 for memory usage

## 🚀 Quick Start

### Basic Screenshot
```json
{
  "link_urls": [
    { "url": "https://example.com" }
  ],
  "fullPage": true
}
```

### Multiple URLs
```json
{
  "link_urls": [
    { "url": "https://example.com" },
    { "url": "https://github.com" },
    { "url": "https://stackoverflow.com" }
  ],
  "fullPage": false,
  "waitUntil": "domcontentloaded"
}
```

### Custom Viewport
```json
{
  "link_urls": [
    { "url": "https://example.com" }
  ],
  "window_Width": 1366,
  "window_Height": 768,
  "waitUntil": "networkidle0"
}
```

### With Authentication
```json
{
  "link_urls": [
    { "url": "https://secure-site.com/dashboard" }
  ],
  "cookies": [
    {
      "name": "session_token",
      "value": "abc123xyz",
      "domain": ".secure-site.com"
    }
  ],
  "fullPage": true
}
```

## 📋 Input Configuration

### 🎯 Basic Settings

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `link_urls` | Array | `[{"url": "https://apify.com/"}]` | List of URL objects to capture screenshots from |
| `fullPage` | Boolean | `false` | Capture entire page height vs viewport only |
| `waitUntil` | String | `"domcontentloaded"` | Page load completion condition |

### 📱 Viewport Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `window_Width` | Integer | `1920` | Browser window width in pixels |
| `window_Height` | Integer | `1080` | Browser window height in pixels |

### 🔄 Scrolling Options

*Note: Scrolling features have been removed from this version. Use `fullPage: true` to capture the entire page height.*

### 🍪 Authentication

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `cookies` | Array | `[]` | Cookie objects for authenticated sessions |

### 🌐 Network Settings

| Parameter | Type | Options | Description |
|-----------|------|---------|-------------|
| `waitUntil` | String | `load`, `domcontentloaded`, `networkidle0`, `networkidle2` | Navigation completion condition |

#### Wait Conditions Explained:
- **`load`**: Wait until all resources are loaded (slower but complete)
- **`domcontentloaded`**: Wait until HTML is parsed (faster, recommended for complex sites)
- **`networkidle0`**: Wait until no network connections (may timeout on complex sites)
- **`networkidle2`**: Wait until minimal network connections (may timeout on complex sites)

## 📊 Output Data

Each successful capture returns:

```json
{
  "screenshot_url": "https://api.apify.com/v2/key-value-stores/QNNAmIXDEDePpHEd5/records/hrp8rcmv12jgllxf.png",
  "linkUrl": "https://www.medium.com"
}
```

### Output Details:
- **`screenshot_url`**: Direct download link to the captured PNG image
- **`linkUrl`**: Original URL that was captured (extracted from the URL object)
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
  "link_urls": [
    { "url": "https://example.com" }
  ],
  "window_Width": 2560,
  "window_Height": 1440,
  "fullPage": true,
  "waitUntil": "networkidle0"
}
```

### Fast Processing
```json
{
  "link_urls": [
    { "url": "https://fast-site.com" }
  ],
  "fullPage": false,
  "waitUntil": "domcontentloaded"
}
```

### Mobile Viewport Simulation
```json
{
  "link_urls": [
    { "url": "https://mobile-site.com" }
  ],
  "window_Width": 375,
  "window_Height": 812,
  "fullPage": true
}
```

### Authenticated Session
```json
{
  "link_urls": [
    { "url": "https://dashboard.example.com" }
  ],
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

1. **Cost Planning**: Use our [cost calculator](https://script.google.com/macros/s/AKfycbw3sBQ4KOnXk91-eUDADAl1EDeooRkVubBAHBBrSpqQX_l-vbmmc2ID1M92JmB1YZyN/exec) to estimate expenses
2. **Input Configuration**: Set your parameters using JSON or the visual editor
3. **Execute**: Run the actor and monitor progress
4. **Results**: Access screenshots via the generated dataset
5. **Download**: Use the provided URLs to download images

### Integration Options

- **Apify API**: Programmatic access via REST API
- **Webhooks**: Automated notifications on completion
- **Scheduling**: Run captures at regular intervals
- **Zapier Integration**: Connect with other tools and services

## 🔍 Troubleshooting

### Common Issues

**Screenshots are blank or incomplete?**
- Try `waitUntil: "networkidle2"` for slower sites
- Enable `fullPage: true` for complete page capture
- Check if site blocks automation tools
- Verify URL accessibility

**Page won't load properly?**
- Increase timeout by using different `waitUntil` conditions
- Verify URL accessibility
- Check for required cookies/authentication
- Try `waitUntil: "domcontentloaded"` for faster loading

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
1. **Plan Costs First**: Use our cost calculator to optimize your budget
2. **Test First**: Start with default settings and adjust gradually
3. **Monitor Performance**: Balance quality vs speed based on needs
4. **Handle Failures**: Implement retry logic for critical captures
5. **Optimize Timing**: Adjust `Sleep` and `delay` for your target sites
6. **Use Appropriate Viewports**: Match your analysis requirements

### Performance Optimization
- Use `domcontentloaded` for fast, static sites (default)
- Use `networkidle0` for dynamic, interactive sites
- Use `fullPage: false` for faster viewport-only captures
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

## 🤝 Support & Resources

### **Getting Help**
- **📧 Email**: [flowextractapi@outlook.com](mailto:flowextractapi@outlook.com)
- **🐙 GitHub**: [FlowExtractAPI](https://github.com/FlowExtractAPI)
- **🐦 Twitter**: [@FlowExtractAPI](https://x.com/FlowExtractAPI)
- **🔧 Apify**: [FlowExtract API](https://apify.com/dz_omar?fpr=smcx63)

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