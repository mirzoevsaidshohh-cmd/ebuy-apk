#!/usr/bin/env python3
"""
Insert a high-specificity redesign <style> block before <script type="text/babel">
in vuslat.html.
"""

FILEPATH = "/home/user/ebuy-apk/vuslat.html"
MARKER   = '<script type="text/babel">'

CSS_BLOCK = '''<style id="vsl-pro-redesign">
/* ============================================================
   VUSLAT PRO REDESIGN  —  high-specificity override layer
   Prefix: html body #root .phone
   All declarations use !important to beat existing CSS
   ============================================================ */

/* ----------------------------------------------------------
   1. DESIGN TOKENS
   ---------------------------------------------------------- */
html body #root .phone {
  --vsl-blue:       #223F83 !important;
  --vsl-blue-light: #2A4FA0 !important;
  --vsl-blue-dark:  #1A3268 !important;
  --vsl-gold:       #C8A24A !important;
  --vsl-bg:         #F4F7FA !important;
  --vsl-white:      #FFFFFF !important;
  --vsl-text:       #0F172A !important;
  --vsl-body:       #405166 !important;
  --vsl-muted:      #6B7A90 !important;
  --vsl-line:       #E5E7EB !important;
  --vsl-success:    #0F766E !important;
  --vsl-danger:     #DC2626 !important;
  --vsl-r-xs:       8px   !important;
  --vsl-r-sm:       12px  !important;
  --vsl-r-md:       16px  !important;
  --vsl-r-lg:       20px  !important;
  --vsl-r-xl:       24px  !important;
  --vsl-shadow-xs:  0 1px 4px rgba(0,0,0,.06) !important;
  --vsl-shadow-sm:  0 2px 8px rgba(0,0,0,.08) !important;
  --vsl-shadow-md:  0 4px 16px rgba(0,0,0,.10) !important;
  --vsl-shadow-lg:  0 8px 28px rgba(0,0,0,.12) !important;
}

/* ----------------------------------------------------------
   2. KEYFRAME ANIMATIONS
   ---------------------------------------------------------- */
@keyframes vslFadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: none; }
}
@keyframes vslBounce {
  0%, 80%, 100% { transform: scale(.5); opacity: .4; }
  40%           { transform: scale(1);  opacity: 1;  }
}
@keyframes vslPulse {
  0%, 100% { opacity: 1; }
  50%      { opacity: .4; }
}
@keyframes vslShimmer {
  from { background-position: -200% center; }
  to   { background-position:  200% center; }
}
@keyframes vslSpring {
  0%   { transform: scale(1); }
  40%  { transform: scale(.92); }
  70%  { transform: scale(1.06); }
  100% { transform: scale(1); }
}
@keyframes vslOnlinePulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(34,197,94,.4); }
  50%      { box-shadow: 0 0 0 4px rgba(34,197,94,0); }
}

/* ----------------------------------------------------------
   3. AUTH SCREENS  (Welcome, Login, Register)
   ---------------------------------------------------------- */

/* ---- Welcome / white screen ---- */
html body #root .phone .welcome-white-screen {
  background: #FFFFFF !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  min-height: 100% !important;
  padding: 40px 24px !important;
}

/* ---- Auth outer screen ---- */
html body #root .phone .auth-v332-screen {
  background: linear-gradient(160deg, #EEF4FF 0%, #F8FAFF 50%, #FFFFFF 100%) !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  min-height: 100% !important;
  padding: 32px 16px 32px !important;
  overflow-y: auto !important;
}

/* ---- Auth card ---- */
html body #root .phone .auth-v332-card {
  background: #FFFFFF !important;
  border-radius: 28px !important;
  padding: 32px 24px 28px !important;
  width: 100% !important;
  max-width: 400px !important;
  box-shadow: 0 8px 40px rgba(34,63,131,.10), 0 2px 8px rgba(0,0,0,.04) !important;
  border: 1px solid rgba(34,63,131,.06) !important;
}

/* ---- Auth logo wrap ---- */
html body #root .phone .auth-v332-logo-wrap {
  display: flex !important;
  justify-content: center !important;
  margin-bottom: 20px !important;
}
html body #root .phone .auth-v332-logo {
  width: 80px !important;
  height: 80px !important;
  border-radius: 24px !important;
  box-shadow: 0 4px 16px rgba(34,63,131,.18) !important;
  object-fit: cover !important;
}

/* ---- Auth title ---- */
html body #root .phone .auth-v332-title {
  font-size: 26px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  text-align: center !important;
  margin-bottom: 6px !important;
  letter-spacing: -.4px !important;
}

/* ---- Auth tabs ---- */
html body #root .phone .auth-v332-tabs {
  display: flex !important;
  background: #F1F5F9 !important;
  border-radius: 14px !important;
  padding: 4px !important;
  margin-bottom: 22px !important;
  gap: 4px !important;
}
html body #root .phone .auth-v332-tab {
  flex: 1 !important;
  height: 40px !important;
  border-radius: 10px !important;
  border: none !important;
  background: transparent !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  color: #6B7A90 !important;
  cursor: pointer !important;
  transition: all 180ms ease !important;
}
html body #root .phone .auth-v332-tab.active,
html body #root .phone .auth-v332-tab[data-active="true"],
html body #root .phone .auth-v332-tab:focus {
  background: #FFFFFF !important;
  color: #223F83 !important;
  box-shadow: 0 1px 6px rgba(0,0,0,.10) !important;
}

/* ---- Auth form ---- */
html body #root .phone .auth-v332-form {
  display: flex !important;
  flex-direction: column !important;
  gap: 14px !important;
}

/* ---- Input label ---- */
html body #root .phone .auth-v332-label {
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #405166 !important;
  margin-bottom: 6px !important;
  display: block !important;
  letter-spacing: .1px !important;
}

/* ---- Input shell (wrapper) ---- */
html body #root .phone .auth-v332-input-shell {
  display: flex !important;
  align-items: center !important;
  height: 56px !important;
  min-height: 56px !important;
  border-radius: 16px !important;
  border: 1.5px solid #E5E7EB !important;
  background: #F8FAFF !important;
  padding: 0 16px !important;
  transition: border-color 200ms ease, box-shadow 200ms ease !important;
  position: relative !important;
  overflow: hidden !important;
}
html body #root .phone .auth-v332-input-shell:focus-within {
  border-color: #223F83 !important;
  box-shadow: 0 0 0 3px rgba(34,63,131,.12) !important;
  background: #FFFFFF !important;
}

/* ---- Phone prefix (country code) ---- */
html body #root .phone .auth-v332-prefix {
  font-size: 15px !important;
  font-weight: 600 !important;
  color: #0F172A !important;
  padding-right: 10px !important;
  border-right: 1.5px solid #E5E7EB !important;
  margin-right: 10px !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
}
html body #root .phone .auth-v332-phone-local {
  flex: 1 !important;
  border: none !important;
  background: transparent !important;
  outline: none !important;
  font-size: 15px !important;
  color: #0F172A !important;
}

/* ---- Input inside shell ---- */
html body #root .phone .auth-v332-input {
  flex: 1 !important;
  border: none !important;
  background: transparent !important;
  outline: none !important;
  font-size: 15px !important;
  color: #0F172A !important;
  width: 100% !important;
}
html body #root .phone .auth-v332-input::placeholder {
  color: #A0ABBB !important;
  font-weight: 400 !important;
}

/* ---- Submit button ---- */
html body #root .phone .auth-v332-submit {
  height: 56px !important;
  min-height: 56px !important;
  width: 100% !important;
  border-radius: 16px !important;
  border: none !important;
  background: #223F83 !important;
  color: #FFFFFF !important;
  font-size: 16px !important;
  font-weight: 700 !important;
  letter-spacing: .2px !important;
  cursor: pointer !important;
  transition: background 160ms ease, transform 120ms ease, box-shadow 160ms ease !important;
  margin-top: 4px !important;
}
html body #root .phone .auth-v332-submit:not(:disabled) {
  box-shadow: 0 4px 14px rgba(34,63,131,.28) !important;
}
html body #root .phone .auth-v332-submit:not(:disabled):active {
  transform: scale(.97) !important;
  box-shadow: 0 2px 8px rgba(34,63,131,.20) !important;
}
html body #root .phone .auth-v332-submit:disabled {
  background: #93A4C4 !important;
  cursor: not-allowed !important;
  box-shadow: none !important;
}

/* ---- Bottom switch link ---- */
html body #root .phone .auth-v332-bottom-switch {
  text-align: center !important;
  margin-top: 16px !important;
  font-size: 14px !important;
  color: #6B7A90 !important;
}
html body #root .phone .auth-v332-link {
  color: #223F83 !important;
  font-weight: 600 !important;
  text-decoration: none !important;
  cursor: pointer !important;
}

/* ---- Error / success messages ---- */
html body #root .phone .auth-v332-error {
  background: #FEF2F2 !important;
  border: 1px solid #FECACA !important;
  border-radius: 10px !important;
  padding: 10px 14px !important;
  font-size: 13px !important;
  color: #DC2626 !important;
  font-weight: 500 !important;
}
html body #root .phone .auth-v332-success {
  background: #F0FDF4 !important;
  border: 1px solid #BBF7D0 !important;
  border-radius: 10px !important;
  padding: 10px 14px !important;
  font-size: 13px !important;
  color: #0F766E !important;
  font-weight: 500 !important;
}

/* ----------------------------------------------------------
   4. HOME SCREEN
   ---------------------------------------------------------- */

/* ---- Outer shell ---- */
html body #root .phone .executive-shell {
  background: #F4F7FA !important;
  min-height: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  position: relative !important;
  overflow-x: hidden !important;
}

/* ---- Blue header / top bar ---- */
html body #root .phone .home-blue-top {
  background: linear-gradient(135deg, #1A3268 0%, #223F83 60%, #2A4FA0 100%) !important;
  padding: 16px 16px 20px !important;
  border-radius: 0 0 28px 28px !important;
  position: relative !important;
  z-index: 10 !important;
}

/* ---- Market / job carousel ---- */
html body #root .phone .market-carousel {
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
  padding: 16px 16px 24px !important;
}

/* ---- Vacancy card ---- */
html body #root .phone .vacancy-card-pro {
  background: #FFFFFF !important;
  border-radius: 22px !important;
  padding: 16px 16px 16px 20px !important;
  box-shadow: 0 2px 12px rgba(0,0,0,.07), 0 1px 3px rgba(0,0,0,.04) !important;
  border: 1px solid rgba(229,231,235,.6) !important;
  border-left: 4px solid #223F83 !important;
  position: relative !important;
  overflow: hidden !important;
  animation: vslFadeUp 320ms ease both !important;
}
html body #root .phone .vacancy-card-pro:nth-child(1) { animation-delay:  40ms !important; }
html body #root .phone .vacancy-card-pro:nth-child(2) { animation-delay:  90ms !important; }
html body #root .phone .vacancy-card-pro:nth-child(3) { animation-delay: 140ms !important; }
html body #root .phone .vacancy-card-pro:nth-child(4) { animation-delay: 190ms !important; }
html body #root .phone .vacancy-card-pro:nth-child(5) { animation-delay: 240ms !important; }
html body #root .phone .vacancy-card-pro:nth-child(n+6) { animation-delay: 280ms !important; }

html body #root .phone .vacancy-card-pro:active {
  transform: scale(.985) !important;
  box-shadow: 0 1px 6px rgba(0,0,0,.07) !important;
}

/* ---- Vacancy icon ---- */
html body #root .phone .vacancy-icon {
  width: 44px !important;
  height: 44px !important;
  border-radius: 12px !important;
  background: #EEF4FF !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
}

/* ---- Salary pill ---- */
html body #root .phone .salary-pill {
  background: #EEF4FF !important;
  color: #223F83 !important;
  border-radius: 8px !important;
  padding: 4px 10px !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  white-space: nowrap !important;
}

/* ---- Vacancy action button ---- */
html body #root .phone .vacancy-btn {
  background: #223F83 !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 12px !important;
  padding: 9px 18px !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  cursor: pointer !important;
  transition: background 150ms ease, transform 120ms ease !important;
}
html body #root .phone .vacancy-btn:active {
  background: #1A3268 !important;
  transform: scale(.96) !important;
}

/* ---- Vacancy info grid ---- */
html body #root .phone .vacancy-info-grid {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 6px !important;
  margin-top: 10px !important;
}
html body #root .phone .vacancy-info-item {
  display: flex !important;
  align-items: center !important;
  gap: 5px !important;
  font-size: 12px !important;
  color: #6B7A90 !important;
}

/* ---- Vacancy footer ---- */
html body #root .phone .vacancy-footer {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  margin-top: 12px !important;
  padding-top: 10px !important;
  border-top: 1px solid #F1F5F9 !important;
}

/* ---- Vacancy status badge ---- */
html body #root .phone .vacancy-status {
  display: inline-flex !important;
  align-items: center !important;
  gap: 4px !important;
  padding: 3px 10px !important;
  border-radius: 20px !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  background: #F0FDF4 !important;
  color: #0F766E !important;
}

/* ----------------------------------------------------------
   5. BOTTOM NAVIGATION
   ---------------------------------------------------------- */
html body #root .phone .bottom-nav-clean {
  position: fixed !important;
  bottom: 0 !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: 100% !important;
  max-width: 430px !important;
  z-index: 100 !important;
  padding: 0 !important;
}
html body #root .phone .bottom-nav-card {
  background: #FFFFFF !important;
  box-shadow: 0 -2px 16px rgba(0,0,0,.08), 0 -1px 4px rgba(0,0,0,.04) !important;
  border-radius: 20px 20px 0 0 !important;
  display: flex !important;
  align-items: stretch !important;
  padding: 6px 4px calc(6px + env(safe-area-inset-bottom)) !important;
}

html body #root .phone .bottom-nav-item {
  flex: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 3px !important;
  padding: 6px 2px !important;
  border-radius: 12px !important;
  cursor: pointer !important;
  transition: background 160ms ease, transform 120ms ease !important;
  border: none !important;
  background: transparent !important;
  min-height: 52px !important;
}
html body #root .phone .bottom-nav-item:active {
  transform: scale(.92) !important;
  background: #F1F5F9 !important;
  animation: vslSpring 300ms ease forwards !important;
}
html body #root .phone .bottom-nav-item.active {
  background: #EEF4FF !important;
}

html body #root .phone .bottom-nav-icon {
  width: 24px !important;
  height: 24px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  color: #6B7A90 !important;
  transition: color 160ms ease !important;
}
html body #root .phone .bottom-nav-item.active .bottom-nav-icon {
  color: #223F83 !important;
}

html body #root .phone .bottom-nav-icon svg {
  transition: transform 260ms cubic-bezier(.34,1.56,.64,1) !important;
  width: 22px !important;
  height: 22px !important;
}
html body #root .phone .bottom-nav-item.active .bottom-nav-icon svg {
  transform: scale(1.15) translateY(-1px) !important;
}

html body #root .phone .bottom-nav-label {
  font-size: 10px !important;
  font-weight: 600 !important;
  color: #A0ABBB !important;
  line-height: 1.2 !important;
  letter-spacing: .1px !important;
  transition: color 160ms ease !important;
}
html body #root .phone .bottom-nav-item.active .bottom-nav-label {
  color: #223F83 !important;
}

/* ----------------------------------------------------------
   6. AI ASSISTANT
   ---------------------------------------------------------- */

/* ---- AI page wrapper ---- */
html body #root .phone .ai-page {
  display: flex !important;
  flex-direction: column !important;
  height: 100% !important;
  min-height: 100% !important;
  background: #F8FAFF !important;
  position: relative !important;
  overflow: hidden !important;
}

/* ---- AI header ---- */
html body #root .phone .ai-header {
  background: #FFFFFF !important;
  border-bottom: 1px solid #E5E7EB !important;
  padding: 12px 16px !important;
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  flex-shrink: 0 !important;
  box-shadow: 0 1px 4px rgba(0,0,0,.05) !important;
  z-index: 10 !important;
}

/* ---- AI orb / avatar in header ---- */
html body #root .phone .ai-orb {
  width: 42px !important;
  height: 42px !important;
  border-radius: 50% !important;
  background: linear-gradient(135deg, #223F83 0%, #2A4FA0 100%) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
  box-shadow: 0 2px 8px rgba(34,63,131,.28) !important;
}

/* ---- AI title block ---- */
html body #root .phone .ai-title-block {
  flex: 1 !important;
  min-width: 0 !important;
}
html body #root .phone .ai-title-block > *:first-child {
  font-size: 16px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  line-height: 1.3 !important;
  display: block !important;
}

/* ---- Status row ---- */
html body #root .phone .ai-status-row {
  display: flex !important;
  align-items: center !important;
  gap: 5px !important;
  margin-top: 2px !important;
}
html body #root .phone .ai-online-dot {
  width: 8px !important;
  height: 8px !important;
  border-radius: 50% !important;
  background: #22C55E !important;
  flex-shrink: 0 !important;
  animation: vslOnlinePulse 2s ease infinite !important;
}
html body #root .phone .ai-status-text {
  font-size: 12px !important;
  color: #6B7A90 !important;
  font-weight: 500 !important;
}

/* ---- Thread (message list) ---- */
html body #root .phone .ai-thread {
  flex: 1 !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  padding: 16px 14px 160px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
  scroll-behavior: smooth !important;
  -webkit-overflow-scrolling: touch !important;
}

/* ---- Message row base ---- */
html body #root .phone .ai-message-row {
  display: flex !important;
  align-items: flex-end !important;
  gap: 8px !important;
  animation: vslFadeUp 220ms ease both !important;
}

/* ---- User message row (right-aligned) ---- */
html body #root .phone .ai-message-row-user,
html body #root .phone .ai-message-row.user {
  justify-content: flex-end !important;
  flex-direction: row-reverse !important;
}

/* ---- Assistant message row (left-aligned) ---- */
html body #root .phone .ai-message-row-assistant,
html body #root .phone .ai-message-row.assistant {
  justify-content: flex-start !important;
  flex-direction: row !important;
}

/* ---- Message bubble base ---- */
html body #root .phone .ai-message {
  padding: 11px 14px !important;
  border-radius: 18px !important;
  font-size: 14px !important;
  line-height: 1.55 !important;
  max-width: 82% !important;
  word-break: break-word !important;
  position: relative !important;
}

/* ---- User bubble ---- */
html body #root .phone .ai-message.user {
  background: #223F83 !important;
  color: #FFFFFF !important;
  max-width: 78% !important;
  border-radius: 18px 18px 4px 18px !important;
  box-shadow: 0 2px 8px rgba(34,63,131,.22) !important;
}

/* ---- Assistant bubble ---- */
html body #root .phone .ai-message.assistant {
  background: #FFFFFF !important;
  color: #0F172A !important;
  max-width: 82% !important;
  border-radius: 4px 18px 18px 18px !important;
  border: 1px solid #E5E7EB !important;
  box-shadow: 0 1px 6px rgba(0,0,0,.06) !important;
}

/* ---- Message text ---- */
html body #root .phone .ai-message-text {
  font-size: 14px !important;
  line-height: 1.55 !important;
}

/* ---- AI avatar (small circle beside bubble) ---- */
html body #root .phone .ai-avatar {
  width: 32px !important;
  height: 32px !important;
  border-radius: 50% !important;
  background: linear-gradient(135deg, #223F83 0%, #2A4FA0 100%) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
  font-size: 14px !important;
  color: #FFFFFF !important;
  box-shadow: 0 2px 6px rgba(34,63,131,.22) !important;
  align-self: flex-end !important;
}

/* ---- Follow-up chips ---- */
html body #root .phone .ai-followups {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 6px !important;
  padding: 0 14px !important;
}
html body #root .phone .ai-followup {
  background: #FFFFFF !important;
  border: 1.5px solid #E2E8F0 !important;
  border-radius: 20px !important;
  padding: 7px 14px !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  color: #223F83 !important;
  cursor: pointer !important;
  transition: background 150ms ease, border-color 150ms ease !important;
  white-space: nowrap !important;
}
html body #root .phone .ai-followup:active {
  background: #EEF4FF !important;
  border-color: #223F83 !important;
}

/* ---- Suggestion chips ---- */
html body #root .phone .ai-suggestions {
  display: flex !important;
  flex-direction: column !important;
  gap: 8px !important;
  padding: 8px 14px !important;
}
html body #root .phone .ai-suggestion {
  background: #FFFFFF !important;
  border: 1.5px solid #E2E8F0 !important;
  border-radius: 14px !important;
  padding: 12px 14px !important;
  font-size: 14px !important;
  color: #223F83 !important;
  cursor: pointer !important;
  text-align: left !important;
  transition: background 150ms ease, border-color 150ms ease !important;
}
html body #root .phone .ai-suggestion:active {
  background: #EEF4FF !important;
  border-color: #223F83 !important;
}

/* ---- Typing indicator ---- */
html body #root .phone .ai-typing {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
}
html body #root .phone .ai-typing-dots {
  display: flex !important;
  align-items: center !important;
  gap: 4px !important;
  background: #FFFFFF !important;
  border: 1px solid #E5E7EB !important;
  border-radius: 18px !important;
  padding: 11px 16px !important;
  box-shadow: 0 1px 6px rgba(0,0,0,.06) !important;
}
html body #root .phone .ai-typing-dots > span {
  width: 8px !important;
  height: 8px !important;
  border-radius: 50% !important;
  background: #93A4C4 !important;
  display: block !important;
  animation: vslBounce 1.2s infinite ease !important;
}
html body #root .phone .ai-typing-dots > span:nth-child(1) { animation-delay: 0ms !important; }
html body #root .phone .ai-typing-dots > span:nth-child(2) { animation-delay: 160ms !important; }
html body #root .phone .ai-typing-dots > span:nth-child(3) { animation-delay: 320ms !important; }

/* ---- Composer wrapper (fixed at bottom) ---- */
html body #root .phone .ai-composer-wrap {
  position: absolute !important;
  bottom: 0 !important;
  left: 0 !important;
  right: 0 !important;
  background: #F8FAFF !important;
  padding: 10px 12px calc(10px + env(safe-area-inset-bottom)) !important;
  z-index: 20 !important;
  border-top: 1px solid #E5E7EB !important;
}

/* ---- Composer inner card ---- */
html body #root .phone .ai-composer {
  display: flex !important;
  align-items: flex-end !important;
  gap: 8px !important;
  background: #FFFFFF !important;
  border: 1.5px solid #E5E7EB !important;
  border-radius: 22px !important;
  padding: 8px 8px 8px 14px !important;
  box-shadow: 0 2px 10px rgba(0,0,0,.06) !important;
  transition: border-color 200ms ease !important;
}
html body #root .phone .ai-composer:focus-within {
  border-color: #223F83 !important;
  box-shadow: 0 2px 10px rgba(34,63,131,.10) !important;
}

/* ---- Composer textarea / input ---- */
html body #root .phone .ai-input {
  flex: 1 !important;
  border: none !important;
  background: transparent !important;
  outline: none !important;
  font-size: 15px !important;
  color: #0F172A !important;
  resize: none !important;
  min-height: 24px !important;
  max-height: 120px !important;
  line-height: 1.5 !important;
  overflow-y: auto !important;
  padding: 0 !important;
}
html body #root .phone .ai-input::placeholder {
  color: #A0ABBB !important;
}

/* ---- Send button ---- */
html body #root .phone .ai-send {
  width: 38px !important;
  height: 38px !important;
  border-radius: 50% !important;
  border: none !important;
  background: #223F83 !important;
  color: #FFFFFF !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  flex-shrink: 0 !important;
  transition: background 150ms ease, transform 120ms ease !important;
  box-shadow: 0 2px 8px rgba(34,63,131,.25) !important;
}
html body #root .phone .ai-send:active {
  background: #1A3268 !important;
  transform: scale(.92) !important;
}
html body #root .phone .ai-send:disabled {
  background: #C4CEDE !important;
  box-shadow: none !important;
  cursor: not-allowed !important;
}

/* ---- Copy / action buttons near messages ---- */
html body #root .phone .ai-copy {
  background: transparent !important;
  border: none !important;
  cursor: pointer !important;
  padding: 4px !important;
  border-radius: 6px !important;
  color: #6B7A90 !important;
  transition: color 150ms ease, background 150ms ease !important;
}
html body #root .phone .ai-copy:hover {
  color: #223F83 !important;
  background: #EEF4FF !important;
}
html body #root .phone .ai-actions {
  display: flex !important;
  gap: 4px !important;
  margin-top: 4px !important;
}

/* ----------------------------------------------------------
   7. PROFILE SCREEN
   ---------------------------------------------------------- */

/* ---- Profile page wrapper ---- */
html body #root .phone .profile-v107-page {
  background: #F4F7FA !important;
  min-height: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  overflow-x: hidden !important;
}

/* ---- Hero header ---- */
html body #root .phone .profile-final-hero {
  background: linear-gradient(135deg, #1A3268 0%, #223F83 60%, #2A4FA0 100%) !important;
  padding: 40px 20px 32px !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  border-radius: 0 0 32px 32px !important;
  position: relative !important;
  overflow: hidden !important;
}
html body #root .phone .profile-final-hero::before {
  content: '' !important;
  position: absolute !important;
  top: -30px !important;
  right: -30px !important;
  width: 140px !important;
  height: 140px !important;
  border-radius: 50% !important;
  background: rgba(200,162,74,.12) !important;
  pointer-events: none !important;
}
html body #root .phone .profile-final-hero::after {
  content: '' !important;
  position: absolute !important;
  bottom: -20px !important;
  left: -20px !important;
  width: 100px !important;
  height: 100px !important;
  border-radius: 50% !important;
  background: rgba(255,255,255,.05) !important;
  pointer-events: none !important;
}

/* ---- Avatar ---- */
html body #root .phone .profile-final-avatar {
  width: 88px !important;
  height: 88px !important;
  border-radius: 50% !important;
  border: 3px solid rgba(255,255,255,.85) !important;
  box-shadow: 0 4px 16px rgba(0,0,0,.22) !important;
  object-fit: cover !important;
  margin-bottom: 14px !important;
  position: relative !important;
  z-index: 1 !important;
}

/* ---- Profile name ---- */
html body #root .phone .profile-final-name {
  font-size: 22px !important;
  font-weight: 700 !important;
  color: #FFFFFF !important;
  margin-bottom: 4px !important;
  letter-spacing: -.3px !important;
  position: relative !important;
  z-index: 1 !important;
}

/* ---- Subtitle / welcome ---- */
html body #root .phone .profile-final-welcome {
  font-size: 14px !important;
  color: rgba(255,255,255,.72) !important;
  font-weight: 400 !important;
  position: relative !important;
  z-index: 1 !important;
}

/* ---- Profile ID badge ---- */
html body #root .phone .profile-final-id {
  margin-top: 10px !important;
  background: rgba(255,255,255,.15) !important;
  border: 1px solid rgba(255,255,255,.25) !important;
  border-radius: 20px !important;
  padding: 4px 14px !important;
  font-size: 12px !important;
  color: rgba(255,255,255,.85) !important;
  font-weight: 500 !important;
  letter-spacing: .5px !important;
  position: relative !important;
  z-index: 1 !important;
}

/* ---- Timeline ---- */
html body #root .phone .profile-v107-timeline {
  padding: 20px 16px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0 !important;
  position: relative !important;
}

/* ---- Timeline step ---- */
html body #root .phone .profile-v107-timeline-step {
  display: flex !important;
  align-items: flex-start !important;
  gap: 14px !important;
  position: relative !important;
  padding-bottom: 20px !important;
  animation: vslFadeUp 320ms ease both !important;
}
html body #root .phone .profile-v107-timeline-step:nth-child(1) { animation-delay:  60ms !important; }
html body #root .phone .profile-v107-timeline-step:nth-child(2) { animation-delay: 110ms !important; }
html body #root .phone .profile-v107-timeline-step:nth-child(3) { animation-delay: 160ms !important; }
html body #root .phone .profile-v107-timeline-step:nth-child(4) { animation-delay: 210ms !important; }
html body #root .phone .profile-v107-timeline-step:nth-child(n+5) { animation-delay: 260ms !important; }

html body #root .phone .profile-v107-timeline-step::after {
  content: '' !important;
  position: absolute !important;
  left: 15px !important;
  top: 28px !important;
  bottom: 0 !important;
  width: 2px !important;
  background: #E5E7EB !important;
}
html body #root .phone .profile-v107-timeline-step:last-child::after {
  display: none !important;
}

/* ---- Profile card / menu item ---- */
html body #root .phone .profile-v107-card {
  background: #FFFFFF !important;
  border-radius: 16px !important;
  box-shadow: 0 1px 6px rgba(0,0,0,.06) !important;
  border: 1px solid #F1F5F9 !important;
  overflow: hidden !important;
  margin: 0 16px 12px !important;
}

/* ----------------------------------------------------------
   8. ANKETA / FORM SCREEN
   ---------------------------------------------------------- */

/* ---- Anketa page ---- */
html body #root .phone .anketa-page {
  background: #F4F7FA !important;
  min-height: 100% !important;
  display: flex !important;
  flex-direction: column !important;
}

/* ---- Anketa header ---- */
html body #root .phone .anketa-header {
  background: linear-gradient(135deg, #1A3268 0%, #223F83 100%) !important;
  padding: 20px 16px 24px !important;
  border-radius: 0 0 28px 28px !important;
  color: #FFFFFF !important;
}

/* ---- Anketa title ---- */
html body #root .phone .anketa-title {
  font-size: 20px !important;
  font-weight: 700 !important;
  color: #FFFFFF !important;
  margin-bottom: 4px !important;
  letter-spacing: -.2px !important;
}

/* ---- Progress bar ---- */
html body #root .phone .anketa-progress {
  height: 6px !important;
  background: rgba(255,255,255,.25) !important;
  border-radius: 3px !important;
  margin-top: 14px !important;
  overflow: hidden !important;
}
html body #root .phone .anketa-progress-fill {
  height: 100% !important;
  background: #C8A24A !important;
  border-radius: 3px !important;
  transition: width 400ms cubic-bezier(.4,0,.2,1) !important;
}

/* ---- Anketa card ---- */
html body #root .phone .anketa-card {
  background: #FFFFFF !important;
  border-radius: 20px !important;
  padding: 20px !important;
  margin: 12px 16px !important;
  box-shadow: 0 2px 10px rgba(0,0,0,.06) !important;
  border: 1px solid #F1F5F9 !important;
}

/* ---- Anketa section header ---- */
html body #root .phone .anketa-section {
  font-size: 13px !important;
  font-weight: 700 !important;
  color: #223F83 !important;
  text-transform: uppercase !important;
  letter-spacing: .6px !important;
  margin-bottom: 12px !important;
  padding-bottom: 8px !important;
  border-bottom: 2px solid #EEF4FF !important;
}

/* ----------------------------------------------------------
   9. QUIZ SCREEN
   ---------------------------------------------------------- */

/* ---- Quiz page ---- */
html body #root .phone .quiz-page {
  background: #F4F7FA !important;
  min-height: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  padding: 0 !important;
}

/* ---- Quiz choice button (default) ---- */
html body #root .phone .quiz-choice-btn {
  display: flex !important;
  align-items: center !important;
  width: 100% !important;
  padding: 14px 16px !important;
  border-radius: 14px !important;
  border: 1.5px solid #E5E7EB !important;
  background: #FFFFFF !important;
  color: #0F172A !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  cursor: pointer !important;
  transition: background 150ms ease, border-color 150ms ease, transform 120ms ease !important;
  text-align: left !important;
  margin-bottom: 8px !important;
}
html body #root .phone .quiz-choice-btn:active {
  transform: scale(.98) !important;
}

/* ---- Quiz choice selected ---- */
html body #root .phone .quiz-choice-btn.is-selected {
  background: #EEF4FF !important;
  border-color: #223F83 !important;
  color: #223F83 !important;
  font-weight: 600 !important;
  box-shadow: 0 0 0 3px rgba(34,63,131,.08) !important;
}

/* ---- Quiz result card ---- */
html body #root .phone .quiz-result-card {
  background: #FFFFFF !important;
  border-radius: 24px !important;
  padding: 28px 24px !important;
  margin: 16px !important;
  box-shadow: 0 4px 20px rgba(0,0,0,.08) !important;
  border: 1px solid #F1F5F9 !important;
  text-align: center !important;
  animation: vslFadeUp 300ms ease both !important;
}

/* ----------------------------------------------------------
   10. GLOBAL UTILITY OVERRIDES
   ---------------------------------------------------------- */

/* Smooth scrolling and safe area for all scrollable panes */
html body #root .phone [class*="-thread"],
html body #root .phone [class*="-scroll"],
html body #root .phone [class*="-list"] {
  -webkit-overflow-scrolling: touch !important;
  scroll-behavior: smooth !important;
}

/* Generic section title used in many screens */
html body #root .phone .section-title,
html body #root .phone [class*="section-title"] {
  font-size: 17px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  letter-spacing: -.2px !important;
  margin-bottom: 10px !important;
}

/* Ensure phone container clips overflow */
html body #root .phone {
  overflow: hidden !important;
  position: relative !important;
}

/* Safe-area bottom padding for scrollable content pages */
html body #root .phone .executive-shell,
html body #root .phone .ai-page,
html body #root .phone .profile-v107-page,
html body #root .phone .anketa-page,
html body #root .phone .quiz-page {
  padding-bottom: env(safe-area-inset-bottom) !important;
}

/* ----------------------------------------------------------
   11. RESPONSIVE TWEAKS
   ---------------------------------------------------------- */
@media (max-height: 700px) {
  html body #root .phone .auth-v332-screen {
    padding-top: max(12px, env(safe-area-inset-top)) !important;
  }
  html body #root .phone .auth-v332-card {
    padding: 20px !important;
    border-radius: 22px !important;
  }
  html body #root .phone .auth-v332-input-shell,
  html body #root .phone .auth-v332-submit {
    min-height: 50px !important;
    height: 50px !important;
  }
}

@media (min-width: 400px) {
  html body #root .phone .ai-message.user  { max-width: 74% !important; }
  html body #root .phone .ai-message.assistant { max-width: 78% !important; }
}

</style>
'''

def main():
    with open(FILEPATH, "r", encoding="utf-8") as f:
        content = f.read()

    if 'id="vsl-pro-redesign"' in content:
        print("⚠️  vsl-pro-redesign block already present — replacing it.")
        import re
        content = re.sub(
            r'<style id="vsl-pro-redesign">.*?</style>\s*',
            '',
            content,
            flags=re.DOTALL
        )

    idx = content.find(MARKER)
    if idx == -1:
        print("ERROR: Could not find marker:", MARKER)
        return

    new_content = content[:idx] + CSS_BLOCK + content[idx:]

    with open(FILEPATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Done. File written: {FILEPATH}")
    print(f"New file size: {len(new_content):,} bytes")
    print(f"CSS block size: {len(CSS_BLOCK):,} bytes")
    print(f"Style block present: {'vsl-pro-redesign' in new_content}")

if __name__ == "__main__":
    main()
