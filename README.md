# 🎮 Steam Game Recommendation System

A machine learning-powered game recommendation system built with Python, Streamlit, and scikit-learn. This application analyzes Steam game data to provide personalized game recommendations based on genres and user ratings.

## 🚀 Features

- **Smart Recommendations**: Uses TF-IDF vectorization and cosine similarity
- **Interactive Web Interface**: Built with Streamlit for easy interaction
- **Large Dataset**: Analyzes over 27,000 Steam games
- **Real-time Processing**: Cached data loading for optimal performance
- **User-friendly**: Simple dropdown selection and instant results

## 📋 Prerequisites

Before running this application, ensure you have:

- **Python 3.13 or higher** (required as specified in `pyproject.toml`)
- **Git** (for cloning the repository)
- **Package manager**: Either `pip` or `uv` (recommended)

## 🛠️ Installation & Setup

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone <repository-url>
cd game-rec

# Or download and extract the project files manually
```

### Step 2: Install Dependencies

#### Option A: Using `uv` (Recommended - Modern Python package manager)

```bash
# Install uv if you don't have it
pip install uv

# Install all dependencies
uv sync
```

#### Option B: Using `pip` (Traditional approach)

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Verify Required Files

Ensure you have these files in your project directory:

```
game-rec/
├── app.py              # Main Streamlit application
├── steam.csv           # Dataset with ~27,076 Steam games
├── pyproject.toml      # Project configuration
├── requirements.txt    # Python dependencies
├── uv.lock            # Lock file (if using uv)
└── README.md          # This file
```

### Step 4: Run the Application

```bash
# Start the Streamlit application
streamlit run app.py
```

The application will:
- Start a local web server (usually at `http://localhost:8501`)
- Open your default browser automatically
- Display the Steam Game Recommendation interface

## 🎯 How to Use

1. **Select a Game**: Choose from a random sample of 10 games in the dropdown
2. **Get Recommendations**: Click the "Rekomendasikan Game Serupa" button
3. **View Results**: See 6 similar games with their details including:
   - Game name and genre
   - Similarity score
   - Positive and negative ratings
   - Rating ratio

## 🔧 Technical Architecture

### Core Technologies

- **Python 3.13+**: Main programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms
- **NumPy**: Numerical computing

### Recommendation Algorithm

1. **Data Preprocessing**: 
   - Loads Steam game data from CSV
   - Combines genres, positive ratings, and negative ratings
   - Handles missing data

2. **Feature Engineering**:
   - Creates combined text features from game attributes
   - Prepares data for vectorization

3. **Machine Learning Pipeline**:
   - **TF-IDF Vectorization**: Converts text features to numerical vectors
   - **Cosine Similarity**: Calculates similarity between games
   - **Ranking**: Returns top 6 most similar games

4. **Caching**: Uses Streamlit's `@st.cache_data` for performance optimization

### Data Structure

The `steam.csv` dataset contains:
- **27,076 Steam games** with comprehensive metadata
- **Key features**: `name`, `genres`, `positive_ratings`, `negative_ratings`
- **Additional data**: release dates, developers, publishers, platforms, etc.

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. "File steam.csv tidak ditemukan" Error
```
❌ File steam.csv tidak ditemukan! Pastikan file berada di direktori yang sama dengan aplikasi ini.
```

**Solution**: Ensure `steam.csv` is in the same directory as `app.py`

#### 2. Python Version Issues
```bash
# Check your Python version
python --version

# Should be 3.13 or higher
```

**Solution**: Install Python 3.13+ from [python.org](https://python.org)

#### 3. Dependency Installation Failures
```bash
# Update pip first
pip install --upgrade pip

# Try installing with verbose output
pip install -r requirements.txt -v
```

**Solution**: Use a virtual environment to avoid conflicts

#### 4. Streamlit Port Issues
```
# If port 8501 is busy, Streamlit will use the next available port
# Check terminal output for the correct URL
```

**Solution**: Check the terminal output for the correct localhost URL

#### 5. Memory Issues with Large Dataset
**Solution**: The application is optimized with caching, but ensure you have at least 2GB RAM available

## 📊 Performance Notes

- **First Run**: May be slower due to initial data loading and model creation
- **Subsequent Runs**: Faster due to Streamlit caching
- **Memory Usage**: Efficiently handles 27K+ games
- **Response Time**: Recommendations appear within seconds

## 🚀 Production Deployment

For production deployment, consider these enhancements:

### Scalability Improvements
- **Database Integration**: Replace CSV with PostgreSQL/MongoDB
- **Redis Caching**: Implement Redis for better caching
- **API Integration**: Connect to Steam API for real-time data

### Security Enhancements
- **Input Validation**: Add comprehensive input sanitization
- **Rate Limiting**: Implement request throttling
- **Authentication**: Add user authentication system

### Monitoring & Logging
- **Error Tracking**: Integrate Sentry or similar
- **Performance Monitoring**: Add application metrics
- **Logging**: Implement structured logging

### Containerization
```dockerfile
# Example Dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Steam for providing the game data
- Streamlit team for the excellent web framework
- Scikit-learn community for the machine learning tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information about your problem

---

**Happy Gaming! 🎮** 