# She Safe - AI Support Against Gender-Based Violence

## Overview

She Safe is a confidential, AI-powered chatbot application designed to provide support, resources, and guidance to survivors of Gender-Based Violence (GBV). The application serves as a safe digital space where users can access empathetic AI assistance, complete comprehensive assessments, and receive immediate access to emergency resources and mental health support. The system is specifically designed with cultural sensitivity for users in Ethiopia and Cameroon, prioritizing privacy and user safety above all else.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
The application uses Streamlit as its primary web framework, providing a Python-based solution for rapid deployment and user interface development. The frontend implements a centered layout with custom CSS styling to create a calming, safe environment for users. Key UI components include a panic button for emergency exits, emergency contact sections, and support message displays with color-coded styling for different types of content.

### AI Integration Layer
The core AI functionality is powered by OpenAI's GPT-4o model, accessed through the OpenAI Python client. The system implements a specialized system prompt that trains the AI to provide GBV-specific guidance, ensuring responses are empathetic, culturally sensitive, and focused on user safety. The AI is designed to prioritize emergency situations, provide actionable guidance, and maintain strict confidentiality.

### Assessment System
The application features a comprehensive 8-category questionnaire system covering personal safety assessment, GBV type identification, support resource evaluation, mental health screening, and digital safety assessment. This modular approach allows for targeted support based on user-specific needs and circumstances.

### Safety and Privacy Design
The architecture prioritizes user privacy with no permanent data storage, ensuring conversations remain confidential. The system includes emergency features such as panic buttons, quick-exit functionality, and immediate access to local emergency contacts for Ethiopia and Cameroon.

### Content Management
The system provides structured access to safety resources, mental health support tools (including breathing exercises and coping strategies), educational materials about GBV types and legal rights, and culturally appropriate guidance for the target regions.

## External Dependencies

### AI Services
- **OpenAI API**: GPT-4o model for conversational AI responses and GBV-specific guidance
- **Python OpenAI Client**: Official OpenAI Python library for API integration

### Web Framework
- **Streamlit**: Primary web application framework for user interface and interaction handling

### Environment Management
- **python-dotenv**: Environment variable management for secure API key storage and configuration

### Deployment Infrastructure
- **Docker**: Containerization support for consistent deployment across environments
- The application is designed to be deployment-ready with configurable server settings

### Regional Support Services
The application integrates knowledge of emergency services and support organizations in Ethiopia and Cameroon, including police, ambulance services, and specialized GBV hotlines, though these are informational rather than direct API integrations.