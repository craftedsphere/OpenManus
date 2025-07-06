// CraftedAi Demo Platform JavaScript

// Global state
let currentSection = 'dashboard';
let currentScenario = 'curriculum-design';
let workflowRunning = false;
let currentStep = 0;
let mobileMenuOpen = false;

// Live Demo Management
let currentDemoCategory = 'education';
let demoRunning = false;
let demoStartTime = 0;

const demoConfigs = {
    education: {
        title: 'Education Agent Demo',
        description: 'Personalized learning path generation and student progress tracking',
        placeholder: 'Try: "Create a personalized learning path for a 10th grade student interested in computer science"',
        responses: [
            'Analyzing student profile and learning objectives...',
            'Generating personalized curriculum structure...',
            'Creating adaptive assessment framework...',
            'Setting up progress tracking milestones...',
            'Curriculum generated successfully! The learning path includes:\n\n• Foundation modules in programming basics\n• Interactive coding projects\n• Real-world application scenarios\n• Progress assessments every 2 weeks\n• Mentorship connection opportunities'
        ]
    },
    healthcare: {
        title: 'Healthcare Agent Demo',
        description: 'Patient relationship management and appointment scheduling with clinical support',
        placeholder: 'Try: "Schedule a follow-up appointment for patient John Smith and send reminder notifications"',
        responses: [
            'Accessing patient records and medical history...',
            'Checking available appointment slots...',
            'Verifying insurance coverage...',
            'Scheduling appointment and sending confirmations...',
            'Appointment scheduled successfully!\n\n📅 Date: July 15, 2025 at 2:00 PM\n👨‍⚕️ Doctor: Dr. Sarah Johnson\n📍 Location: Main Medical Center, Room 302\n📧 Confirmation sent to john.smith@email.com\n📱 SMS reminder scheduled for 24h before\n\nAdditional services offered:\n• Pre-appointment questionnaire\n• Insurance verification\n• Medical record updates'
        ]
    },
    hr: {
        title: 'HR Agent Demo',
        description: 'AI-powered recruitment and employee management automation',
        placeholder: 'Try: "Find candidates for a Senior Software Engineer position and schedule initial interviews"',
        responses: [
            'Analyzing job requirements and candidate criteria...',
            'Searching through candidate database...',
            'Matching skills and experience levels...',
            'Generating candidate shortlist...',
            'Candidate search completed!\n\n🎯 Top 5 candidates identified:\n\n1. Sarah Chen - 8 years experience, Python/React\n2. Michael Rodriguez - 6 years, Full-stack development\n3. Emily Watson - 7 years, Cloud architecture\n4. David Kim - 9 years, DevOps & backend\n5. Lisa Thompson - 5 years, Frontend specialist\n\n📅 Interviews scheduled:\n• Sarah Chen: July 12, 10:00 AM\n• Michael Rodriguez: July 12, 2:00 PM\n• Emily Watson: July 13, 11:00 AM\n\n📧 Interview invitations sent\n📋 Pre-interview assessments assigned'
        ]
    },
    onboarding: {
        title: 'Onboarding Agent Demo',
        description: 'Streamlined client acquisition and onboarding processes',
        placeholder: 'Try: "Onboard a new enterprise client for our AI platform with custom integration requirements"',
        responses: [
            'Processing client information and requirements...',
            'Generating custom onboarding checklist...',
            'Setting up integration configurations...',
            'Creating welcome package and documentation...',
            'Onboarding process initiated!\n\n🏢 Client: TechCorp Solutions\n📋 Custom Onboarding Checklist:\n\nPhase 1 (Week 1):\n• Account setup and user provisioning\n• API key generation and security setup\n• Initial training session scheduled\n\nPhase 2 (Week 2):\n• Custom integration development\n• Data migration assistance\n• Workflow configuration\n\nPhase 3 (Week 3):\n• User acceptance testing\n• Go-live preparation\n• Support team handover\n\n📧 Welcome package sent\n👥 Dedicated success manager assigned\n📞 Kickoff call scheduled for tomorrow'
        ]
    },
    enterprise: {
        title: 'Enterprise Automation Demo',
        description: 'Business process automation and decision-making workflows',
        placeholder: 'Try: "Automate the monthly expense report processing and approval workflow"',
        responses: [
            'Analyzing current expense processing workflow...',
            'Identifying automation opportunities...',
            'Configuring approval routing rules...',
            'Setting up automated notifications...',
            'Workflow automation configured!\n\n⚙️ Automated Expense Processing:\n\n📊 Process Flow:\n1. Expense submission → OCR data extraction\n2. Policy compliance check → Auto-approval/rejection\n3. Manager review → Escalation if needed\n4. Finance approval → Payment processing\n\n🔔 Notifications:\n• Submission confirmations\n• Approval status updates\n• Policy violation alerts\n• Payment confirmations\n\n📈 Expected Results:\n• 70% reduction in processing time\n• 95% accuracy in policy compliance\n• 24/7 automated processing\n• Real-time reporting dashboard'
        ]
    },
    finance: {
        title: 'Financial Analytics Demo',
        description: 'Advanced financial modeling and risk assessment',
        placeholder: 'Try: "Analyze portfolio risk and generate investment recommendations for Q3"',
        responses: [
            'Accessing portfolio data and market conditions...',
            'Running risk assessment models...',
            'Analyzing market trends and correlations...',
            'Generating investment recommendations...',
            'Financial analysis completed!\n\n📊 Portfolio Risk Assessment:\n\n🎯 Current Risk Level: Moderate (6.2/10)\n📈 Expected Return: 8.5% annually\n💼 Portfolio Value: $2.4M\n\n⚠️ Risk Factors Identified:\n• High tech sector concentration (45%)\n• Emerging market exposure (18%)\n• Currency volatility impact\n\n💡 Q3 Recommendations:\n\n1. Diversification Actions:\n   • Reduce tech exposure by 10%\n   • Increase defensive sectors (healthcare, utilities)\n   • Add bond allocation (15%)\n\n2. New Opportunities:\n   • Renewable energy ETFs\n   • International developed markets\n   • Real estate investment trusts\n\n3. Risk Mitigation:\n   • Implement stop-loss orders\n   • Hedge currency exposure\n   • Regular rebalancing schedule'
        ]
    }
};

// Demo scenarios
const scenarios = {
    'curriculum-design': {
        title: 'Curriculum Design Workflow',
        steps: [
            {
                title: 'Data Collection',
                description: 'Gathering student profiles and requirements',
                outputs: [
                    'Connecting to student database...',
                    'Retrieving 1,247 student profiles...',
                    'Analyzing learning objectives and prerequisites...',
                    'Mapping course dependencies and skill requirements...',
                    'Data collection completed successfully.'
                ]
            },
            {
                title: 'Analysis',
                description: 'Processing and analyzing collected data',
                outputs: [
                    'Running machine learning algorithms on student data...',
                    'Identifying learning patterns and preferences...',
                    'Calculating skill gaps and competency levels...',
                    'Analyzing course effectiveness metrics...',
                    'Analysis phase completed with 94% accuracy.'
                ]
            },
            {
                title: 'Generation',
                description: 'Creating personalized content and recommendations',
                outputs: [
                    'Generating personalized learning paths...',
                    'Creating adaptive curriculum structures...',
                    'Optimizing content delivery sequences...',
                    'Integrating multimedia and interactive elements...',
                    'Content generation completed successfully.'
                ]
            },
            {
                title: 'Validation',
                description: 'Quality assurance and compliance checking',
                outputs: [
                    'Running quality assurance checks...',
                    'Validating educational standards compliance...',
                    'Testing accessibility and usability...',
                    'Finalizing curriculum documentation...',
                    '✅ Curriculum design workflow completed successfully!'
                ]
            }
        ]
    },
    'student-assessment': {
        title: 'Student Assessment Workflow',
        steps: [
            {
                title: 'Data Collection',
                description: 'Gathering assessment data and performance metrics',
                outputs: [
                    'Connecting to assessment platforms...',
                    'Retrieving 2,847 assessment records...',
                    'Analyzing performance patterns and trends...',
                    'Mapping assessment criteria and rubrics...',
                    'Assessment data collection completed.'
                ]
            },
            {
                title: 'Analysis',
                description: 'Processing assessment data and generating insights',
                outputs: [
                    'Running statistical analysis on performance data...',
                    'Identifying strengths and improvement areas...',
                    'Calculating competency levels and skill mastery...',
                    'Generating comparative analytics...',
                    'Assessment analysis completed successfully.'
                ]
            },
            {
                title: 'Generation',
                description: 'Creating personalized feedback and recommendations',
                outputs: [
                    'Generating personalized feedback reports...',
                    'Creating improvement recommendations...',
                    'Designing targeted intervention strategies...',
                    'Preparing progress tracking dashboards...',
                    'Feedback generation completed.'
                ]
            },
            {
                title: 'Validation',
                description: 'Quality assurance and accuracy verification',
                outputs: [
                    'Validating assessment accuracy and reliability...',
                    'Cross-referencing with learning objectives...',
                    'Ensuring feedback quality and relevance...',
                    'Finalizing assessment reports...',
                    '✅ Student assessment workflow completed successfully!'
                ]
            }
        ]
    },
    'compliance-audit': {
        title: 'Compliance Audit Workflow',
        steps: [
            {
                title: 'Data Collection',
                description: 'Gathering compliance data and regulatory requirements',
                outputs: [
                    'Connecting to compliance databases...',
                    'Retrieving current regulatory requirements...',
                    'Analyzing institutional policies and procedures...',
                    'Mapping compliance frameworks and standards...',
                    'Compliance data collection completed.'
                ]
            },
            {
                title: 'Analysis',
                description: 'Analyzing compliance status and identifying gaps',
                outputs: [
                    'Running compliance gap analysis...',
                    'Identifying regulatory violations and risks...',
                    'Calculating compliance scores and metrics...',
                    'Analyzing historical compliance trends...',
                    'Compliance analysis completed successfully.'
                ]
            },
            {
                title: 'Generation',
                description: 'Creating compliance reports and action plans',
                outputs: [
                    'Generating comprehensive compliance reports...',
                    'Creating remediation action plans...',
                    'Designing monitoring and tracking systems...',
                    'Preparing audit documentation...',
                    'Compliance reporting completed.'
                ]
            },
            {
                title: 'Validation',
                description: 'Quality assurance and regulatory verification',
                outputs: [
                    'Validating compliance report accuracy...',
                    'Cross-referencing with regulatory authorities...',
                    'Ensuring audit trail completeness...',
                    'Finalizing compliance documentation...',
                    '✅ Compliance audit workflow completed successfully!'
                ]
            }
        ]
    }
};

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    setupNavigation();
    setupEventListeners();
    updateStats();
    startRealTimeUpdates();
}

// Navigation
function setupNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetSection = this.getAttribute('href').substring(1);
            navigateToSection(targetSection);
        });
    });
}

function navigateToSection(sectionId) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(section => {
        section.classList.remove('active');
    });

    // Show target section
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active');
    }

    // Update navigation
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
    });

    const activeLink = document.querySelector(`[href="#${sectionId}"]`);
    if (activeLink) {
        activeLink.classList.add('active');
    }

    currentSection = sectionId;
}

// Event Listeners
function setupEventListeners() {
    // Theme toggle
    const themeBtn = document.querySelector('[onclick="toggleTheme()"]');
    if (themeBtn) {
        themeBtn.addEventListener('click', toggleTheme);
    }

    // Demo start
    const demoBtn = document.querySelector('[onclick="startDemo()"]');
    if (demoBtn) {
        demoBtn.addEventListener('click', startDemo);
    }
}

// Theme Management
function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    const themeBtn = document.querySelector('[onclick="toggleTheme()"] i');
    if (themeBtn) {
        themeBtn.className = document.body.classList.contains('dark-theme')
            ? 'fas fa-sun'
            : 'fas fa-moon';
    }
}

// Demo Functions
function startDemo() {
    navigateToSection('workflows');
    showNotification('Demo started! Navigate to the Workflows section to see the interactive demo.', 'info');
}

// Agent Management
function createAgent() {
    showModal('create-agent-modal');
}

function confirmCreateAgent() {
    const name = document.getElementById('agent-name').value;
    const type = document.getElementById('agent-type').value;
    const description = document.getElementById('agent-description').value;

    if (!name || !type) {
        showNotification('Please fill in all required fields.', 'warning');
        return;
    }

    // Add agent to grid (in a real app, this would make an API call)
    addAgentToGrid(name, type, description);
    closeModal('create-agent-modal');
    showNotification(`Agent "${name}" created successfully!`, 'success');

    // Clear form
    document.getElementById('create-agent-form').reset();
}

function addAgentToGrid(name, type, description) {
    const agentsGrid = document.querySelector('.agents-grid');
    if (!agentsGrid) return;

    const agentCard = document.createElement('div');
    agentCard.className = 'agent-card';
    agentCard.innerHTML = `
        <div class="agent-header">
            <div class="agent-icon">
                <i class="${getAgentIcon(type)}"></i>
            </div>
            <div class="agent-status idle">Idle</div>
        </div>
        <div class="agent-content">
            <h3>${name}</h3>
            <p>${description || 'AI agent for automated tasks'}</p>
            <div class="agent-metrics">
                <div class="metric">
                    <span class="metric-label">Tasks Completed</span>
                    <span class="metric-value">0</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Success Rate</span>
                    <span class="metric-value">0%</span>
                </div>
            </div>
        </div>
        <div class="agent-actions">
            <button class="btn-small" onclick="testAgent('${name}')">Test</button>
            <button class="btn-small" onclick="configureAgent('${name}')">Configure</button>
            <button class="btn-small primary" onclick="startAgent('${name}')">Start</button>
        </div>
    `;

    agentsGrid.appendChild(agentCard);
}

function getAgentIcon(type) {
    const icons = {
        'curriculum': 'fas fa-book-open',
        'compliance': 'fas fa-shield-alt',
        'analytics': 'fas fa-chart-pie',
        'assessment': 'fas fa-chart-bar'
    };
    return icons[type] || 'fas fa-robot';
}

function testAgent(agentName) {
    const agents = {
        'onboarding': 'Testing onboarding automation with sample client data...',
        'healthcare': 'Running healthcare assistant diagnostics...',
        'psychiatric': 'Analyzing mental health monitoring systems...',
        'hr': 'Testing HR coordination workflows...',
        'curriculum': 'Generating sample curriculum structures...',
        'compliance': 'Running compliance audit simulations...'
    };

    const message = agents[agentName] || 'Testing agent functionality...';
    showNotification(message, 'info');

    setTimeout(() => {
        showNotification(`${agentName.charAt(0).toUpperCase() + agentName.slice(1)} agent test completed successfully!`, 'success');
    }, 3000);
}

function configureAgent(agentName) {
    const configOptions = {
        'onboarding': ['Document Types', 'Verification Rules', 'Welcome Flow', 'Integration Settings'],
        'healthcare': ['HIPAA Compliance', 'Patient Data Fields', 'Appointment Rules', 'Alert Thresholds'],
        'psychiatric': ['Crisis Detection', 'Mood Tracking', 'Clinical Guidelines', 'Emergency Contacts'],
        'hr': ['Recruitment Pipeline', 'Performance Metrics', 'Onboarding Steps', 'Compliance Rules'],
        'curriculum': ['Learning Objectives', 'Assessment Criteria', 'Adaptive Rules', 'Content Sources'],
        'compliance': ['Regulatory Frameworks', 'Audit Schedules', 'Reporting Rules', 'Alert Settings']
    };

    const options = configOptions[agentName] || ['General Settings', 'Performance Tuning', 'Integration Options'];

    showModal('configModal');

    const modal = document.getElementById('configModal');
    if (modal) {
        modal.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h3>Configure ${agentName.charAt(0).toUpperCase() + agentName.slice(1)} Agent</h3>
                    <button class="modal-close" onclick="closeModal('configModal')">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                <div class="modal-body">
                    <div style="display: grid; gap: 16px;">
                        ${options.map(option => `
                            <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px; background: var(--bg-secondary); border-radius: 8px;">
                                <span style="color: var(--text-primary);">${option}</span>
                                <button class="btn-small" onclick="configureOption('${option}')">Configure</button>
                            </div>
                        `).join('')}
                    </div>
                </div>
                <div class="modal-footer">
                    <button class="btn-secondary" onclick="closeModal('configModal')">Cancel</button>
                    <button class="btn-primary" onclick="saveConfiguration()">Save Configuration</button>
                </div>
            </div>
        `;
    }
}

function configureOption(option) {
    showNotification(`Configuring ${option}...`, 'info');
    setTimeout(() => {
        showNotification(`${option} configured successfully!`, 'success');
    }, 2000);
}

function saveConfiguration() {
    showNotification('Configuration saved successfully!', 'success');
    closeModal('configModal');
}

function startAgent(agentName) {
    showNotification(`Starting agent: ${agentName}`, 'info');
    setTimeout(() => {
        showNotification(`Agent ${agentName} started successfully!`, 'success');
    }, 1500);
}

function stopAgent(agentName) {
    showNotification(`Stopping agent: ${agentName}`, 'info');
    setTimeout(() => {
        showNotification(`Agent ${agentName} stopped successfully!`, 'success');
    }, 1000);
}

// Workflow Functions
function changeScenario() {
    const selector = document.getElementById('scenario-selector');
    if (selector) {
        currentScenario = selector.value;
        resetWorkflow();
        updateWorkflowSteps();
    }
}

function startWorkflow() {
    if (workflowRunning) return;

    workflowRunning = true;
    currentStep = 0;
    clearOutput();
    updateWorkflowSteps();

    showNotification('Workflow started!', 'info');
    executeWorkflowStep();
}

function executeWorkflowStep() {
    if (!workflowRunning || currentStep >= scenarios[currentScenario].steps.length) {
        completeWorkflow();
        return;
    }

    const step = scenarios[currentScenario].steps[currentStep];
    const stepElement = document.querySelector(`[data-step="${currentStep}"]`);

    if (stepElement) {
        stepElement.classList.add('active');
    }

    // Add step outputs
    step.outputs.forEach((output, index) => {
        setTimeout(() => {
            addOutputMessage(output);
        }, index * 800);
    });

    // Move to next step after delay
    setTimeout(() => {
        if (stepElement) {
            stepElement.classList.remove('active');
            stepElement.classList.add('completed');
        }
        currentStep++;
        executeWorkflowStep();
    }, step.outputs.length * 800 + 1000);
}

function completeWorkflow() {
    workflowRunning = false;
    showNotification('Workflow completed successfully!', 'success');
}

function pauseWorkflow() {
    if (workflowRunning) {
        workflowRunning = false;
        showNotification('Workflow paused', 'warning');
    }
}

function resetWorkflow() {
    workflowRunning = false;
    currentStep = 0;
    clearOutput();
    updateWorkflowSteps();
    addOutputMessage('Workflow ready. Select a scenario and click Start to begin.');
}

function updateWorkflowSteps() {
    const steps = document.querySelectorAll('.step');
    steps.forEach((step, index) => {
        step.classList.remove('active', 'completed');

        const stepContent = step.querySelector('.step-content');
        if (stepContent && scenarios[currentScenario].steps[index]) {
            const scenarioStep = scenarios[currentScenario].steps[index];
            stepContent.querySelector('h4').textContent = scenarioStep.title;
            stepContent.querySelector('p').textContent = scenarioStep.description;
        }
    });
}

// Output Management
function addOutputMessage(message) {
    const outputContainer = document.getElementById('workflow-output');
    if (!outputContainer) return;

    const messageElement = document.createElement('div');
    messageElement.className = 'output-message';

    const timestamp = new Date().toLocaleTimeString();
    messageElement.innerHTML = `
        <span class="timestamp">[${timestamp}]</span>
        <span class="message">${message}</span>
    `;

    outputContainer.appendChild(messageElement);
    outputContainer.scrollTop = outputContainer.scrollHeight;
}

function clearOutput() {
    const outputContainer = document.getElementById('workflow-output');
    if (outputContainer) {
        outputContainer.innerHTML = '';
    }
}

function exportLog() {
    const outputContainer = document.getElementById('workflow-output');
    if (!outputContainer) return;

    const messages = Array.from(outputContainer.querySelectorAll('.output-message'))
        .map(msg => msg.textContent)
        .join('\n');

    const blob = new Blob([messages], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `workflow-log-${new Date().toISOString().slice(0, 19)}.txt`;
    a.click();
    URL.revokeObjectURL(url);

    showNotification('Workflow log exported successfully!', 'success');
}

// Quick Actions
function createWorkflow() {
    showNotification('Create workflow functionality coming soon!', 'info');
}

function runTest() {
    showNotification('Running system tests...', 'info');
    setTimeout(() => {
        showNotification('All tests passed successfully!', 'success');
    }, 3000);
}

function exportData() {
    showNotification('Exporting data...', 'info');
    setTimeout(() => {
        showNotification('Data exported successfully!', 'success');
    }, 2000);
}

// Modal Management
function showModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
    }
}

// Notification System
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-icon">
            <i class="${getNotificationIcon(type)}"></i>
        </div>
        <div class="notification-content">
            <div class="notification-message">${message}</div>
        </div>
        <button class="notification-close" onclick="this.parentElement.remove()">
            <i class="fas fa-times"></i>
        </button>
    `;

    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        display: flex;
        align-items: center;
        gap: 12px;
        z-index: 10000;
        max-width: 400px;
        animation: slideInRight 0.3s ease-out;
    `;

    document.body.appendChild(notification);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.remove();
        }
    }, 5000);
}

function getNotificationIcon(type) {
    const icons = {
        'success': 'fas fa-check-circle',
        'error': 'fas fa-exclamation-circle',
        'warning': 'fas fa-exclamation-triangle',
        'info': 'fas fa-info-circle'
    };
    return icons[type] || icons.info;
}

// Real-time Updates
function updateStats() {
    // Simulate real-time stat updates
    const statValues = document.querySelectorAll('.stat-value');
    statValues.forEach(stat => {
        const currentValue = parseInt(stat.textContent.replace(/[^\d]/g, ''));
        const newValue = currentValue + Math.floor(Math.random() * 5);
        stat.textContent = stat.textContent.replace(/\d+/, newValue);
    });
}

function startRealTimeUpdates() {
    // Update stats every 30 seconds
    setInterval(updateStats, 30000);

    // Add random activity feed items
    setInterval(addRandomActivity, 45000);
}

function addRandomActivity() {
    const activities = [
        {
            icon: 'success',
            title: 'Analytics Agent completed report',
            desc: 'Generated quarterly performance insights for 2,847 students',
            time: '1 minute ago'
        },
        {
            icon: 'info',
            title: 'Compliance Monitor check',
            desc: 'Completed regulatory compliance audit for Q3',
            time: '3 minutes ago'
        },
        {
            icon: 'warning',
            title: 'System maintenance alert',
            desc: 'Scheduled maintenance window starting in 30 minutes',
            time: '5 minutes ago'
        }
    ];

    const randomActivity = activities[Math.floor(Math.random() * activities.length)];
    addActivityFeedItem(randomActivity);
}

function addActivityFeedItem(activity) {
    const feedContainer = document.querySelector('.feed-container');
    if (!feedContainer) return;

    const feedItem = document.createElement('div');
    feedItem.className = 'feed-item';
    feedItem.innerHTML = `
        <div class="feed-icon ${activity.icon}">
            <i class="fas ${activity.icon === 'success' ? 'fa-check' : activity.icon === 'info' ? 'fa-info' : 'fa-exclamation'}"></i>
        </div>
        <div class="feed-content">
            <div class="feed-title">${activity.title}</div>
            <div class="feed-desc">${activity.desc}</div>
            <div class="feed-time">${activity.time}</div>
        </div>
    `;

    feedContainer.insertBefore(feedItem, feedContainer.firstChild);

    // Remove old items if too many
    const items = feedContainer.querySelectorAll('.feed-item');
    if (items.length > 5) {
        items[items.length - 1].remove();
    }
}

// Add CSS for notifications
const notificationStyles = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    .notification-close {
        background: none;
        border: none;
        color: #94a3b8;
        cursor: pointer;
        padding: 4px;
        border-radius: 4px;
        transition: all 0.2s;
    }

    .notification-close:hover {
        background: #f1f5f9;
        color: #64748b;
    }

    .notification-icon {
        color: #10b981;
    }

    .notification-error .notification-icon {
        color: #ef4444;
    }

    .notification-warning .notification-icon {
        color: #f59e0b;
    }

    .notification-info .notification-icon {
        color: #3b82f6;
    }
`;

// Inject notification styles
const styleSheet = document.createElement('style');
styleSheet.textContent = notificationStyles;
document.head.appendChild(styleSheet);

// Framework Tab Management
function switchTab(tabName) {
    // Remove active class from all tabs and content
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => btn.classList.remove('active'));
    tabContents.forEach(content => content.classList.remove('active'));

    // Add active class to selected tab and content
    const activeTab = document.querySelector(`[onclick="switchTab('${tabName}')"]`);
    const activeContent = document.getElementById(`${tabName}-tab`);

    if (activeTab) activeTab.classList.add('active');
    if (activeContent) activeContent.classList.add('active');
}

// Showcase Management
function viewShowcase(showcaseType) {
    const showcases = {
        'education': {
            title: 'Education Platform Demo',
            description: 'See how CraftedAi powers personalized learning experiences',
            features: ['Curriculum Generation', 'Student Progress Tracking', 'Adaptive Learning', 'Performance Analytics']
        },
        'enterprise': {
            title: 'Enterprise Automation Demo',
            description: 'Streamline business processes with intelligent automation',
            features: ['Process Automation', 'Decision Making', 'Workflow Optimization', 'Performance Monitoring']
        },
        'hr': {
            title: 'Human Resources Demo',
            description: 'AI-powered recruitment and employee management',
            features: ['Recruitment Automation', 'Employee Onboarding', 'Performance Reviews', 'Talent Development']
        },
        'onboarding': {
            title: 'Client Onboarding Demo',
            description: 'Streamlined client acquisition and onboarding processes',
            features: ['Document Processing', 'Identity Verification', 'Welcome Experience', 'Progress Tracking']
        },
        'healthcare': {
            title: 'Healthcare Demo',
            description: 'Patient relationship management and health monitoring',
            features: ['Patient Management', 'Appointment Scheduling', 'Health Monitoring', 'Clinical Support']
        },
        'finance': {
            title: 'Financial Analytics Demo',
            description: 'Advanced financial modeling and risk assessment',
            features: ['Risk Assessment', 'Market Analysis', 'Portfolio Management', 'Compliance Monitoring']
        }
    };

    const showcase = showcases[showcaseType];
    if (!showcase) return;

    showModal('showcaseModal');

    // Update modal content
    const modal = document.getElementById('showcaseModal');
    if (modal) {
        modal.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h3>${showcase.title}</h3>
                    <button class="modal-close" onclick="closeModal('showcaseModal')">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                <div class="modal-body">
                    <p style="margin-bottom: 20px; color: var(--text-secondary);">${showcase.description}</p>
                    <div style="display: grid; gap: 12px;">
                        ${showcase.features.map(feature => `
                            <div style="display: flex; align-items: center; gap: 12px; padding: 12px; background: var(--bg-secondary); border-radius: 8px;">
                                <i class="fas fa-check" style="color: var(--primary-color);"></i>
                                <span style="color: var(--text-primary);">${feature}</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
                <div class="modal-footer">
                    <button class="btn-secondary" onclick="closeModal('showcaseModal')">Close</button>
                    <button class="btn-primary" onclick="requestDemo('${showcaseType}')">Request Demo</button>
                </div>
            </div>
        `;
    }
}

// Demo Request Management
function submitDemoRequest(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    // Validate required fields
    if (!data.name || !data.email || !data.company || !data.industry) {
        showNotification('Please fill in all required fields.', 'error');
        return;
    }

    // Simulate form submission
    showNotification('Demo request submitted successfully! We\'ll contact you within 24 hours.', 'success');

    // Reset form
    event.target.reset();

    // Close modal if open
    closeModal('demoModal');
}

function requestDemo(showcaseType = null) {
    if (showcaseType) {
        // Pre-fill industry based on showcase type
        const industryMap = {
            'education': 'education',
            'healthcare': 'healthcare',
            'finance': 'finance',
            'hr': 'hr',
            'enterprise': 'enterprise',
            'onboarding': 'enterprise'
        };

        const industry = industryMap[showcaseType];
        if (industry) {
            const industrySelect = document.getElementById('industry');
            if (industrySelect) {
                industrySelect.value = industry;
            }
        }
    }

    // Scroll to demo section
    const demoSection = document.getElementById('demo');
    if (demoSection) {
        demoSection.scrollIntoView({ behavior: 'smooth' });
    }
}

// Enhanced Navigation
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Platform Demo Functions
function startPlatformDemo() {
    showNotification('Starting platform demo...', 'info');

    // Simulate platform loading
    setTimeout(() => {
        showNotification('Platform demo loaded successfully!', 'success');

        // Add demo activity
        addActivityFeedItem({
            icon: 'success',
            title: 'Platform Demo Started',
            desc: 'Interactive demo session initiated for white-label framework',
            time: 'Just now'
        });
    }, 2000);
}

// Initialize enhanced functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize existing functionality
    initializeApp();

    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Initialize framework tabs
    const firstTab = document.querySelector('.tab-btn');
    if (firstTab) {
        firstTab.classList.add('active');
        const firstTabContent = document.querySelector('.tab-content');
        if (firstTabContent) {
            firstTabContent.classList.add('active');
        }
    }

    // Add form validation
    const demoForm = document.getElementById('demoForm');
    if (demoForm) {
        demoForm.addEventListener('submit', submitDemoRequest);
    }

    // Initialize platform demo
    const startDemoBtn = document.querySelector('[onclick="startDemo()"]');
    if (startDemoBtn) {
        startDemoBtn.addEventListener('click', startPlatformDemo);
    }
});

function selectDemoCategory(category) {
    currentDemoCategory = category;

    // Update active category button
    document.querySelectorAll('.demo-category').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[onclick="selectDemoCategory('${category}')"]`).classList.add('active');

    // Update demo interface
    const config = demoConfigs[category];
    document.getElementById('demo-title').textContent = config.title;
    document.getElementById('demo-description').textContent = config.description;
    document.getElementById('demo-input').placeholder = config.placeholder;

    // Reset demo state
    resetDemo();
}

function startLiveDemo() {
    if (demoRunning) return;

    demoRunning = true;
    demoStartTime = Date.now();

    // Update UI
    document.getElementById('agent-status').textContent = 'Processing';
    document.querySelector('[onclick="startLiveDemo()"]').innerHTML = '<i class="fas fa-pause"></i> Pause Demo';
    document.querySelector('[onclick="startLiveDemo()"]').onclick = pauseLiveDemo;

    // Clear output
    const outputArea = document.getElementById('demo-output');
    outputArea.innerHTML = '';

    // Start flow animation
    animateFlow();

    // Simulate processing
    setTimeout(() => {
        addOutputMessage('system', 'Demo started. Enter your request in the input field to see the agent in action.');
    }, 500);
}

function pauseLiveDemo() {
    demoRunning = false;

    // Update UI
    document.getElementById('agent-status').textContent = 'Paused';
    document.querySelector('[onclick="pauseLiveDemo()"]').innerHTML = '<i class="fas fa-play"></i> Resume Demo';
    document.querySelector('[onclick="pauseLiveDemo()"]').onclick = startLiveDemo;

    // Stop flow animation
    stopFlowAnimation();
}

function resetDemo() {
    demoRunning = false;
    demoStartTime = 0;

    // Reset UI
    document.getElementById('agent-status').textContent = 'Ready';
    document.getElementById('response-time').textContent = '0.0s';
    document.getElementById('success-rate').textContent = '100%';

    const startBtn = document.querySelector('[onclick="startLiveDemo()"]');
    if (startBtn) {
        startBtn.innerHTML = '<i class="fas fa-play"></i> Start Demo';
        startBtn.onclick = startLiveDemo;
    }

    // Clear output
    const outputArea = document.getElementById('demo-output');
    outputArea.innerHTML = `
        <div class="output-placeholder">
            <i class="fas fa-comments"></i>
            <p>Start the demo to see the agent in action</p>
        </div>
    `;

    // Reset flow steps
    resetFlowSteps();

    // Clear input
    document.getElementById('demo-input').value = '';
}

function submitDemoInput() {
    if (!demoRunning) {
        showNotification('Please start the demo first', 'warning');
        return;
    }

    const input = document.getElementById('demo-input').value.trim();
    if (!input) {
        showNotification('Please enter a request', 'warning');
        return;
    }

    // Add user message
    addOutputMessage('user', input);

    // Clear input
    document.getElementById('demo-input').value = '';

    // Simulate agent processing
    simulateAgentResponse(input);
}

function simulateAgentResponse(userInput) {
    const config = demoConfigs[currentDemoCategory];
    const responses = config.responses;

    // Update metrics
    document.getElementById('agent-status').textContent = 'Processing';

    // Animate flow steps
    animateFlowSteps(responses.length);

    // Simulate progressive responses
    responses.forEach((response, index) => {
        setTimeout(() => {
            addOutputMessage('agent', response);

            // Update response time
            const responseTime = ((Date.now() - demoStartTime) / 1000).toFixed(1);
            document.getElementById('response-time').textContent = responseTime + 's';

            // Complete flow on last response
            if (index === responses.length - 1) {
                document.getElementById('agent-status').textContent = 'Completed';
                completeFlowAnimation();
            }
        }, (index + 1) * 1500);
    });
}

function addOutputMessage(type, content) {
    const outputArea = document.getElementById('demo-output');

    // Remove placeholder if present
    const placeholder = outputArea.querySelector('.output-placeholder');
    if (placeholder) {
        placeholder.remove();
    }

    const message = document.createElement('div');
    message.className = `output-message ${type}`;

    const timestamp = new Date().toLocaleTimeString();
    const typeLabel = type === 'user' ? 'You' : type === 'agent' ? 'AI Agent' : 'System';

    message.innerHTML = `
        <div class="message-header">
            <span>${typeLabel}</span>
            <span>${timestamp}</span>
        </div>
        <div class="message-content">${content.replace(/\n/g, '<br>')}</div>
    `;

    outputArea.appendChild(message);
    outputArea.scrollTop = outputArea.scrollHeight;
}

function animateFlow() {
    const flowSteps = document.querySelectorAll('.flow-step');
    const flowArrows = document.querySelectorAll('.flow-arrow');

    flowSteps.forEach((step, index) => {
        setTimeout(() => {
            step.classList.add('active');
            if (flowArrows[index]) {
                flowArrows[index].classList.add('active');
            }
        }, index * 500);
    });
}

function animateFlowSteps(totalSteps) {
    const flowSteps = document.querySelectorAll('.flow-step');
    const flowArrows = document.querySelectorAll('.flow-arrow');

    // Reset all steps
    flowSteps.forEach(step => {
        step.classList.remove('active', 'completed', 'processing');
    });
    flowArrows.forEach(arrow => arrow.classList.remove('active'));

    // Animate through steps
    flowSteps.forEach((step, index) => {
        setTimeout(() => {
            step.classList.add('active');
            if (flowArrows[index]) {
                flowArrows[index].classList.add('active');
            }

            // Add processing animation
            setTimeout(() => {
                step.classList.remove('active');
                step.classList.add('processing');
            }, 1000);

            // Complete step
            setTimeout(() => {
                step.classList.remove('processing');
                step.classList.add('completed');
            }, 2000);
        }, index * 3000);
    });
}

function completeFlowAnimation() {
    const flowSteps = document.querySelectorAll('.flow-step');
    const flowArrows = document.querySelectorAll('.flow-arrow');

    flowSteps.forEach(step => {
        step.classList.remove('active', 'processing');
        step.classList.add('completed');
    });

    flowArrows.forEach(arrow => {
        arrow.classList.remove('active');
    });
}

function stopFlowAnimation() {
    const flowSteps = document.querySelectorAll('.flow-step');
    flowSteps.forEach(step => {
        step.classList.remove('active', 'processing');
    });
}

function resetFlowSteps() {
    const flowSteps = document.querySelectorAll('.flow-step');
    const flowArrows = document.querySelectorAll('.flow-arrow');

    flowSteps.forEach(step => {
        step.classList.remove('active', 'completed', 'processing');
    });

    flowArrows.forEach(arrow => {
        arrow.classList.remove('active');
    });
}

// Mobile Menu Functions
function toggleMobileMenu() {
    const nav = document.getElementById('mobile-nav');
    const toggle = document.querySelector('.mobile-menu-toggle i');

    mobileMenuOpen = !mobileMenuOpen;

    if (mobileMenuOpen) {
        nav.classList.add('active');
        toggle.classList.remove('fa-bars');
        toggle.classList.add('fa-times');
    } else {
        nav.classList.remove('active');
        toggle.classList.remove('fa-times');
        toggle.classList.add('fa-bars');
    }
}

// Close mobile menu when clicking on a nav link
function closeMobileMenu() {
    const nav = document.getElementById('mobile-nav');
    const toggle = document.querySelector('.mobile-menu-toggle i');

    mobileMenuOpen = false;
    nav.classList.remove('active');
    toggle.classList.remove('fa-times');
    toggle.classList.add('fa-bars');
}

// Close mobile menu when clicking outside
document.addEventListener('click', function(event) {
    const nav = document.getElementById('mobile-nav');
    const toggle = document.querySelector('.mobile-menu-toggle');

    if (mobileMenuOpen && !nav.contains(event.target) && !toggle.contains(event.target)) {
        closeMobileMenu();
    }
});

// Close mobile menu when clicking on nav links
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });
});
