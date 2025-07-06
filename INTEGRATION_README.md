# OpenManus + Autonomous LXP Integration

## 🚀 Overview

This integration combines the power of **OpenManus**'s general-purpose AI agent framework with **Autonomous LXP**'s specialized learning capabilities to create a comprehensive AI-powered learning and task execution platform.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Integrated AI Platform                    │
├─────────────────────────────────────────────────────────────┤
│  OpenManus Core (Agent Framework + Tools)                   │
│  ├── Manus Agent (General Purpose)                          │
│  ├── Data Analysis Agent                                    │
│  ├── LXP Agent (Learning Specialist)                        │
│  └── Tool Collection (Python, Browser, MCP, Learning)       │
├─────────────────────────────────────────────────────────────┤
│  LXP Integration Layer                                      │
│  ├── LXP Tool (for Manus Agent)                             │
│  ├── LXP Agent (Standalone)                                 │
│  └── Learning Capabilities                                  │
├─────────────────────────────────────────────────────────────┤
│  Shared Infrastructure                                       │
│  ├── Configuration Management                               │
│  ├── Logging and Monitoring                                 │
│  └── Memory and State Management                            │
└─────────────────────────────────────────────────────────────┘
```

## ✨ Key Features

### 🔧 OpenManus Capabilities
- **Multi-tool Integration**: Python execution, browser automation, MCP tools, file operations
- **Flexible Agent Architecture**: State management, memory, step-based execution
- **Sandbox Environment**: Secure execution for code and tools
- **Extensible Design**: Easy to add new agents and tools

### 🎓 LXP Learning Capabilities
- **Skill Assessment**: Comprehensive skill gap analysis
- **Personalized Curriculum**: AI-generated learning paths
- **Adaptive Learning**: Dynamic path adjustment based on progress
- **Progress Tracking**: Real-time learning analytics
- **Interactive Exercises**: Hands-on learning experiences
- **Feedback System**: Personalized guidance and recommendations

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd OpenManus

# Install dependencies
pip install -r requirements.txt

# Set up configuration
cp config/config.example.toml config/config.toml
# Edit config/config.toml with your API keys
```

### 2. Run the Integration Demo

```bash
# Run the comprehensive demo
python demo_integration.py
```

### 3. Use the Integrated System

```bash
# Run with all agents including LXP
python run_flow.py
```

## 📚 Usage Examples

### Example 1: Learning Request with Manus Agent

```python
from app.agent.manus import Manus

# Initialize Manus (now includes LXP capabilities)
manus = Manus()

# Ask for learning help
request = """
I'm a data analyst who wants to learn machine learning.
Can you assess my skills and create a personalized learning plan?
"""

# Manus will use LXP tools to help
result = await manus.run(request)
```

### Example 2: Standalone LXP Agent

```python
from app.agent.lxp import LXPAgent

# Initialize LXP agent
lxp_agent = LXPAgent()

# Create a learning session
session = """
I want to learn Python programming for data science.
I'm a complete beginner but motivated to learn.
"""

# Run the learning agent
result = await lxp_agent.run(session)
```

### Example 3: Direct LXP Tool Usage

```python
from app.tool.lxp_tool import LXPTool

# Initialize LXP tool
lxp_tool = LXPTool()

# Assess skills
assessment = await lxp_tool.execute(
    action="assess_skills",
    learner_profile={"name": "Alice", "role": "Data Analyst"},
    learning_goals=["Master machine learning"],
    context={"learner_id": "alice_001"}
)

# Generate curriculum
curriculum = await lxp_tool.execute(
    action="generate_curriculum",
    context={"learner_id": "alice_001"}
)
```

## 🛠️ Available LXP Actions

### 1. `assess_skills`
Assess learner's current skills and knowledge gaps.

**Parameters:**
- `learner_profile`: Learner information
- `learning_goals`: Target learning objectives
- `context`: Additional context

### 2. `generate_curriculum`
Create a personalized learning curriculum.

**Parameters:**
- `learner_profile`: Current skills and background
- `learning_goals`: Learning objectives
- `context`: Learner context

### 3. `provide_feedback`
Give personalized feedback on progress.

**Parameters:**
- `context`: Learner ID and current progress

### 4. `create_exercise`
Generate interactive learning exercises.

**Parameters:**
- `context`: Current module and learning context

### 5. `explain_concept`
Explain learning concepts clearly.

**Parameters:**
- `context`: Concept to explain and learner level

### 6. `track_progress`
Analyze and track learning progress.

**Parameters:**
- `context`: Learner ID

### 7. `adjust_path`
Adjust learning path based on performance.

**Parameters:**
- `context`: Learner ID and performance data

## 🔧 Configuration

### OpenManus Configuration

Edit `config/config.toml`:

```toml
[llm]
model = "gpt-4o"
api_key = "your-api-key"
base_url = "https://api.openai.com/v1"

[runflow]
use_data_analysis_agent = true
```

### LXP Configuration

The LXP system uses the same configuration as OpenManus but can be extended:

```toml
[lxp]
# Learning-specific settings
default_curriculum_duration = "12 weeks"
assessment_frequency = "weekly"
feedback_style = "constructive"
```

## 📊 Monitoring and Analytics

### System Health

```bash
# Check system health
curl http://localhost:5000/health

# View system metrics
curl http://localhost:5000/api/system/metrics
```

### Learning Analytics

The LXP system tracks:
- Learner progress and completion rates
- Skill improvement over time
- Learning path effectiveness
- Engagement metrics
- Performance analytics

## 🔒 Security and Safety

### Sandbox Execution
- All code execution happens in isolated environments
- File operations are restricted to workspace
- Network access is controlled and monitored

### Data Privacy
- Learner data is stored locally by default
- No personal information is shared with external services
- Configurable data retention policies

## 🚀 Deployment

### Local Development

```bash
# Run in development mode
python run_flow.py
```

### Production Deployment

```bash
# Using Docker
docker build -t openmanus-lxp .
docker run -p 5000:5000 openmanus-lxp

# Using systemd service
sudo systemctl enable openmanus-lxp
sudo systemctl start openmanus-lxp
```

## 🤝 Contributing

### Adding New Learning Tools

1. Create a new tool in `app/tool/`
2. Inherit from `BaseTool`
3. Implement the `execute` method
4. Add to the appropriate agent's tool collection

### Extending LXP Capabilities

1. Add new actions to `LXPTool`
2. Implement corresponding methods
3. Update the tool's parameters schema
4. Add tests for new functionality

## 📈 Roadmap

### Phase 1: Foundation ✅
- [x] Basic integration between OpenManus and LXP
- [x] LXP tool for Manus agent
- [x] Standalone LXP agent
- [x] Core learning capabilities

### Phase 2: Enhanced Features 🚧
- [ ] Advanced skill assessment algorithms
- [ ] Integration with external learning platforms
- [ ] Real-time collaboration features
- [ ] Advanced analytics dashboard

### Phase 3: Enterprise Features 📋
- [ ] Multi-tenant support
- [ ] SSO integration
- [ ] Advanced reporting
- [ ] API for third-party integrations

## 🐛 Troubleshooting

### Common Issues

1. **Linter Errors**: Some type checking issues may occur due to dynamic tool loading
2. **API Rate Limits**: Configure appropriate rate limiting for LLM APIs
3. **Memory Usage**: Monitor memory usage for long-running learning sessions

### Debug Mode

```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
python run_flow.py
```

## 📞 Support

- **Documentation**: Check the main OpenManus README
- **Issues**: Report bugs on GitHub
- **Discussions**: Join the community discussions
- **Email**: Contact the maintainers directly

## 📄 License

This integration is licensed under the same terms as OpenManus (MIT License).

---

**🎉 Welcome to the future of AI-powered learning and task execution!**
