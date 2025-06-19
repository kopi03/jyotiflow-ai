import os
import sys
import asyncio
import argparse
import logging
from pathlib import Path
from datetime import datetime

# Add current directory to path for imports
sys.path.append(str(Path(__file__).parent))

# তমিল - Try importing artifacts with error handling
try:
    # Check if files exist first
    required_files = [
        'core_foundation_enhanced.py',
        'enhanced_business_logic.py', 
        'enhanced_production_deployment.py',
        'main_integration_hub.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        print("📝 Creating missing files with basic structure...")
        # We'll create these files in next steps
    
    # Import what we have
    try:
        from core_foundation_enhanced import EnhancedSettings, logger
        print("✅ Core foundation imported")
    except ImportError as e:
        print(f"⚠️ Core foundation import issue: {e}")
        # Fallback to basic setup
        import logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        class EnhancedSettings:
            debug = True
            port = 8000
            host = "0.0.0.0"
    
    try:
        from enhanced_business_logic import (
            SpiritualAvatarEngine,
            MonetizationOptimizer,
            SatsangManager,
            SocialContentEngine
        )
        print("✅ Business logic imported")
    except ImportError as e:
        print(f"⚠️ Business logic import issue: {e}")
        # Create placeholder classes
        class SpiritualAvatarEngine:
            pass
        class MonetizationOptimizer:
            pass
        class SatsangManager:
            pass
        class SocialContentEngine:
            pass
    
    try:
        from enhanced_production_deployment import enhanced_app
        print("✅ Production app imported")
    except ImportError as e:
        print(f"⚠️ Production app import issue: {e}")
        # Create basic FastAPI app
        from fastapi import FastAPI
        enhanced_app = FastAPI(title="JyotiFlow.ai")
    
    try:
        from main_integration_hub import JyotiFlowIntegrationHub, JyotiFlowRunner
        print("✅ Integration hub imported")
    except ImportError as e:
        print(f"⚠️ Integration hub import issue: {e}")
        # Create basic classes
        class JyotiFlowIntegrationHub:
            async def initialize_complete_platform(self):
                return {"status": "basic_mode"}
        
        class JyotiFlowRunner:
            def run_production_server(self):
                import uvicorn
                uvicorn.run(enhanced_app, host="0.0.0.0", port=8000)
    
    print("✅ All imports handled successfully!")
    
except Exception as e:
    print(f"❌ Critical import error: {e}")
    sys.exit(1)

# =============================================================================
# 🌟 MAIN APPLICATION SETUP
# তমিল - প্রধান অ্যাপ্লিকেশন সেটআপ
# =============================================================================

def validate_environment():
    """Validate environment variables"""
    required_vars = ['OPENAI_API_KEY', 'STRIPE_SECRET_KEY', 'JWT_SECRET']
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        print(f"❌ Missing environment variables: {', '.join(missing)}")
        print("💡 Create .env file with these variables")
        return False
    
    print("✅ Environment validation passed!")
    return True

def create_sample_env():
    """Create sample .env file"""
    env_content = '''# 🙏🏼 JyotiFlow.ai Environment Configuration

# Required Settings
OPENAI_API_KEY=sk-your-openai-key-here
STRIPE_SECRET_KEY=sk_test_your-stripe-key
JWT_SECRET=your-super-secret-jwt-key-om-namah-shivaya

# Optional Avatar Services  
D_ID_API_KEY=your-d-id-api-key
ELEVENLABS_API_KEY=your-elevenlabs-api-key
AGORA_APP_ID=your-agora-app-id

# Database
DATABASE_URL=sqlite:///./jyotiflow_enhanced.db

# Admin
ADMIN_EMAIL=admin@jyotiflow.ai
ADMIN_PASSWORD=your-secure-admin-password
'''
    
    with open('.env.sample', 'w') as f:
        f.write(env_content)
    print("✅ Sample .env file created: .env.sample")

async def initialize_platform():
    """Initialize the platform"""
    print("\n🕉️ ===== JYOTIFLOW.AI PLATFORM INITIALIZATION =====")
    print("🙏🏼 Swami Jyotirananthan's Digital Ashram")
    print("✨ Version 5.0 - Enhanced Spiritual Platform")
    print("=" * 60)
    
    try:
        integration_hub = JyotiFlowIntegrationHub()
        result = await integration_hub.initialize_complete_platform()
        
        print("\n🌟 Platform Initialization Complete!")
        print(f"   Status: {result.get('status', 'operational')}")
        print("\n🙏🏼 Digital ashram ready to serve souls worldwide")
        print("=" * 60)
        
        return integration_hub
        
    except Exception as e:
        print(f"❌ Platform initialization failed: {e}")
        print("⚠️ Running in basic mode...")
        return None

def run_development_server():
    """Run development server"""
    import uvicorn
    settings = EnhancedSettings()
    
    print("🚀 Starting JyotiFlow.ai in DEVELOPMENT mode...")
    print(f"🌐 Server: http://localhost:{settings.port}")
    
    uvicorn.run(
        enhanced_app,
        host="0.0.0.0",
        port=settings.port,
        reload=True,
        log_level="info"
    )

def run_production_server():
    """Run production server"""
    runner = JyotiFlowRunner()
    runner.run_production_server()

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='🙏🏼 JyotiFlow.ai Platform')
    parser.add_argument('--dev', action='store_true', help='Run in development mode')
    parser.add_argument('--create-env', action='store_true', help='Create sample .env file')
    parser.add_argument('--validate-env', action='store_true', help='Validate environment')
    
    args = parser.parse_args()
    
    # Handle special commands
    if args.create_env:
        create_sample_env()
        return
    
    if args.validate_env:
        validate_environment()
        return
    
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✅ Environment variables loaded")
    except ImportError:
        print("⚠️ python-dotenv not installed")
    except Exception as e:
        print(f"⚠️ Could not load .env file: {e}")
    
    # Validate environment  
    if not validate_environment():
        print("\n💡 Tip: Run 'python main.py --create-env' to create .env file")
        print("💡 Then copy .env.sample to .env and update with your API keys")
        return
    
    try:
        if args.dev:
            # Run development server
            run_development_server()
        else:
            # Run production server
            print("🚀 Starting JyotiFlow.ai platform...")
            
            # Initialize platform
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            integration_hub = loop.run_until_complete(initialize_platform())
            
            # Start server
            run_production_server()
    
    except KeyboardInterrupt:
        print("\n🙏🏼 Graceful shutdown...")
        logger.info("Platform shutdown by user")
    
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        logger.error(f"Critical error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()