# CraftedAi - White-Label AI Framework Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Web%20%7C%20Mobile%20%7C%20Desktop-brightgreen.svg)](https://craftedai.ngrok.io)

> **Enterprise-Grade White-Label AI Framework for Building, Deploying, and Scaling AI Applications**

CraftedAi transforms the OpenManus project into a complete white-label AI framework platform, providing everything needed to build, deploy, and manage AI applications at enterprise scale.

## 🚀 Live Demo

**Access the live platform:** [https://craftedai.ngrok.io](https://craftedai.ngrok.io)

## ✨ Features

### 🎯 Core Platform
- **White-Label Ready**: Customize branding, colors, and UI to match your brand
- **Modular Architecture**: Pick and choose components for your specific needs
- **Enterprise Security**: SOC 2 compliance, end-to-end encryption, role-based access
- **Cloud-Native**: Auto-scaling, load balancing, multi-region deployment
- **Mobile-First**: Responsive design optimized for iPhone and mobile devices

### 🤖 AI Agent Ecosystem
- **Education Agent**: Personalized learning paths, curriculum design, student assessment
- **Healthcare Agent**: Patient management, appointment scheduling, clinical support
- **HR Agent**: Recruitment automation, employee management, skill matching
- **Onboarding Agent**: Client acquisition, integration workflows, welcome automation
- **Enterprise Agent**: Business process automation, decision workflows
- **Finance Agent**: Risk assessment, portfolio analysis, investment recommendations

### 🛠️ Development Tools
- **Visual Agent Builder**: Drag-and-drop agent creation
- **Code Editor & Debugger**: Integrated development environment
- **Testing Framework**: Comprehensive testing and validation
- **CI/CD Integration**: Automated deployment pipelines

### 📊 Analytics & Monitoring
- **Real-Time Dashboards**: Live performance metrics and insights
- **Usage Analytics**: Detailed usage patterns and optimization
- **Error Tracking**: Comprehensive error monitoring and alerting
- **Cost Optimization**: Resource usage tracking and optimization

## 🏗️ Architecture

```
CraftedAi Platform
├── Frontend (React/Vanilla JS)
│   ├── Dashboard Interface
│   ├── Live Demo System
│   ├── Agent Management
│   └── Analytics Visualization
├── Backend (Python)
│   ├── Agent Orchestration
│   ├── Workflow Engine
│   ├── API Gateway
│   └── Data Processing
├── AI Agents
│   ├── Education Suite
│   ├── Healthcare Suite
│   ├── HR Suite
│   ├── Onboarding Suite
│   ├── Enterprise Suite
│   └── Finance Suite
└── Integrations
    ├── ActOne HR/L&D Platform
    ├── Third-party APIs
    ├── Database Systems
    └── Cloud Services
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+ (for development)
- Git
- ngrok (for public access)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/craftedsphere/OpenManus.git
   cd OpenManus
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Start the platform**
   ```bash
   # Start the Python server
   cd frontend
   python -m http.server 8000

   # In another terminal, start ngrok (optional)
   ngrok http --domain=craftedai.ngrok.io 8000
   ```

4. **Access the platform**
   - Local: http://localhost:8000
   - Public: https://craftedai.ngrok.io

### Background Service Setup

For production deployment, use the provided startup script:

```bash
# Make executable
chmod +x start-craftedai-services.sh

# Start services in background
./start-craftedai-services.sh
```

## 📱 Mobile Experience

The platform is fully optimized for mobile devices:

- **iPhone Optimized**: Touch-friendly interface with proper sizing
- **Responsive Design**: Adapts to all screen sizes and orientations
- **Mobile Navigation**: Collapsible hamburger menu
- **Touch Interactions**: Optimized for finger navigation
- **Safe Areas**: Support for iPhone X and newer models

## 🤖 AI Agent Categories

### Education Agent
- **Personalized Learning Paths**: AI-driven curriculum design
- **Student Assessment**: Automated evaluation and feedback
- **Progress Tracking**: Real-time learning analytics
- **Adaptive Content**: Dynamic content adjustment

### Healthcare Agent
- **Patient Management**: Comprehensive patient relationship management
- **Appointment Scheduling**: Intelligent scheduling and reminders
- **Clinical Support**: Medical record analysis and insights
- **Compliance**: Healthcare regulation compliance

### HR Agent
- **Recruitment Automation**: AI-powered candidate matching
- **Employee Management**: Performance tracking and development
- **Skill Analysis**: Competency assessment and gap analysis
- **Training Coordination**: Learning path optimization

### Onboarding Agent
- **Client Acquisition**: Streamlined client onboarding
- **Integration Setup**: Automated system integration
- **Welcome Automation**: Personalized welcome experiences
- **Success Tracking**: Onboarding progress monitoring

### Enterprise Agent
- **Process Automation**: Business workflow automation
- **Decision Support**: AI-powered decision making
- **Resource Optimization**: Intelligent resource allocation
- **Performance Monitoring**: Real-time business metrics

### Finance Agent
- **Risk Assessment**: Portfolio risk analysis
- **Investment Recommendations**: AI-driven investment advice
- **Market Analysis**: Real-time market insights
- **Compliance Monitoring**: Financial regulation compliance

## 🛠️ Development

### Project Structure
```
OpenManus/
├── frontend/                 # Web interface
│   ├── index.html           # Main dashboard
│   ├── styles.css           # Responsive styling
│   ├── script.js            # Interactive functionality
│   └── vercel.json          # Deployment config
├── app/                     # Backend application
│   ├── agent/              # AI agents
│   ├── tool/               # Tools and integrations
│   ├── prompt/             # AI prompts
│   └── mcp/                # Model Context Protocol
├── config/                 # Configuration files
├── tests/                  # Test suite
└── docs/                   # Documentation
```

### Adding New Agents

1. Create agent file in `app/agent/`
2. Define agent capabilities and tools
3. Add to agent registry in `config/`
4. Update frontend demo system
5. Test and validate

### Customization

- **Branding**: Update colors and logos in CSS variables
- **Agents**: Add new agent types and capabilities
- **Integrations**: Connect to external systems and APIs
- **Deployment**: Configure for your infrastructure

## 📊 Live Demo Features

### Interactive Agent Demos
- **Real-time Processing**: Watch agents work in real-time
- **Flow Visualization**: See the agentic workflow steps
- **Input/Output Panels**: Interactive conversation interface
- **Live Metrics**: Real-time performance tracking

### Demo Categories
1. **Education**: Curriculum design and student assessment
2. **Healthcare**: Patient management and scheduling
3. **HR**: Recruitment and employee management
4. **Onboarding**: Client acquisition and integration
5. **Enterprise**: Business process automation
6. **Finance**: Risk assessment and investment analysis

## 🔧 Configuration

### Environment Variables
```bash
# API Keys
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

# Database
DATABASE_URL=your_database_url

# Security
SECRET_KEY=your_secret_key
```

### Agent Configuration
```toml
# config/actone/agent_registry.toml
[agents.education]
name = "Education Agent"
description = "Personalized learning and curriculum design"
tools = ["curriculum_builder", "assessment_engine"]
```

## 🚀 Deployment

### Local Development
```bash
# Start development server
cd frontend
python -m http.server 8000
```

### Production Deployment
```bash
# Using the startup script
./start-craftedai-services.sh

# Or manually
nohup python -m http.server 8000 > logs/server.log 2>&1 &
nohup ngrok http --domain=your-domain.ngrok.io 8000 > logs/ngrok.log 2>&1 &
```

### Cloud Deployment
- **Vercel**: Frontend deployment with `vercel.json`
- **Heroku**: Full-stack deployment
- **AWS**: Containerized deployment with ECS
- **Docker**: Containerized application

## 📈 Monitoring & Analytics

### Real-time Metrics
- **Response Time**: Agent processing speed
- **Success Rate**: Task completion rates
- **Usage Patterns**: User interaction analytics
- **System Health**: Platform performance monitoring

### Logging
- **Application Logs**: Detailed operation logs
- **Error Tracking**: Comprehensive error monitoring
- **Performance Metrics**: System performance tracking
- **User Analytics**: Usage pattern analysis

## 🔒 Security

### Enterprise Security Features
- **End-to-End Encryption**: All data encrypted in transit and at rest
- **Role-Based Access**: Granular permission system
- **Audit Logging**: Comprehensive activity tracking
- **SOC 2 Compliance**: Enterprise security standards
- **Data Privacy**: GDPR and CCPA compliant

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on the foundation of [OpenManus](https://github.com/FoundationAgents/OpenManus)
- Inspired by modern AI frameworks and platforms
- Community contributions and feedback

## 📞 Support

- **Documentation**: [Integration Guides](INTEGRATION_README.md)
- **Issues**: [GitHub Issues](https://github.com/craftedsphere/OpenManus/issues)
- **Discussions**: [GitHub Discussions](https://github.com/craftedsphere/OpenManus/discussions)

---

**CraftedAi** - Transforming AI development with enterprise-grade white-label solutions.

*Built with ❤️ by the CraftedAi team*
