HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AEROBRAIN AI | Don Smith Spare Parts Concierge</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --neon-cyan: #00f0ff;
            --neon-orange: #ff6b35;
            --neon-green: #00ff88;
            --neon-purple: #b829ff;
            --dark-bg: #0a0e17;
            --panel-bg: rgba(16, 24, 39, 0.85);
            --glass-border: rgba(0, 240, 255, 0.15);
            --text-primary: #e2e8f0;
            --text-secondary: #94a3b8;
            --grid-line: rgba(0, 240, 255, 0.05);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Rajdhani', 'Inter', sans-serif;
            background: var(--dark-bg);
            color: var(--text-primary);
            overflow-x: hidden;
            min-height: 100vh;
        }

        /* Boot Sequence Overlay */
        #bootOverlay {
            position: fixed;
            inset: 0;
            background: var(--dark-bg);
            z-index: 9999;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            transition: opacity 0.8s ease;
        }

        /* Animated Background Grid */
        .bg-grid {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(var(--grid-line) 1px, transparent 1px),
                linear-gradient(90deg, var(--grid-line) 1px, transparent 1px);
            background-size: 50px 50px;
            z-index: -2;
            pointer-events: none;
        }

        .bg-particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            pointer-events: none;
        }

        .particle {
            position: absolute;
            width: 2px;
            height: 2px;
            background: var(--neon-cyan);
            border-radius: 50%;
            opacity: 0.6;
            animation: float 15s infinite ease-in-out;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0) translateX(0); opacity: 0.3; }
            25% { transform: translateY(-100px) translateX(50px); opacity: 0.8; }
            50% { transform: translateY(-50px) translateX(-30px); opacity: 0.5; }
            75% { transform: translateY(-150px) translateX(20px); opacity: 0.9; }
        }

        /* Header */
        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 70px;
            background: rgba(10, 14, 23, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--glass-border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 40px;
            z-index: 1000;
        }

        .logo-section {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .logo-icon {
            width: 45px;
            height: 45px;
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.3);
            animation: pulse-glow 3s infinite;
        }

        @keyframes pulse-glow {
            0%, 100% { box-shadow: 0 0 20px rgba(0, 240, 255, 0.3); }
            50% { box-shadow: 0 0 40px rgba(0, 240, 255, 0.6); }
        }

        .logo-text {
            font-family: 'Orbitron', sans-serif;
            font-size: 22px;
            font-weight: 700;
            letter-spacing: 2px;
            background: linear-gradient(90deg, var(--neon-cyan), var(--neon-orange));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .logo-sub {
            font-size: 11px;
            color: var(--text-secondary);
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-top: -5px;
        }

        .nav-buttons {
            display: flex;
            gap: 12px;
        }

        .nav-btn {
            padding: 10px 24px;
            border: 1px solid var(--glass-border);
            background: rgba(0, 240, 255, 0.05);
            color: var(--neon-cyan);
            font-family: 'Rajdhani', sans-serif;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .nav-btn:hover, .nav-btn.active {
            background: rgba(0, 240, 255, 0.15);
            border-color: var(--neon-cyan);
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
            transform: translateY(-2px);
        }

        .nav-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0, 240, 255, 0.2), transparent);
            transition: left 0.5s;
        }

        .nav-btn:hover::before {
            left: 100%;
        }

        .status-bar {
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .status-item {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 12px;
            color: var(--text-secondary);
        }

        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--neon-green);
            box-shadow: 0 0 10px var(--neon-green);
            animation: blink 2s infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
        }

        /* Main Container */
        .main-container {
            margin-top: 70px;
            padding: 30px 40px;
            display: grid;
            grid-template-columns: 1fr 400px;
            gap: 25px;
            max-width: 1600px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Glass Panel Base */
        .glass-panel {
            background: var(--panel-bg);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 24px;
            backdrop-filter: blur(20px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.05);
            position: relative;
            overflow: hidden;
        }

        .glass-panel::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--neon-cyan), transparent);
            opacity: 0.5;
        }

        .panel-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .panel-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 16px;
            font-weight: 600;
            color: var(--neon-cyan);
            letter-spacing: 2px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .panel-title i {
            font-size: 14px;
            color: var(--neon-orange);
        }

        /* Hero Dashboard */
        .hero-section {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr;
            gap: 20px;
            margin-bottom: 10px;
        }

        .hero-main {
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 40px;
        }

        .hero-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 36px;
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #fff 0%, var(--neon-cyan) 50%, var(--neon-orange) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-subtitle {
            font-size: 16px;
            color: var(--text-secondary);
            margin-bottom: 30px;
            line-height: 1.6;
        }

        .hero-buttons {
            display: flex;
            gap: 15px;
        }

        .btn-primary {
            padding: 14px 32px;
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
            border: none;
            color: #000;
            font-family: 'Orbitron', sans-serif;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            cursor: pointer;
            border-radius: 10px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            box-shadow: 0 0 30px rgba(0, 240, 255, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 0 50px rgba(0, 240, 255, 0.5);
        }

        .btn-secondary {
            padding: 14px 32px;
            background: transparent;
            border: 1px solid var(--neon-orange);
            color: var(--neon-orange);
            font-family: 'Orbitron', sans-serif;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            cursor: pointer;
            border-radius: 10px;
            transition: all 0.3s ease;
        }

        .btn-secondary:hover {
            background: rgba(255, 107, 53, 0.1);
            box-shadow: 0 0 30px rgba(255, 107, 53, 0.3);
            transform: translateY(-3px);
        }

        .stat-card {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 30px 20px;
        }

        .stat-value {
            font-family: 'Orbitron', sans-serif;
            font-size: 36px;
            font-weight: 700;
            color: var(--neon-cyan);
            text-shadow: 0 0 20px rgba(0, 240, 255, 0.5);
        }

        .stat-label {
            font-size: 13px;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-top: 8px;
        }

        .stat-change {
            font-size: 12px;
            color: var(--neon-green);
            margin-top: 5px;
            font-weight: 600;
        }

        /* AI Chat Interface */
        .chat-container {
            height: 600px;
            display: flex;
            flex-direction: column;
        }

        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 10px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .chat-messages::-webkit-scrollbar {
            width: 6px;
        }

        .chat-messages::-webkit-scrollbar-track {
            background: rgba(0, 240, 255, 0.05);
            border-radius: 3px;
        }

        .chat-messages::-webkit-scrollbar-thumb {
            background: var(--neon-cyan);
            border-radius: 3px;
        }

        .message {
            display: flex;
            gap: 12px;
            max-width: 90%;
            animation: messageSlide 0.4s ease;
        }

        @keyframes messageSlide {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .message.user {
            align-self: flex-end;
            flex-direction: row-reverse;
        }

        .message.ai .message-avatar {
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
        }

        .message.user .message-avatar {
            background: linear-gradient(135deg, var(--neon-orange), #ff3366);
        }

        .message-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            flex-shrink: 0;
            color: #000;
            font-weight: bold;
        }

        .message-content {
            background: rgba(0, 240, 255, 0.08);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-radius: 16px;
            padding: 14px 18px;
            font-size: 14px;
            line-height: 1.6;
            color: var(--text-primary);
        }

        .message.user .message-content {
            background: rgba(255, 107, 53, 0.1);
            border-color: rgba(255, 107, 53, 0.3);
        }

        .message-time {
            font-size: 10px;
            color: var(--text-secondary);
            margin-top: 6px;
            text-align: right;
        }

        .typing-indicator {
            display: flex;
            gap: 4px;
            padding: 14px 18px;
        }

        .typing-dot {
            width: 8px;
            height: 8px;
            background: var(--neon-cyan);
            border-radius: 50%;
            animation: typingBounce 1.4s infinite ease-in-out;
        }

        .typing-dot:nth-child(2) { animation-delay: 0.2s; }
        .typing-dot:nth-child(3) { animation-delay: 0.4s; }

        @keyframes typingBounce {
            0%, 80%, 100% { transform: scale(0); opacity: 0.5; }
            40% { transform: scale(1); opacity: 1; }
        }

        .chat-input-area {
            display: flex;
            gap: 10px;
            padding-top: 15px;
            border-top: 1px solid var(--glass-border);
            margin-top: 10px;
        }

        .chat-input {
            flex: 1;
            background: rgba(0, 240, 255, 0.05);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 14px 18px;
            color: var(--text-primary);
            font-family: 'Rajdhani', sans-serif;
            font-size: 15px;
            outline: none;
            transition: all 0.3s ease;
        }

        .chat-input:focus {
            border-color: var(--neon-cyan);
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.1);
        }

        .chat-input::placeholder {
            color: var(--text-secondary);
        }

        .chat-actions {
            display: flex;
            gap: 8px;
        }

        .chat-action-btn {
            width: 48px;
            height: 48px;
            border: 1px solid var(--glass-border);
            background: rgba(0, 240, 255, 0.05);
            color: var(--neon-cyan);
            border-radius: 12px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            font-size: 16px;
        }

        .chat-action-btn:hover {
            background: rgba(0, 240, 255, 0.15);
            border-color: var(--neon-cyan);
            transform: scale(1.05);
        }

        .send-btn {
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple)) !important;
            color: #000 !important;
            font-weight: 700;
        }

        /* Quick Actions */
        .quick-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 15px;
        }

        .quick-chip {
            padding: 8px 16px;
            background: rgba(0, 240, 255, 0.08);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-radius: 20px;
            font-size: 12px;
            color: var(--neon-cyan);
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Rajdhani', sans-serif;
            font-weight: 600;
        }

        .quick-chip:hover {
            background: rgba(0, 240, 255, 0.2);
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 240, 255, 0.2);
        }

        /* Part Search Section */
        .search-section {
            margin-bottom: 25px;
        }

        .search-bar {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
        }

        .search-input-wrapper {
            flex: 1;
            position: relative;
        }

        .search-input {
            width: 100%;
            padding: 16px 20px 16px 50px;
            background: rgba(0, 240, 255, 0.05);
            border: 1px solid var(--glass-border);
            border-radius: 14px;
            color: var(--text-primary);
            font-family: 'Rajdhani', sans-serif;
            font-size: 16px;
            outline: none;
            transition: all 0.3s ease;
        }

        .search-input:focus {
            border-color: var(--neon-cyan);
            box-shadow: 0 0 30px rgba(0, 240, 255, 0.1);
        }

        .search-icon {
            position: absolute;
            left: 18px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--neon-cyan);
            font-size: 16px;
        }

        .search-filters {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .filter-btn {
            padding: 10px 20px;
            background: rgba(0, 240, 255, 0.05);
            border: 1px solid var(--glass-border);
            border-radius: 10px;
            color: var(--text-secondary);
            font-family: 'Rajdhani', sans-serif;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .filter-btn:hover, .filter-btn.active {
            background: rgba(0, 240, 255, 0.15);
            border-color: var(--neon-cyan);
            color: var(--neon-cyan);
        }

        /* Part Cards */
        .parts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }

        .part-card {
            background: rgba(16, 24, 39, 0.6);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 20px;
            transition: all 0.4s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .part-card:hover {
            transform: translateY(-5px);
            border-color: var(--neon-cyan);
            box-shadow: 0 10px 40px rgba(0, 240, 255, 0.15);
        }

        .part-card::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(0, 240, 255, 0.1) 0%, transparent 70%);
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
        }

        .part-card:hover::after {
            opacity: 1;
        }

        .part-image {
            width: 100%;
            height: 160px;
            background: linear-gradient(135deg, rgba(0, 240, 255, 0.1), rgba(184, 41, 255, 0.1));
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 16px;
            position: relative;
            overflow: hidden;
        }

        .part-image i {
            font-size: 48px;
            color: var(--neon-cyan);
            opacity: 0.8;
        }

        .part-badge {
            position: absolute;
            top: 10px;
            right: 10px;
            padding: 4px 10px;
            background: rgba(0, 255, 136, 0.2);
            border: 1px solid var(--neon-green);
            color: var(--neon-green);
            font-size: 10px;
            font-weight: 700;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .part-badge.limited {
            background: rgba(255, 107, 53, 0.2);
            border-color: var(--neon-orange);
            color: var(--neon-orange);
        }

        .part-name {
            font-family: 'Orbitron', sans-serif;
            font-size: 15px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 6px;
        }

        .part-number {
            font-size: 12px;
            color: var(--neon-cyan);
            font-family: 'Courier New', monospace;
            margin-bottom: 10px;
            cursor: pointer;
            transition: color 0.2s;
        }

        .part-number:hover {
            color: var(--neon-green);
            text-decoration: underline;
        }

        .part-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }

        .part-price {
            font-family: 'Orbitron', sans-serif;
            font-size: 20px;
            font-weight: 700;
            color: var(--neon-green);
        }

        .part-condition {
            padding: 4px 10px;
            background: rgba(0, 240, 255, 0.1);
            border-radius: 6px;
            font-size: 11px;
            color: var(--neon-cyan);
            font-weight: 600;
        }

        .part-actions {
            display: flex;
            gap: 10px;
        }

        .part-btn {
            flex: 1;
            padding: 10px;
            border: 1px solid var(--glass-border);
            background: rgba(0, 240, 255, 0.05);
            color: var(--neon-cyan);
            font-family: 'Rajdhani', sans-serif;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .part-btn:hover {
            background: rgba(0, 240, 255, 0.2);
            border-color: var(--neon-cyan);
        }

        .part-btn.primary {
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
            color: #000;
            border: none;
        }

        .part-btn.primary:hover {
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
        }

        /* Digital Twin Visualization */
        .twin-viewer {
            height: 350px;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .twin-canvas {
            width: 100%;
            height: 100%;
            border-radius: 12px;
        }

        .twin-overlay {
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            display: flex;
            gap: 15px;
        }

        .twin-metric {
            flex: 1;
            background: rgba(10, 14, 23, 0.9);
            border: 1px solid var(--glass-border);
            border-radius: 10px;
            padding: 12px;
            text-align: center;
        }

        .twin-metric-value {
            font-family: 'Orbitron', sans-serif;
            font-size: 20px;
            color: var(--neon-cyan);
        }

        .twin-metric-label {
            font-size: 10px;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 4px;
        }

        /* Inventory Map */
        .map-container {
            height: 300px;
            position: relative;
            background: rgba(0, 20, 40, 0.5);
            border-radius: 12px;
            overflow: hidden;
        }

        .map-canvas {
            width: 100%;
            height: 100%;
        }

        /* Upload Zone */
        .upload-zone {
            border: 2px dashed var(--glass-border);
            border-radius: 16px;
            padding: 40px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
            margin-bottom: 20px;
        }

        .upload-zone:hover, .upload-zone.dragover {
            border-color: var(--neon-cyan);
            background: rgba(0, 240, 255, 0.05);
        }

        .upload-zone i {
            font-size: 48px;
            color: var(--neon-cyan);
            margin-bottom: 15px;
            display: block;
        }

        .upload-text {
            font-size: 16px;
            color: var(--text-secondary);
            margin-bottom: 8px;
        }

        .upload-subtext {
            font-size: 12px;
            color: var(--text-secondary);
            opacity: 0.7;
        }

        /* Voice Wave */
        .voice-wave {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 3px;
            height: 40px;
        }

        .voice-bar {
            width: 4px;
            background: linear-gradient(to top, var(--neon-cyan), var(--neon-purple));
            border-radius: 2px;
            animation: voiceAnimate 1s infinite ease-in-out;
        }

        .voice-bar:nth-child(1) { height: 20%; animation-delay: 0s; }
        .voice-bar:nth-child(2) { height: 40%; animation-delay: 0.1s; }
        .voice-bar:nth-child(3) { height: 70%; animation-delay: 0.2s; }
        .voice-bar:nth-child(4) { height: 50%; animation-delay: 0.3s; }
        .voice-bar:nth-child(5) { height: 80%; animation-delay: 0.4s; }
        .voice-bar:nth-child(6) { height: 60%; animation-delay: 0.5s; }
        .voice-bar:nth-child(7) { height: 90%; animation-delay: 0.6s; }
        .voice-bar:nth-child(8) { height: 40%; animation-delay: 0.7s; }
        .voice-bar:nth-child(9) { height: 70%; animation-delay: 0.8s; }
        .voice-bar:nth-child(10) { height: 30%; animation-delay: 0.9s; }

        @keyframes voiceAnimate {
            0%, 100% { transform: scaleY(0.5); }
            50% { transform: scaleY(1); }
        }

        /* Modal */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 2000;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
        }

        .modal-overlay.active {
            opacity: 1;
            visibility: visible;
        }

        .modal-content {
            background: var(--panel-bg);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 40px;
            max-width: 500px;
            width: 90%;
            transform: scale(0.9);
            transition: transform 0.3s ease;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        }

        .modal-overlay.active .modal-content {
            transform: scale(1);
        }

        .modal-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 20px;
            color: var(--neon-cyan);
            margin-bottom: 20px;
            text-align: center;
        }

        /* Responsive */
        @media (max-width: 1200px) {
            .main-container {
                grid-template-columns: 1fr;
            }
            .hero-section {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 768px) {
            .header {
                padding: 0 20px;
            }
            .nav-buttons {
                display: none;
            }
            .main-container {
                padding: 20px;
            }
            .hero-title {
                font-size: 28px;
            }
        }

        /* Scanning Animation */
        .scan-line {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--neon-cyan), transparent);
            animation: scan 3s infinite linear;
            pointer-events: none;
        }

        @keyframes scan {
            0% { top: 0; opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { top: 100%; opacity: 0; }
        }

        /* Notification Toast */
        .toast-container {
            position: fixed;
            top: 90px;
            right: 30px;
            z-index: 3000;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .toast {
            background: var(--panel-bg);
            border: 1px solid var(--glass-border);
            border-left: 3px solid var(--neon-cyan);
            border-radius: 10px;
            padding: 16px 20px;
            min-width: 300px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            animation: toastSlide 0.4s ease;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        @keyframes toastSlide {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        .toast-icon {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(0, 240, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--neon-cyan);
            flex-shrink: 0;
        }

        .toast-content {
            flex: 1;
        }

        .toast-title {
            font-weight: 600;
            font-size: 14px;
            margin-bottom: 2px;
        }

        .toast-message {
            font-size: 12px;
            color: var(--text-secondary);
        }

        /* Tab Content */
        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: grid;
            animation: fadeIn 0.4s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Blockchain Verification Badge */
        .blockchain-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            background: rgba(0, 255, 136, 0.1);
            border: 1px solid var(--neon-green);
            border-radius: 20px;
            font-size: 11px;
            color: var(--neon-green);
            font-weight: 600;
        }

        .blockchain-badge i {
            font-size: 10px;
        }
    </style>
</head>
<body>
    <!-- Boot Sequence Overlay -->
    <div id="bootOverlay">
        <div style="font-family: 'Orbitron', sans-serif; font-size: 32px; color: var(--neon-cyan); margin-bottom: 20px; text-shadow: 0 0 20px rgba(0, 240, 255, 0.5);">
            AEROBRAIN <span style="color: var(--neon-orange);">AI</span>
        </div>
        <div style="width: 300px; height: 4px; background: rgba(0, 240, 255, 0.1); border-radius: 2px; overflow: hidden;">
            <div id="bootProgress" style="width: 0%; height: 100%; background: linear-gradient(90deg, var(--neon-cyan), var(--neon-purple)); transition: width 0.1s linear;"></div>
        </div>
        <div id="bootText" style="margin-top: 15px; font-family: 'Rajdhani', monospace; color: var(--text-secondary); font-size: 14px;">Initializing neural networks...</div>
    </div>

    <!-- Background Effects -->
    <div class="bg-grid"></div>
    <div class="bg-particles" id="particles"></div>

    <!-- Header -->
    <header class="header">
        <div class="logo-section">
            <div class="logo-icon">
                <i class="fas fa-brain"></i>
            </div>
            <div>
                <div class="logo-text">AEROBRAIN</div>
                <div class="logo-sub">AI Spare Parts Concierge</div>
            </div>
        </div>
        <div class="nav-buttons">
            <button class="nav-btn active" onclick="switchTab('dashboard', this)">
                <i class="fas fa-table-cells-large"></i> Dashboard
            </button>
            <button class="nav-btn" onclick="switchTab('search', this)">
                <i class="fas fa-search"></i> Part Search
            </button>
            <button class="nav-btn" onclick="switchTab('twin', this)">
                <i class="fas fa-cube"></i> Digital Twin
            </button>
            <button class="nav-btn" onclick="switchTab('inventory', this)">
                <i class="fas fa-globe"></i> Global Inventory
            </button>
        </div>
        <div class="status-bar">
            <div class="status-item">
                <div class="status-dot"></div>
                <span>AI Online</span>
            </div>
            <div class="status-item">
                <i class="fas fa-database" style="color: var(--neon-cyan);"></i>
                <span>12,847 Parts</span>
            </div>
            <div class="status-item">
                <i class="fas fa-satellite-dish" style="color: var(--neon-orange);"></i>
                <span>Live Feed</span>
            </div>
        </div>
    </header>

    <!-- Toast Container -->
    <div class="toast-container" id="toastContainer"></div>

    <!-- Main Content -->
    <div class="main-container">

        <!-- DASHBOARD TAB -->
        <div id="dashboard" class="tab-content active" style="grid-column: 1 / -1; grid-template-columns: 1fr 400px; gap: 25px;">
            <!-- Left Column -->
            <div style="display: flex; flex-direction: column; gap: 25px;">
                <!-- Hero Section -->
                <div class="hero-section">
                    <div class="glass-panel hero-main">
                        <div class="scan-line"></div>
                        <h1 class="hero-title">Welcome to the Future of Aviation Parts</h1>
                        <p class="hero-subtitle">
                            AI-powered spare parts concierge for Don Smith's aviation business. 
                            Visual identification, predictive maintenance, and global inventory intelligence — all in one neural interface.
                        </p>
                        <div class="hero-buttons">
                            <button class="btn-primary" onclick="switchTab('search', document.querySelectorAll('.nav-btn')[1])">
                                <i class="fas fa-rocket"></i> Find Parts Now
                            </button>
                            <button class="btn-secondary" onclick="startVoiceSearch()">
                                <i class="fas fa-microphone"></i> Voice Command
                            </button>
                        </div>
                    </div>
                    <div class="glass-panel stat-card">
                        <div class="stat-value" id="statParts">0</div>
                        <div class="stat-label">Parts in Stock</div>
                        <div class="stat-change">+234 this week</div>
                    </div>
                    <div class="glass-panel stat-card">
                        <div class="stat-value" id="statClients">0</div>
                        <div class="stat-label">Active Clients</div>
                        <div class="stat-change">+12 this month</div>
                    </div>
                </div>

                <!-- AI Visual Search -->
                <div class="glass-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <i class="fas fa-camera"></i> AI Visual Part Identification
                        </div>
                        <span class="blockchain-badge">
                            <i class="fas fa-link"></i> Blockchain Verified
                        </span>
                    </div>
                    <div class="upload-zone" id="uploadZone" onclick="document.getElementById('fileInput').click()">
                        <i class="fas fa-cloud-upload-alt"></i>
                        <div class="upload-text">Drop part image here or click to upload</div>
                        <div class="upload-subtext">Supports JPG, PNG, HEIC | AI will identify part number, condition & compatibility</div>
                    </div>
                    <input type="file" id="fileInput" style="display: none;" accept="image/*" onchange="handleImageUpload(event)">

                    <div id="uploadPreview" style="display: none; margin-bottom: 20px;">
                        <div style="display: flex; gap: 20px; align-items: flex-start;">
                            <div style="width: 200px; height: 200px; border-radius: 12px; overflow: hidden; border: 1px solid var(--glass-border);">
                                <img id="previewImg" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div style="flex: 1;">
                                <div style="font-family: 'Orbitron', sans-serif; color: var(--neon-cyan); margin-bottom: 10px;">
                                    <i class="fas fa-robot"></i> AI Analysis Results
                                </div>
                                <div id="analysisResults" style="font-size: 14px; line-height: 1.8;"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Recent Parts -->
                <div class="glass-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <i class="fas fa-clock"></i> Recently Added Parts
                        </div>
                        <button class="nav-btn" style="padding: 6px 14px; font-size: 11px;" onclick="switchTab('search', document.querySelectorAll('.nav-btn')[1])">
                            View All
                        </button>
                    </div>
                    <div class="parts-grid" id="recentParts"></div>
                </div>
            </div>

            <!-- Right Column - AI Chat -->
            <div class="glass-panel chat-container">
                <div class="panel-header">
                    <div class="panel-title">
                        <i class="fas fa-robot"></i> AERO AI Concierge
                    </div>
                    <div style="display: flex; gap: 10px; align-items: center;">
                        <div class="voice-wave" id="voiceWave" style="display: none;">
                            <div class="voice-bar"></div><div class="voice-bar"></div><div class="voice-bar"></div>
                            <div class="voice-bar"></div><div class="voice-bar"></div><div class="voice-bar"></div>
                            <div class="voice-bar"></div><div class="voice-bar"></div><div class="voice-bar"></div><div class="voice-bar"></div>
                        </div>
                        <button class="chat-action-btn" style="width: 32px; height: 32px; font-size: 12px;" onclick="clearChat()" title="Clear Chat">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>

                <div class="quick-actions">
                    <div class="quick-chip" onclick="sendQuickMessage('Find brake assembly for Boeing 737')">
                        <i class="fas fa-plane"></i> 737 Brake
                    </div>
                    <div class="quick-chip" onclick="sendQuickMessage('Check APU availability')">
                        <i class="fas fa-fan"></i> APU Stock
                    </div>
                    <div class="quick-chip" onclick="sendQuickMessage('Predictive alert for engine parts')">
                        <i class="fas fa-bell"></i> Predictive
                    </div>
                    <div class="quick-chip" onclick="sendQuickMessage('Show landing gear inventory')">
                        <i class="fas fa-cogs"></i> Landing Gear
                    </div>
                </div>

                <div class="chat-messages" id="chatMessages"></div>

                <div class="chat-input-area">
                    <input type="text" class="chat-input" id="chatInput" placeholder="Ask AI about parts, pricing, compatibility..." onkeypress="handleChatKeypress(event)">
                    <div class="chat-actions">
                        <button class="chat-action-btn" onclick="startVoiceSearch()" title="Voice Search">
                            <i class="fas fa-microphone"></i>
                        </button>
                        <button class="chat-action-btn send-btn" onclick="sendMessage()" title="Send">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- SEARCH TAB -->
        <div id="search" class="tab-content" style="grid-column: 1 / -1;">
            <div class="glass-panel search-section">
                <div class="panel-header">
                    <div class="panel-title">
                        <i class="fas fa-search"></i> Neural Part Search
                    </div>
                </div>
                <div class="search-bar">
                    <div class="search-input-wrapper">
                        <i class="fas fa-search search-icon"></i>
                        <input type="text" class="search-input" id="searchInput" placeholder="Search by part number, aircraft type, description, or say 'brake assembly for 737-800'..." onkeypress="handleSearchKeypress(event)">
                    </div>
                    <button class="btn-primary" onclick="performSearch()">
                        <i class="fas fa-search"></i> Search
                    </button>
                </div>
                <div class="search-filters">
                    <button class="filter-btn active" onclick="setFilter(this, 'all')">
                        <i class="fas fa-table-cells-large"></i> All Parts
                    </button>
                    <button class="filter-btn" onclick="setFilter(this, 'engine')">
                        <i class="fas fa-fan"></i> Engine
                    </button>
                    <button class="filter-btn" onclick="setFilter(this, 'landing')">
                        <i class="fas fa-cogs"></i> Landing Gear
                    </button>
                    <button class="filter-btn" onclick="setFilter(this, 'avionics')">
                        <i class="fas fa-microchip"></i> Avionics
                    </button>
                    <button class="filter-btn" onclick="setFilter(this, 'hydraulic')">
                        <i class="fas fa-tint"></i> Hydraulic
                    </button>
                    <button class="filter-btn" onclick="setFilter(this, 'apu')">
                        <i class="fas fa-bolt"></i> APU
                    </button>
                    <button class="filter-btn" onclick="setFilter(this, 'new')">
                        <i class="fas fa-certificate"></i> New Arrivals
                    </button>
                </div>
            </div>
            <div class="parts-grid" id="searchResults"></div>
        </div>

        <!-- DIGITAL TWIN TAB -->
        <div id="twin" class="tab-content" style="grid-column: 1 / -1; grid-template-columns: 2fr 1fr; gap: 25px;">
            <div class="glass-panel">
                <div class="panel-header">
                    <div class="panel-title">
                        <i class="fas fa-cube"></i> Digital Twin Engine Monitor
                    </div>
                    <span style="font-size: 12px; color: var(--neon-green);">
                        <i class="fas fa-circle" style="font-size: 8px;"></i> Live Data Stream
                    </span>
                </div>
                <div class="twin-viewer">
                    <canvas id="twinCanvas" class="twin-canvas"></canvas>
                    <div class="twin-overlay">
                        <div class="twin-metric">
                            <div class="twin-metric-value" id="twinTemp">842°C</div>
                            <div class="twin-metric-label">Core Temp</div>
                        </div>
                        <div class="twin-metric">
                            <div class="twin-metric-value" id="twinRPM">14,250</div>
                            <div class="twin-metric-label">RPM</div>
                        </div>
                        <div class="twin-metric">
                            <div class="twin-metric-value" id="twinHealth">98%</div>
                            <div class="twin-metric-label">Health</div>
                        </div>
                        <div class="twin-metric">
                            <div class="twin-metric-value" id="twinLife">4,200h</div>
                            <div class="twin-metric-label">Remaining Life</div>
                        </div>
                    </div>
                </div>
            </div>
            <div style="display: flex; flex-direction: column; gap: 25px;">
                <div class="glass-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <i class="fas fa-exclamation-triangle"></i> Predictive Alerts
                        </div>
                    </div>
                    <div id="predictiveAlerts" style="display: flex; flex-direction: column; gap: 12px;"></div>
                </div>
                <div class="glass-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <i class="fas fa-tools"></i> Maintenance Schedule
                        </div>
                    </div>
                    <div id="maintenanceSchedule" style="display: flex; flex-direction: column; gap: 10px;"></div>
                </div>
            </div>
        </div>

        <!-- INVENTORY TAB -->
        <div id="inventory" class="tab-content" style="grid-column: 1 / -1; grid-template-columns: 2fr 1fr; gap: 25px;">
            <div class="glass-panel">
                <div class="panel-header">
                    <div class="panel-title">
                        <i class="fas fa-globe"></i> Global Inventory Network
                    </div>
                    <div style="display: flex; gap: 15px; font-size: 12px; flex-wrap: wrap;">
                        <span style="color: var(--neon-cyan);"><i class="fas fa-circle" style="font-size: 8px;"></i> Nairobi (HQ)</span>
                        <span style="color: var(--neon-orange);"><i class="fas fa-circle" style="font-size: 8px;"></i> Dubai</span>
                        <span style="color: var(--neon-green);"><i class="fas fa-circle" style="font-size: 8px;"></i> Amsterdam</span>
                        <span style="color: var(--neon-purple);"><i class="fas fa-circle" style="font-size: 8px;"></i> Singapore</span>
                    </div>
                </div>
                <div class="map-container">
                    <canvas id="mapCanvas" class="map-canvas"></canvas>
                </div>
            </div>
            <div style="display: flex; flex-direction: column; gap: 25px;">
                <div class="glass-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <i class="fas fa-warehouse"></i> Warehouse Status
                        </div>
                    </div>
                    <div id="warehouseStatus" style="display: flex; flex-direction: column; gap: 15px;"></div>
                </div>
                <div class="glass-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <i class="fas fa-chart-line"></i> Market Intelligence
                        </div>
                    </div>
                    <div id="marketIntel" style="display: flex; flex-direction: column; gap: 12px;"></div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal -->
    <div class="modal-overlay" id="modal" onclick="if(event.target === this) closeModal()">
        <div class="modal-content">
            <div class="modal-title" id="modalTitle">Part Details</div>
            <div id="modalBody"></div>
            <div style="display: flex; gap: 10px; margin-top: 25px;">
                <button class="btn-primary" style="flex: 1;" onclick="showToast('Quote Requested', 'AI-generated quote sent to your email'); closeModal()">Request Quote</button>
                <button class="btn-secondary" style="flex: 1;" onclick="closeModal()">Close</button>
            </div>
        </div>
    </div>

    <script>
        // ==================== DATA ====================
        const partsDatabase = [
            { id: "P001", name: "CFM56-7B Brake Assembly", number: "261-2310-001", aircraft: "Boeing 737-800", category: "landing", price: 48500, condition: "Overhauled", availability: "In Stock", location: "Nairobi", cert: "FAA/EASA", blockchain: "0x7a8f...3e2d", image: "fa-cogs" },
            { id: "P002", name: "APU GTCP 131-9B", number: "380-0702-01", aircraft: "Airbus A320", category: "apu", price: 125000, condition: "Serviceable", availability: "Limited", location: "Dubai", cert: "FAA/EASA", blockchain: "0x9b2c...7f1a", image: "fa-bolt" },
            { id: "P003", name: "Landing Gear Actuator", number: "65-44676-12", aircraft: "Boeing 737 MAX", category: "landing", price: 32000, condition: "New", availability: "In Stock", location: "Amsterdam", cert: "OEM", blockchain: "0x3d4e...9a5b", image: "fa-cogs" },
            { id: "P004", name: "Engine HPT Blade Set", number: "340-402-503-0", aircraft: "CFM LEAP-1B", category: "engine", price: 78000, condition: "Overhauled", availability: "In Stock", location: "Nairobi", cert: "EASA", blockchain: "0x1a2b...4c5d", image: "fa-fan" },
            { id: "P005", name: "Avionics Display Unit", number: "822-1234-020", aircraft: "Boeing 787", category: "avionics", price: 15600, condition: "New", availability: "In Stock", location: "Singapore", cert: "FAA", blockchain: "0x6e7f...8a9b", image: "fa-microchip" },
            { id: "P006", name: "Hydraulic Pump Assembly", number: "271-2116-02", aircraft: "Boeing 777", category: "hydraulic", price: 42000, condition: "Overhauled", availability: "Limited", location: "Dubai", cert: "FAA/EASA", blockchain: "0x2b3c...4d5e", image: "fa-tint" },
            { id: "P007", name: "APU Starter Motor", number: "350-1234-01", aircraft: "Boeing 737 NG", category: "apu", price: 18500, condition: "Serviceable", availability: "In Stock", location: "Nairobi", cert: "FAA", blockchain: "0x8c9d...0e1f", image: "fa-bolt" },
            { id: "P008", name: "Nose Wheel Assembly", number: "261-1230-010", aircraft: "Boeing 737-800", category: "landing", price: 28000, condition: "Overhauled", availability: "In Stock", location: "Amsterdam", cert: "EASA", blockchain: "0x4f5a...6b7c", image: "fa-circle" }
        ];

        const aiResponses = {
            "brake": "🔍 <strong>Analysis Complete:</strong> I've located 3 brake assemblies matching your query.<br><br>✈️ <strong>Top Match:</strong> CFM56-7B Brake Assembly (P/N: 261-2310-001)<br>🛩️ <strong>Aircraft:</strong> Boeing 737-800<br>💰 <strong>Price:</strong> $48,500 (Overhauled)<br>📍 <strong>Location:</strong> Nairobi HQ<br>🔗 <strong>Traceability:</strong> Blockchain verified (0x7a8f...3e2d)<br><br>Shall I reserve this unit and generate an AOG delivery quote?",
            "apu": "🔍 <strong>APU Inventory Check:</strong> I found 2 APU units in stock.<br><br>1️⃣ <strong>GTCP 131-9B</strong> (380-0702-01) for A320<br>💰 $125,000 | 📍 Dubai | 🔗 Blockchain verified<br><br>2️⃣ <strong>APU Starter Motor</strong> for 737 NG<br>💰 $18,500 | 📍 Nairobi<br><br>Would you like me to check compatibility with your specific aircraft serial?",
            "engine": "🔧 <strong>Engine Parts Intelligence:</strong> Engine components are our specialty!<br><br>I currently have HPT Blade Sets for CFM LEAP-1B at $78,000 and various compressor components in stock.<br><br>💡 <strong>AI Insight:</strong> Would you like me to run a predictive analysis on which parts you'll likely need based on your fleet's flight hours?",
            "landing": "🛬 <strong>Landing Gear Components:</strong> I have actuators, nose wheels, and brake assemblies available.<br><br>The 737 MAX Landing Gear Actuator (65-44676-12) is in <strong>New</strong> condition at $32,000 from Amsterdam.<br><br>🚀 I can arrange AOG delivery within 24 hours to any African airport.",
            "predictive": "📊 <strong>Predictive Maintenance Alert:</strong> Based on your fleet's digital twin data, I predict you'll need:<br><br>1️⃣ HPT Blade inspection at 4,200 cycles (2 months)<br>2️⃣ Brake replacement at 1,800 landings (6 weeks)<br>3️⃣ APU starter check at next C-check<br><br>Shall I pre-order these parts to secure current pricing?",
            "price": "💹 <strong>Market Intelligence:</strong> Our pricing is dynamically optimized using AI.<br><br>Current best deals:<br>• Brake Assembly: $48,500 <span style='color:var(--neon-green)'>(-8%)</span><br>• APU GTCP 131-9B: $125,000 <span style='color:var(--neon-orange)'>(+3%)</span><br>• Avionics Display: $15,600 <span style='color:var(--neon-green)'>(-12%)</span><br><br>Prices update every 15 minutes based on global demand.",
            "compatibility": "🔄 <strong>Compatibility Check:</strong> I can verify cross-compatibility instantly.<br><br>Please provide your aircraft type, serial number, or engine model. My neural network has access to 2.4 million part cross-references including OEM, PMA, and DER alternatives.",
            "default": "👋 I'm <strong>AEROBRAIN</strong>, your AI aviation parts concierge. I can help you:<br>• 🔍 Find parts visually or by P/N<br>• 🔄 Check compatibility<br>• 📊 Predict maintenance needs<br>• 🔗 Verify blockchain traceability<br>• 🚀 Arrange global AOG logistics<br><br>What aircraft or part are you looking for today?"
        };

        const warehouses = [
            { name: "Nairobi (HQ)", location: "Kenya", stock: 4520, status: "Online", color: "#00f0ff" },
            { name: "Dubai", location: "UAE", stock: 3890, status: "Online", color: "#ff6b35" },
            { name: "Amsterdam", location: "Netherlands", stock: 2150, status: "Online", color: "#00ff88" },
            { name: "Singapore", location: "Singapore", stock: 1287, status: "Maintenance", color: "#b829ff" }
        ];

        const alerts = [
            { type: "warning", title: "HPT Blade Wear Detected", message: "Engine SN: E-78432 approaching limit. Order replacement within 200 cycles.", time: "2 min ago" },
            { type: "info", title: "Price Drop Alert", message: "CFM56 Brake Assembly dropped 8% in Dubai market. Good time to buy.", time: "15 min ago" },
            { type: "success", title: "New Stock Arrived", message: "12 overhauled landing gear actuators arrived in Nairobi from Amsterdam.", time: "1 hour ago" }
        ];

        // ==================== BOOT SEQUENCE ====================
        window.addEventListener('DOMContentLoaded', () => {
            const bootProgress = document.getElementById('bootProgress');
            const bootText = document.getElementById('bootText');
            const bootOverlay = document.getElementById('bootOverlay');
            
            const steps = [
                "Connecting to global inventory nodes...",
                "Loading blockchain verification protocols...",
                "Calibrating digital twin sensors...",
                "Synchronizing AI concierge models...",
                "System ready. Welcome, Don."
            ];
            
            let progress = 0;
            let stepIndex = 0;
            
            const bootInterval = setInterval(() => {
                progress += 2;
                bootProgress.style.width = progress + '%';
                
                if (progress % 20 === 0 && stepIndex < steps.length) {
                    bootText.textContent = steps[stepIndex];
                    stepIndex++;
                }
                
                if (progress >= 100) {
                    clearInterval(bootInterval);
                    setTimeout(() => {
                        bootOverlay.style.opacity = '0';
                        setTimeout(() => {
                            bootOverlay.style.display = 'none';
                            initializeApp();
                        }, 800);
                    }, 500);
                }
            }, 30);
        });

        function initializeApp() {
            createParticles();
            initChat();
            renderRecentParts();
            renderSearchResults(partsDatabase);
            initDigitalTwin();
            initMap();
            renderWarehouses();
            renderAlerts();
            renderMaintenance();
            renderMarketIntel();
            animateStats();
        }

        // ==================== PARTICLES ====================
        function createParticles() {
            const container = document.getElementById('particles');
            for (let i = 0; i < 50; i++) {
                const p = document.createElement('div');
                p.className = 'particle';
                p.style.left = Math.random() * 100 + '%';
                p.style.top = Math.random() * 100 + '%';
                p.style.animationDelay = Math.random() * 15 + 's';
                p.style.animationDuration = (10 + Math.random() * 20) + 's';
                container.appendChild(p);
            }
        }

        // ==================== TABS ====================
        function switchTab(tabId, btnElement) {
            document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            
            if (btnElement) {
                btnElement.classList.add('active');
            } else {
                const btn = document.querySelector(`.nav-btn[onclick*="'${tabId}'"]`);
                if (btn) btn.classList.add('active');
            }
        }

        // ==================== CHAT ====================
        function initChat() {
            addMessage('ai', "Welcome to AEROBRAIN, Don. I'm your AI aviation parts concierge. I can visually identify parts, predict maintenance needs, check global inventory, and arrange instant quotes. How can I assist your operations today?");
        }

        function clearChat() {
            document.getElementById('chatMessages').innerHTML = '';
            initChat();
            showToast('Chat Cleared', 'Conversation history reset');
        }

        function addMessage(sender, text) {
            const container = document.getElementById('chatMessages');
            const msg = document.createElement('div');
            msg.className = `message ${sender}`;
            const time = new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
            msg.innerHTML = `
                <div class="message-avatar">
                    <i class="fas fa-${sender === 'ai' ? 'robot' : 'user'}"></i>
                </div>
                <div>
                    <div class="message-content">${text}</div>
                    <div class="message-time">${time}</div>
                </div>
            `;
            container.appendChild(msg);
            container.scrollTop = container.scrollHeight;
        }

        function showTyping() {
            const container = document.getElementById('chatMessages');
            const typing = document.createElement('div');
            typing.className = 'message ai';
            typing.id = 'typingIndicator';
            typing.innerHTML = `
                <div class="message-avatar"><i class="fas fa-robot"></i></div>
                <div class="message-content typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            `;
            container.appendChild(typing);
            container.scrollTop = container.scrollHeight;
        }

        function removeTyping() {
            const typing = document.getElementById('typingIndicator');
            if (typing) typing.remove();
        }

        function handleChatKeypress(e) {
            if (e.key === 'Enter') sendMessage();
        }

        function sendMessage() {
            const input = document.getElementById('chatInput');
            const text = input.value.trim();
            if (!text) return;

            addMessage('user', text);
            input.value = '';
            showTyping();

            setTimeout(() => {
                removeTyping();
                const response = generateAIResponse(text);
                addMessage('ai', response);
            }, 1500 + Math.random() * 1000);
        }

        function sendQuickMessage(text) {
            document.getElementById('chatInput').value = text;
            sendMessage();
        }

        function generateAIResponse(text) {
            const lower = text.toLowerCase();
            if (lower.includes('brake')) return aiResponses.brake;
            if (lower.includes('apu')) return aiResponses.apu;
            if (lower.includes('engine') || lower.includes('turbine') || lower.includes('blade')) return aiResponses.engine;
            if (lower.includes('landing') || lower.includes('gear') || lower.includes('wheel')) return aiResponses.landing;
            if (lower.includes('predict') || lower.includes('alert') || lower.includes('maintenance')) return aiResponses.predictive;
            if (lower.includes('price') || lower.includes('cost') || lower.includes('cheap') || lower.includes('market')) return aiResponses.price;
            if (lower.includes('compatible') || lower.includes('fit') || lower.includes('work with')) return aiResponses.compatibility;
            return aiResponses.default;
        }

        // ==================== VOICE SEARCH ====================
        let voiceActive = false;
        function startVoiceSearch() {
            const wave = document.getElementById('voiceWave');
            if (voiceActive) {
                voiceActive = false;
                wave.style.display = 'none';
                showToast('Voice Search', 'Voice input deactivated');
            } else {
                voiceActive = true;
                wave.style.display = 'flex';
                showToast('Voice Search', 'Listening... Say something like "Find brake assembly for 737"');

                setTimeout(() => {
                    if (voiceActive) {
                        voiceActive = false;
                        wave.style.display = 'none';
                        document.getElementById('chatInput').value = 'Find brake assembly for Boeing 737-800';
                        sendMessage();
                    }
                }, 4000);
            }
        }

        // ==================== PARTS RENDERING ====================
        function renderPartCard(part) {
            const isLimited = part.availability === 'Limited';
            return `
                <div class="part-card" onclick="showPartDetail('${part.id}')">
                    <div class="part-image">
                        <i class="fas ${part.image}"></i>
                        <span class="part-badge ${isLimited ? 'limited' : ''}">${part.availability}</span>
                    </div>
                    <div class="part-name">${part.name}</div>
                    <div class="part-number" onclick="event.stopPropagation(); copyPartNumber('${part.number}')" title="Click to copy">
                        <i class="fas fa-copy" style="font-size: 10px; margin-right: 4px;"></i>${part.number}
                    </div>
                    <div class="part-meta">
                        <div class="part-price">$${part.price.toLocaleString()}</div>
                        <div class="part-condition">${part.condition}</div>
                    </div>
                    <div style="font-size: 12px; color: var(--text-secondary); margin-bottom: 12px;">
                        <i class="fas fa-plane"></i> ${part.aircraft} &nbsp;|&nbsp; 
                        <i class="fas fa-map-marker-alt"></i> ${part.location}
                    </div>
                    <div class="blockchain-badge" style="margin-bottom: 12px;">
                        <i class="fas fa-link"></i> ${part.blockchain}
                    </div>
                    <div class="part-actions">
                        <button class="part-btn" onclick="event.stopPropagation(); showToast('Quote Requested', 'Quote sent for ${part.name}')">
                            <i class="fas fa-file-invoice"></i> Quote
                        </button>
                        <button class="part-btn primary" onclick="event.stopPropagation(); showToast('Added to Cart', '${part.name} added to procurement list')">
                            <i class="fas fa-cart-plus"></i> Add
                        </button>
                    </div>
                </div>
            `;
        }

        function copyPartNumber(number) {
            navigator.clipboard.writeText(number).then(() => {
                showToast('Copied!', `Part number ${number} copied to clipboard`);
            });
        }

        function renderRecentParts() {
            const container = document.getElementById('recentParts');
            container.innerHTML = partsDatabase.slice(0, 4).map(renderPartCard).join('');
        }

        function renderSearchResults(parts) {
            const container = document.getElementById('searchResults');
            if (parts.length === 0) {
                container.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-secondary);">
                    <i class="fas fa-search" style="font-size: 48px; margin-bottom: 15px; opacity: 0.3;"></i>
                    <p>No parts found matching your criteria. Try adjusting your filters.</p>
                </div>`;
                return;
            }
            container.innerHTML = parts.map(renderPartCard).join('');
        }

        // ==================== SEARCH ====================
        function handleSearchKeypress(e) {
            if (e.key === 'Enter') performSearch();
        }

        function performSearch() {
            const query = document.getElementById('searchInput').value.toLowerCase();
            if (!query) {
                renderSearchResults(partsDatabase);
                return;
            }

            const filtered = partsDatabase.filter(p => 
                p.name.toLowerCase().includes(query) ||
                p.number.toLowerCase().includes(query) ||
                p.aircraft.toLowerCase().includes(query) ||
                p.category.toLowerCase().includes(query)
            );

            renderSearchResults(filtered);
            showToast('Search Complete', `Found ${filtered.length} parts matching "${query}"`);
        }

        function setFilter(btn, category) {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            if (category === 'all') {
                renderSearchResults(partsDatabase);
            } else if (category === 'new') {
                const filtered = partsDatabase.filter(p => p.condition === 'New');
                renderSearchResults(filtered);
            } else {
                const filtered = partsDatabase.filter(p => p.category === category);
                renderSearchResults(filtered);
            }
        }

        // ==================== IMAGE UPLOAD ====================
        function handleImageUpload(event) {
            const file = event.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('previewImg').src = e.target.result;
                document.getElementById('uploadPreview').style.display = 'block';
                document.getElementById('uploadZone').style.display = 'none';

                document.getElementById('analysisResults').innerHTML = `
                    <div style="color: var(--neon-cyan); margin-bottom: 10px;">
                        <i class="fas fa-spinner fa-spin"></i> Analyzing image with neural network...
                    </div>
                `;

                setTimeout(() => {
                    document.getElementById('analysisResults').innerHTML = `
                        <div style="margin-bottom: 8px;"><strong style="color: var(--neon-cyan);">Part Identified:</strong> CFM56-7B Brake Assembly</div>
                        <div style="margin-bottom: 8px;"><strong style="color: var(--neon-cyan);">Part Number:</strong> 261-2310-001</div>
                        <div style="margin-bottom: 8px;"><strong style="color: var(--neon-cyan);">Condition Estimate:</strong> <span style="color: var(--neon-orange);">Overhauled (87% confidence)</span></div>
                        <div style="margin-bottom: 8px;"><strong style="color: var(--neon-cyan);">Compatible Aircraft:</strong> Boeing 737-600/700/800/900</div>
                        <div style="margin-bottom: 8px;"><strong style="color: var(--neon-cyan);">Market Price:</strong> <span style="color: var(--neon-green);">$48,500</span></div>
                        <div><strong style="color: var(--neon-cyan);">Availability:</strong> <span style="color: var(--neon-green);">In Stock - Nairobi Warehouse</span></div>
                        <div style="margin-top: 15px;">
                            <button class="btn-primary" style="padding: 10px 20px; font-size: 12px;" onclick="showToast('Quote Requested', 'AI-generated quote sent to your email')">
                                <i class="fas fa-file-invoice"></i> Get Instant Quote
                            </button>
                        </div>
                    `;
                    showToast('AI Analysis Complete', 'Part identified with 87% confidence');
                }, 2500);
            };
            reader.readAsDataURL(file);
        }

        // ==================== DIGITAL TWIN ====================
        function initDigitalTwin() {
            const canvas = document.getElementById('twinCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            
            function resize() {
                canvas.width = canvas.offsetWidth;
                canvas.height = canvas.offsetHeight;
            }
            resize();
            window.addEventListener('resize', resize);

            let angle = 0;

            function draw() {
                ctx.fillStyle = 'rgba(0, 20, 40, 0.3)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                const cx = canvas.width / 2;
                const cy = canvas.height / 2;

                for (let i = 0; i < 5; i++) {
                    ctx.beginPath();
                    ctx.arc(cx, cy, 40 + i * 25, 0, Math.PI * 2);
                    ctx.strokeStyle = `rgba(0, 240, 255, ${0.1 + i * 0.05})`;
                    ctx.lineWidth = 2;
                    ctx.stroke();
                }

                for (let i = 0; i < 8; i++) {
                    const bladeAngle = angle + (i * Math.PI / 4);
                    const x1 = cx + Math.cos(bladeAngle) * 50;
                    const y1 = cy + Math.sin(bladeAngle) * 50;
                    const x2 = cx + Math.cos(bladeAngle) * 140;
                    const y2 = cy + Math.sin(bladeAngle) * 140;

                    ctx.beginPath();
                    ctx.moveTo(x1, y1);
                    ctx.lineTo(x2, y2);
                    ctx.strokeStyle = `rgba(0, 240, 255, ${0.3 + Math.sin(angle * 2 + i) * 0.2})`;
                    ctx.lineWidth = 3;
                    ctx.stroke();
                }

                ctx.beginPath();
                ctx.arc(cx, cy, 30, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(0, 240, 255, 0.2)';
                ctx.fill();
                ctx.strokeStyle = 'var(--neon-cyan)';
                ctx.lineWidth = 2;
                ctx.stroke();

                for (let i = 0; i < 20; i++) {
                    const px = cx + (Math.random() - 0.5) * 200;
                    const py = cy + (Math.random() - 0.5) * 200;
                    ctx.beginPath();
                    ctx.arc(px, py, Math.random() * 3, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(255, 107, 53, ${Math.random() * 0.5})`;
                    ctx.fill();
                }

                angle += 0.02;
                requestAnimationFrame(draw);
            }
            draw();

            setInterval(() => {
                const tempEl = document.getElementById('twinTemp');
                const rpmEl = document.getElementById('twinRPM');
                const healthEl = document.getElementById('twinHealth');
                if(tempEl) tempEl.textContent = (840 + Math.floor(Math.random() * 10)) + '°C';
                if(rpmEl) rpmEl.textContent = (14200 + Math.floor(Math.random() * 100)).toLocaleString();
                if(healthEl) healthEl.textContent = (97 + Math.floor(Math.random() * 3)) + '%';
            }, 2000);
        }

        function renderAlerts() {
            const container = document.getElementById('predictiveAlerts');
            const icons = { warning: 'fa-exclamation-triangle', info: 'fa-info-circle', success: 'fa-check-circle' };
            const colors = { warning: 'var(--neon-orange)', info: 'var(--neon-cyan)', success: 'var(--neon-green)' };

            container.innerHTML = alerts.map(a => `
                <div style="padding: 14px; background: rgba(0,0,0,0.3); border-radius: 10px; border-left: 3px solid ${colors[a.type]};">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 6px;">
                        <div style="font-weight: 600; font-size: 13px; color: ${colors[a.type]};">
                            <i class="fas ${icons[a.type]}"></i> ${a.title}
                        </div>
                        <div style="font-size: 10px; color: var(--text-secondary);">${a.time}</div>
                    </div>
                    <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">${a.message}</div>
                </div>
            `).join('');
        }

        function renderMaintenance() {
            const container = document.getElementById('maintenanceSchedule');
            const items = [
                { task: 'C-Check Due', aircraft: '5Y-KYA', due: '12 days', urgency: 'high' },
                { task: 'Engine HSI', aircraft: '5Y-KYB', due: '28 days', urgency: 'medium' },
                { task: 'Landing Gear OH', aircraft: '5Y-KYC', due: '45 days', urgency: 'low' },
                { task: 'APU Inspection', aircraft: '5Y-KYD', due: '60 days', urgency: 'low' }
            ];

            const colors = { high: 'var(--neon-orange)', medium: 'var(--neon-cyan)', low: 'var(--neon-green)' };

            container.innerHTML = items.map(item => `
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px; background: rgba(0,0,0,0.3); border-radius: 8px;">
                    <div>
                        <div style="font-weight: 600; font-size: 13px;">${item.task}</div>
                        <div style="font-size: 11px; color: var(--text-secondary);">${item.aircraft}</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 12px; color: ${colors[item.urgency]}; font-weight: 600;">${item.due}</div>
                        <div style="font-size: 10px; color: var(--text-secondary);">remaining</div>
                    </div>
                </div>
            `).join('');
        }

        // ==================== MAP ====================
        function initMap() {
            const canvas = document.getElementById('mapCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            
            function resize() {
                canvas.width = canvas.offsetWidth;
                canvas.height = canvas.offsetHeight;
            }
            resize();
            window.addEventListener('resize', resize);

            const locations = [
                { x: 0.55, y: 0.45, name: 'Nairobi', color: '#00f0ff', pulse: 0 },
                { x: 0.6, y: 0.35, name: 'Dubai', color: '#ff6b35', pulse: 1 },
                { x: 0.48, y: 0.25, name: 'Amsterdam', color: '#00ff88', pulse: 2 },
                { x: 0.75, y: 0.5, name: 'Singapore', color: '#b829ff', pulse: 3 }
            ];

            let time = 0;

            function draw() {
                ctx.fillStyle = 'rgba(0, 10, 20, 0.8)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.strokeStyle = 'rgba(0, 240, 255, 0.05)';
                ctx.lineWidth = 1;
                for (let i = 0; i < canvas.width; i += 30) {
                    ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke();
                }
                for (let i = 0; i < canvas.height; i += 30) {
                    ctx.beginPath(); ctx.moveTo(0, i); ctx.lineTo(canvas.width, i); ctx.stroke();
                }

                ctx.strokeStyle = 'rgba(0, 240, 255, 0.1)';
                ctx.lineWidth = 1;
                for (let i = 0; i < locations.length; i++) {
                    for (let j = i + 1; j < locations.length; j++) {
                        ctx.beginPath();
                        ctx.moveTo(locations[i].x * canvas.width, locations[i].y * canvas.height);
                        ctx.lineTo(locations[j].x * canvas.width, locations[j].y * canvas.height);
                        ctx.stroke();
                    }
                }

                locations.forEach(loc => {
                    const x = loc.x * canvas.width;
                    const y = loc.y * canvas.height;

                    const pulseSize = 20 + Math.sin(time * 2 + loc.pulse) * 10;
                    ctx.beginPath();
                    ctx.arc(x, y, pulseSize, 0, Math.PI * 2);
                    ctx.fillStyle = loc.color + '20';
                    ctx.fill();

                    ctx.beginPath();
                    ctx.arc(x, y, 6, 0, Math.PI * 2);
                    ctx.fillStyle = loc.color;
                    ctx.fill();
                    ctx.strokeStyle = loc.color + '80';
                    ctx.lineWidth = 2;
                    ctx.stroke();

                    ctx.fillStyle = '#fff';
                    ctx.font = '12px Rajdhani';
                    ctx.textAlign = 'center';
                    ctx.fillText(loc.name, x, y + 25);
                });

                const packetPos = (time * 0.5) % 1;
                for (let i = 0; i < locations.length; i++) {
                    const next = (i + 1) % locations.length;
                    const x = locations[i].x * canvas.width + (locations[next].x * canvas.width - locations[i].x * canvas.width) * packetPos;
                    const y = locations[i].y * canvas.height + (locations[next].y * canvas.height - locations[i].y * canvas.height) * packetPos;
                    ctx.beginPath();
                    ctx.arc(x, y, 3, 0, Math.PI * 2);
                    ctx.fillStyle = 'var(--neon-cyan)';
                    ctx.fill();
                }

                time += 0.01;
                requestAnimationFrame(draw);
            }
            draw();
        }

        function renderWarehouses() {
            const container = document.getElementById('warehouseStatus');
            container.innerHTML = warehouses.map(w => `
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 14px; background: rgba(0,0,0,0.3); border-radius: 10px; border-left: 3px solid ${w.color};">
                    <div>
                        <div style="font-weight: 600; font-size: 14px; color: ${w.color};">${w.name}</div>
                        <div style="font-size: 11px; color: var(--text-secondary);">${w.location}</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-family: 'Orbitron'; font-size: 18px; color: var(--text-primary);">${w.stock.toLocaleString()}</div>
                        <div style="font-size: 10px; color: var(--neon-green);">${w.status}</div>
                    </div>
                </div>
            `).join('');
        }

        function renderMarketIntel() {
            const container = document.getElementById('marketIntel');
            const intel = [
                { item: 'CFM56 Brake Assembly', trend: 'down', change: '-8%', price: '$48,500' },
                { item: 'APU GTCP 131-9B', trend: 'up', change: '+3%', price: '$125,000' },
                { item: 'LEAP HPT Blades', trend: 'down', change: '-12%', price: '$78,000' },
                { item: 'Avionics Display', trend: 'stable', change: '0%', price: '$15,600' }
            ];

            const colors = { up: 'var(--neon-orange)', down: 'var(--neon-green)', stable: 'var(--text-secondary)' };
            const icons = { up: 'fa-arrow-up', down: 'fa-arrow-down', stable: 'fa-minus' };

            container.innerHTML = intel.map(item => `
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid var(--glass-border);">
                    <div>
                        <div style="font-size: 13px; font-weight: 600;">${item.item}</div>
                        <div style="font-size: 11px; color: ${colors[item.trend]};">
                            <i class="fas ${icons[item.trend]}"></i> ${item.change} this week
                        </div>
                    </div>
                    <div style="font-family: 'Orbitron'; font-size: 14px; color: var(--neon-cyan);">${item.price}</div>
                </div>
            `).join('');
        }

        // ==================== STATS ANIMATION ====================
        function animateStats() {
            const targets = { statParts: 12847, statClients: 48 };
            Object.keys(targets).forEach(id => {
                const el = document.getElementById(id);
                if (!el) return;
                let current = 0;
                const target = targets[id];
                const increment = target / 50;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    el.textContent = Math.floor(current).toLocaleString();
                }, 30);
            });
        }

        // ==================== MODAL ====================
        function showPartDetail(partId) {
            const part = partsDatabase.find(p => p.id === partId);
            if (!part) return;

            document.getElementById('modalTitle').textContent = part.name;
            document.getElementById('modalBody').innerHTML = `
                <div style="text-align: center; margin-bottom: 20px;">
                    <div style="width: 120px; height: 120px; background: linear-gradient(135deg, rgba(0,240,255,0.1), rgba(184,41,255,0.1)); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; border: 1px solid var(--glass-border);">
                        <i class="fas ${part.image}" style="font-size: 48px; color: var(--neon-cyan);"></i>
                    </div>
                    <div style="font-family: 'Orbitron'; font-size: 24px; color: var(--neon-green); margin-bottom: 5px;">$${part.price.toLocaleString()}</div>
                    <div style="font-size: 12px; color: var(--text-secondary);">${part.condition} | ${part.cert}</div>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px;">
                    <div style="padding: 10px; background: rgba(0,0,0,0.3); border-radius: 8px;">
                        <div style="font-size: 10px; color: var(--text-secondary);">PART NUMBER</div>
                        <div style="font-family: monospace; font-size: 13px; color: var(--neon-cyan); cursor: pointer;" onclick="copyPartNumber('${part.number}')">${part.number} <i class="fas fa-copy"></i></div>
                    </div>
                    <div style="padding: 10px; background: rgba(0,0,0,0.3); border-radius: 8px;">
                        <div style="font-size: 10px; color: var(--text-secondary);">AIRCRAFT</div>
                        <div style="font-size: 13px; color: var(--text-primary);">${part.aircraft}</div>
                    </div>
                    <div style="padding: 10px; background: rgba(0,0,0,0.3); border-radius: 8px;">
                        <div style="font-size: 10px; color: var(--text-secondary);">LOCATION</div>
                        <div style="font-size: 13px; color: var(--text-primary);">${part.location}</div>
                    </div>
                    <div style="padding: 10px; background: rgba(0,0,0,0.3); border-radius: 8px;">
                        <div style="font-size: 10px; color: var(--text-secondary);">BLOCKCHAIN</div>
                        <div style="font-size: 11px; color: var(--neon-green); font-family: monospace;">${part.blockchain}</div>
                    </div>
                </div>
                <div style="font-size: 13px; line-height: 1.6; color: var(--text-secondary);">
                    This part has been verified through our blockchain traceability system. 
                    Full maintenance history, previous operators, and certification documents are available. 
                    AOG delivery available within 24 hours to any African airport.
                </div>
            `;
            document.getElementById('modal').classList.add('active');
        }

        function closeModal() {
            document.getElementById('modal').classList.remove('active');
        }

        // ==================== TOAST ====================
        function showToast(title, message) {
            const container = document.getElementById('toastContainer');
            const toast = document.createElement('div');
            toast.className = 'toast';
            toast.innerHTML = `
                <div class="toast-icon"><i class="fas fa-bell"></i></div>
                <div class="toast-content">
                    <div class="toast-title">${title}</div>
                    <div class="toast-message">${message}</div>
                </div>
            `;
            container.appendChild(toast);
            setTimeout(() => {
                toast.style.opacity = '0';
                setTimeout(() => toast.remove(), 400);
            }, 4000);
        }

        // ==================== DRAG AND DROP ====================
        const uploadZone = document.getElementById('uploadZone');
        if (uploadZone) {
            uploadZone.addEventListener('dragover', (e) => {
                e.preventDefault();
                uploadZone.classList.add('dragover');
            });
            uploadZone.addEventListener('dragleave', (e) => {
                e.preventDefault();
                uploadZone.classList.remove('dragover');
            });
            uploadZone.addEventListener('drop', (e) => {
                e.preventDefault();
                uploadZone.classList.remove('dragover');
                if (e.dataTransfer.files.length) {
                    document.getElementById('fileInput').files = e.dataTransfer.files;
                    handleImageUpload({ target: { files: e.dataTransfer.files } });
                }
            });
        }
    </script>
</body>
</html>'''

if __name__ == '__main__':
    print(HTML)