#!/usr/bin/env python3
"""
WP / Telegram Number Seller Bot — v9.40 (MANAGE REFUND: CHEK NUMBER & REFUND - one-tap bulk check+refund: paste numbers line-by-line, every number is checked for its current owner, its refund history and its OTP arrival (DB + a second LIVE probe) and the buyer is refunded EXACTLY what he paid, all through the same atomic zero-loss spine as Refund Send; Sell Number Send fully removed including its code; v9.39 REAL-DEPOSIT-ONLY All User Balance intact: live money screen now counts ONLY real deposit money - any balance ever modified from the admin panel is EXCLUDED from every tier and every total (admin money is not a real deposit) and is shown separately on a shield line instead; everything else of v9.38 ALL USER BALANCE intact - users ABOVE $100 and ABOVE $50 are listed SEPARATELY one-by-one and are NEVER merged into the combined figure, the rest is one combined live total, the Refresh button re-reads the DB fresh every time - zero cache; v9.37 BULLETPROOF PREMIUM EMOJI + usa.py intact (cooldown+heal design: NOTHING can turn premium off permanently), v9.36 SELF-HEAL + FAILSAFE START, v9.35 EXACT AMOUNTS, v9.34 MENU RESHAPE + BULK MANAGE, v9.33 SILENT BOOT and v9.32 BINANCE PAY intact)
======================================================

WHAT'S NEW IN v9.40 (MANAGE REFUND: CHEK NUMBER & REFUND + SELL NUMBER SEND REMOVED)
1. OWNER ORDER: "manage refund ke ander ek button add karo -
   Chek Number & Refund. Isme mai line by line number duga; ye
   number kiske pass hai, pahle kabhi refund hua ya nahi, otp
   aaya hai ya nahi - nahi aaya hoga to utna refund jitna buy
   kiya tha. Sahi se loss na ho mera." + "Sell Number Send
   button remove kar do fully - code se bhi cleanup."
2. THE NEW TOOL (Admin Panel -> Manage Refund -> "Chek Number
   & Refund"): paste numbers line-by-line (or a .txt) - one
   worker-pool run checks EVERY number and refunds the eligible
   ones in the SAME pass, live progress bar + full report card.
3. THE CHECK CHAIN (per number, exactly the owner's order):
   current owner lookup (phone match tries +/- variants) ->
   refund history (a refunded row is dead + data-wiped and can
   never match again) -> OTP arrived? (DB code + a SECOND LIVE
   provider probe before any money moves) -> refund = what the
   buyer ACTUALLY paid (order price, rate fallback) + instant
   user notification + pending referral commission cancelled.
4. ZERO-LOSS BY CONSTRUCTION (same spine as Refund Send): the
   refund is an ATOMIC guard that wins only while the row is
   still sold AND OTP-free; the OTP claim path refuses refunded
   rows so a buyer can never hold BOTH the OTP and the refund;
   refunded data is wiped (re-sending the same numbers is a
   mathematical no-op); an 'unknown' provider answer moves NO
   money (re-run later).
5. SELL NUMBER SEND fully removed: button, Old/New inline
   batches, 3-take/pin/cursor machinery, batch settings and the
   callback handler registration - ALL gone; its keyboard slot
   now hosts the new tool (same premium icon ID). The hub
   report is renumbered to the three live tools.
6. Everything else (v9.39 real-deposit-only All User Balance,
   v9.37 bulletproof premium emoji, v9.36 self-heal + failsafe
   start, v9.35 exact amounts, v9.34 menu reshape + Bulk
   Manage, v9.33 silent boot, v9.32 Binance Pay) untouched.

WHAT'S NEW IN v9.39 (ALL USER BALANCE = REAL DEPOSIT ONLY)
1. OWNER ORDER: "baisa balance add nahi hoga jiska admin panel se
   modify keya hua hoga - jo real me deposit kar ke balance bala
   hai uska batayega."
2. THE RULE: any balance ever written through the admin panel
   (Modify User -> Balance: Set / Add / Deduct) marks that user
   adm_modified=1 (one DB column, safe auto-add on old DBs). The
   All User Balance screen EXCLUDES those users from EVERY tier
   and EVERY total - that is admin money, not a real deposit.
3. THE SCREEN: same live card, real money only - header says REAL
   DEPOSIT, a shield line shows exactly how many admin-modified
   users and how much money was kept OUT (nothing hidden), the
   tier/total math is unchanged, GRAND TOTAL is now the
   real-deposit users total, and a footer line states the rule.
4. SINGLE CHOKE POINT: set_balance() is the only admin balance
   write path (audited) - the flag can never be forgotten. Real
   deposits (Binance auto + manual confirm), refunds and referral
   payouts still count as real money; purchases still spend it
   normally. Excluded figures are live too (fresh DB read).
5. Everything else (v9.38 All User Balance screen + Refresh,
   v9.37 bulletproof premium emoji, v9.36 self-heal + failsafe
   start, v9.35 exact amounts, v9.34 menu reshape + Bulk Manage,
   v9.33 silent boot, v9.32 Binance Pay) untouched.

WHAT'S NEW IN v9.38 (ADMIN: ALL USER BALANCE - LIVE MONEY SCREEN)
1. OWNER ORDER: "admin panel me All User Balance button add karo -
   click karne pe jitne bhi user hai bot pe, sare ka balance EK SATH
   dikhega; jo user $100 se jayda ya $50 se jayda hai wo ALAG dikhega
   aur combined figure me add nahi hoga; baki sab ka live combined
   total + sare user ka total dollar me."
2. THE BUTTON: new full-width row on the admin panel (under Set
   Wallet / Total Deposit): "💵 All User Balance" (owner-pack premium
   icon, live ID from the same pack as the whole panel).
3. THE SCREEN (one tap, everything at once):
   - RED ABOVE $100 holders: listed ONE BY ONE (user id + amount,
     high->low, banned users flagged with a ban-mark) + subtotal;
   - YELLOW $50-$100 holders: listed the same way + subtotal;
   - holders-ka-total is printed SEPARATELY with an explicit "NOT
     added in the combined figure" note (the owner rule);
   - GREEN ALL REST (<= $50): ONE combined live figure - the "baki
     all live balance" number, no per-user dump;
   - COMBINED (without above-$50 holders) AND GRAND TOTAL (every
     user) both printed - nothing hidden anywhere.
4. LIVE BY DESIGN: every tap AND the Refresh button re-read the DB
   fresh (zero cache, zero stale numbers). Screen keyboard = Refresh
   + Admin Panel back. Banned users' money still counts (it is real
   money in the DB) - they are just flagged in the lists.
5. BOUNDARY + SIZE SAFE: "se jayda" = strictly more ($100.00 sits in
   the $50-$100 tier, $50.00 sits in the rest) with the 1e-6 money
   epsilon killing float noise; lists capped at 25 per tier with an
   honest "+N more" note, so the card can NEVER blow the 4096-char
   Telegram limit no matter how many users exist.
6. Everything else (v9.37 bulletproof premium emoji + usa.py, v9.36
   self-heal + failsafe start, v9.35 exact amounts, v9.34 menu
   reshape + Bulk Manage, v9.33 silent boot, v9.32 Binance Pay)
   untouched.

WHAT'S NEW IN v9.37 (NOTHING CAN KILL PREMIUM EMOJIS ANYMORE + usa.py)
1. OWNER REPORT: "sare premium emoji hatt gaye, ek bhi nahi dhik
   rahe". LIVE-API DIAGNOSIS (real Telegram, zero guessing): all 47
   premium IDs are ALIVE, a <tg-emoji> send is accepted with the
   custom_emoji entities coming back INTACT, icon buttons and edits
   are accepted. Telegram-side is 100% healthy -> the remaining
   killers were in-code state flips, and they are GONE now:
   - BUTTON ICONS: one runtime rejection used to flip _BICONS_ACTIVE
     OFF PERMANENTLY (until a restart) - from that single event every
     menu in the bot lost its premium icon. Now a rejection only
     opens the same 10-MIN COOLDOWN as the message layer.
   - MESSAGE LAYER: ANY rejection of a premium-tagged text used to
     cool the WHOLE layer for 30 min - unrelated errors (chat,
     markup, flood) could keep it hot forever = "sare emoji hatt
     gaye". Now ONLY emoji/entity/parse-caused rejections cool the
     layer (10 min); every other error strips that one message and
     leaves premium untouched for everyone else.
   - HEAL LOOP (every 10 min, read-only): a healthy probe now
     REVIVES EVERYTHING - message layer AND button icons leave their
     cooldowns immediately. Premium self-restores mid-run: no
     restart, no waiting, no permanent state anywhere.
   - cooldown 30 min -> 10 min (faster recovery everywhere).
2. BROADCAST: the same-to-same copy_message engine is unchanged.
3. START FAILSAFE: unchanged - a handler crash can never silence a
   user; the plain menu is always delivered.
4. MAIN FILE RENAME (owner request): the main file is now usa.py
   (bot_v9.py remains as a byte-identical build/test alias).
5. Everything else (v9.36 self-heal + failsafe + gate repair, v9.35
   exact amounts + balance epsilon, v9.34 menu reshape + Bulk
   Manage, v9.33 silent boot, v9.32 Binance Pay) untouched.

WHAT'S NEW IN v9.36 (SELF-HEALING EMOJI + FAILSAFE START + GATE REPAIR)
1. PREMIUM EMOJI NEVER PERMANENTLY OFF AGAIN (owner: "ek baar fix
   kiya tha, 2 din baad phir se normal ho gaya"): the old design
   flipped the WHOLE layer OFF on ONE dead ID at boot or ONE runtime
   rejection - only a restart ever brought it back. Now:
   - a dead/rotated ID is pruned ALONE (the rest of the pack stays
     premium - per-ID graveyard);
   - a rejected send opens a 30-MIN COOLDOWN, then premium is
     retried automatically - no restart, no permanent state;
   - a 30-min READ-ONLY heal loop re-probes every ID while the bot
     runs: IDs that come back are revived instantly (owner renewed
     Premium / pack restored -> layer self-restores within 30 min).
2. START CAN NEVER GO SILENT (owner: "100 me se 40 user ka crash -
   start ho nahi hota, kuch kaam nahi karta"): the old safety net
   only matched parse/entity rejections, so a raw CUSTOM_EMOJI_INVALID
   crashed the handler AND the error card (it carried the same tags)
   -> user saw NOTHING. Now:
   - _pem_send strips and retries on ANY rejection of a tagged text -
     the message itself is never lost to a premium tag;
   - every user-facing handler (start, menu, language, help, text
     router, media, all user callbacks) runs inside _failsafe: if the
     real screen dies for ANY reason, the user still gets a plain
     no-HTML, no-icon menu that Telegram's parser cannot reject;
   - the error card itself has a stripped plain-text fallback.
3. ZERO-SEND STRIP DETECTOR: after each real send of a tagged text
   the returned Message is checked - if Telegram silently stripped
   the premium entities (bot eligibility), a cooldown opens and ONE
   journalctl line names it. Owners can see exactly why emojis look
   normal (Fragment username / owner Premium eligibility) without
   any test message being sent.
4. FORCE-JOIN GATE REPAIR: a managed chat the bot can no longer see
   (kicked/deleted) used to lock users on the join screen FOREVER.
   Boot probe (read-only) + verify-button double-check now mark such
   chats broken and the gate auto-passes them - users can never be
   trapped by a dead channel again.
5. BROADCAST: the same-to-same copy engine is unchanged (copy_message
   IS the maximum-fidelity send); a diagnostic log line now reports
   when a broadcast source carries premium entities so flattening is
   always explainable from journalctl.
6. Everything else (v9.35 exact amounts + balance epsilon, v9.34
   menu reshape + Bulk Manage, v9.33 silent boot, v9.32 Binance Pay)
   untouched.

WHAT'S NEW IN v9.35 (EXACT DEPOSIT AMOUNTS + BALANCE EPSILON FIX)
1. DEPOSIT 0.31 BUG FIXED (owner: "0.3 select karta to 0.31 deposit
   karne bol raha hai - 0.30 hi ho, koi bhi binance me ya kahi
   bhi"): Binance Pay orders now charge EXACTLY the picked amount.
   The v9.32 unique-cent bump (+$0.01 steps) is RETIRED - the card
   shows 0.30 and 0.30 is what the user pays, everywhere.
2. ORDER-ID MATCH FIXED (owner: "order id to 0.30 ka hai lekin
   match nahi ho raha"): the manual verify compares against the
   EXACT order amount, and the credit always binds to the
   SUBMITTER's own pending order - a user's own Order ID credits
   his own deposit, every single time.
3. AUTO-SWEEP STILL LOOT-PROOF: the 45s sweep keeps its ambiguity
   pre-scan - an incoming payment whose amount maps to MORE than
   one pending order is left untouched for the manual Order-ID
   path; a still-unique amount auto-credits exactly as before.
   Deposits created before this update keep their stored pay
   amount and verify normally.
4. BALANCE EPSILON FIX (owner: "0.17 price, balance me bhi 0.17,
   phir bhi enough balance nahi batata"): float noise like
   0.16999999999999998 can no longer fail a purchase - the balance
   guards in BOTH purchase engines (single + bulk) and the
   max-affordable math now use a 1e-6 epsilon. A real shortage
   (0.16 vs 0.17) is still always declined.
5. Everything else (v9.34 menu reshape + Bulk Manage, v9.33
   silent boot, v9.32 Binance Pay engine, v9.31 user Bulk Buy)
   untouched.

WHAT'S NEW IN v9.34 (MENU RESHAPE + BULK MANAGE - OWNER LAYOUT)
1. USER MENU RESHAPED (owner's exact sketch):
   Row 1: Buy Number + Bulk Buy (topmost, the money-makers)
   Row 2: Deposit + Profile
   Row 3: Support + Active Numbers
   Row 4: Refer & Earn - and for the owner the Admin Panel button
   sits RIGHT BESIDE Refer & Earn on the same row.
2. ADMIN PANEL: the Users button and its list screen are REMOVED
   (owner order: "users ka button and uska kaam pura hatao") -
   Modify User still covers every per-user job (balance, ban, view).
3. ADMIN BULK BUY -> BULK MANAGE: the old withdraw-numbers-to-file
   tool is gone. The new Bulk Manage screen sets the USER bulk-buy
   discount: MINIMUM QUANTITY + PER-NUMBER $ OFF, stored in the DB
   and applied LIVE everywhere - pick card, qty card, confirm card,
   receipt, the price engine and the boot log, no restart needed.
4. The discount rule is now DYNAMIC in all 13 languages
   ({min}+ = ${amt} off) - the owner changes the config and every
   user sees the new rule on their very next message.
5. Everything else (v9.33 silent boot, v9.32 Binance Pay, v9.31
   user Bulk Buy engine, v9.28 delivery net, v9.27 refund hub)
   untouched.

WHAT'S NEW IN v9.33 (SILENT BOOT - ZERO TEST MESSAGES)
1. OWNER COMPLAINT FIXED: every restart used to DM the admins a pile of
   test cards - the 47-emoji Premium Emoji Check card, the button-icon
   card + its test reply keyboard + the URL canary button, and the
   icons-off alert. The bot now starts COMPLETELY SILENT: zero messages
   are sent at boot, to anyone, ever.
2. HOW THE CHECKS STILL WORK (invisible, message-free):
   - Premium emoji layer: every ID verified through the READ-ONLY
     getCustomEmojiStickers API - a dead/deleted ID turns the layer
     off and only writes one journalctl log line.
   - Button icons: the PTB capability probe (import-time) + the same
     sticker liveness check for all mapped icon IDs. No card, no
     keyboard, no canary, no alert DM.
   - The runtime safety net (_pem_send) stays: if Telegram ever
     rejects an icon/emoji on a REAL message, that one send
     auto-downgrades and the layer flips off silently - the user
     never sees an error, the owner sees one log line.
3. Boot logs keep the version markers (journalctl only - nothing is
   sent into Telegram).
4. Everything else (v9.32 Binance Pay, v9.31 user Bulk Buy, v9.30
   admin Bulk Buy, v9.29 token + @RTO_LiveUsa0tp, v9.28 delivery net,
   v9.27 refund hub) untouched.

WHAT'S NEW IN v9.32 (BINANCE PAY DEPOSITS - AUTO-VERIFY BY ORDER ID)
--------------------------------------------------------
1. 4TH DEPOSIT NETWORK: the network picker now shows
   🏦 Binance Pay beside USDT BEP-20 (button icon = the owner's
   premium emoji ID 5420232672964275159). Callback dep:net:binance.
2. UNIQUE CENT AMOUNTS (loot-proof binding): every Binance order is
   created with a UNIQUE pay amount (+$0.01 steps, e.g. $1.02 while
   another pending order holds $1.01). The card says exactly what to
   send. Two pending orders can never share one amount, so one
   incoming payment maps to EXACTLY ONE order - deterministic.
3. ORDER-ID AUTO VERIFY (owner spec: "order I'd se match karta hai"):
   - 45s background sweep: pulls the owner's incoming Binance Pay
     USDT history (official signed API, /sapi/v1/pay/transactions)
     and credits pending Binance orders by exact unique amount -
     NO user input at all, deposit-group forward + user DM same as
     every other network.
   - I PAID path: the user pastes the Binance ORDER ID (from the
     app: Pay -> transfer details); the bot matches it against the
     same official history, checks incoming + USDT + amount +
     recency, and credits instantly.
4. ONE ORDER ID = ONE CREDIT, EVER: credit_auto_deposit re-checks
   pending-only + global tx_hash replay inside ONE immediate
   transaction. The sweep and a manual submission racing on the same
   payment: exactly one wins. Same Order ID from 2 phones / 2
   accounts / double-tap: one credit, the rest get the replay text.
5. ANTI-TRICK INPUT: pasted Order IDs are stripped of ALL whitespace
   ("M_P_ 123", multi-line, quotes all work), format-checked
   (M_P_... / P_... or bare digits), tail-matched (M_P_1234 == 1234).
   A wrong FORMAT never touches the API and never burns an attempt
   (same kindness as the TXID paths) - the 15-attempt lock only
   counts REAL verifications that came back declined.
6. RECIENCY GUARD: a payment can only bind to an order created
   BEFORE it (5-min clock-skew grace) - a month-old transfer can
   never pay a fresh order; underpayments are declined with the
   exact got/want amounts (overpayment credits the actual paid
   value); non-USDT assets and OUTGOING transfers are rejected with
   dedicated texts.
7. API-SAFE: every Binance failure (network, auth, IP-whitelist,
   rate limit) maps to a "verification busy - try in a minute"
   message that does NOT burn attempts and stores nothing; orders
   stay pending; the owner can still approve manually from Pending
   Deposits. Boot prints an API probe result + the exact fix hint.
8. Owner credentials live in ONE config block (BINANCE_PAY_API_KEY /
   SECRET / Pay ID 1033766199, env-overridable); the Pay ID is a
   setting, shown on the card, forwarded in the group post with an
   "Order ID" label instead of TXID.
9. DB FIX (found by the v9.32 two-phone race test): the shared
   aiosqlite connection now runs FULL AUTOCOMMIT - the old implicit
   transaction per write could collide with the atomic engines'
   BEGIN IMMEDIATE ("cannot start a transaction within a
   transaction") when two users raced deposit/purchase at the same
   moment. Single statements commit themselves, the lock-protected
   atomic engines keep their exact guarantees, rowcount guards
   unchanged - the crash window is gone.
Everything else (v9.31 user Bulk Buy, v9.30 admin Bulk Buy,
v9.29 token + OTP success channel, v9.28 OTP 100% delivery net,
v9.27 refund hub, referral, 13 languages) is 100% untouched.

WHAT'S NEW IN v9.31 (USER-SIDE BULK BUY + BUTTON ICON DIAGNOSIS)
--------------------------------------------------------
1. NEW USER BUTTON: Bulk Buy (own row in the MAIN MENU, under Active
   Numbers, all 13 languages). Tap -> pick WhatsApp or Telegram ->
   the card shows LIVE availability + rate + the discount rule.
2. TYPE HOW MANY -> CONFIRM -> FILE: the buyer types the quantity,
   the bot shows a receipt-style confirm card (type, count, unit
   rate, total, balance-after) and on confirm delivers an
   otphub.<n><country>.txt (e.g. otphub.60usa.txt) with EXACTLY the
   purchased numbers in the same 'phone | url' stock format.
3. BALANCE FIRST (user balance ke anusar): the purchase is paid from
   the buyer's own balance - not enough balance shows the exact max
   affordable count; not enough stock shows the real available count.
   The engine is ONE BEGIN IMMEDIATE transaction: guarded stock
   claims + guarded deduct (balance can never go negative) + only
   what was ACTUALLY claimed gets charged (honest partials).
4. BULK DISCOUNT (owner-configurable since v9.34, Admin Panel >
   Bulk Manage): at N or more numbers in one order the user pays
   LESS per number (default 30+ = $0.01 off, e.g. $0.15 -> $0.14),
   never below zero - the owner sets BOTH the threshold and the
   amount, live from the admin panel.
5. REFUND-PERFECT LEDGER: every number gets its OWN order row
   (rate_at_purchase = discounted unit). The owner's existing
   Refund Send / Check Number flow matches and refunds each bulk
   number exactly like a normal single buy - 100 numbers bought,
   100 match, each refunds its own price. Referral commission stays
   pending per number and pays only when THAT number's OTP arrives.
6. OTP DELIVERY: instant pollers for the first numbers + the
   permanent sweeper covers every remaining one within ~2 minutes;
   each delivered OTP lands in the buyer's chat automatically and
   posts to the success channel (v9.29) as usual.
7. PREMIUM BUTTON ICONS DIAGNOSIS: if button icons are ever off,
   the boot now says WHY in a loud owner alert (old python-telegram-
   bot on the VPS vs Telegram rejection) instead of silently
   degrading - plus the boot log prints the PTB version.
8. LOOT GUARDS: banned + force-join gates re-checked inside the
   flow, strict integer input, 1,000 per-request cap, in-flight
   double-tap lock, confirm step before any money moves.
Everything else (v9.30 admin Bulk Buy, v9.29 token + @RTO_LiveUsa0tp,
v9.28 OTP 100% delivery net, v9.27 refund hub) is 100% untouched.

WHAT'S NEW IN v9.30 (ADMIN PANEL -> BULK BUY)
--------------------------------------------------------
1. NEW ADMIN BUTTON: Bulk Buy (own row, right under Add Stock /
   Stock Stats). Tap it -> the bot shows the CURRENT available stock
   and asks HOW MANY numbers to buy.
2. TYPE A NUMBER -> GET A FILE: whatever quantity the owner types
   (1 - 50,000), the bot answers with a .txt containing EXACTLY that
   many numbers in the SAME TO SAME format as Add Stock:
       +14133525884 | http://otp-api-link/xyz
   One line per number - the file can be re-uploaded via Add Stock
   (paste or .txt) at any time, zero conversion.
3. NUMBERS ARE TAKEN OUT OF THE POOL (that is what buying means):
   every delivered number is REMOVED from available stock in the
   same action - users can never buy a number the owner already
   took. Want them back in the bot? Upload the file via Add Stock.
4. RACE-PROOF ENGINE: the withdraw runs in guarded cycles - it
   SELECTs candidates and DELETEs only rows STILL status='available'.
   A user buying at the same moment can never lose their purchase,
   the loop tops up from fresh candidates until the full quantity is
   met or the pool is empty, and concurrent Bulk Buys can never
   double-hand out the same number.
5. SAFE INPUTS: quantity must be a whole number, capped at 50,000
   per request; typing more than available shows the exact available
   count instead of a partial file; a file upload in this state gets
   a clear 'type a number' hint. Stale state recovers to the panel.
Everything else (v9.29 new token + OTP success channel @RTO_LiveUsa0tp,
v9.28 OTP 100% delivery net, v9.27 refund hub, Active Numbers,
referral on OTP, second admin FULL access) is 100% untouched.

WHAT'S NEW IN v9.29 (BOT TOKEN CHANGED + OTP SUCCESS CHANNEL)
--------------------------------------------------------
1. BOT TOKEN CHANGED: the bot now runs on the new owner-provided
   token (default swapped; .env BOT_TOKEN still overrides it).
2. OTP SUCCESS CHANNEL (owner request): the moment a buyer's OTP is
   delivered, a fixed-format post lands in @RTO_LiveUsa0tp -
       \U0001F389Successfully otp received
       \U0001F916User :- {buyer NAME}
       \U0001F7E2Number {masked - only last 4 digits visible}
       \u2705OTP :- {code}
       Price :- {$0.15}
   - the WHOLE post is BOLD (owner styling), plain text, no design.
   - the buyer's NAME is posted, NEVER the @username - strangers
     must not be able to DM the buyer from the public channel.
   - the number uses the same mask_number() as the purchase log:
     only the last 4 digits are visible, the rest is ****.
   - the price is the rate the buyer ACTUALLY paid (order lookup,
     get_order_amount_for fallback).
3. ALL THREE DELIVERY PATHS POST: fast poller, permanent sweeper and
   the Get OTP button - every path runs inside the atomic
   update_otp_for_stock claim, so the channel post is EXACTLY-ONCE
   by construction (no path can win the claim twice).
4. FIRE-AND-FORGET + CRASH-PROOF: the post is scheduled as its own
   task - the buyer's OTP delivery never waits on the channel, and a
   dead/forbidden channel (bot not admin yet, network blip) retries
   once and then only logs - it can NEVER cost a delivery or crash
   the poller/sweeper.
5. Channel target is one constant at the top (OTP_SUCCESS_CHANNEL,
   env-overridable) - change it in one place.
Everything else (v9.28 OTP 100% delivery net: restart recovery +
permanent sweeper + refund/OTP race guard; v9.27 refund hub with
Check Number / Refund Send / Chek Number & Refund; Active Numbers;
referral pays on OTP arrival; second admin FULL access) is intact.

WHAT'S NEW IN v9.28 (OTP 100% DELIVERY NET + FULL A-TO-Z RUN AUDIT)
--------------------------------------------------------
1. THREE INDEPENDENT OTP DELIVERY PATHS (isse nahi to usse aa gaya):
   1) FAST POLLER (v9.26) - 5s checks for 10 min after purchase.
   2) RECOVERY (new) - a restart used to silently kill every in-flight
      poller (they lived only in RAM). Now post_init re-arms a fast
      poller for EVERY undelivered sale of the last 24h right after
      boot - a VPS restart can no longer cost a delivery.
   3) SWEEPER WORKER (new) - a permanent low-rate background worker:
      every 2 min it probes sold numbers with no OTP yet and no live
      poller (window over / poller crashed / process restarted /
      anything) and delivers the moment the provider shows a code.
      DB-bounded (300/cycle), semaphore-bounded (20 workers),
      crash-proof - and there is NO TIME LIMIT anymore: the code
      reaches the buyer whenever it lands, automatically.
2. REFUND vs OTP RACE GUARD (owner money fix): the atomic OTP claim
   now also requires the row to still be a live sold number - a
   refund that wins the race can never be followed by an OTP delivery
   (before, a buyer could receive the refund AND the code). The Get
   OTP button re-checks the same and shows the blocked card instead
   of a code on a refunded number.
3. GET OTP BUTTON HARDENING: the typing indicator is cosmetic now -
   a transient Telegram error there used to abort the whole fetch
   after the 'Fetching...' toast. The fetch itself can never die on
   it anymore.
4. REFERRAL PAYOUT SELF-HEAL: if the delivery-time commission payout
   ever failed (DB busy/transient), pressing Get OTP on the delivered
   number now retries it - the atomic pending->paid guard keeps it
   exactly-once.
5. FULL LIVE RUN AUDIT: every button, callback, state and admin flow
   was EXECUTED against a real running instance (fake Telegram wire +
   live fake provider). All routes answered, no crash, no loot.
6. CLEANUP: dead fetch_otp helper deleted; boot/selftest strings
   bumped to v9.28.
Everything else (v9.27 refund hub, referral-on-OTP, Active Numbers,
OTP delivery v9.26 machine-endpoint fetch, second admin) is intact.

WHAT'S NEW IN v9.27 (REFUND SYSTEM REBUILT — FULLY CLEAN)
--------------------------------------------------------
1. OLD REFUND SYSTEM DELETED 100%:
   - the user-side Refund button on the receipt is GONE (receipt is
     now Get OTP + Back), the 5-minute cooldown, refund requests,
     pending list, failed-urls matching, Seller Input.txt, refund
     bells, refund i18n - every trace removed from every screen.
2. ADMIN PANEL -> MANAGE REFUND (all-new hub, 3 tools):
   a) CHECK NUMBER - upload a stock-format file (phone | url), the
      bot live-checks EVERY number (10k / 20k+, 30-way worker pool)
      with a LIVE progress bar and returns a .txt of the numbers
      where NO OTP arrived (same stock format, forward-ready).
   b) REFUND SEND - forward the checked file: every URL that belongs
      to a sold number with no OTP is refunded AUTOMATICALLY - the
      buyer gets 'Your Refund Successfully' with number + price,
      the owner gets a full match report (URLs / matched / refunded
      / OTP-blocked / no-owner). A second LIVE check runs before any
      money moves (a URL whose OTP arrived is skipped - no loss).
      AFTER a refund the stock row is wiped (url + owner deleted,
      status refunded, OTP blocked) - re-sending the same file can
      NEVER match again: one refund per number, ever, loot-proof.
   c) SELL NUMBER SEND - sold numbers as a stock-format file:
      Old Sell Number (previous batch) / New Sell Number (latest
      batch). Each file can be taken 3 times, then 'already taken'
      until 5 hours pass and a fresh batch can be built. Every file
      is PINNED in the chat.
3. REFERRAL COMMISSION FIX: commission is no longer paid at
   purchase. It is recorded PENDING at buy and PAID THE MOMENT the
   buyer's OTP arrives (paid on success only). A refunded number's
   pending commission is cancelled - commission exists only for
   numbers whose OTP arrived successfully.
4. USER MENU -> ACTIVE NUMBERS: every user sees their numbers that
   are still active (OTP not arrived, not refunded) as tap-to-copy
   monospace lines. Sending a number back to the bot opens it in
   the familiar post-purchase view with Get OTP (poller restarts,
   no time limit - the code reaches the user whenever it lands).
5. DATABASE: stock.order_id column + otp_url / sold-status indexes,
   per-item guarded atomic refunds, 30-way concurrency with live
   progress edits - 20k-number checks stay smooth and crash-free.
Everything else (OTP delivery v9.26, second admin, referral,
channels, force join, broadcast copy, group silence) is untouched.

WHAT'S NEW IN v9.26 (OTP LOSS FIX — DEEP OVERHAUL)
--------------------------------------------------------
ROOT CAUSE of the lost numbers (user bought, OTP arrived at the
provider, user never received it, refund -> owner loss):
  1. The bot fetched the provider's pretty /sms/ page. That page is
     rendered by JavaScript in the buyer's browser - server-side it
     can say WAITING forever while the real code is already live at
     the provider's machine endpoint /api/sms/ (proven live: page
     WAITING, /api/sms/ returned 869870).
  2. _otp_codes() matched the RAW HTML and picked up CSS junk
     (#16213e -> '16213', layout values -> '64748').
  3. An EMPTY baseline (fresh bulk number, no old SMS) was stored as
     '[]' but read back as 'never captured' - the next fetch then
     re-baselined and the buyer's fast-arriving OTP swallowed itself
     as 'old SMS'. It was never delivered; Get OTP kept saying
     waiting; the user refunded; the owner lost the numbers.
THE FIX:
  1. fetch_sms_text_smart(): every OTP read now probes /api/sms/
     FIRST (status-checked); the /sms/ page is only a fallback.
  2. _otp_codes() is HTML-safe: script/style/tags stripped before
     matching - CSS junk can never become an 'OTP' again.
  3. Baseline is captured EXACTLY ONCE (poller's first fetch at
     purchase) and persisted; empty '[]' is a REAL state meaning
     'every new code belongs to the buyer'. NO path ever re-baselines
     - Get OTP included. A missing baseline (legacy purchases) reads
     as empty, so the waiting buyer always gets what the API has.
  4. check_live_otp() (refund gate) is now status-checked too: a 404
     page reads as 'unknown', never as 'no code'.
Everything else (second admin, referral, channels, force join,
broadcast copy, group silence) is 100% untouched.

WHAT'S NEW IN v9.25 (SECOND OWNER-ADMIN — FULL ACCESS)
--------------------------------------------------------
1. NEW ADMIN: 9876543210 is now a SECOND OWNER-ADMIN with FULL access -
   the exact same powers as the owner: admin panel, buy/stock
   management, deposits, refunds, broadcast, channels, reffer system,
   ban/unban, every admin state, command and callback.
2. EVERYTHING ADMIN-GATED IS AUTOMATICALLY OPEN TO HIM - the whole
   permission model runs through one gate (is_admin -> ADMIN_IDS), so
   there is no hidden owner-only corner left behind.
3. ADMIN NOTIFICATIONS NOW REACH BOTH ADMINS:
   - boot self-test cards (premium emojis + button icons),
   - new refund request bells,
   - deposit-confirmed notices (deduped with the group target).
4. BOTH ADMINS ARE BAN-PROOF: no admin can ban the owner or the other
   owner-admin. The DB crown (users.is_admin) is stamped for both at
   boot, even if the row already existed.
5. Deliberately unchanged: the supplier input.txt claim identity stays
   the OWNER's username|id no matter which admin downloads it.
6. Everything else (referral system, channels, force join, broadcast
   copy, group silence, OTP relay) is 100% untouched.

WHAT'S NEW IN v9.24 (REFER & EARN — FULL REFERRAL SYSTEM)
--------------------------------------------------------
1. USER: REFER & EARN (main-menu button, owner premium icon 5440410042773824003)
   - Every user gets a personal deep link  t.me/<bot>?start=ref<userid>.
   - The referral screen shows the link, referred count, total earned,
     the last earnings and a one-tap SHARE button (native Telegram share).
   - Fully translated in all 13 languages.
2. COMMISSION (loot-proof by design)
   - Every successful purchase of a referred user credits the referrer
     INSIDE the same atomic purchase transaction (BEGIN IMMEDIATE):
     balance check + stock claim + deduct + order + commission commit
     together or not at all. The earning row is UNIQUE per order id -
     a double pay is impossible even under a race.
   - Default commission $0.005 per buy (owner changes it any time).
   - VIP referrers earn their own special rate (e.g. $0.010) - only the
     chat IDs the admin adds to the VIP list get it.
   - Commission is bound to the buyer from their very FIRST /start via
     the link (existing users can never re-bind; self-referral blocked;
     first binding wins under a race). No link = no commission = no loot.
3. ADMIN: MANAGE REFFER (inside the admin panel, 2-per-row layout)
   - Set Reffer Price: change the per-buy commission live (shown before/
     after, validated, e.g. 0.005).
   - Manage VIP: ADD VIP (chat ID + special rate) / REMOVE VIP
     (tap-to-remove list) / VIP LIST. The VIP user is told their rate.
   - Reffer System ON/OFF: one tap toggles. OFF = commissions STOP for
     everyone (VIP + normal) and the Refer & Earn button is REMOVED from
     every user menu until the owner turns it back on.
4. REFUND REVERSAL (money stays honest)
   - When a purchase is refunded, its referral earning is reversed: the
     row is marked reversed and the commission is deducted from the
     referrer's balance (never below $0.00). The referrer is notified.
5. Everything else (channels, force join, broadcast copy, group silence,
   rates, deposits, OTP relay) is 100% untouched.

WHAT'S NEW IN v9.23 (MANAGE CHANNELS + FORCE JOIN + PERFECT BROADCAST + GROUP SILENCE)
--------------------------------------------------------
1. ADMIN: MANAGE CHANNELS (Add / Remove / List)
   - Add accepts @username, t.me link, -100 ID or a FORWARDED message -
     the bot auto-detects title, type, public/private and the join link.
   - The bot must ALREADY be admin in that chat, or the chat is refused.
   - Private chats get a bot-created join-REQUEST link.
2. FORCE JOIN (owner rule: bot stays at LANGUAGE until joined)
   - After picking a language every user must join ALL managed chats:
     JOIN CHANNEL / JOIN GROUP buttons (owner envelope icon) + Verify.
   - Public chats: verified live via real membership; leaving the chat
     locks the bot again (real-time chat_member tracking).
   - Private chats: the user can only SEND A REQUEST - the request
     itself unlocks the bot; the bot NEVER approves it.
   - JOIN CHANNEL / JOIN GROUP + the whole join screen are fully
     translated in all 13 languages.
3. BROADCAST = EXACT COPY (copy_message)
   - Text, photo, video, file (APK), audio, GIF: copied same-to-same.
   - Premium custom emojis arrive PREMIUM (the old re-type flattened
     them to normal emoji). Managed chats receive it too.
4. GROUP SILENCE
   - In groups/channels the bot never talks: no menu, no commands, no
     replies. The ONLY posts it ever makes there are admin broadcasts.
5. Admin panel stays 2 buttons per row (Manage Channels + Back row).

WHAT'S NEW IN v9.22 (CLEAN ICON BUTTONS + BULLETPROOF ROUTING)
--------------------------------------------------------
1. NO MORE DOUBLE EMOJI ON BUTTONS
   - A button that carries the owner's premium icon now shows that
     icon INSTEAD of its normal unicode emoji (the normal leading
     emoji is removed from the label at render time). Buttons look
     clean: one premium icon + text, never icon + emoji + text.
2. BUTTONS KEEP WORKING AFTER THE CHANGE (the owner's #1 concern)
   - The whole text router is now emoji-tolerant (btn_eq): a tap on
     a new icon-stripped keyboard ("Buy Number") and a tap on an old
     emoji keyboard ("🛒 Buy Number") BOTH route correctly, in all
     13 languages, for every button: main menu, Back/Cancel, buy
     type/country/confirm, deposit menu/amount/network/cancel,
     admin panel + every admin flow button.
   - country/rate/ban pickers and the Buy-confirm price check were
     made emoji-tolerant the same way; old keyboards never break.
3. BACK FROM TXID SCREEN = ADDRESS CARD (state consistency fix)
   - Back on the TXID prompt re-opens the SAME pending deposit's
     address card (I PAID / Cancel) instead of dropping the user at
     the main menu with a live TXID state. A dead deposit clears
     cleanly. No more orphaned TXID state confusion.
4. RE-SYNC FIX: unknown text on the network screen re-opens the
   network picker with the SAME amount (was: main menu + stuck state).
5. ADMIN PANEL = 2 BUTTONS PER ROW (owner order): Add Stock+Stock
   Stats / Pending+Users / Modify+Statistics / Set Rate+Broadcast /
   Set Wallet+Total Deposit / Ban+Refund / Back.
6. Money flows, callbacks, red lines: 100% unchanged (v9.21
   loot-proofing fully intact).

WHAT'S NEW IN v9.21 (LOOT-PROOF SECURITY PASS — MONEY FLOWS HARDENED)
--------------------------------------------------------
1. DOUBLE-REFUND IMPOSSIBLE
   - A refund claim is now a single atomic INSERT: one
     pending/approved refund per number, ever. Double-tapping Refund
     (or two devices) can no longer create two payable requests, and
     the admin approval batch additionally pays each number at most
     once per batch (duplicates auto-rejected, unpaid).
2. TXID REPLAY IMPOSSIBLE (cross-user)
   - Deposits confirm inside ONE transaction that re-checks on-chain
     replay: the same valid TXID submitted by two accounts on two
     pending deposits credits exactly one of them. One payment =
     one credited deposit, mathematically.
3. EXACTLY-ONCE OTP DELIVERY
   - The 10-minute OTP poller and the Get OTP button can race; an
     atomic claim decides the single winner, so the user can never
     receive the same OTP twice and the OTP counter never double-
     counts. Stored codes are never overwritten.
4. DEFENSE-IN-DEPTH
   - Every admin input state (rate, balance, wallet, broadcast, ban,
     stock, ledger reset) re-verifies the admin inside the handler -
     a forged/leaked state can no longer touch anything.
   - Refund replies survive stale/deleted messages (no more crash on
     very old buttons); admin inline gate answers stale queries safe.
5. Button texts, callbacks, flows, red lines: 100% unchanged.

WHAT'S NEW IN v9.20 (FULL AUDIT — BUG FIXES + 40K PERFORMANCE + CLEANUP)
--------------------------------------------------------
1. BUTTON-CLICK CRASH FIXES (single-answer discipline)
   - Get OTP / Refund / admin Approve-Reject toasts could crash the
     handler (double q.answer -> 'query already answered'). Every
     callback now answers exactly once, with the right localized
     toast instead of a generic error.
2. 40K-USER SMOOTHNESS
   - Broadcast rebuilt: id-only query, chunked concurrent sends
     (~25/s), Telegram 429 RetryAfter respected, live progress.
   - Users list: SQL LIMIT + COUNT (never loads all user rows).
   - Bulk stock add: batched duplicate check + one executemany.
   - OTP poller registry pruning (no unbounded growth).
3. ROBUSTNESS
   - NaN/Infinity amounts rejected everywhere (deposit + admin).
   - Shared SQLite Row factory set ONCE at connection creation
     (race-proof; the atomic purchase no longer depends on call
     order for name-based row access).
   - Fresh users get a DB row on any text message, not only /start.
   - Stale-message edits wrapped; OTP poller re-check None-safe.
4. DEAD CODE REMOVED
   - unused random import, _nav_row, _clear_last_msg stub,
     _kb_dedupe passthrough, phone_in_available_stock,
     get_all_users, per-call row_factory lines, local hashlib.
   - Button texts, callbacks, flows, red lines: 100% unchanged.

WHAT'S NEW IN v9.19 (88 PER-BUTTON OWNER ICON IDS - A TO Z)
--------------------------------------------------------
1. EVERY BUTTON GETS ITS OWN OWNER ICON ID (88-button map)
   - Owner assigned one premium custom-emoji ID per button (A-to-Z
     inventory: main menu, language picker, buy flow, deposit flow,
     OTP receipt, admin panel, input screens, refund menu, admin
     pickers, user card, deposit report, reset confirm).
   - Resolution order per button: callback-exact (language picker)
     > callback-prefix (deposit amount presets) > keyboard map
     full-text (admin English labels) > keyboard map leading emoji
     (i18n safe, all languages) > message-pack fallback.
   - Per-KEYBOARD maps: same label on different screens can carry
     different icons (e.g. the two "Admin Panel" backs, the two
     "💰" admin buttons, Telegram buy vs Telegram stock).
   - Button TEXTS + callback_data 100% unchanged; old PTB builds or
     a Telegram rejection auto-disable icons (plain buttons, no
     errors). Red lines untouched.

WHAT'S NEW IN v9.18 (PREMIUM BUTTON ICONS - ALL BUTTONS)
--------------------------------------------------------
1. PREMIUM CUSTOM-EMOJI ICONS ON BUTTONS (Bot API 9.4+)
   - Every button now carries the owner's premium custom emoji as the
     official icon_custom_emoji_id field: user-side INLINE buttons,
     user-side bottom REPLY keyboards, ADMIN panel + admin inline
     keyboards, receipt (Get OTP / Refund) and group Approve/Reject.
   - Icons reuse the SAME 47-ID owner pack as the messages (+ one
     alias: the emoji Back-arrow shows the owner's left-arrow icon).
   - Button TEXTS are 100% unchanged (router/menu matching safe);
     non-premium users see exactly the same buttons as before.
   - Boot self-test DMs the owner a live icon preview; any Telegram
     rejection auto-disables icons -> plain buttons, zero errors.

WHAT'S NEW IN v9.17 (PREMIUM EMOJIS + 13 LANGUAGES)

---------------------------------------------------
1. PREMIUM CUSTOM EMOJIS (47 OWNER IDS)
   - Every user-side message now renders Telegram PREMIUM custom emojis
     in all 13 languages through one render-time layer (pem()).
   - Buttons / toasts keep normal emojis (Telegram platform rule).
   - Boot self-test DMs the owner all 47 premium emojis; any rejection
     auto-disables the layer -> normal emojis, zero user-facing errors.

2. 4 NEW LANGUAGES - 13 TOTAL
   - Portugues (pt), Espanol (es), Kiswahili (sw), Hindi (hi)
   - Full 147-key translations, same emoji/placeholder/HTML parity as
     the existing 9 languages; picker now shows 13 languages.

3. EVERYTHING ELSE UNCHANGED
   - v9.14 perf core + v9.16 report/reset intact; red lines safe
     (no deletions, short replies, no auto-refund).

WHAT'S NEW IN v9.16 (9 LANGUAGES + ADMIN DEPOSIT REPORT)
------------------------------------------------------------
1. 9 LANGUAGES — FULL TRANSLATION (v9.16)
   - English, Bengali, Urdu, Chinese, Arabic, Indonesian,
     Turkish, Russian, Persian (146 strings each, parity-checked)
   - every user-side screen, button, toast and notification now speaks
     the user's language (rates / numbers / wallets never change)
   - NEW user starts with a LANGUAGE PICKER on /start, then lands in
     the main menu in that language; the choice is saved per user
   - /language command (also in the Telegram commands menu) reopens
     the picker anytime; instant switch, cache kept fresh
3. Everything else (atomic buy, wallets, TXID security, trace,
   design, Back navigation) untouched. Admin screens stay English.

WHAT'S NEW IN v9.15 (support username + Back navigation)
------------------------------------------------------------
1. SUPPORT USERNAME CHANGED
   - Support screen now shows @costumersupprot (old personal
     handle fully removed everywhere)
2. "Main Menu" BUTTONS -> "Back"
   - every inline Main Menu button is now a single clean "Back"
     (goes one step back when a back screen exists, otherwise
     straight to the main menu)
   - receipt keyboard (Get OTP / Refund) third button -> Back
   - admin panel bottom keyboard button -> Back
   - callbacks untouched: nav:home / nav:back behave exactly the same

WHAT'S NEW IN v9.14 (performance + flow integrity)
------------------------------------------------------------
1. FAST EVERYWHERE (async I/O done right)
   - ONE shared HTTP session: OTP polling + BSC/Polygon/Tron RPC reuse
     TCP/TLS connections (no fresh handshake on every single call)
   - ONE shared SQLite connection (WAL): no per-query file open/close,
     sqlite statement cache persists across calls
   - hot-path indexes on stock / deposits / orders / refunds
   - settings micro-cache (2s) for rates + min-deposit reads; admin
     changes still apply instantly (cache invalidated on save)
   - concurrent updates: different users' handlers run in parallel
2. ATOMIC PURCHASE (race-proof buy flow)
   - balance check + stock claim + deduct + order insert now run in ONE
     transaction with status='available' + balance>=? row guards:
     two buyers can never receive the same number, balance can never
     go negative, the double-tap lock is kept
3. Behaviour of v9.13 / v9.12 / v9.11 / v9.10.1 untouched: messages,
   buttons, TXID-only security, wallets, deposit trace.

WHAT'S NEW IN v9.13 (user-designed message redesign)
------------------------------------------------------------
1. NEW DESIGN SYSTEM ON EVERY USER MESSAGE
   - light thin divider, emoji-anchored Title Case titles
   - status emoji glossary: success/failed/pending/locked/replay/
     info/warning always mean the same thing
   - every card ends with a small 'next step' line
   - typos fixed: OTP Received, Your Number
2. ALL USER-SIDE CARDS REDESIGNED (GLB/BUY/OTP/RFD/DEP/PRF + toasts)
   - buttons, callbacks, labels: UNTOUCHED
   - admin screens / group posts: UNTOUCHED

WHAT'S NEW IN v9.12 (wallet rotation + traceability)
------------------------------------------------------------
1. ALL WALLETS ROTATED (old addresses retired everywhere)
   - BEP-20 (BSC)  : 0x837459f63a3aceb18f33b9f7697defdb221f426a
   - (TRC-20 / Polygon FRIEND EDITION me removed hain)
   - On boot, init_db swaps any leftover OLD wallet still stored
     in a database for the matching NEW wallet automatically -
     a retired address can never stay live.
2. FULL DEPOSIT TRACE (audit trail)
   - New deposit_trace table records EVERY event: order created,
     bad TXID format, declined (pending/failed/wrong token/
     wrong recipient), TXID replay, amount mismatch, credited,
     order locked, wallet changed/rotated - with time, order id,
     user id, network, TXID and reason.
   - Admin command: /trace (last 25) or /trace DEPXXXXXXXX.
   - Every order BINDS the exact wallet it was shown, so a later
     wallet rotation never breaks pending orders; the admin group
     post now shows Order + Wallet + Network + TXID + scan link.
3. Admin SET WALLET screen now lists all three network wallets.

WHAT'S NEW IN v9.11 (clean deposit UI)
------------------------------------------------------------
1. DEAD BUTTONS REMOVED (user report)
   - Custom-amount screen: I PAID removed (the user only types
     the amount there) - it now has just Cancel Deposit.
   - TXID screen: I PAID removed (the TXID itself is the only
     thing needed) - it now has just Cancel Deposit.
   - Redundant "Main Menu" buttons removed from every deposit
     screen - Cancel / Back handle navigation.
2. CANCEL = BACK TO MAIN MENU
   - Cancel Deposit closes the order AND lands the user
     straight on the main menu.
3. CLEANER TEXTS
   - Deposit screens rewritten short and scannable: SEND $X
     card, tap-to-copy address, clearer TXID prompt, plain
     DEPOSIT CONFIRMED receipt (fancy unicode fonts dropped -
     they render as empty boxes on some phones).

WHAT'S NEW IN v9.10.1 (TXID-ONLY verification - no auto-credit)
------------------------------------------------------------
1. POLLER AUTO-CREDIT DELETED
   - The 45s BSC sweep that credited pending deposits by amount
     matching is fully removed. With 200 users paying at once,
     equal amounts ($0.50, $1.00 ...) can be bound safely to
     nobody by an amount alone - so the bot no longer guesses.
2. VERIFICATION = TXID, ALWAYS
   - Money is credited ONLY after the user taps I PAID and sends
     the transaction hash, which is checked on-chain (right
     network, right wallet, USDT contract, success, amount).
   - No TXID -> no verification -> no credit. No exceptions.
3. HIGH-SECURITY HARDENING
   - EVM deposits need >= 3 block confirmations before the TXID
     is accepted (BSC + Polygon).
   - Wrong-TXID attempts per order are capped (lockout) to stop
     brute-force probing.
   - One TXID pays ONE order only (cross-network hash guard),
     double-credit guards and pending-only credit unchanged.

WHAT'S NEW IN v9.9.2 (keyless on-chain verification)
------------------------------------------------------------
1. PUBLIC BSC RPC INSTEAD OF THE EXPLORER API
   - Etherscan deprecated the free V1 endpoint and the free V2
     tier no longer covers BSC. The bot now reads USDT Transfer
     logs DIRECTLY from public BSC nodes (eth_getLogs) and uses
     eth_getTransactionReceipt for TX checks: 100% keyless,
     no rate limits, 5 endpoints rotated automatically.
   - The BscScan key stays configured but is now optional.

WHAT'S NEW IN v9.9.1 (guided auto-deposit + live API key)
------------------------------------------------------------
1. BSCSCAN API KEY ARMED
   - OWNER's free BscScan key is now the built-in default
     (bscscan.com, ~100k lookups/day). Existing databases get
     it seeded automatically on first start. .env overrides.

2. USER'S 3-STEP DEPOSIT FLOW (asked order enforced)
   1) Pay the exact unique amount
   2) Paste the TX Hash -> bot verifies it on-chain INSTANTLY
      (recipient + reuse + amount + pending guards)
   3) Bot asks for the payment screenshot -> balance is
      credited AUTOMATICALLY right after it (or tap
      Confirm Now to skip the screenshot - money never waits)
   - While the screenshot is pending the background poller
     still credits within ~45s, so the step can never trap
     money. A stray Cancel can NOT orphan a verified payment.

3. EVERYTHING ELSE UNCHANGED
   - Same unique-amount payment codes, same double-credit
     guards, same admin manual approve fallback, refunds are
     still NEVER instant.

WHAT'S NEW IN v9.9 (USDT BEP20 auto-verify deposits)
------------------------------------------------------------
1. AUTO-VERIFY DEPOSITS (no admin wait)
   - User picks an amount and gets a UNIQUE pay amount
     (base + .01-.99 cent payment code) plus the BEP20 wallet.
   - A background poller sweeps BscScan every 45s; the moment a
     USDT transfer with that exact unique amount lands in the
     wallet, the balance is credited automatically and the user
     + admin group receive the on-chain proof.
   - The user can also paste the TX hash for an instant check
     (same safe credit path).

2. OWNER'S WALLET SET
   - BEP20 wallet (purana wallet hata diya) active by default; official
     USDT (BSC) contract pinned; bscscan_api_key setting ready
     (free key from bscscan.com = 100k lookups/day).

3. STILL SAFE
   - One TX hash verifies ONE deposit only (reuse blocked).
   - Pending-only credit guard: double-poll / double-tap can
     never pay twice.
   - Unknown incoming transfers (wrong amount) are reported to
     the admin group once each - money is never silently lost.
   - Admin manual Approve/Reject still works as a fallback.

WHAT'S NEW IN v9.8 (seller-grade refunds + full audit pass)
------------------------------------------------------------
1. LIVE /api/sms/ DOUBLE-CHECK BEFORE ANY REFUND
   - Matched refunds are probed on the provider's clean endpoint
     (URL /sms/ -> /api/sms/) right before approval. A pure-digit
     answer means the OTP exists -> refund BLOCKED automatically
     (no payment). Waiting / text / network error = dead number ->
     refund approved. Only POSITIVE proof ever blocks a payout.

2. SELLER INPUT.TXT EXPORT (supplier claim)
   - Admin Panel -> Manage Refund -> Seller Input.txt sends every
     APPROVED dead number in the supplier's exact format
     username|user_id|phone|url as a file literally named
     input.txt (the seller's checker tool loads it directly;
     claim ~$0.10 per dead number back from the supplier).

3. REFUND IS STILL NEVER INSTANT
   - Money moves ONLY when the admin uploads/pastes the
     failed-urls list, every match passes the live check and the
     batch is approved. Request -> PENDING -> admin -> payout.

4. FULL A-TO-Z AUDIT FIXES
   - .txt uploads were silently DEAD (handler only accepted image
     documents): failed-urls upload AND stock .txt upload now work.
   - Deposit Approve/Reject is double-tap safe (status-guarded;
     approving twice can no longer credit the balance twice).
   - Buy button double-tap lock (cannot charge twice).
   - Admin can no longer ban himself; broadcasts skip banned
     users; pasting the failed-URL list works like uploading the
     .txt; re-adding a previously sold number warns about
     double-sell; deposit-cancel re-attaches the main menu;
     deprecated utcnow()/get_event_loop() removed; profile open
     self-heals; short-id mask fix.

WHAT'S NEW IN v9.7
------------------
1. OTP FIXES
   - Get OTP was showing the FIRST code in the API response (old SMS)
     so two numbers from the same provider session showed the SAME
     code. Baseline is now persisted per number; only NEW codes are
     delivered. No new code -> "OTP NOT RECEIVED YET".
   - Notification format is exactly:
       **\U0001F389 OTP RECEIVED** (bold)
       \U0001F7E2 {number}
       \u2705 {otp}

2. REFUND SYSTEM (strict)
   - Refund button next to Get OTP on the receipt.
   - 5-minute cooldown after purchase; OTP already received -> refund
     permanently refused; refund request blocks OTP for that number
     FOREVER (poller killed instantly).
   - Refund money is never instant: it stays PENDING until the admin
     approves. Admin Panel -> Manage Refund -> download the refund
     list (.txt, "number | url"), check every URL, upload a .txt of
     the FAILED urls -> matched refunds auto-approved and users paid
     automatically; unmatched ones are rejected and returned as .txt.

WHAT'S NEW IN v9.6
------------------
1. USA COUNTRY BUTTON FIXED (buy flow)
   - Tapping a country re-opened the country list instead of the
     confirm screen (callback format mismatch). Confirm is now
     reachable: country tap -> Confirm -> number delivered.

WHAT'S NEW IN v9.5
------------------
1. BUY FIXED (Out-of-Stock bug)
   - Purchases queried stock with the short code ("wa"/"tg") but
     inventory stores full names ("whatsapp"/"telegram"). The query
     never matched -> every buy showed Out of Stock. Type is now
     converted before the query.

WHAT'S NEW IN v9.4
------------------
1. ADD STOCK BUTTON FIXED
   - The Add Stock screen's keyboard function went missing during the
     v9.2 admin-panel compression -> every tap raised NameError and
     NOTHING happened. Function restored; type picker is inline again.

2. REPLY KEYBOARD NOW CLOSES
   - Bottom keyboard is no longer persistent: it closes automatically
     after every button tap (submenus stay clean), and re-opens when a
     top-level screen (main menu / admin panel / input prompt) arrives.

3. ERRORS ARE NEVER SILENT
   - If anything breaks, the user now gets a small warning message
     instead of dead silence.

WHAT'S NEW IN v9.3
------------------
1. BULK STOCK SYSTEM  (+number | otp-api-link)
   - Add stock ONE PER LINE:  +14133525884 | http://169.58.215.134:11111/...
   - Or upload a .txt file with the same format.
   - Auto-fixes small format mistakes (missing +, spaces, commas,
     semicolons, missing http://) and reports every skipped line.

2. INSTANT BACKGROUND OTP (10 minutes)
   - After purchase the bot polls the number's OWN OTP API every 5s
     for 10 minutes in the background.
   - First response = baseline (old SMS ignored); the moment a NEW code
     appears the user gets instantly:
       🎉 OTP received
       🟢 Your Number: +14133525884
       🔥 OTP :- 000000
   - After 10 min: polite timeout notice; the receipt's Get OTP button
     still works forever.

WHAT'S NEW IN v9.2
------------------
1. KEYBOARD NO LONGER COVERS HALF THE SCREEN
   - Identical bottom keyboards are NOT re-attached on every message
     (re-attaching re-opens/expands the keyboard on mobile phones).
   - Admin panel compressed to 3 columns.

2. ADMIN: MODIFY USER
   - Admin Panel -> Modify User -> send chat ID -> full user card
     (balance, deposits, spent, numbers bought, OTPs, orders...).
   - Inline Modify Balance: set exact / +add / -deduct.

3. ONLY USA
   - Country lists reduced to USA everywhere.

v9.1 (user-feedback fixes)
--------------------------
1. NOTHING GETS DELETED ANYMORE
   - Tapping any button NEVER deletes earlier messages. Receipts, OTPs,
     profiles — everything stays in the chat.

2. HYBRID NAVIGATION (back to the classic UX)
   - MAIN MENU stays in the bottom Reply Keyboard (Buy / Deposit /
     Profile / Support / Admin) — always pinned at the bottom.
   - SUB-MENUS (Buy type, Country picker, Confirm, Deposit amount,
     Admin flows...) are INLINE keyboards again, attached to the message,
     and they EDIT IN PLACE like the classic bot.
   - Smart state memory: press the phone's back button, reopen the chat,
     type /start — the SAME screen reappears.

3. STUCK-STATE BUG FIXED (kept from v9)
   - Tapping a menu button while the bot waits for input (e.g. TX Hash)
     no longer saves the button text as data.

4. 2026 PREMIUM LOOK (kept from v9)
   - Divider cards, receipt-style order confirmations, live balance +
     stock on the welcome screen, live rates on the buy screen, quick
     stats on the admin panel.

- python-telegram-bot v22.8
- Reply keyboard: main menu + admin panel + text-input prompts.
- Inline keyboards: every sub-menu + actions (Get OTP, Approve/Reject).
- NO Refer system. OTP delivered inline with purchase.
"""

import os
import re
import json
import time
import asyncio
import hashlib
import hmac
import math
import atexit
import uuid
import logging
import functools
from datetime import datetime, timedelta, timezone
from html import escape as html_escape, unescape as html_unescape
from urllib.parse import quote as url_quote

import aiosqlite
import aiohttp
from dotenv import load_dotenv

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from telegram.constants import ParseMode, ChatAction, KeyboardButtonStyle
from telegram.error import BadRequest, RetryAfter
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    TypeHandler,
    ChatJoinRequestHandler,
    ChatMemberHandler,
    filters,
)

# --------------------------------------------------------------------------- #
#  LOGGING
# --------------------------------------------------------------------------- #
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("wpbot")
logging.getLogger("telegram").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

# --------------------------------------------------------------------------- #
#  CONFIG
# --------------------------------------------------------------------------- #
load_dotenv()

# v9.29: owner rotated the bot token - new default below. A BOT_TOKEN
# set in .env / environment still wins over this default.
BOT_TOKEN = os.getenv("BOT_TOKEN", "8818136528:AAFZYCQECDMnj8eDg0GX8ocaTQj6sp4zWhk")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8105697199"))
# v9.25: SECOND OWNER-ADMIN - FULL access, the exact same powers as the
# owner (admin panel, add/remove stock, deposits, refunds, broadcast,
# channels, reffer, ban/unban, every admin state and callback).
# v9.41: EK hi hardcoded MAIN admin. ADMIN_ID_2 sirf legacy-compat ke
# liye ab MAIN ke barabar hai; dynamic extra admins Manage Admin panel
# se aate hain (settings 'extra_admins' + is_admin sync cache).
ADMIN_ID_2 = ADMIN_ID
ADMIN_IDS = {ADMIN_ID}

# Group where deposit payment requests (TX hash + screenshot) are forwarded
DEPOSIT_GROUP_ID = -1004444  # @usadepsitideatikdsw - Usa Deposit group
# Group where every successful purchase is logged (order history)
ORDER_HISTORY_GROUP_ID = -10044444  # (same group: deposit + order history)
# v9.29: PUBLIC channel where every successfully delivered OTP is
# posted (buyer name, masked number, OTP, price). The bot must be an
# ADMIN of this channel (owner already promoted it).
OTP_SUCCESS_CHANNEL = os.getenv("OTP_SUCCESS_CHANNEL", "Li0tp")

# --------------------------------------------------------------------------- #
#  v9.32 BINANCE PAY DEPOSITS (owner-provided credentials; env can override)
#  Flow: user picks the Binance Pay network -> pays the order's EXACT
#  amount to the owner's Pay ID -> payment auto-verifies two ways:
#    (1) a 45s background sweep matches incoming Pay history by exact
#        amount when it maps to exactly ONE pending order (no user
#        input at all; shared amounts go to the manual path), and
#    (2) the user can tap I PAID and paste the Binance ORDER ID, which is
#        matched against the same official API history.
#  ONE Order ID / ONE payment = ONE credited deposit, ever - the atomic
#  credit engine re-checks pending-only + global tx replay inside one
#  immediate transaction, so a manual submit and the sweep racing on the
#  same payment can never both win, and 2-phone/double-tap stay harmless.
# --------------------------------------------------------------------------- #
BINANCE_PAY_API_KEY = os.getenv(
    "BINANCE_PAY_API_KEY",
    "sJl7I1cH8areQOEqX")
BINANCE_PAY_SECRET = os.getenv(
    "BINANCE_PAY_SECRET",
    "uXNoWtcxqUJ8242ZvXuaFH3GGJJwYMgBTygoP")
BINANCE_PAY_ID_DEFAULT = "1"
BINANCE_API_BASE = os.getenv("BINANCE_API_BASE", "https://api.binance.com")
BINANCE_PAY_TIMEOUT = 15          # seconds per Binance API call
BINANCE_SWEEP_SECONDS = 45        # background auto-verify cadence
BINANCE_HISTORY_LIMIT = 100       # newest Pay transactions per fetch
BINANCE_TIME_GRACE_S = 300        # clock-skew grace (payment after order)
BINANCE_ORDER_ID_RE = re.compile(r"[A-Za-z0-9_]{5,40}")

# --------------------------------------------------------------------------- #
#  v9.9 USDT BEP20 AUTO-VERIFY CONFIG
# --------------------------------------------------------------------------- #
# OWNER's BEP20 (BNB Smart Chain) wallet - deposits here auto-verify.
USDT_BEP20_WALLET = "0x83746a"
# Official Binance-Peg USDT token contract on BSC.
USDT_BEP20_CONTRACT = "0x5"
BSCSCAN_TX_URL = "https://bscscan.com/tx/"   # user-facing tx links
# v9.9.2: on-chain verification runs DIRECTLY on public BSC RPC
# nodes (keyless). The BscScan API key is no longer required - it
# stays configured below only as an optional reserve.
BSCSCAN_API_KEY_DEFAULT = ""
BSCSCAN_API_KEY_ENV = os.getenv("BSCSCAN_API_KEY", BSCSCAN_API_KEY_DEFAULT)
BSC_RPC_ENDPOINTS = [
    "https://bsc.publicnode.com",        # getLogs-friendly, first choice
    "https://1rpc.io/bnb",
    "https://bsc-dataseed.binance.org",  # receipts/blocks; getLogs limited
    "https://bsc-dataseed1.defibit.io",
    "https://bsc-dataseed1.ninicoin.io",
]
USDT_TRANSFER_TOPIC = ("0xddf252ad1be2caa952ba7f163c"
                       "43b3ef")  # Transfer(address,uint)
BSC_SCAN_RANGE = 3000          # max blocks scanned on a cold start
BSC_MAX_CATCHUP = 3000        # never chase scan-block further than
                              # this behind head (deposit lives 30m)
BSC_GETLOGS_CHUNK = 500        # blocks per eth_getLogs call (node-safe)
BSC_RPC_TIMEOUT = 20           # seconds per RPC call
AMOUNT_MATCH_TOLERANCE = 0.005   # USDT value matching tolerance
_MONEY_EPS = 1e-6    # v9.35: float-noise epsilon for balance compares -
                     # 0.30 - 0.13 = 0.16999999... must still afford 0.17
EVM_MIN_CONFIRMATIONS = 3        # TXID path: min block depth (BSC/Polygon)
MAX_TXID_ATTEMPTS = 15           # wrong-TXID tries allowed per deposit order

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "bot.db")
os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)

# v9.10 deposit networks (FRIEND EDITION: TRC20 + Polygon REMOVED -
# sirf Binance Pay + BEP20. Legacy vars khali hain taaki purana
# unreachable verification code reference error na de.)
TRC20_WALLET_DEFAULT = ""
POLYGON_WALLET_DEFAULT = ""
TRC20_USDT_CONTRACT = "TR7NHqjeKotSzgjLj6t"   # USDT on Tron
POLYGON_USDT_CONTRACT = "0xc2132D05D04B58e8F"
POLYGON_RPC_ENDPOINTS = [
    "https://polygon-rpc.com",
    "https://polygon-bor-rpc.publicnode.com",
    "https://rpc.ankr.com/polygon",
]
TRONGRID_BASE = "https://api.trongrid.io"
DEPOSIT_NETWORKS = {
    # FRIEND EDITION: sirf 2 networks - Binance Pay + USDT BEP-20.
    # (TRC-20 + Polygon owner ke order pe REMOVED - entries hata di gayi
    # hain; koi purana/unknown callback ho to bep20 fallback me aa jata hai)
    "bep20":   {"label": "USDT BEP-20 (BSC)",    "short": "BEP-20 (BSC)",
                "wallet_key": "usdt_wallet_address",
                "default": None,   # falls back to usdt_wallet_address
                "scan": "https://bscscan.com/tx/"},
    # v9.32: Binance Pay - no on-chain address; the user pays the order's
    # EXACT amount to the owner's Pay ID and the payment matches by
    # ORDER ID through the official Binance Pay history API.
    "binance": {"label": "Binance Pay",          "short": "Binance Pay",
                "wallet_key": "binance_pay_id",
                "default": BINANCE_PAY_ID_DEFAULT,
                "scan": ""},
}
DEPOSIT_AMOUNT_PRESETS = [0.30, 0.50, 1.00, 3.00]


DEFAULT_SETTINGS = {
    "whatsapp_rate": "0.20",
    "telegram_rate": "0.22",
    "min_deposit": "0.20",
    "trc20_wallet_address": TRC20_WALLET_DEFAULT,
    "polygon_wallet_address": POLYGON_WALLET_DEFAULT,
    "deposit_expiry_minutes": "30",
    "usdt_wallet_address": USDT_BEP20_WALLET,
    "usdt_network": "BEP20",
    "usdt_bep20_contract": USDT_BEP20_CONTRACT,
    "bscscan_api_key": BSCSCAN_API_KEY_ENV,
    "deposit_group_id": str(DEPOSIT_GROUP_ID),
    "order_history_group_id": str(ORDER_HISTORY_GROUP_ID),
    "bot_name": "VIP Numbers Store",
    # v9.24 REFERRAL SYSTEM: per-buy commission for referrers.
    # ref_enabled "1"/"0" - OFF hides the Refer & Earn button and stops
    # every commission (VIP + normal) until the owner turns it back on.
    "ref_enabled": "1",
    "ref_rate": "0.005",
    # v9.32: the Binance Pay ID users pay TO (shown on the deposit card)
    "binance_pay_id": BINANCE_PAY_ID_DEFAULT,
    # v9.34: USER bulk-buy discount, owner-set via Admin Panel >
    # Bulk Manage (min quantity threshold + per-number $ off; 0 = OFF)
    "bulk_disc_min": "30",
    "bulk_disc_per": "0.01",
}

# v9.12: RETIRED wallets. If one of these is still stored in a
# database, init_db swaps it for the matching NEW wallet and logs
# a wallet_rotated trace event. Old addresses can never stay live.
WALLET_ROTATE = {
    "usdt_wallet_address":     {"0x837459f63a3aceb1fdb221f426a": USDT_BEP20_WALLET},
}

# (name, flag)
COUNTRIES = [
    ("USA", "\U0001F1FA\U0001F1F8"),
]

SUPPORT_USERNAME = ""
DIV = "\u2508" * 17  # ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ light divider (v9.13)

# --------------------------------------------------------------------------- #
#  BUTTON LABELS  (single source of truth for the keyboard + text router)
# --------------------------------------------------------------------------- #
BTN_BUY        = "\U0001F6D2 Buy Number"
BTN_PROFILE    = "\U0001F464 Profile"
BTN_DEPOSIT    = "\U0001F4B3 Deposit"
BTN_SUPPORT    = "\U0001F4AC Support"
BTN_ADMIN      = "\U0001F6E0\uFE0F Admin Panel"
BTN_HOME       = "\u2B05\uFE0F Back"    # v9.15: Back label, home action
BTN_BACK       = "\u2B05\uFE0F Back"
BTN_CANCEL     = "\u274C Cancel"
BTN_CANCEL_DEP = "\u274C Cancel Deposit"

BTN_WA = "\U0001F7E2 WhatsApp"
BTN_TG = "\U0001F535 Telegram"

BTN_DEP_NEW  = "\U0001F4B5 New Deposit"
BTN_DEP_HIST = "\U0001F4DC History"

BTN_ADD_STOCK   = "\U0001F4E6 Add Stock"
BTN_STOCK_STATS = "\U0001F4CA Stock Stats"
# v9.34: admin BULK MANAGE - configure the USER bulk-buy discount
# (min quantity + per-number $ off). The old v9.30 withdraw-to-file
# Bulk Buy tool is removed (owner order).
BTN_BULK_MANAGE = "\U0001F4E6 Bulk Manage"

# v9.31: USER-side Bulk Buy - buy many numbers at once, paid from the
# buyer's own balance; delivered as an otphub.<n><country>.txt file in
# the same 'phone | url' stock format. Every number gets its OWN order
# row (rate_at_purchase = discounted unit) so the owner's existing
# Refund Send flow matches and refunds each number exactly as before.
BTN_USER_BULKBUY = "\U0001F4E6 Bulk Buy"   # distinct emoji from Buy's cart
USER_BULK_MAX    = 1000      # per-request cap (loot guard)
BULK_DISCOUNT_MIN = 30       # DEFAULT min qty (settings: bulk_disc_min)
BULK_DISCOUNT     = 0.01     # DEFAULT $ off per number (bulk_disc_per)
BTN_PENDING     = "\U0001F4B0 Pending Deposits"
BTN_STATS       = "\U0001F4C8 Statistics"
BTN_SET_RATE    = "\u2699\uFE0F Set Rate"
BTN_BROADCAST   = "\U0001F4E3 Broadcast"
BTN_SET_WALLET  = "\U0001F511 Set Wallet"
BTN_BAN         = "\U0001F512 Ban/Unban"

BTN_MODIFY_USER = "\u270f\ufe0f Modify User"
# v9.27 REFUND HUB (Manage Refund -> tools); v9.40 one-tap tool
BTN_MANAGE_REFUND = "\U0001F4B8 Manage Refund"
BTN_MANAGE_ADMINS = "\U0001F465 Manage Admin"   # v9.41 (MAIN admin only)
BTN_ADMA_ADD = "\u2795 Add Admin"
BTN_ADMA_REM = "\u2796 Remove Admin"
BTN_ADMA_LIST = "\U0001F4CB List Admins"
BTN_CHECK_NUMBER = "\U0001F522 Check Number"
BTN_REFUND_SEND  = "\U0001F4B8 Refund Send"
BTN_CHECK_REFUND = "\U0001F501 Chek Number & Refund"

BTN_WA_STOCK   = "\U0001F7E2 WhatsApp Stock"
BTN_TG_STOCK   = "\U0001F535 Telegram Stock"
BTN_BAN_USER   = "\U0001F512 Ban User"
BTN_UNBAN_USER = "\U0001F513 Unban User"

# v9.16: admin Total Deposit report (reply-keyboard button, English UI)

# v9.38: ALL USER BALANCE (admin live money screen, owner order)
BTN_ALL_BAL       = "\U0001F4B5 All User Balance"
BTN_ALLBAL_REFRESH = "\U0001F504 Refresh"   # live re-read button

# v9.23: Manage Channels (force-join + broadcast destinations)
BTN_CHANNELS  = "\U0001F4E1 Manage Channels"
BTN_CH_ADD    = "\u2795 Add Channel"
BTN_CH_REMOVE = "\u2796 Remove Channel"
BTN_CH_LIST   = "\U0001F4CB List Channels"
JOIN_EMOJI_ID = "6264777724741556322"   # owner envelope icon (JOIN btns)

# v9.24: REFERRAL SYSTEM (admin Manage Reffer + user Refer & Earn)
REFER_EMOJI_ID = "5440410042773824003"  # owner icon for both refer buttons
BTN_REFER_MGMT    = "\U0001F91D Manage Reffer"
BTN_REF_PRICE     = "\U0001F4B5 Set Reffer Price"
BTN_REF_VIP       = "\U0001F451 Manage VIP"
BTN_REF_VIP_ADD   = "\u2795 Add VIP"
BTN_REF_VIP_REM   = "\u2796 Remove VIP"
BTN_REF_VIP_LIST  = "\U0001F4CB VIP List"
BTN_REF_TOGGLE_ON  = "\U0001F504 Reffer System: ON"
BTN_REF_TOGGLE_OFF = "\U0001F504 Reffer System: OFF"

# --------------------------------------------------------------------------- #
#  v9.17 LANGUAGES — 13 languages, every user-side word lives in LANGS
#  EN is the fallback: a missing key renders English, never an empty string.
#  Placeholders use str.format named fields ({amount}, {bal}, ...).
# --------------------------------------------------------------------------- #
LANGUAGES = [   # (code, native name, flag) — picker order
    ("en", "English",   "\U0001F1EC\U0001F1E7"),
    ("bn", "বাংলা",     "\U0001F1E7\U0001F1E9"),
    ("ur", "اردو",      "\U0001F1F5\U0001F1F0"),
    ("zh", "中文",       "\U0001F1E8\U0001F1F3"),
    ("ar", "العربية",   "\U0001F1F8\U0001F1E6"),
    ("id", "Indonesia", "\U0001F1EE\U0001F1E9"),
    ("tr", "Türkçe",    "\U0001F1F9\U0001F1F7"),
    ("ru", "Русский",   "\U0001F1F7\U0001F1FA"),
    ("fa", "فارسی",     "\U0001F1EE\U0001F1F7"),
    ("pt", "Português",  "\U0001F1F5\U0001F1F9"),
    ("es", "Español",    "\U0001F1EA\U0001F1F8"),
    ("sw", "Kiswahili",  "\U0001F1F0\U0001F1EA"),
    ("hi", "हिन्दी",     "\U0001F1EE\U0001F1F3"),
]
LANG_CODES = [c for c, _n, _f in LANGUAGES]
LANG_NAMES = {c: n for c, n, _f in LANGUAGES}
DEFAULT_LANG = "en"

__LANGS_SRC__ = LANGS = {
    "en": {
    "btn_buy": "🛒 Buy Number",
    "btn_profile": "👤 Profile",
    "btn_deposit": "💳 Deposit",
    "btn_support": "💬 Support",
    "btn_back": "⬅️ Back",
    "btn_cancel_dep": "❌ Cancel Deposit",
    "btn_wa": "🟢 WhatsApp",
    "btn_tg": "🔵 Telegram",
    "btn_dep_new": "💵 New Deposit",
    "btn_dep_hist": "📜 History",
    "btn_custom_amount": "✏️ Custom Amount",
    "btn_i_paid": "✅ I PAID — Send TXID",
    "btn_get_otp": "📩 Get OTP",
    "btn_buy_now": "✅ Buy — ${price}",
    "kb_placeholder": "Choose an option 👇",
    "menu_title": "🏠 <b>Main Menu</b>",
    "menu_where": "👉 Where to next?",
    "menu_footer": "✅ Done! You're back at the main menu 👇",
    "blocked": "🔒 <b>Access blocked</b>\nThis account can't use the bot anymore.",
    "lang_pick_title": "🌐 <b>Choose Your Language</b>",
    "lang_pick_hint": "👉 Tap your language to continue",
    "lang_set_ok": "✅ Language set: {lang}",
    "lang_current": "🌐 Current language: <b>{lang}</b>\nTap a language below to switch.",
    "welcome_hi": "👋 <b>Hey {name}, welcome back!</b>",
    "welcome_tagline": "📱 Premium WhatsApp &amp; Telegram numbers\n⚡ Instant delivery • OTP included",
    "welcome_balance": "💰 Balance: <code>${bal}</code>",
    "welcome_stock": "📦 In Stock: <code>{total}</code> numbers",
    "welcome_cta": "👉 Tap a button below to get started",
    "profile_title": "👤 <b>Your Profile</b>",
    "lbl_id": "🆔 ID:",
    "lbl_name": "📝 Name:",
    "lbl_username": "🌐 Username:",
    "prof_purchased": "🛒 Purchased: <code>{n}</code>",
    "prof_spent": "💸 Spent: <code>${amount}</code>",
    "prof_deposited": "🏦 Deposited: <code>${amount}</code>",
    "prof_otps": "📩 OTPs: <code>{n} ({pct})</code>",
    "support_title": "💬 <b>Need Help?</b>",
    "support_admin": "👨‍💻 Admin: {handle}",
    "support_time": "⚡ Reply time: usually just minutes",
    "support_body": "Payments, OTP issues, stock questions — just message us, we've got you. 🙌",
    "buy_title": "🛒 <b>Buy a Number</b>",
    "buy_wa_price": "🟢 WhatsApp — <code>${wa}</code>",
    "buy_tg_price": "🔵 Telegram — <code>${tg}</code>",
    "buy_pick": "👉 Pick a type to continue",
    "ctry_title": "🌍 <b>Choose a Country</b>",
    "ctry_avail": "📱 {label} numbers available",
    "cta_select": "👉 Select below",
    "confirm_title": "🧾 <b>Confirm Your Order</b>",
    "cf_type": "📱 Type: {label}",
    "cf_country": "🌍 Country: {flag} {country}",
    "cf_price": "💵 Price: <code>${rate}</code>",
    "cf_balance": "💰 Your Balance: <code>${bal}</code>",
    "cf_cta": "👉 All good? Confirm below",
    "ps_title": "✅ <b>Purchase Complete!</b>",
    "ps_number": "📱 Number: <code>{number}</code>",
    "ps_label": "🏷️ {label} • {flag} {country}",
    "ps_paid": "💵 Paid: <code>${rate}</code>",
    "ps_order": "🧾 Order: <code>{order}</code>",
    "ps_get_otp": "📩 Tap <b>Get OTP</b> below anytime to fetch your code",
    "ps_copy": "📋 Tap the number to copy it",
    "ins_title": "⚠️ <b>Not Enough Balance</b>",
    "ins_price": "💵 Price: <code>${rate}</code>",
    "ins_balance": "💰 Balance: <code>${bal}</code>",
    "ins_need": "❗ You need: <code>${need}</code> more",
    "ins_cta": "👉 Top up in one tap",
    "oos_title": "❌ <b>Out of Stock</b>",
    "oos_label": "🏷️ {label} — {flag} {country}",
    "oos_cta": "👉 Try another country, or ping 💬 Support",
    "otp_received": "🎉 <b>OTP Received!</b>",
    "otp_waiting": "⏳ <b>Still Waiting on the OTP</b>",
    "otp_waiting_body": "SMS can take a moment — we're still checking in the background. It'll land here automatically. 👀",
    "otp_blocked": "🔒 <b>OTP Blocked</b>",
    "otp_blocked_body": "This number was refunded — OTP can never arrive here again.",
    "toast_no_link": "ℹ️ No OTP link on this number — contact support",
    "otp_timeout": "⏳ <b>No OTP After 10 Minutes</b>",
    "otp_timeout_body": "SMS delays happen. Tap 🔑 <b>Get OTP</b> on your receipt to check again anytime.",
    "toast_not_yours": "❌ Not your number",
    "toast_not_found": "❌ Number not found",
    "dep_title": "💳 <b>Deposit</b>",
    "dep_min_line": "💵 Min: <code>${min}</code> • TXID-verified 🔐",
    "dep_min_only": "💵 Min: <code>${min}</code>",
    "cta_pick": "👉 Pick an option",
    "dep_amt_title": "💰 <b>Select an Amount</b>",
    "dep_amt_hint": "👉 Tap an amount, or go ✏️ Custom",
    "dep_net_title": "🌐 <b>Select Network</b>",
    "dep_net_amount": "💵 <code>${amount}</code> USDT",
    "dep_net_hint": "👉 Tap your network",
    "dep_hist_title": "📜 <b>Deposit History</b>",
    "dep_hist_empty": "No deposits yet — your first one will show up here.",
    "dep_min_warn": "⚠️ Minimum deposit is <code>${min}</code>\n👉 Choose again below",
    "custom_title": "✏️ <b>Type Your Amount</b>\n💵 In USDT — min <code>${min}</code>\nExample: <code>1.50</code>",
    "custom_err": "❌ Minimum deposit is <code>${min}</code>\n💵 Type the USDT amount again\nExample: <code>1.50</code>",
    "card_send": "💸 <b>Send ${amount} USDT</b>",
    "card_network": "🌐 Network: <b>{net}</b>",
    "card_address": "📍 Address (tap to copy):",
    "card_warn": "⚠️ <b>{net}</b> only — wrong network = funds lost.",
    "card_paid": "✅ Paid? Tap <b>I PAID</b> → send your TXID next.",
    "card_expire": "🧾 <code>{dep_id}</code> • expires {expires} ⏳",
    "txid_title": "🔑 <b>Paste Your {net} TXID</b>",
    "txid_body": "📋 The transaction hash of your payment.",
    "txid_format": "Format: <code>{fmt}</code>",
    "txid_ok_line": "✅ Verified → instant credit",
    "txid_no_line": "❌ No TXID → no credit",
    "dep_cancelled": "❌ <b>Deposit cancelled.</b>",
    "dep_expired_session": "ℹ️ Session expired.\nStart a fresh deposit from the menu.",
    "dep_no_active": "ℹ️ No active deposit order found.\nStart a fresh deposit from the menu.",
    "dep_closed": "ℹ️ This deposit order is already closed.\nStart a fresh one from the menu.",
    "toast_bad_amount": "❌ Invalid amount",
    "scr_needed": "❌ <b>No screenshot needed.</b>\nPlease send your <b>TXID</b> (the transaction hash) as text.",
    "txid_bad_fmt": "❌ <b>Invalid TXID format</b>\n{net} needs <code>{fmt}</code>. Copy the full hash from your wallet.",
    "dep_checking": "⏳ Checking your {net} transaction...",
    "dep_locked": "🔒 Order locked — too many wrong TXIDs.\nContact admin with order ID <code>{order}</code>.",
    "txid_replay": "🔁 This TXID was already used.\nOne TXID = one order. Send your new transaction hash.",
    "bin_pay_id": "🏦 <b>Binance Pay ID</b> - send TO this ID:",
    "bin_card_hint": "⚠️ Pay via the <b>Binance app → Pay</b>\n💵 Send <b>USDT only</b>, the exact amount above.\n❌ Wrong ID or asset = money lost.",
    "bin_auto_line": "⚡ Payment auto-verifies in ~1 minute.\nOr tap I PAID and paste the Order ID.",
    "bin_txid_title": "🔑 <b>Paste Your Binance Pay Order ID</b>",
    "bin_txid_body": "📋 Binance app → Pay → open your transfer → copy the <b>Order ID</b> and paste it here.",
    "bin_bad_fmt": "❌ <b>That is not a Binance Pay Order ID.</b>\nIt looks like <code>M_P_123456789012345678</code> - copy it from Binance app → Pay → transfer details.",
    "bin_amt_mismatch": "❌ <b>Amount mismatch.</b>\nPayment shows <code>${got}</code>, this order needs <code>${want}</code>.\nPay the exact amount, then paste that Order ID.",
    "bin_decline_pending": "⏳ No payment found for this Order ID yet.\nPay first, double-check the Order ID, and send it again in a minute.",
    "bin_decline_stale": "❌ This Order ID cannot be used for this order.\nIt is older than the order or already spent.\nPay fresh and paste the new Order ID.",
    "bin_decline_out": "❌ That is an OUTGOING transfer - you sent money away.\nPaste the Order ID of the transfer you SENT TO us.",
    "dep_api_busy": "⏳ Binance verification is busy right now.\nYour order is safe - please try again in a minute.",
    "amt_mismatch": "❌ <b>Amount mismatch.</b>\nTransaction shows <code>${got}</code>, order needs <code>${want}</code>.\nSend the correct hash, or start a fresh deposit.",
    "dep_already": "✅ This deposit was already confirmed.\nYour balance is already up to date.",
    "dep_ok_title": "✅ <b>Deposit Confirmed!</b>",
    "dep_ok_credited": "💵 Credited: <code>${amount}</code>",
    "dep_ok_balance": "💰 Balance: <code>${bal}</code>",
    "dep_ok_cta": "🛒 Happy shopping — tap Buy below!",
    "decline_pending": "⏳ Transaction not found on {net} yet.\nDouble-check the TXID and send it again in a minute.",
    "decline_failed": "❌ Transaction failed on-chain — no funds moved.\nSend a new, successful TXID.",
    "decline_token": "❌ That wasn't a USDT transfer on {net}.\nPlease send USDT only.",
    "decline_recipient": "❌ Wrong recipient.\nThis TXID didn't send USDT to our {net} address.",
    "dm_credited": "✅ Credited <code>${amount}</code> • Balance <code>${bal}</code>\n🧾 Order <code>{order}</code>",
    "dm_dep_confirmed": "✅ <b>DEPOSIT CONFIRMED</b>\n\n{div}\n💵 <b>Amount:</b> ${amount}\n🧾 <b>Order:</b> <code>{order}</code>\n{div}\n\n💰 <b>Balance updated! Happy shopping 🛒</b>",
    "dm_dep_rejected": "❌ <b>DEPOSIT REJECTED</b>\n\n{div}\n🧾 <b>Order:</b> <code>{order}</code>\n{div}\n\n💬 Contact Support if you think this is an error.",
    "help_title": "📖 <b>Quick Help</b>",
    "help_lines": "/start — open main menu\n/menu — show main menu\n/language — change language\n/admin — admin panel",
    "help_cta": "💡 Everything's just a tap away on the buttons below.",
    "err_generic": "⚠️ <b>Something went wrong.</b>\nPlease try again — or press /start.",
    "toast_processing": "Processing your purchase... ⏳",
    "toast_invalid": "Invalid request",
    "toast_expired": "❌ This button expired — please retry",
    "btn_join_channel": "✉️ JOIN CHANNEL",
    "btn_join_group": "✉️ JOIN GROUP",
    "fj_title": "🔒 <b>One Step to Unlock</b>",
    "fj_body": "👉 Join our channel below to use the bot.\n✅ After joining, tap <b>Verify</b>.",
    "btn_fj_check": "✅ Verify",
    "fj_toast_no": "❌ You have not joined yet — join, then tap Verify.",
    "fj_done": "✅ <b>Verified!</b>\n🎉 Welcome — your main menu is unlocked below 👇",
    "fj_dm": "✅ <b>Join verified!</b>\n👋 Welcome — main menu unlocked 👇",
    "btn_refer": "🎁 Refer & Earn",
    "btn_active": "📱 Active Numbers",
    "btn_ubulk": "📦 Bulk Buy",
    "ub_pick": "📦 <b>Bulk Buy</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> available • <code>${wa_rate}</code> each\n🔵 Telegram — <code>{tg_n}</code> available • <code>${tg_rate}</code> each\n\n🎁 <b>{dmin}+ numbers = ${damt} less per number</b>\n\n👉 Pick a type:",
    "ub_qty": "📦 <b>Bulk Buy — {label}</b>\n\n📱 Available: <code>{n}</code> numbers\n💵 Rate: <code>${rate}</code> per number\n💰 Balance: <code>${bal}</code>\n\n🎁 {dmin}+ = <b>${damt} off per number</b>\n\n👉 Type HOW MANY numbers you want:",
    "ub_bad_qty": "❌ Please type a plain NUMBER (1 to {cap}).\n👉 Try again:",
    "ub_stock_low": "⚠️ Only <code>{n}</code> available right now.\n👉 Type a smaller quantity:",
    "ub_no_bal": "⚠️ {n} numbers = <code>${total}</code>\n💰 Balance: <code>${bal}</code>\n👉 Max affordable: <code>{maxn}</code> numbers. Type that (or less):",
    "ub_confirm": "🧾 <b>Confirm Bulk Order</b>\n\n{div}\n📱 Type: <b>{label}</b>\n🔢 Numbers: <code>{n}</code>\n💵 Rate: <code>${unit}</code> each {disc}\n💰 Total: <code>${total}</code>\n💰 After: <code>${after}</code>\n{div}\n\n👉 Confirm below — the .txt file arrives instantly.",
    "ub_disc": "({dmin}+ discount ✅)",
    "ub_expired": "⏳ Session expired — start again from 📦 Bulk Buy.",
    "ub_done": "✅ <b>Bulk Order Complete!</b>\n\n{div}\n📱 Numbers delivered: <code>{n}</code>\n💵 Paid: <code>${total}</code> (<code>${unit}</code> each {disc})\n💰 Balance: <code>${bal}</code>\n{div}\n\n📎 <code>{fname}</code> attached — every number with its OTP API link.\n📩 Each OTP lands in this chat automatically the moment it arrives.\n📱 Track them anytime under 📱 Active Numbers.",
    "ub_partial": "⚠️ Stock moved fast — only <code>{n}</code> were available. You were charged for <code>{n}</code> only.",
    "ub_none": "❌ <b>Out of stock</b> — nothing was charged.",
    "ub_hint_file": "❌ That\'s a file — here I need a NUMBER.\n👉 Type HOW MANY numbers you want:",
    "act_title": "📞 <b>Your Active Numbers</b> ({n})",
    "act_none": "📭 You have no active numbers right now.\n🛒 Buy a number — it appears here instantly.",
    "act_hint": "▶️ Tap any number to copy it, then send it here — the number opens with its Get OTP button.",
    "act_more": "…and {extra} more",
    "act_card_title": "🟢 <b>Your Active Number</b>",
    "act_card_body": "📩 Tap GET OTP any time — the code reaches you the moment it arrives. No time limit.",
    "rfs_title": "🎉 <b>Your Refund Successfully</b>",
    "rfs_body": "🟢 <code>{number}</code>\n💰 <code>${amount}</code> added to your balance",
    "ref_title": "🤝 <b>Refer &amp; Earn</b>",
    "ref_body": "Share your link — you earn <b>${rate}</b> every time a friend buys a number. For life.",
    "ref_link": "🔗 Your referral link:",
    "ref_stats": "👥 Referred: <b>{count}</b>\n💰 Total earned: <b>${earned}</b>",
    "ref_rate_line": "💵 Your rate: <b>${rate}</b> per buy",
    "ref_vip_line": "👑 <b>VIP referrer</b> — special rate <b>${rate}</b> per buy",
    "btn_ref_share": "📤 Share Link",
    "ref_share_text": "🎁 Premium WhatsApp & Telegram numbers — instant OTP!",
    "ref_none_yet": "No referrals yet — share your link to start earning 👇",
    "ref_earned_notif": "🎉 <b>Referral Bonus!</b>\n{div}\n👤 {name} bought a number\n💰 <b>+${amount}</b> added to your balance\n💼 Balance: <b>${bal}</b>\n{div}",
    "ref_new_ref": "👥 <b>New referral!</b>\n👤 {name} joined with your link\n💰 You earn on every purchase they make",
    "ref_paused": "⏸ The referral program is paused right now.\n💡 Check back soon!",
},

    "bn": {
    "btn_buy": "🛒 নম্বর কিনুন",
    "btn_profile": "👤 প্রোফাইল",
    "btn_deposit": "💳 ডিপোজিট",
    "btn_support": "💬 সাপোর্ট",
    "btn_back": "⬅️ পেছনে",
    "btn_cancel_dep": "❌ ডিপোজিট বাতিল",
    "btn_wa": "🟢 WhatsApp",
    "btn_tg": "🔵 Telegram",
    "btn_dep_new": "💵 নতুন ডিপোজিট",
    "btn_dep_hist": "📜 হিস্টোরি",
    "btn_custom_amount": "✏️ কাস্টম অ্যামাউন্ট",
    "btn_i_paid": "✅ পেমেন্ট করেছি — TXID পাঠান",
    "btn_get_otp": "📩 OTP নিন",
    "btn_buy_now": "✅ কিনুন — ${price}",
    "kb_placeholder": "একটি অপশন বেছে নিন 👇",
    "menu_title": "🏠 <b>মেইন মেনু</b>",
    "menu_where": "👉 এখন কোথায় যেতে চান?",
    "menu_footer": "✅ হয়ে গেছে! আপনি আবার মেইন মেনুতে 👇",
    "blocked": "🔒 <b>প্রবেশ বন্ধ</b>\nএই অ্যাকাউন্ট আর বট ব্যবহার করতে পারবে না।",
    "lang_pick_title": "🌐 <b>আপনার ভাষা বেছে নিন</b>",
    "lang_pick_hint": "👉 চালিয়ে যেতে আপনার ভাষায় ট্যাপ করুন",
    "lang_set_ok": "✅ ভাষা সেট হয়েছে: {lang}",
    "lang_current": "🌐 বর্তমান ভাষা: <b>{lang}</b>\nবদলাতে নিচের কোনো ভাষায় ট্যাপ করুন।",
    "welcome_hi": "👋 <b>হে {name}, আবার স্বাগতম!</b>",
    "welcome_tagline": "📱 প্রিমিয়াম WhatsApp ও Telegram নম্বর\n⚡ সাথে সাথে ডেলিভারি • OTP সহ",
    "welcome_balance": "💰 ব্যালেন্স: <code>${bal}</code>",
    "welcome_stock": "📦 স্টকে আছে: <code>{total}</code>টি নম্বর",
    "welcome_cta": "👉 শুরু করতে নিচের বাটনে ট্যাপ করুন",
    "profile_title": "👤 <b>আপনার প্রোফাইল</b>",
    "lbl_id": "🆔 আইডি:",
    "lbl_name": "📝 নাম:",
    "lbl_username": "🌐 ইউজারনেম:",
    "prof_purchased": "🛒 কেনা হয়েছে: <code>{n}</code>",
    "prof_spent": "💸 খরচ: <code>${amount}</code>",
    "prof_deposited": "🏦 জমা: <code>${amount}</code>",
    "prof_otps": "📩 OTP: <code>{n} ({pct})</code>",
    "support_title": "💬 <b>সাহায্য দরকার?</b>",
    "support_admin": "👨‍💻 অ্যাডমিন: {handle}",
    "support_time": "⚡ উত্তরের সময়: সাধারণত কয়েক মিনিট",
    "support_body": "পেমেন্ট, OTP সমস্যা বা স্টক নিয়ে প্রশ্ন — শুধু আমাদের মেসেজ দিন, আমরা পাশে আছি। 🙌",
    "buy_title": "🛒 <b>নম্বর কিনুন</b>",
    "buy_wa_price": "🟢 WhatsApp — <code>${wa}</code>",
    "buy_tg_price": "🔵 Telegram — <code>${tg}</code>",
    "buy_pick": "👉 চালিয়ে যেতে একটি ধরন বেছে নিন",
    "ctry_title": "🌍 <b>দেশ বেছে নিন</b>",
    "ctry_avail": "📱 {label} নম্বর স্টকে আছে",
    "cta_select": "👉 নিচে বেছে নিন",
    "confirm_title": "🧾 <b>অর্ডার নিশ্চিত করুন</b>",
    "cf_type": "📱 ধরন: {label}",
    "cf_country": "🌍 দেশ: {flag} {country}",
    "cf_price": "💵 দাম: <code>${rate}</code>",
    "cf_balance": "💰 আপনার ব্যালেন্স: <code>${bal}</code>",
    "cf_cta": "👉 সব ঠিক আছে? নিচে নিশ্চিত করুন",
    "ps_title": "✅ <b>কেনা সম্পন্ন!</b>",
    "ps_number": "📱 নম্বর: <code>{number}</code>",
    "ps_label": "🏷️ {label} • {flag} {country}",
    "ps_paid": "💵 পরিশোধ: <code>${rate}</code>",
    "ps_order": "🧾 অর্ডার: <code>{order}</code>",
    "ps_get_otp": "📩 যখন দরকার নিচে <b>Get OTP</b> ট্যাপ করে কোড নিন",
    "ps_copy": "📋 কপি করতে নম্বরে ট্যাপ করুন",
    "ins_title": "⚠️ <b>পর্যাপ্ত ব্যালেন্স নেই</b>",
    "ins_price": "💵 দাম: <code>${rate}</code>",
    "ins_balance": "💰 ব্যালেন্স: <code>${bal}</code>",
    "ins_need": "❗ আরও দরকার: <code>${need}</code>",
    "ins_cta": "👉 এক ট্যাপে টাকা যোগ করুন",
    "oos_title": "❌ <b>স্টক শেষ</b>",
    "oos_label": "🏷️ {label} — {flag} {country}",
    "oos_cta": "👉 অন্য দেশ দেখুন, বা 💬 সাপোর্টে জানান",
    "otp_received": "🎉 <b>OTP পেয়েছেন!</b>",
    "otp_waiting": "⏳ <b>OTP-র অপেক্ষায়</b>",
    "otp_waiting_body": "SMS-এ একটু সময় লাগতে পারে — আমরা পেছনে চেক করছি। এটি এখানে নিজে থেকেই আসবে। 👀",
    "otp_blocked": "🔒 <b>OTP বন্ধ</b>",
    "otp_blocked_body": "এই নম্বরে রিফান্ড হয়ে গেছে — এখানে আর কখনও OTP আসবে না।",
    "toast_no_link": "ℹ️ এই নম্বরে OTP লিংক নেই — সাপোর্টে যোগাযোগ করুন",
    "otp_timeout": "⏳ <b>১০ মিনিটে OTP আসেনি</b>",
    "otp_timeout_body": "SMS-এ দেরি হয়। রিসিটের 🔑 <b>Get OTP</b> ট্যাপ করে যখন চান আবার চেক করুন।",
    "toast_not_yours": "❌ এটি আপনার নম্বর নয়",
    "toast_not_found": "❌ নম্বর পাওয়া যায়নি",
    "dep_title": "💳 <b>ডিপোজিট</b>",
    "dep_min_line": "💵 সর্বনিম্ন: <code>${min}</code> • TXID-যাচাই 🔐",
    "dep_min_only": "💵 সর্বনিম্ন: <code>${min}</code>",
    "cta_pick": "👉 একটি অপশন বেছে নিন",
    "dep_amt_title": "💰 <b>অ্যামাউন্ট বেছে নিন</b>",
    "dep_amt_hint": "👉 অ্যামাউন্টে ট্যাপ করুন, বা ✏️ কাস্টম",
    "dep_net_title": "🌐 <b>নেটওয়ার্ক বেছে নিন</b>",
    "dep_net_amount": "💵 <code>${amount}</code> USDT",
    "dep_net_hint": "👉 আপনার নেটওয়ার্কে ট্যাপ করুন",
    "dep_hist_title": "📜 <b>ডিপোজিট হিস্টোরি</b>",
    "dep_hist_empty": "এখনও কোনো ডিপোজিট নেই — প্রথমটি এখানে দেখা যাবে।",
    "dep_min_warn": "⚠️ সর্বনিম্ন ডিপোজিট <code>${min}</code>\n👉 নিচে আবার বেছে নিন",
    "custom_title": "✏️ <b>অ্যামাউন্ট লিখুন</b>\n💵 USDT-তে — সর্বনিম্ন <code>${min}</code>\nউদাহরণ: <code>1.50</code>",
    "custom_err": "❌ সর্বনিম্ন ডিপোজিট <code>${min}</code>\n💵 আবার USDT অ্যামাউন্ট লিখুন\nউদাহরণ: <code>1.50</code>",
    "card_send": "💸 <b>${amount} USDT পাঠান</b>",
    "card_network": "🌐 নেটওয়ার্ক: <b>{net}</b>",
    "card_address": "📍 অ্যাড্রেস (কপি করতে ট্যাপ):",
    "card_warn": "⚠️ শুধু <b>{net}</b> — ভুল নেটওয়ার্ক = টাকা হারাবে।",
    "card_paid": "✅ পেমেন্ট করেছেন? <b>I PAID</b> ট্যাপ করুন → এরপর TXID পাঠান।",
    "card_expire": "🧾 <code>{dep_id}</code> • শেষ হবে {expires} ⏳",
    "txid_title": "🔑 <b>আপনার {net} TXID পেস্ট করুন</b>",
    "txid_body": "📋 আপনার পেমেন্টের ট্রানজেকশন হ্যাশ।",
    "txid_format": "ফরম্যাট: <code>{fmt}</code>",
    "txid_ok_line": "✅ ভেরিফাই হলে → সাথে সাথে ব্যালেন্স",
    "txid_no_line": "❌ TXID ছাড়া → কোনো ব্যালেন্স নেই",
    "dep_cancelled": "❌ <b>ডিপোজিট বাতিল হয়েছে।</b>",
    "dep_expired_session": "ℹ️ সেশন শেষ।\nমেনু থেকে নতুন ডিপোজিট শুরু করুন।",
    "dep_no_active": "ℹ️ কোনো চালু ডিপোজিট পাওয়া যায়নি।\nমেনু থেকে নতুন ডিপোজিট শুরু করুন।",
    "dep_closed": "ℹ️ এই ডিপোজিট অর্ডার আগেই বন্ধ হয়ে গেছে।\nমেনু থেকে নতুনটি শুরু করুন।",
    "toast_bad_amount": "❌ অ্যামাউন্ট ভুল",
    "scr_needed": "❌ <b>স্ক্রিনশট লাগবে না।</b>\nঅনুগ্রহ করে আপনার <b>TXID</b> (ট্রানজেকশন হ্যাশ) লেখা হিসেবে পাঠান।",
    "txid_bad_fmt": "❌ <b>TXID ফরম্যাট ভুল</b>\n{net}-এ লাগবে <code>{fmt}</code>। ওয়ালেট থেকে পুরো হ্যাশ কপি করুন।",
    "dep_checking": "⏳ আপনার {net} ট্রানজেকশন চেক করা হচ্ছে...",
    "dep_locked": "🔒 অর্ডার লক — অনেকবার ভুল TXID।\nঅর্ডার আইডি <code>{order}</code> দিয়ে অ্যাডমিনের সাথে যোগাযোগ করুন।",
    "txid_replay": "🔁 এই TXID আগে ব্যবহার হয়েছে।\nএক TXID = এক অর্ডার। নতুন ট্রানজেকশন হ্যাশ পাঠান।",
    "bin_pay_id": "🏦 <b>Binance Pay ID</b> - এই ID-তে পাঠান:",
    "bin_card_hint": "⚠️ <b>Binance app → Pay</b> দিয়ে পেমেন্ট করুন\n💵 শুধু <b>USDT</b>, উপরের ঠিক পরিমাণ পাঠান।\n❌ ভুল ID বা অন্য কয়েন = টাকা হারাবেন।",
    "bin_auto_line": "⚡ পেমেন্ট প্রায় ১ মিনিটে অয়টো-ভেরিফাই হয়।\nঅথবা I PAID চেপে Order ID পাঠান।",
    "bin_txid_title": "🔑 <b>আপনার Binance Pay Order ID পাঠান</b>",
    "bin_txid_body": "📋 Binance app → Pay → আপনার ট্রান্সফার খুলুন → <b>Order ID</b> কপি করে এখানে পাঠান।",
    "bin_bad_fmt": "❌ <b>এটা Binance Pay Order ID নয়।</b>\nএটা এমন দেখায়: <code>M_P_123456789012345678</code> - Binance app → Pay → transfer details থেকে কপি করুন।",
    "bin_amt_mismatch": "❌ <b>পরিমাণ মেলেনি।</b>\nপেমেন্ট দেখাচ্ছে <code>${got}</code>, অর্ডার দরকার <code>${want}</code>।\nঠিক পরিমাণ পাঠিয়ে সেই Order ID পাঠান।",
    "bin_decline_pending": "⏳ এই Order ID-র কোনো পেমেন্ট পাওয়া যায়নি।\nআগে পেমেন্ট করুন, Order ID মিলিয়ে এক মিনিট পর আবার পাঠান।",
    "bin_decline_stale": "❌ এই Order ID এই অর্ডারে ব্যবহার করা যাবে না।\nএটা অর্ডারের চেয়ে পুরানো বা আগেই খরচ হয়ে গেছে।\nনতুন পেমেন্ট করে নতুন Order ID পাঠান।",
    "bin_decline_out": "❌ এটা একটা OUTGOING ট্রান্সফার - টাকা বাইরে গেছে।\nআমাদের কাছে পাঠানো ট্রান্সফারের Order ID পাঠান।",
    "dep_api_busy": "⏳ Binance যাচাই এখন ব্যস্ত।\nআপনার অর্ডার নিরাপদ - এক মিনিট পর আবার চেষ্টা করুন।",
    "amt_mismatch": "❌ <b>অ্যামাউন্ট মেলেনি।</b>\nট্রানজেকশনে আছে <code>${got}</code>, অর্ডারে দরকার <code>${want}</code>।\nসঠিক হ্যাশ পাঠান, বা নতুন ডিপোজিট শুরু করুন।",
    "dep_already": "✅ এই ডিপোজিট আগেই কনফার্ম হয়েছে।\nআপনার ব্যালেন্স আগেই আপডেট।",
    "dep_ok_title": "✅ <b>ডিপোজিট কনফার্ম!</b>",
    "dep_ok_credited": "💵 যোগ হয়েছে: <code>${amount}</code>",
    "dep_ok_balance": "💰 ব্যালেন্স: <code>${bal}</code>",
    "dep_ok_cta": "🛒 আনন্দে কেনাকাটা করুন — নিচে Buy ট্যাপ করুন!",
    "decline_pending": "⏳ {net}-এ ট্রানজেকশন এখনও পাওয়া যায়নি।\nTXID আবার দেখে এক মিনিট পর পাঠান।",
    "decline_failed": "❌ ট্রানজেকশন চেইনে ব্যর্থ — টাকা যায়নি।\nনতুন, সফল TXID পাঠান।",
    "decline_token": "❌ এটা {net}-এ USDT ট্রানজেকশন নয়।\nশুধু USDT পাঠান।",
    "decline_recipient": "❌ প্রাপক ভুল।\nএই TXID-এ আমাদের {net} অ্যাড্রেসে USDT যায়নি।",
    "dm_credited": "✅ যোগ হয়েছে <code>${amount}</code> • ব্যালেন্স <code>${bal}</code>\n🧾 অর্ডার <code>{order}</code>",
    "dm_dep_confirmed": "✅ <b>ডিপোজিট কনফার্ম</b>\n\n{div}\n💵 <b>অ্যামাউন্ট:</b> ${amount}\n🧾 <b>অর্ডার:</b> <code>{order}</code>\n{div}\n\n💰 <b>ব্যালেন্স আপডেট! আনন্দে কেনাকাটা 🛒</b>",
    "dm_dep_rejected": "❌ <b>ডিপোজিট বাতিল</b>\n\n{div}\n🧾 <b>অর্ডার:</b> <code>{order}</code>\n{div}\n\n💬 ভুল মনে হলে সাপোর্টে যোগাযোগ করুন।",
    "help_title": "📖 <b>কুইক হেল্প</b>",
    "help_lines": "/start — মেইন মেনু\n/menu — মেনু দেখান\n/language — ভাষা বদলান\n/admin — অ্যাডমিন প্যানেল",
    "help_cta": "💡 সবকিছু নিচের বাটনে এক ট্যাপ দূরে।",
    "err_generic": "⚠️ <b>কিছু একটা সমস্যা হয়েছে।</b>\nআবার চেষ্টা করুন — বা /start চাপুন।",
    "toast_processing": "প্রসেস হচ্ছে... ⏳",
    "toast_invalid": "অনুরোধ ভুল",
    "toast_expired": "❌ এই বাটনের মেয়াদ শেষ — আবার চেষ্টা করুন",
    "btn_join_channel": "✉️ চ্যানেলে জয়েন করুন",
    "btn_join_group": "✉️ গ্রুপে জয়েন করুন",
    "fj_title": "🔒 <b>আনলক করতে একটি ধাপ বাকি</b>",
    "fj_body": "👉 বট ব্যবহার করতে নিচের চ্যানেলে জয়েন করুন।\n✅ জয়েন করার পর <b>ভেরিফাই</b> ট্যাপ করুন।",
    "btn_fj_check": "✅ ভেরিফাই",
    "fj_toast_no": "❌ আপনি এখনো জয়েন করেননি — জয়েন করে আবার ভেরিফাই ট্যাপ করুন।",
    "fj_done": "✅ <b>ভেরিফাই সম্পন্ন!</b>\n🎉 স্বাগতম — নিচে আপনার মেইন মেনু আনলক হয়েছে 👇",
    "fj_dm": "✅ <b>জয়েন ভেরিফাইড!</b>\n👋 স্বাগতম — মেইন মেনু আনলক 👇",
    "btn_refer": "🎁 রেফার ও আয় করুন",
    "btn_active": "📱 সক্রিয় নম্বর",
    "btn_ubulk": "📦 বাল্ক কিনুন",
    "ub_pick": "📦 <b>বাল্ক কিনুন</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> আছে • প্রতি টেগ <code>${wa_rate}</code>\n🔵 Telegram — <code>{tg_n}</code> আছে • প্রতি টেগ <code>${tg_rate}</code>\n\n🎁 <b>{dmin}+ নম্বর = প্রতি টেগ ${damt} ছাড়</b>\n\n👉 টাইপ বাছুন:",
    "ub_qty": "📦 <b>বাল্ক কিনুন — {label}</b>\n\n📱 আছে: <code>{n}</code> নম্বর\n💵 রেট: প্রতি নম্বর <code>${rate}</code>\n💰 ব্যালেন্স: <code>${bal}</code>\n\n🎁 {dmin}+ = প্রতি নম্বরে <b>${damt} ছাড়</b>\n\n👉 কত নম্বর চান লিখুন:",
    "ub_bad_qty": "❌ শুধু নম্বর লিখুন (1 থেকে {cap})।\n👉 আবার চেষ্টা করুন:",
    "ub_stock_low": "⚠️ এখন মাত্র <code>{n}</code> আছে।\n👉 কম সংখ্যা লিখুন:",
    "ub_no_bal": "⚠️ {n} নম্বর = <code>${total}</code>\n💰 ব্যালেন্স: <code>${bal}</code>\n👉 সর্বোচ্চ <code>{maxn}</code> নম্বর নিতে পারবেন। তা লিখুন:",
    "ub_confirm": "🧾 <b>কনফার্ম করুন</b>\n\n{div}\n📱 টাইপ: <b>{label}</b>\n🔢 নম্বর: <code>{n}</code>\n💵 রেট: প্রতি টেগ <code>${unit}</code> {disc}\n💰 মোট: <code>${total}</code>\n💰 পরে: <code>${after}</code>\n{div}\n\n👉 নিচে Confirm করুন — .txt ফাইল সাথে আসবে।",
    "ub_disc": "({dmin}+ ছাড় ✅)",
    "ub_expired": "⏳ সেশন শেষ — 📦 বাল্ক কিনুন থেকে আবার শুরু করুন।",
    "ub_done": "✅ <b>বাল্ক অর্ডার সম্পন্ন!</b>\n\n{div}\n📱 নম্বর: <code>{n}</code>\n💵 পেইড: <code>${total}</code> (প্রতি টেগ <code>${unit}</code> {disc})\n💰 ব্যালেন্স: <code>${bal}</code>\n{div}\n\n📎 <code>{fname}</code> ফাইলে প্রতি নম্বরের OTP API লিঙ্ক আছে।\n📩 প্রতিটি OTP আসামাত্র এই চ্যাটে চলে আসবে।\n📱 📱 Active Numbers এ সব ট্রাক করুন।",
    "ub_partial": "⚠️ স্টক দ্রুত শেষ — মাত্র <code>{n}</code> ছিল। শুধু <code>{n}</code> এর জন্য চার্জ হয়েছে।",
    "ub_none": "❌ <b>স্টক নেই</b> — কোন টাকা কাটা হয়নি।",
    "ub_hint_file": "❌ এটা ফাইল — এখানে নম্বর লাগবে।\n👉 কত নম্বর চান লিখুন:",
    "act_title": "📞 <b>আপনার সক্রিয় নম্বর</b> ({n})",
    "act_none": "📭 এখন আপনার কোনো সক্রিয় নম্বর নেই।\n🛒 নম্বর কিনুন — এখানে সাথে সাথে দেখা যাবে।",
    "act_hint": "▶️ কপি করতে যেকোনো নম্বরে ট্যাপ করুন, তারপর এখানে পাঠান — Get OTP বোতামসহ নম্বর খুলে যাবে।",
    "act_more": "…আরও {extra}টি",
    "act_card_title": "🟢 <b>আপনার সক্রিয় নম্বর</b>",
    "act_card_body": "📩 যখনই ইচ্ছা GET OTP চাপুন — OTP আসার মুহূর্তেই পাবেন। কোনো সময়সীমা নেই।",
    "rfs_title": "🎉 <b>আপনার রিফান্ড সফল</b>",
    "rfs_body": "🟢 <code>{number}</code>\n💰 <code>${amount}</code> ব্যালেন্সে যোগ হয়েছে",
    "ref_title": "🤝 <b>রেফার ও আয়</b>",
    "ref_body": "আপনার লিংক শেয়ার করুন — কোনো বন্ধু নাম্বার কিনলেই আপনি পাবেন <b>${rate}</b>। সারাজীবনের জন্য।",
    "ref_link": "🔗 আপনার রেফারেল লিংক:",
    "ref_stats": "👥 রেফার করেছেন: <b>{count}</b>\n💰 মোট আয়: <b>${earned}</b>",
    "ref_rate_line": "💵 আপনার রেট: প্রতি কেনায় <b>${rate}</b>",
    "ref_vip_line": "👑 <b>VIP রেফারার</b> — বিশেষ রেট প্রতি কেনায় <b>${rate}</b>",
    "btn_ref_share": "📤 লিংক শেয়ার করুন",
    "ref_share_text": "🎁 প্রিমিয়াম WhatsApp ও Telegram নাম্বার — সাথে সাথে OTP!",
    "ref_none_yet": "এখনো কোনো রেফার নেই — আয় শুরু করতে আপনার লিংক শেয়ার করুন 👇",
    "ref_earned_notif": "🎉 <b>রেফারেল বোনাস!</b>\n{div}\n👤 {name} একটি নাম্বার কিনেছে\n💰 আপনার ব্যালেন্সে <b>+${amount}</b> যোগ হয়েছে\n💼 ব্যালেন্স: <b>${bal}</b>\n{div}",
    "ref_new_ref": "👥 <b>নতুন রেফারেল!</b>\n👤 {name} আপনার লিংক দিয়ে জয়েন করেছে\n💰 তাদের প্রতিটি কেনাকাটায় আপনি আয় করবেন",
    "ref_paused": "⏸ রেফারেল প্রোগ্রামটি এখন সাময়িক বন্ধ আছে।\n💡 শীঘ্রই আবার দেখুন!",
},

    "ur": {
    "btn_buy": "🛒 نمبر خریدیں",
    "btn_profile": "👤 پروفائل",
    "btn_deposit": "💳 ڈپازٹ",
    "btn_support": "💬 سپورٹ",
    "btn_back": "⬅️ واپس",
    "btn_cancel_dep": "❌ ڈپازٹ منسوخ کریں",
    "btn_wa": "🟢 WhatsApp",
    "btn_tg": "🔵 Telegram",
    "btn_dep_new": "💵 نیا ڈپازٹ",
    "btn_dep_hist": "📜 ہسٹری",
    "btn_custom_amount": "✏️ اپنی رقم",
    "btn_i_paid": "✅ پیمنٹ کر دی — TXID بھیجیں",
    "btn_get_otp": "📩 OTP حاصل کریں",
    "btn_buy_now": "✅ خریدیں — ${price}",
    "kb_placeholder": "کوئی آپشن منتخب کریں 👇",
    "menu_title": "🏠 <b>مین مینو</b>",
    "menu_where": "👉 اب کہاں جانا چاہتے ہیں؟",
    "menu_footer": "✅ ہو گیا! آپ واپس مین مینو پر ہیں 👇",
    "blocked": "🔒 <b>رسائی روک دی گئی</b>\nیہ اکاؤنٹ اب بوت استعمال نہیں کر سکتا۔",
    "lang_pick_title": "🌐 <b>اپنی زبان منتخب کریں</b>",
    "lang_pick_hint": "👉 جاری رکھنے کے لیے اپنی زبان پر ٹیپ کریں",
    "lang_set_ok": "✅ زبان سیٹ ہو گئی: {lang}",
    "lang_current": "🌐 موجودہ زبان: <b>{lang}</b>\nتبدیل کرنے کے لیے نیچے کسی زبان پر ٹیپ کریں۔",
    "welcome_hi": "👋 <b>ہیلو {name}، دوبارہ خوش آمدید!</b>",
    "welcome_tagline": "📱 پریمیم WhatsApp اور Telegram نمبرز\n⚡ فوری ڈیلیوری • OTP شامل",
    "welcome_balance": "💰 بیلنس: <code>${bal}</code>",
    "welcome_stock": "📦 اسٹاک میں: <code>{total}</code> نمبرز",
    "welcome_cta": "👉 شروع کرنے کے لیے نیچے بٹن پر ٹیپ کریں",
    "profile_title": "👤 <b>آپ کی پروفائل</b>",
    "lbl_id": "🆔 آئی ڈی:",
    "lbl_name": "📝 نام:",
    "lbl_username": "🌐 یوزرنیم:",
    "prof_purchased": "🛒 خریدے گئے: <code>{n}</code>",
    "prof_spent": "💸 خرچ: <code>${amount}</code>",
    "prof_deposited": "🏦 جمع: <code>${amount}</code>",
    "prof_otps": "📩 OTPs: <code>{n} ({pct})</code>",
    "support_title": "💬 <b>مدد چاہیے؟</b>",
    "support_admin": "👨‍💻 ایڈمن: {handle}",
    "support_time": "⚡ جواب کا وقت: عام طور پر صرف چند منٹ",
    "support_body": "پیمنٹ، OTP مسئلے یا اسٹاک کے سوالات — ہمیں میسج کریں، ہم آپ کے لیے حاضر ہیں۔ 🙌",
    "buy_title": "🛒 <b>نمبر خریدیں</b>",
    "buy_wa_price": "🟢 WhatsApp — <code>${wa}</code>",
    "buy_tg_price": "🔵 Telegram — <code>${tg}</code>",
    "buy_pick": "👉 جاری رکھنے کے لیے ایک قسم منتخب کریں",
    "ctry_title": "🌍 <b>ملک منتخب کریں</b>",
    "ctry_avail": "📱 {label} نمبرز دستیاب ہیں",
    "cta_select": "👉 نیچے سے منتخب کریں",
    "confirm_title": "🧾 <b>آرڈر کی تصدیق کریں</b>",
    "cf_type": "📱 قسم: {label}",
    "cf_country": "🌍 ملک: {flag} {country}",
    "cf_price": "💵 قیمت: <code>${rate}</code>",
    "cf_balance": "💰 آپ کا بیلنس: <code>${bal}</code>",
    "cf_cta": "👉 سب ٹھیک ہے؟ نیچے تصدیق کریں",
    "ps_title": "✅ <b>خریداری مکمل!</b>",
    "ps_number": "📱 نمبر: <code>{number}</code>",
    "ps_label": "🏷️ {label} • {flag} {country}",
    "ps_paid": "💵 ادائیگی: <code>${rate}</code>",
    "ps_order": "🧾 آرڈر: <code>{order}</code>",
    "ps_get_otp": "📩 جب چاہیں نیچے <b>Get OTP</b> پر ٹیپ کریں اور کوڈ لیں",
    "ps_copy": "📋 کاپی کرنے کے لیے نمبر پر ٹیپ کریں",
    "ins_title": "⚠️ <b>بیلنس کافی نہیں</b>",
    "ins_price": "💵 قیمت: <code>${rate}</code>",
    "ins_balance": "💰 بیلنس: <code>${bal}</code>",
    "ins_need": "❗ آپ کو چاہیے: <code>${need}</code> مزید",
    "ins_cta": "👉 ایک ٹیپ میں بیلنس بڑھائیں",
    "oos_title": "❌ <b>اسٹاک ختم</b>",
    "oos_label": "🏷️ {label} — {flag} {country}",
    "oos_cta": "👉 دوسرا ملک آزمائیں، یا 💬 سپورٹ سے کہیں",
    "otp_received": "🎉 <b>OTP مل گیا!</b>",
    "otp_waiting": "⏳ <b>OTP کا انتظار جاری ہے</b>",
    "otp_waiting_body": "SMS میں تھوڑا وقت لگ سکتا ہے — ہم پس منظر میں چیک کر رہے ہیں۔ یہ خود بخود یہاں آ جائے گا۔ 👀",
    "otp_blocked": "🔒 <b>OTP بلاک ہے</b>",
    "otp_blocked_body": "یہ نمبر ریفنڈ ہو چکا ہے — یہاں اب کبھی OTP نہیں آ سکتا۔",
    "toast_no_link": "ℹ️ اس نمبر پر OTP لنک نہیں — سپورٹ سے رابطہ کریں",
    "otp_timeout": "⏳ <b>10 منٹ میں OTP نہیں آیا</b>",
    "otp_timeout_body": "SMS میں تاخیر ہو سکتی ہے۔ رسید پر 🔑 <b>Get OTP</b> دبا کر کبھی بھی دوبارہ چیک کریں۔",
    "toast_not_yours": "❌ یہ آپ کا نمبر نہیں",
    "toast_not_found": "❌ نمبر نہیں ملا",
    "dep_title": "💳 <b>ڈپازٹ</b>",
    "dep_min_line": "💵 کم از کم: <code>${min}</code> • TXID تصدیق شدہ 🔐",
    "dep_min_only": "💵 کم از کم: <code>${min}</code>",
    "cta_pick": "👉 کوئی آپشن منتخب کریں",
    "dep_amt_title": "💰 <b>رقم منتخب کریں</b>",
    "dep_amt_hint": "👉 رقم پر ٹیپ کریں، یا ✏️ اپنی رقم",
    "dep_net_title": "🌐 <b>نیٹ ورک منتخب کریں</b>",
    "dep_net_amount": "💵 <code>${amount}</code> USDT",
    "dep_net_hint": "👉 اپنے نیٹ ورک پر ٹیپ کریں",
    "dep_hist_title": "📜 <b>ڈپازٹ ہسٹری</b>",
    "dep_hist_empty": "ابھی کوئی ڈپازٹ نہیں — آپ کا پہلا ڈپازٹ یہاں دکھے گا۔",
    "dep_min_warn": "⚠️ کم از کم ڈپازٹ <code>${min}</code> ہے\n👉 نیچے دوبارہ منتخب کریں",
    "custom_title": "✏️ <b>اپنی رقم لکھیں</b>\n💵 USDT میں — کم از کم <code>${min}</code>\nمثال: <code>1.50</code>",
    "custom_err": "❌ کم از کم ڈپازٹ <code>${min}</code> ہے\n💵 دوبارہ USDT رقم لکھیں\nمثال: <code>1.50</code>",
    "card_send": "💸 <b>${amount} USDT بھیجیں</b>",
    "card_network": "🌐 نیٹ ورک: <b>{net}</b>",
    "card_address": "📍 ایڈریس (کاپی کرنے کے لیے ٹیپ):",
    "card_warn": "⚠️ صرف <b>{net}</b> — غلط نیٹ ورک = رقم ضائع۔",
    "card_paid": "✅ ادائیگی ہو گئی؟ <b>I PAID</b> دبائیں → اگلا TXID بھیجیں۔",
    "card_expire": "🧾 <code>{dep_id}</code> • ختم ہوگا {expires} ⏳",
    "txid_title": "🔑 <b>اپنا {net} TXID پیسٹ کریں</b>",
    "txid_body": "📋 آپ کی پیمنٹ کا ٹرانزیکشن ہیش۔",
    "txid_format": "فارمیٹ: <code>{fmt}</code>",
    "txid_ok_line": "✅ تصدیق → فوری بیلنس",
    "txid_no_line": "❌ TXID نہیں → کوئی کریڈٹ نہیں",
    "dep_cancelled": "❌ <b>ڈپازٹ منسوخ ہو گیا۔</b>",
    "dep_expired_session": "ℹ️ سیشن ختم ہو گیا۔\nمینو سے نیا ڈپازٹ شروع کریں۔",
    "dep_no_active": "ℹ️ کوئی فعال ڈپازٹ آرڈر نہیں ملا۔\nمینو سے نیا ڈپازٹ شروع کریں۔",
    "dep_closed": "ℹ️ یہ ڈپازٹ آرڈر پہلے ہی بند ہو چکا ہے۔\nمینو سے نیا شروع کریں۔",
    "toast_bad_amount": "❌ رقم غلط ہے",
    "scr_needed": "❌ <b>اسکرین شاٹ کی ضرورت نہیں۔</b>\nبراہ کرم اپنا <b>TXID</b> (ٹرانزیکشن ہیش) متن کے طور پر بھیجیں۔",
    "txid_bad_fmt": "❌ <b>TXID فارمیٹ غلط</b>\n{net} کو <code>{fmt}</code> چاہیے۔ اپنے والیٹ سے مکمل ہیش کاپی کریں۔",
    "dep_checking": "⏳ آپ کا {net} ٹرانزیکشن چیک ہو رہا ہے...",
    "dep_locked": "🔒 آرڈر لاک — بہت زیادہ غلط TXIDs۔\nآرڈر آئی ڈی <code>{order}</code> کے ساتھ ایڈمن سے رابطہ کریں۔",
    "txid_replay": "🔁 یہ TXID پہلے استعمال ہو چکا ہے۔\nایک TXID = ایک آرڈر۔ نیا ٹرانزیکشن ہیش بھیجیں۔",
    "bin_pay_id": "🏦 <b>بیننس پی آئی ڈی</b> - اسی آئی ڈی پر بھیجیں:",
    "bin_card_hint": "⚠️ <b>بیننس ایپ → Pay</b> سے ادایگی کریں\n💵 صرف <b>USDT</b>، اوپر والی درست رقم بھیجیں۔\n❌ غلط آئی ڈی یا کوئین = رقم ضائع۔",
    "bin_auto_line": "⚡ ادایگی تقریباً 1 منٹ میں خودکار تصدیق ہو جاتی ہے۔\nیا I PAID دبا کر Order ID بھیجیں۔",
    "bin_txid_title": "🔑 <b>اپنی Binance Pay Order ID پیسٹ کریں</b>",
    "bin_txid_body": "📋 بیننس ایپ → Pay → اپنی ٹرانسفر کھولیں → <b>Order ID</b> کاپی کر کے یہاں پیسٹ کریں۔",
    "bin_bad_fmt": "❌ <b>یہ Binance Pay Order ID نہیں ہے۔</b>\nایسا دکھتا ہے: <code>M_P_123456789012345678</code> - بیننس ایپ → Pay → transfer details سے کاپی کریں۔",
    "bin_amt_mismatch": "❌ <b>رقم مطابق نہیں۔</b>\nپیمنٹ دکھاتی ہے <code>${got}</code>، آرڈر کو <code>${want}</code> چاہیے۔\nدرست رقم بھیج کر اسی کی Order ID پیسٹ کریں۔",
    "bin_decline_pending": "⏳ اس Order ID کی کوئی ادایگی نہیں ملی٤\nپہلے ادایگی کریں، Order ID چیک کریں، ایک منٹ بعد دوبارہ بھیجیں۔",
    "bin_decline_stale": "❌ یہ Order ID اس آرڈر کے لیے استعمال نہیں ہو سکتا٤\nیہ آرڈر سے پرانا ہے یا پہلے ہی استعمال ہو چکا ہے۔\nنئی ادایگی کر کے نئا Order ID بھیجیں۔",
    "bin_decline_out": "❌ یہ OUTGOING ٹرانسفر ہے - رقم آپ کے پاس سے گئی ہے۔\nہمیں بھیجی گئی ٹرانسفر کی Order ID پیسٹ کریں۔",
    "dep_api_busy": "⏳ بیننس تصدیق ابھی مصروف ہے۔\nآپ کا آرڈر محفوظ ہے - ایک منٹ بعد دوبارہ کوشش کریں۔",
    "amt_mismatch": "❌ <b>رقم مطابق نہیں۔</b>\nٹرانزیکشن میں <code>${got}</code> ہے، آرڈر کو <code>${want}</code> چاہیے۔\nدرست ہیش بھیجیں، یا نیا ڈپازٹ شروع کریں۔",
    "dep_already": "✅ یہ ڈپازٹ پہلے ہی کنفرم ہو چکا ہے۔\nآپ کا بیلنس پہلے ہی اپ ڈیٹ ہے۔",
    "dep_ok_title": "✅ <b>ڈپازٹ کنفرم!</b>",
    "dep_ok_credited": "💵 جمع ہوا: <code>${amount}</code>",
    "dep_ok_balance": "💰 بیلنس: <code>${bal}</code>",
    "dep_ok_cta": "🛒 خوشی سے خریداری کریں — نیچے Buy دبائیں!",
    "decline_pending": "⏳ {net} پر ٹرانزیکشن ابھی نہیں ملا۔\nTXID دوبارہ چیک کر کے ایک منٹ بعد بھیجیں۔",
    "decline_failed": "❌ ٹرانزیکشن چین پر ناکام — رقم نہیں گئی۔\nنیا، کامیاب TXID بھیجیں۔",
    "decline_token": "❌ یہ {net} پر USDT ٹرانزیکشن نہیں تھا۔\nصرف USDT بھیجیں۔",
    "decline_recipient": "❌ وصول کنندہ غلط۔\nاس TXID میں USDT ہمارے {net} ایڈریس پر نہیں گیا۔",
    "dm_credited": "✅ جمع <code>${amount}</code> • بیلنس <code>${bal}</code>\n🧾 آرڈر <code>{order}</code>",
    "dm_dep_confirmed": "✅ <b>ڈپازٹ کنفرم</b>\n\n{div}\n💵 <b>رقم:</b> ${amount}\n🧾 <b>آرڈر:</b> <code>{order}</code>\n{div}\n\n💰 <b>بیلنس اپ ڈیٹ! خوشی سے خریداری 🛒</b>",
    "dm_dep_rejected": "❌ <b>ڈپازٹ مسترد</b>\n\n{div}\n🧾 <b>آرڈر:</b> <code>{order}</code>\n{div}\n\n💬 اگر غلطی لگے تو سپورٹ سے رابطہ کریں۔",
    "help_title": "📖 <b>فوری مدد</b>",
    "help_lines": "/start — مین مینو کھولیں\n/menu — مینو دکھائیں\n/language — زبان تبدیل کریں\n/admin — ایڈمن پینل",
    "help_cta": "💡 سب کچھ نیچے بٹنوں پر ایک ٹیپ کے فاصلے پر ہے۔",
    "err_generic": "⚠️ <b>کچھ غلط ہو گیا۔</b>\nدوبارہ کوشش کریں — یا /start دبائیں۔",
    "toast_processing": "پروسیس ہو رہا ہے... ⏳",
    "toast_invalid": "درخواست غلط",
    "toast_expired": "❌ اس بٹن کی میعاد ختم — دوبارہ کوشش کریں",
    "btn_join_channel": "✉️ چینل جوائن کریں",
    "btn_join_group": "✉️ گروپ جوائن کریں",
    "fj_title": "🔒 <b>کھولنے کے لیے ایک قدم باقی ہے</b>",
    "fj_body": "👉 بوٹ استعمال کرنے کے لیے نیچے دیے گئے چینل میں جوائن کریں۔\n✅ جوائن کے بعد <b>تصدیق کریں</b> پر ٹپ کریں۔",
    "btn_fj_check": "✅ تصدیق کریں",
    "fj_toast_no": "❌ آپ نے ابھی جوائن نہیں کیا — جوائن کریں، پھر تصدیق پر ٹپ کریں۔",
    "fj_done": "✅ <b>تصدیق مکمل!</b>\n🎉 خوش آمدید — آپ کا مین مینو نیچے کھل گیا 👇",
    "fj_dm": "✅ <b>جوائن کی تصدیق ہو گئی!</b>\n👋 خوش آمدید — مین مینو کھل گیا 👇",
    "btn_refer": "🎁 ریفر کریں اور کمائیں",
    "btn_active": "📱 ایکٹو نمبرز",
    "btn_ubulk": "📦 بلک خریدیں",
    "ub_pick": "📦 <b>بلک خریدیں</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> دستیاب • فی <code>${wa_rate}</code>\n🔵 Telegram — <code>{tg_n}</code> دستیاب • فی <code>${tg_rate}</code>\n\n🎁 <b>{dmin}+ نمبر = فی نمبر ${damt} کمی</b>\n\n👉 ٹائپ چونیں:",
    "ub_qty": "📦 <b>بلک خریدیں — {label}</b>\n\n📱 دستیاب: <code>{n}</code>\n💵 ریٹ: فی نمبر <code>${rate}</code>\n💰 بیلنس: <code>${bal}</code>\n\n🎁 {dmin}+ = فی نمبر <b>${damt} کمی</b>\n\n👉 کتنے نمبر چاہیے؟ لکھیں:",
    "ub_bad_qty": "❌ صرف نمبر لکھیں (1 سے {cap})٤\n👉 دوبارہ کوشش کریں:",
    "ub_stock_low": "⚠️ ابھی صرف <code>{n}</code> دستیاب ہیں٤\n👉 کم قتی لکھیں:",
    "ub_no_bal": "⚠️ {n} نمبر = <code>${total}</code>\n💰 بیلنس: <code>${bal}</code>\n👉 زیادہ از کم <code>{maxn}</code> نمبر لے سکتے ہیں٤ اتنا لکھیں:",
    "ub_confirm": "🧾 <b>اردر تائیں کریں</b>\n\n{div}\n📱 ٹائپ: <b>{label}</b>\n🔢 نمبر: <code>{n}</code>\n💵 ریٹ: فی <code>${unit}</code> {disc}\n💰 کل: <code>${total}</code>\n💰 بعد: <code>${after}</code>\n{div}\n\n👉 نیچے تائیں کریں — .txt فائل فورن آئی گی٤",
    "ub_disc": "({dmin}+ ڈسکاؤنٹ ✅)",
    "ub_expired": "⏳ سشن ختم — 📦 بلک خریدیں سے دوبارہ شروع کریں٤",
    "ub_done": "✅ <b>بلک ارڈر مکمل!</b>\n\n{div}\n📱 نمبر: <code>{n}</code>\n💵 ادا شد: <code>${total}</code> (فی <code>${unit}</code> {disc})\n💰 بیلنس: <code>${bal}</code>\n{div}\n\n📎 <code>{fname}</code> فائل ملگئی — ہر نمبر کا OTP API لنک ساتھ٤\n📩 ہر OTP آتے ہی اس چیٹ میں آ جائی گا٤\n📱 📱 Active Numbers میں ٹریک کریں٤",
    "ub_partial": "⚠️ سٹاک جلدی ختم — صرف <code>{n}</code> ملے٤ صرف <code>{n}</code> کا چارج ہوا٤",
    "ub_none": "❌ <b>سٹاک نہیں</b> — کوئی پیسہ کٹا نہیں٤",
    "ub_hint_file": "❌ یہ فائل ہے — یہاں نمبر چاہیے٤\n👉 کتنے نمبر چاہیے؟ لکھیں:",
    "act_title": "📞 <b>آپ کے ایکٹو نمبرز</b> ({n})",
    "act_none": "📭 ابھی آپ کا کوئی ایکٹو نمبر نہیں ہے۔\n🛒 نمبر خریدیں — یہاں فوراً نظر آئیگا۔",
    "act_hint": "▶️ کاپی کرنے کے لیے کسی نمبر پر ٹاپ کریں، پھر یہاں بھیجیں — نمبر Get OTP کے ساتھ کھل جائیگا۔",
    "act_more": "…اور {extra} مزید",
    "act_card_title": "🟢 <b>آپ کا ایکٹو نمبر</b>",
    "act_card_body": "📩 جب چاہیں GET OTP دبائیں — OTP آنے کے لمحے آپ کو مل جائیگا۔ کوئی وقت کی حد نہیں۔",
    "rfs_title": "🎉 <b>آپ کا ریفنڈ کامیاب</b>",
    "rfs_body": "🟢 <code>{number}</code>\n💰 <code>${amount}</code> آپ کے بیلنس میں شامل",
    "ref_title": "🤝 <b>ریفر اینڈ اِرن</b>",
    "ref_body": "اپنا لنک شیئر کریں — جب بھی کوئی دوست نمبر خریدے گا آپ کو <b>${rate}</b> ملیں گے۔ زندگی بھر کے لیے۔",
    "ref_link": "🔗 آپ کا ریفرل لنک:",
    "ref_stats": "👥 ریفر کیے: <b>{count}</b>\n💰 کل کمائی: <b>${earned}</b>",
    "ref_rate_line": "💵 آپ کا ریٹ: ہر خریداری پر <b>${rate}</b>",
    "ref_vip_line": "👑 <b>VIP ریفرر</b> — خصوصی ریٹ ہر خریداری پر <b>${rate}</b>",
    "btn_ref_share": "📤 لنک شیئر کریں",
    "ref_share_text": "🎁 پریمیم WhatsApp اور Telegram نمبر — فوری OTP!",
    "ref_none_yet": "ابھی کوئی ریفر نہیں — کمائی شروع کرنے کے لیے اپنا لنک شیئر کریں 👇",
    "ref_earned_notif": "🎉 <b>ریفرل بونس!</b>\n{div}\n👤 {name} نے ایک نمبر خریدا\n💰 آپ کے بیلنس میں <b>+${amount}</b> شامل ہوئے\n💼 بیلنس: <b>${bal}</b>\n{div}",
    "ref_new_ref": "👥 <b>نیا ریفرل!</b>\n👤 {name} آپ کے لنک سے جوائن ہوا\n💰 اس کی ہر خریداری پر آپ کمائیں گے",
    "ref_paused": "⏸ ریفرل پروگرام اس وقت بند ہے۔\n💡 تھوڑی دیر بعد دوبارہ دیکھیں!",
},

    "zh": {
    "btn_buy": "🛒 购买号码",
    "btn_profile": "👤 个人资料",
    "btn_deposit": "💳 充值",
    "btn_support": "💬 客服",
    "btn_back": "⬅️ 返回",
    "btn_cancel_dep": "❌ 取消充值",
    "btn_wa": "🟢 WhatsApp",
    "btn_tg": "🔵 Telegram",
    "btn_dep_new": "💵 新充值",
    "btn_dep_hist": "📜 历史",
    "btn_custom_amount": "✏️ 自定义金额",
    "btn_i_paid": "✅ 已付款 — 发送 TXID",
    "btn_get_otp": "📩 获取验证码",
    "btn_buy_now": "✅ 购买 — ${price}",
    "kb_placeholder": "选择一个选项 👇",
    "menu_title": "🏠 <b>主菜单</b>",
    "menu_where": "👉 接下来去哪里？",
    "menu_footer": "✅ 完成！已回到主菜单 👇",
    "blocked": "🔒 <b>访问被限制</b>\n此账号无法继续使用本机器人。",
    "lang_pick_title": "🌐 <b>选择您的语言</b>",
    "lang_pick_hint": "👉 点击您的语言继续",
    "lang_set_ok": "✅ 语言已设置：{lang}",
    "lang_current": "🌐 当前语言：<b>{lang}</b>\n点击下方语言即可切换。",
    "welcome_hi": "👋 <b>嗨 {name}，欢迎回来！</b>",
    "welcome_tagline": "📱 高级 WhatsApp 和 Telegram 号码\n⚡ 极速发货 • 含验证码",
    "welcome_balance": "💰 余额：<code>${bal}</code>",
    "welcome_stock": "📦 库存：<code>{total}</code> 个号码",
    "welcome_cta": "👉 点击下方按钮开始",
    "profile_title": "👤 <b>您的资料</b>",
    "lbl_id": "🆔 ID：",
    "lbl_name": "📝 姓名：",
    "lbl_username": "🌐 用户名：",
    "prof_purchased": "🛒 已购买：<code>{n}</code>",
    "prof_spent": "💸 已消费：<code>${amount}</code>",
    "prof_deposited": "🏦 已充值：<code>${amount}</code>",
    "prof_otps": "📩 验证码：<code>{n} ({pct})</code>",
    "support_title": "💬 <b>需要帮助？</b>",
    "support_admin": "👨‍💻 管理员：{handle}",
    "support_time": "⚡ 回复时间：通常只需几分钟",
    "support_body": "付款、验证码问题、库存咨询 — 直接发消息给我们，我们随时为您服务。 🙌",
    "buy_title": "🛒 <b>购买号码</b>",
    "buy_wa_price": "🟢 WhatsApp — <code>${wa}</code>",
    "buy_tg_price": "🔵 Telegram — <code>${tg}</code>",
    "buy_pick": "👉 选择类型继续",
    "ctry_title": "🌍 <b>选择国家</b>",
    "ctry_avail": "📱 {label} 号码有货",
    "cta_select": "👉 在下方选择",
    "confirm_title": "🧾 <b>确认订单</b>",
    "cf_type": "📱 类型：{label}",
    "cf_country": "🌍 国家：{flag} {country}",
    "cf_price": "💵 价格：<code>${rate}</code>",
    "cf_balance": "💰 您的余额：<code>${bal}</code>",
    "cf_cta": "👉 没问题？在下方确认",
    "ps_title": "✅ <b>购买成功！</b>",
    "ps_number": "📱 号码：<code>{number}</code>",
    "ps_label": "🏷️ {label} • {flag} {country}",
    "ps_paid": "💵 已付：<code>${rate}</code>",
    "ps_order": "🧾 订单：<code>{order}</code>",
    "ps_get_otp": "📩 随时点击下方 <b>Get OTP</b> 获取验证码",
    "ps_copy": "📋 点击号码即可复制",
    "ins_title": "⚠️ <b>余额不足</b>",
    "ins_price": "💵 价格：<code>${rate}</code>",
    "ins_balance": "💰 余额：<code>${bal}</code>",
    "ins_need": "❗ 您还需要：<code>${need}</code>",
    "ins_cta": "👉 一键充值",
    "oos_title": "❌ <b>缺货</b>",
    "oos_label": "🏷️ {label} — {flag} {country}",
    "oos_cta": "👉 试试其他国家，或联系 💬 客服",
    "otp_received": "🎉 <b>已收到验证码！</b>",
    "otp_waiting": "⏳ <b>仍在等待验证码</b>",
    "otp_waiting_body": "短信可能需要一点时间 — 我们正在后台持续检查。验证码会自动送达这里。 👀",
    "otp_blocked": "🔒 <b>验证码已被禁用</b>",
    "otp_blocked_body": "该号码已退款 — 不会再收到验证码。",
    "toast_no_link": "ℹ️ 该号码没有验证码链接 — 请联系客服",
    "otp_timeout": "⏳ <b>10 分钟内未收到验证码</b>",
    "otp_timeout_body": "短信偶尔会延迟。随时点击回执上的 🔑 <b>Get OTP</b> 再次查询。",
    "toast_not_yours": "❌ 这不是您的号码",
    "toast_not_found": "❌ 找不到号码",
    "dep_title": "💳 <b>充值</b>",
    "dep_min_line": "💵 最低：<code>${min}</code> • TXID 验证 🔐",
    "dep_min_only": "💵 最低：<code>${min}</code>",
    "cta_pick": "👉 选择一个选项",
    "dep_amt_title": "💰 <b>选择金额</b>",
    "dep_amt_hint": "👉 点击金额，或选择 ✏️ 自定义",
    "dep_net_title": "🌐 <b>选择网络</b>",
    "dep_net_amount": "💵 <code>${amount}</code> USDT",
    "dep_net_hint": "👉 点击您的网络",
    "dep_hist_title": "📜 <b>充值记录</b>",
    "dep_hist_empty": "还没有充值记录 — 您的第一笔充值会显示在这里。",
    "dep_min_warn": "⚠️ 最低充值 <code>${min}</code>\n👉 请在下方重新选择",
    "custom_title": "✏️ <b>输入金额</b>\n💵 USDT — 最低 <code>${min}</code>\n示例：<code>1.50</code>",
    "custom_err": "❌ 最低充值 <code>${min}</code>\n💵 请重新输入 USDT 金额\n示例：<code>1.50</code>",
    "card_send": "💸 <b>发送 ${amount} USDT</b>",
    "card_network": "🌐 网络：<b>{net}</b>",
    "card_address": "📍 地址（点击复制）：",
    "card_warn": "⚠️ 仅限 <b>{net}</b> — 网络错误 = 资金丢失。",
    "card_paid": "✅ 已付款？点击 <b>I PAID</b> → 下一步发送您的 TXID。",
    "card_expire": "🧾 <code>{dep_id}</code> • {expires} 过期 ⏳",
    "txid_title": "🔑 <b>粘贴您的 {net} TXID</b>",
    "txid_body": "📋 您付款的交易哈希。",
    "txid_format": "格式：<code>{fmt}</code>",
    "txid_ok_line": "✅ 验证通过 → 立即到账",
    "txid_no_line": "❌ 无 TXID → 无法到账",
    "dep_cancelled": "❌ <b>充值已取消。</b>",
    "dep_expired_session": "ℹ️ 会话已过期。\n请从菜单开始新的充值。",
    "dep_no_active": "ℹ️ 未找到进行中的充值订单。\n请从菜单开始新的充值。",
    "dep_closed": "ℹ️ 该充值订单已关闭。\n请从菜单开始新订单。",
    "toast_bad_amount": "❌ 金额无效",
    "scr_needed": "❌ <b>无需截图。</b>\n请以文本形式发送您的 <b>TXID</b>（交易哈希）。",
    "txid_bad_fmt": "❌ <b>TXID 格式无效</b>\n{net} 需要 <code>{fmt}</code>。请从钱包复制完整哈希。",
    "dep_checking": "⏳ 正在检查您的 {net} 交易…",
    "dep_locked": "🔒 订单已锁定 — TXID 错误次数过多。\n请携带订单号 <code>{order}</code> 联系管理员。",
    "txid_replay": "🔁 此 TXID 已被使用。\n一个 TXID = 一个订单。请发送您的新交易哈希。",
    "bin_pay_id": "🏦 <b>币安 Pay ID</b> - 请向此 ID 付款:",
    "bin_card_hint": "⚠️ 请用 <b>币安 App → Pay</b> 付款\n💵 只接受 <b>USDT</b>，金额必须与上方完全一致。\n❌ ID 或币种错误 = 资金丢失。",
    "bin_auto_line": "⚡ 付款后约 1 分钟自动到账确认。\n也可点击 I PAID 并粘贴订单号。",
    "bin_txid_title": "🔑 <b>请粘贴您的币安 Pay 订单号</b>",
    "bin_txid_body": "📋 币安 App → Pay → 打开该笔转账 → 复制 <b>订单号 (Order ID)</b> 并粘贴到这里。",
    "bin_bad_fmt": "❌ <b>这不是币安 Pay 订单号。</b>\n格式类似 <code>M_P_123456789012345678</code> - 请在币安 App → Pay → 转账详情中复制。",
    "bin_amt_mismatch": "❌ <b>金额不符。</b>\n到账 <code>${got}</code>，订单需要 <code>${want}</code>。\n请按准确金额付款后粘贴对应订单号。",
    "bin_decline_pending": "⏳ 尚未找到此订单号的付款。\n请先付款，核对订单号，一分钟后重试。",
    "bin_decline_stale": "❌ 此订单号不能用于本订单。\n它早于订单或已被使用。\n请重新付款并粘贴新订单号。",
    "bin_decline_out": "❌ 这是一笔转出（OUTGOING）转账。\n请粘贴您转给我们的那笔转账的订单号。",
    "dep_api_busy": "⏳ 币安验证暂时繁忙。\n您的订单安全 - 请一分钟后重试。",
    "amt_mismatch": "❌ <b>金额不符。</b>\n交易金额为 <code>${got}</code>，订单需要 <code>${want}</code>。\n请发送正确的哈希，或开始新的充值。",
    "dep_already": "✅ 该充值已确认。\n您的余额已更新。",
    "dep_ok_title": "✅ <b>充值成功！</b>",
    "dep_ok_credited": "💵 已到账：<code>${amount}</code>",
    "dep_ok_balance": "💰 余额：<code>${bal}</code>",
    "dep_ok_cta": "🛒 购物愉快 — 点击下方 Buy！",
    "decline_pending": "⏳ 暂时未在 {net} 上找到该交易。\n请核对 TXID，一分钟后重新发送。",
    "decline_failed": "❌ 链上交易失败 — 资金未转出。\n请发送新的成功 TXID。",
    "decline_token": "❌ 这不是 {net} 上的 USDT 转账。\n请只发送 USDT。",
    "decline_recipient": "❌ 收款地址错误。\n此 TXID 没有向我们的 {net} 地址转 USDT。",
    "dm_credited": "✅ 已到账 <code>${amount}</code> • 余额 <code>${bal}</code>\n🧾 订单 <code>{order}</code>",
    "dm_dep_confirmed": "✅ <b>充值已确认</b>\n\n{div}\n💵 <b>金额：</b>${amount}\n🧾 <b>订单：</b><code>{order}</code>\n{div}\n\n💰 <b>余额已更新！购物愉快 🛒</b>",
    "dm_dep_rejected": "❌ <b>充值被拒绝</b>\n\n{div}\n🧾 <b>订单：</b><code>{order}</code>\n{div}\n\n💬 如有疑问请联系客服。",
    "help_title": "📖 <b>快速帮助</b>",
    "help_lines": "/start — 打开主菜单\n/menu — 显示菜单\n/language — 更改语言\n/admin — 管理面板",
    "help_cta": "💡 所有功能都在下方按钮中，一键直达。",
    "err_generic": "⚠️ <b>出错了。</b>\n请重试 — 或按 /start。",
    "toast_processing": "正在处理购买… ⏳",
    "toast_invalid": "请求无效",
    "toast_expired": "❌ 此按钮已过期 — 请重试",
    "btn_join_channel": "✉️ 加入频道",
    "btn_join_group": "✉️ 加入群组",
    "fj_title": "🔒 <b>还差一步即可解锁</b>",
    "fj_body": "👉 请先加入下方频道才能使用机器人。\n✅ 加入后点击<b>验证</b>。",
    "btn_fj_check": "✅ 验证",
    "fj_toast_no": "❌ 你还没有加入——请先加入，再点击验证。",
    "fj_done": "✅ <b>验证成功！</b>\n🎉 欢迎——你的主菜单已在下方解锁 👇",
    "fj_dm": "✅ <b>加入已验证！</b>\n👋 欢迎——主菜单已解锁 👇",
    "btn_refer": "🎁 邀请赚钱",
    "btn_active": "📱 有效号码",
    "btn_ubulk": "📦 批量购买",
    "ub_pick": "📦 <b>批量购买</b>\n\n🟢 WhatsApp — 库存 <code>{wa_n}</code> • 单价 <code>${wa_rate}</code>\n🔵 Telegram — 库存 <code>{tg_n}</code> • 单价 <code>${tg_rate}</code>\n\n🎁 <b>{dmin}+ 个号码 = 每个减 ${damt}</b>\n\n👉 选择类型:",
    "ub_qty": "📦 <b>批量购买 — {label}</b>\n\n📱 库存: <code>{n}</code> 个\n💵 单价: <code>${rate}</code>/个\n💰 余额: <code>${bal}</code>\n\n🎁 {dmin}+ = 每个<b>减 ${damt}</b>\n\n👉 请输入要买的数量:",
    "ub_bad_qty": "❌ 请输入纯数字 (1 到 {cap})。\n👉 重新输入:",
    "ub_stock_low": "⚠️ 目前只有 <code>{n}</code> 个。\n👉 请输入更小的数量:",
    "ub_no_bal": "⚠️ {n} 个 = <code>${total}</code>\n💰 余额: <code>${bal}</code>\n👉 最多可买 <code>{maxn}</code> 个。请输入该数量:",
    "ub_confirm": "🧾 <b>确认订单</b>\n\n{div}\n📱 类型: <b>{label}</b>\n🔢 数量: <code>{n}</code>\n💵 单价: <code>${unit}</code> {disc}\n💰 总计: <code>${total}</code>\n💰 之后余额: <code>${after}</code>\n{div}\n\n👉 在下方确认 — .txt 文件立即发送。",
    "ub_disc": "({dmin}+ 折扣 ✅)",
    "ub_expired": "⏳ 会话已过期 — 请从 📦 批量购买 重新开始。",
    "ub_done": "✅ <b>批量订单完成!</b>\n\n{div}\n📱 已发货: <code>{n}</code> 个\n💵 已支付: <code>${total}</code> (单价 <code>${unit}</code> {disc})\n💰 余额: <code>${bal}</code>\n{div}\n\n📎 已附上 <code>{fname}</code> — 每个号码带 OTP API 链接。\n📩 每个 OTP 会自动发到本聊天。\n📱 随时在 📱 活跃号码 查看。",
    "ub_partial": "⚠️ 库存变化快 — 只有 <code>{n}</code> 个。仅按 <code>{n}</code> 个扣费。",
    "ub_none": "❌ <b>无库存</b> — 未扣费。",
    "ub_hint_file": "❌ 这是文件 — 这里需要数字。\n👉 请输入要买的数量:",
    "act_title": "📞 <b>您的有效号码</b> ({n})",
    "act_none": "📭 您目前没有有效号码。\n🛒 购买号码后会立即显示在这里。",
    "act_hint": "▶️ 点击任意号码即可复制，然后发送到这里 — 号码会带 Get OTP 按钮打开。",
    "act_more": "…还有 {extra} 个",
    "act_card_title": "🟢 <b>您的有效号码</b>",
    "act_card_body": "📩 随时点击 GET OTP — 验证码一到即会送达，没有时间限制。",
    "rfs_title": "🎉 <b>退款成功</b>",
    "rfs_body": "🟢 <code>{number}</code>\n💰 <code>${amount}</code> 已加入余额",
    "ref_title": "🤝 <b>邀请返佣</b>",
    "ref_body": "分享您的链接 — 好友每购买一个号码，您即可获得 <b>${rate}</b> 佣金，永久有效。",
    "ref_link": "🔗 您的邀请链接：",
    "ref_stats": "👥 已邀请：<b>{count}</b> 人\n💰 累计收益：<b>${earned}</b>",
    "ref_rate_line": "💵 您的佣金：每笔购买 <b>${rate}</b>",
    "ref_vip_line": "👑 <b>VIP 推广员</b> — 特惠佣金每笔 <b>${rate}</b>",
    "btn_ref_share": "📤 分享链接",
    "ref_share_text": "🎁 高级 WhatsApp 和 Telegram 号码 — 秒到 OTP！",
    "ref_none_yet": "还没有邀请记录 — 分享您的链接开始赚钱 👇",
    "ref_earned_notif": "🎉 <b>邀请奖励！</b>\n{div}\n👤 {name} 购买了一个号码\n💰 您的余额已增加 <b>+${amount}</b>\n💼 余额：<b>${bal}</b>\n{div}",
    "ref_new_ref": "👥 <b>新邀请！</b>\n👤 {name} 通过您的链接加入\n💰 他们的每笔购买都会为您带来收益",
    "ref_paused": "⏸ 邀请奖励活动暂时暂停。\n💡 请稍后再来看看！",
},

    "ar": {
    "btn_buy": "🛒 شراء رقم",
    "btn_profile": "👤 الملف الشخصي",
    "btn_deposit": "💳 إيداع",
    "btn_support": "💬 الدعم",
    "btn_back": "⬅️ رجوع",
    "btn_cancel_dep": "❌ إلغاء الإيداع",
    "btn_wa": "🟢 WhatsApp",
    "btn_tg": "🔵 Telegram",
    "btn_dep_new": "💵 إيداع جديد",
    "btn_dep_hist": "📜 السجل",
    "btn_custom_amount": "✏️ مبلغ مخصص",
    "btn_i_paid": "✅ لقد دفعت — أرسل TXID",
    "btn_get_otp": "📩 احصل على الرمز",
    "btn_buy_now": "✅ شراء — ${price}",
    "kb_placeholder": "اختر خيارًا 👇",
    "menu_title": "🏠 <b>القائمة الرئيسية</b>",
    "menu_where": "👉 إلى أين تريد الآن؟",
    "menu_footer": "✅ تم! أنت الآن في القائمة الرئيسية 👇",
    "blocked": "🔒 <b>تم حجب الوصول</b>\nلا يمكن لهذا الحساب استخدام البوت بعد الآن.",
    "lang_pick_title": "🌐 <b>اختر لغتك</b>",
    "lang_pick_hint": "👉 اضغط على لغتك للمتابعة",
    "lang_set_ok": "✅ تم تعيين اللغة: {lang}",
    "lang_current": "🌐 اللغة الحالية: <b>{lang}</b>\nاضغط على أي لغة بالأسفل للتغيير.",
    "welcome_hi": "👋 <b>مرحبًا بعودتك يا {name}!</b>",
    "welcome_tagline": "📱 أرقام WhatsApp وTelegram متميزة\n⚡ تسليم فوري • مع رمز التحقق",
    "welcome_balance": "💰 الرصيد: <code>${bal}</code>",
    "welcome_stock": "📦 المتوفر: <code>{total}</code> رقم",
    "welcome_cta": "👉 اضغط على زر بالأسفل للبدء",
    "profile_title": "👤 <b>ملفك الشخصي</b>",
    "lbl_id": "🆔 المعرّف:",
    "lbl_name": "📝 الاسم:",
    "lbl_username": "🌐 اسم المستخدم:",
    "prof_purchased": "🛒 تم شراؤها: <code>{n}</code>",
    "prof_spent": "💸 المصروف: <code>${amount}</code>",
    "prof_deposited": "🏦 الإيداعات: <code>${amount}</code>",
    "prof_otps": "📩 رموز التحقق: <code>{n} ({pct})</code>",
    "support_title": "💬 <b>تحتاج مساعدة؟</b>",
    "support_admin": "👨‍💻 الإدارة: {handle}",
    "support_time": "⚡ وقت الرد: عادةً دقائق فقط",
    "support_body": "المدفوعات، مشاكل رمز التحقق، أسئلة المخزون — راسلنا فقط ونحن معك. 🙌",
    "buy_title": "🛒 <b>شراء رقم</b>",
    "buy_wa_price": "🟢 WhatsApp — <code>${wa}</code>",
    "buy_tg_price": "🔵 Telegram — <code>${tg}</code>",
    "buy_pick": "👉 اختر نوعًا للمتابعة",
    "ctry_title": "🌍 <b>اختر دولة</b>",
    "ctry_avail": "📱 أرقام {label} متوفرة",
    "cta_select": "👉 اختر بالأسفل",
    "confirm_title": "🧾 <b>أكّد طلبك</b>",
    "cf_type": "📱 النوع: {label}",
    "cf_country": "🌍 الدولة: {flag} {country}",
    "cf_price": "💵 السعر: <code>${rate}</code>",
    "cf_balance": "💰 رصيدك: <code>${bal}</code>",
    "cf_cta": "👉 كل شيء جيد؟ أكّد بالأسفل",
    "ps_title": "✅ <b>اكتمل الشراء!</b>",
    "ps_number": "📱 الرقم: <code>{number}</code>",
    "ps_label": "🏷️ {label} • {flag} {country}",
    "ps_paid": "💵 المدفوع: <code>${rate}</code>",
    "ps_order": "🧾 الطلب: <code>{order}</code>",
    "ps_get_otp": "📩 اضغط <b>Get OTP</b> بالأسفل في أي وقت لجلب رمزك",
    "ps_copy": "📋 اضغط على الرقم لنسخه",
    "ins_title": "⚠️ <b>الرصيد غير كافٍ</b>",
    "ins_price": "💵 السعر: <code>${rate}</code>",
    "ins_balance": "💰 الرصيد: <code>${bal}</code>",
    "ins_need": "❗ تحتاج إلى: <code>${need}</code> إضافية",
    "ins_cta": "👉 اشحن بضغطة واحدة",
    "oos_title": "❌ <b>غير متوفر</b>",
    "oos_label": "🏷️ {label} — {flag} {country}",
    "oos_cta": "👉 جرّب دولة أخرى، أو تواصل مع 💬 الدعم",
    "otp_received": "🎉 <b>وصل رمز التحقق!</b>",
    "otp_waiting": "⏳ <b>ما زلنا ننتظر الرمز</b>",
    "otp_waiting_body": "قد تستغرق الرسائل لحظة — نحن نتحقق في الخلفية وسيصل الرمز هنا تلقائيًا. 👀",
    "otp_blocked": "🔒 <b>الرمز محجوب</b>",
    "otp_blocked_body": "تم استرداد هذا الرقم — لن يصل رمز تحقق إليه أبدًا.",
    "toast_no_link": "ℹ️ لا يوجد رابط رمز لهذا الرقم — تواصل مع الدعم",
    "otp_timeout": "⏳ <b>لم يصل رمز التحقق خلال 10 دقائق</b>",
    "otp_timeout_body": "تأخر الرسائل أمر طبيعي. اضغط 🔑 <b>Get OTP</b> في الإيصال للتحقق مرة أخرى في أي وقت.",
    "toast_not_yours": "❌ هذا ليس رقمك",
    "toast_not_found": "❌ الرقم غير موجود",
    "dep_title": "💳 <b>إيداع</b>",
    "dep_min_line": "💵 الحد الأدنى: <code>${min}</code> • تحقق عبر TXID 🔐",
    "dep_min_only": "💵 الحد الأدنى: <code>${min}</code>",
    "cta_pick": "👉 اختر خيارًا",
    "dep_amt_title": "💰 <b>اختر المبلغ</b>",
    "dep_amt_hint": "👉 اضغط على مبلغ، أو ✏️ مخصص",
    "dep_net_title": "🌐 <b>اختر الشبكة</b>",
    "dep_net_amount": "💵 <code>${amount}</code> USDT",
    "dep_net_hint": "👉 اضغط على شبكتك",
    "dep_hist_title": "📜 <b>سجل الإيداعات</b>",
    "dep_hist_empty": "لا إيداعات بعد — سيظهر إيداعك الأول هنا.",
    "dep_min_warn": "⚠️ الحد الأدنى للإيداع <code>${min}</code>\n👉 اختر مرة أخرى بالأسفل",
    "custom_title": "✏️ <b>اكتب المبلغ</b>\n💵 بـ USDT — الحد الأدنى <code>${min}</code>\nمثال: <code>1.50</code>",
    "custom_err": "❌ الحد الأدنى للإيداع <code>${min}</code>\n💵 اكتب مبلغ USDT مرة أخرى\nمثال: <code>1.50</code>",
    "card_send": "💸 <b>أرسل ${amount} USDT</b>",
    "card_network": "🌐 الشبكة: <b>{net}</b>",
    "card_address": "📍 العنوان (اضغط للنسخ):",
    "card_warn": "⚠️ شبكة <b>{net}</b> فقط — الشبكة الخاطئة = خسارة الأموال.",
    "card_paid": "✅ دفعت؟ اضغط <b>I PAID</b> ← ثم أرسل TXID.",
    "card_expire": "🧾 <code>{dep_id}</code> • ينتهي {expires} ⏳",
    "txid_title": "🔑 <b>الصق رمز معاملة {net}</b>",
    "txid_body": "📋 تجزئة معاملة الدفع الخاصة بك.",
    "txid_format": "الصيغة: <code>{fmt}</code>",
    "txid_ok_line": "✅ بعد التحقق ← رصيد فوري",
    "txid_no_line": "❌ بدون TXID ← لا رصيد",
    "dep_cancelled": "❌ <b>تم إلغاء الإيداع.</b>",
    "dep_expired_session": "ℹ️ انتهت الجلسة.\nابدأ إيداعًا جديدًا من القائمة.",
    "dep_no_active": "ℹ️ لا يوجد طلب إيداع نشط.\nابدأ إيداعًا جديدًا من القائمة.",
    "dep_closed": "ℹ️ طلب الإيداع مغلق بالفعل.\nابدأ طلبًا جديدًا من القائمة.",
    "toast_bad_amount": "❌ مبلغ غير صالح",
    "scr_needed": "❌ <b>لا حاجة لصورة شاشة.</b>\nأرسل <b>TXID</b> (تجزئة المعاملة) كنص من فضلك.",
    "txid_bad_fmt": "❌ <b>صيغة TXID غير صالحة</b>\n{net} يتطلب <code>{fmt}</code>. انسخ التجزئة كاملة من محفظتك.",
    "dep_checking": "⏳ جارٍ فحص معاملة {net}...",
    "dep_locked": "🔒 الطلب مقفول — أخطاء TXID كثيرة.\nتواصل مع الإدارة مع رقم الطلب <code>{order}</code>.",
    "txid_replay": "🔁 هذا TXID مستخدم من قبل.\nكل TXID = طلب واحد. أرسل تجزئة معاملتك الجديدة.",
    "bin_pay_id": "🏦 <b>معرف Binance Pay</b> - أرسل إلى هذا المعرف:",
    "bin_card_hint": "⚠️ ادفع عبر <b>تطبيق Binance ← Pay</b>\n💵 أرسل <b>USDT فقط</b> وبالمبلغ المذكور أعلاه بالضبط.\n❌ معرف أو عملة خاطئة = خسارة المال.",
    "bin_auto_line": "⚡ يتم تأكيد الدفع تلقائياً خلال دقيقة تقريباً.\nأو اضغط I PAID والصق رقم الطلب.",
    "bin_txid_title": "🔑 <b>الصق رقم طلب Binance Pay الخاص بك</b>",
    "bin_txid_body": "📋 تطبيق Binance ← Pay ← افتح تحويلتك ← انسخ <b>رقم الطلب (Order ID)</b> والصقه هنا.",
    "bin_bad_fmt": "❌ <b>هذا ليس رقم طلب Binance Pay.</b>\nيبدو هكذا: <code>M_P_123456789012345678</code> - انسخه من التطبيق ← Pay ← تفاصيل التحويل.",
    "bin_amt_mismatch": "❌ <b>المبلغ غير مطابق.</b>\nالدفع يظهر <code>${got}</code> والطلب يحتاج <code>${want}</code>.\nادفع المبلغ بالضبط ثم الصق رقم الطلب الخاص به.",
    "bin_decline_pending": "⏳ لم يتم العثور على دفعة لهذا رقم الطلب بعد.\nادفع أولاً، تحقق من رقم الطلب، وأعد الإرسال بعد دقيقة.",
    "bin_decline_stale": "❌ لا يمكن استخدام رقم الطلب هذا لهذا الطلب.\nإنه أقدم من الطلب أو مستخدم مسبقاً.\nادفع من جديد والصق رقم الطلب الجديد.",
    "bin_decline_out": "❌ هذا تحويل صادر (OUTGOING) - أرسلت المال بعيداً.\nالصق رقم الطلب للتحويل الذي أرسلته إلينا.",
    "dep_api_busy": "⏳ التحقق من Binance مشغول الآن.\nطلبك آمن - حاول مرة أخرى بعد دقيقة.",
    "amt_mismatch": "❌ <b>المبلغ غير مطابق.</b>\nالمعاملة تُظهر <code>${got}</code>، والطلب يحتاج <code>${want}</code>.\nأرسل التجزئة الصحيحة أو ابدأ إيداعًا جديدًا.",
    "dep_already": "✅ هذا الإيداع مؤكد مسبقًا.\nرصيدك محدَّث بالفعل.",
    "dep_ok_title": "✅ <b>تم تأكيد الإيداع!</b>",
    "dep_ok_credited": "💵 أُضيف: <code>${amount}</code>",
    "dep_ok_balance": "💰 الرصيد: <code>${bal}</code>",
    "dep_ok_cta": "🛒 تسوّق سعيدًا — اضغط Buy بالأسفل!",
    "decline_pending": "⏳ لم تُعثر على المعاملة على {net} بعد.\nتحقق من TXID وأرسله مرة أخرى بعد دقيقة.",
    "decline_failed": "❌ فشلت المعاملة على السلسلة — لم تنتقل أموال.\nأرسل TXID جديدًا ناجحًا.",
    "decline_token": "❌ لم تكن معاملة USDT على {net}.\nأرسل USDT فقط.",
    "decline_recipient": "❌ المستلم خطأ.\nلم تُرسل هذه المعاملة USDT إلى عنواننا على {net}.",
    "dm_credited": "✅ أُضيف <code>${amount}</code> • الرصيد <code>${bal}</code>\n🧾 الطلب <code>{order}</code>",
    "dm_dep_confirmed": "✅ <b>تم تأكيد الإيداع</b>\n\n{div}\n💵 <b>المبلغ:</b> ${amount}\n🧾 <b>الطلب:</b> <code>{order}</code>\n{div}\n\n💰 <b>تم تحديث الرصيد! تسوّق سعيد 🛒</b>",
    "dm_dep_rejected": "❌ <b>تم رفض الإيداع</b>\n\n{div}\n🧾 <b>الطلب:</b> <code>{order}</code>\n{div}\n\n💬 تواصل مع الدعم إذا كنت تعتقد أن هذا خطأ.",
    "help_title": "📖 <b>مساعدة سريعة</b>",
    "help_lines": "/start — افتح القائمة الرئيسية\n/menu — اعرض القائمة\n/language — غيّر اللغة\n/admin — لوحة الإدارة",
    "help_cta": "💡 كل شيء على بُعد ضغطة واحدة في الأزرار بالأسفل.",
    "err_generic": "⚠️ <b>حدث خطأ ما.</b>\nحاول مرة أخرى — أو اضغط /start.",
    "toast_processing": "جارٍ تنفيذ الشراء... ⏳",
    "toast_invalid": "طلب غير صالح",
    "toast_expired": "❌ انتهت صلاحية هذا الزر — أعد المحاولة",
    "btn_join_channel": "✉️ انضم إلى القناة",
    "btn_join_group": "✉️ انضم إلى المجموعة",
    "fj_title": "🔒 <b>خطوة واحدة للفتح</b>",
    "fj_body": "👉 انضم إلى قناتنا بالأسفل لاستخدام البوت.\n✅ بعد الانضمام اضغط <b>تحقق</b>.",
    "btn_fj_check": "✅ تحقق",
    "fj_toast_no": "❌ لم تنضم بعد — انضم أولاً ثم اضغط تحقق.",
    "fj_done": "✅ <b>تم التحقق!</b>\n🎉 مرحبًا — تم فتح القائمة الرئيسية بالأسفل 👇",
    "fj_dm": "✅ <b>تم التحقق من الانضمام!</b>\n👋 مرحبًا — القائمة الرئيسية مفتوحة 👇",
    "btn_refer": "🎁 ادعُ واربح",
    "btn_active": "📱 الأرقام النشطة",
    "btn_ubulk": "📦 شراء بالجملة",
    "ub_pick": "📦 <b>شراء بالجملة</b>\n\n🟢 WhatsApp — متاح <code>{wa_n}</code> • <code>${wa_rate}</code> للرقم\n🔵 Telegram — متاح <code>{tg_n}</code> • <code>${tg_rate}</code> للرقم\n\n🎁 <b>{dmin}+ رقم = خصم ${damt} للرقم</b>\n\n👉 اختر النوع:",
    "ub_qty": "📦 <b>شراء بالجملة — {label}</b>\n\n📱 متاح: <code>{n}</code>\n💵 السعر: <code>${rate}</code> للرقم\n💰 الرصيد: <code>${bal}</code>\n\n🎁 {dmin}+ = <b>${damt} خصم للرقم</b>\n\n👉 اكتب عدد الأرقام المطلوب:",
    "ub_bad_qty": "❌ اكتب رقماً صحيحاً (1 إلى {cap})٤\n👉 حاول مرة أخرى:",
    "ub_stock_low": "⚠️ متاح فقط <code>{n}</code> الآن٤\n👉 اكتب عدداً أقل:",
    "ub_no_bal": "⚠️ {n} رقم = <code>${total}</code>\n💰 الرصيد: <code>${bal}</code>\n👉 الحد الأقصى: <code>{maxn}</code> رقم٤ اكتب ذلك:",
    "ub_confirm": "🧾 <b>تأكيد الطلب</b>\n\n{div}\n📱 النوع: <b>{label}</b>\n🔢 الأرقام: <code>{n}</code>\n💵 السعر: <code>${unit}</code> {disc}\n💰 الإجمالي: <code>${total}</code>\n💰 بعد الشراء: <code>${after}</code>\n{div}\n\n👉 أكد أدناه — سيصل ملف .txt فوراً.",
    "ub_disc": "(خصم {dmin}+ ✅)",
    "ub_expired": "⏳ انتهت الجلسة — ابدأ من 📦 شراء بالجملة مجدداً.",
    "ub_done": "✅ <b>تم الطلب!</b>\n\n{div}\n📱 الأرقام: <code>{n}</code>\n💵 الدفع: <code>${total}</code> (<code>${unit}</code> {disc})\n💰 الرصيد: <code>${bal}</code>\n{div}\n\n📎 تم إرفاق <code>{fname}</code> — كل رقم مع رابط OTP API.\n📩 كل OTP يصل إلى هذا المحادثة تلقائياً.\n📱 تابعها في 📱 الأرقام النشطة.",
    "ub_partial": "⚠️ تغيرت المخزون بسرعة — لم يتوفر إلا <code>{n}</code>. تم الخصم عن <code>{n}</code> فقط.",
    "ub_none": "❌ <b>لا مخزون</b> — لم يتم خصم أي مبلغ.",
    "ub_hint_file": "❌ هذا ملف — نحتاج رقماً هنا.\n👉 اكتب عدد الأرقام المطلوب:",
    "act_title": "📞 <b>أرقامك النشطة</b> ({n})",
    "act_none": "📭 لا توجد أرقام نشطة لديك الآن.\n🛒 اشترِ رقماً — سيظهر هنا فوراً.",
    "act_hint": "▶️ اضغط على أي رقم لنسخه ثم أرسله هنا — سيفتح الرقم مع زر Get OTP.",
    "act_more": "…و{extra} أخرى",
    "act_card_title": "🟢 <b>رقمك النشط</b>",
    "act_card_body": "📩 اضغط GET OTP في أي وقت — يصلك الرمز فور وصوله، بلا حد زمني.",
    "rfs_title": "🎉 <b>تم استرداد أموالك بنجاح</b>",
    "rfs_body": "🟢 <code>{number}</code>\n💰 <code>${amount}</code> أُضيفت إلى رصيدك",
    "ref_title": "🤝 <b>الإحالة والأرباح</b>",
    "ref_body": "شارك رابطك — تكسب <b>${rate}</b> في كل مرة يشتري فيها صديقك رقماً، مدى الحياة.",
    "ref_link": "🔗 رابط الإحالة الخاص بك:",
    "ref_stats": "👥 عدد الإحالات: <b>{count}</b>\n💰 إجمالي الأرباح: <b>${earned}</b>",
    "ref_rate_line": "💵 معدلك: <b>${rate}</b> لكل عملية شراء",
    "ref_vip_line": "👑 <b>مُحيل VIP</b> — معدل خاص <b>${rate}</b> لكل عملية شراء",
    "btn_ref_share": "📤 شارك الرابط",
    "ref_share_text": "🎁 أرقام WhatsApp وTelegram مميزة — OTP فوري!",
    "ref_none_yet": "لا إحالات بعد — شارك رابطك لتبدأ الربح 👇",
    "ref_earned_notif": "🎉 <b>مكافأة إحالة!</b>\n{div}\n👤 اشترى {name} رقماً\n💰 أُضيف <b>+${amount}</b> إلى رصيدك\n💼 الرصيد: <b>${bal}</b>\n{div}",
    "ref_new_ref": "👥 <b>إحالة جديدة!</b>\n👤 انضم {name} عبر رابطك\n💰 ستربح من كل عملية شراء يقوم بها",
    "ref_paused": "⏸ برنامج الإحالات متوقف حالياً.\n💡 عد قريباً!",
},

    "id": {
    "btn_buy": "🛒 Beli Nomor",
    "btn_profile": "👤 Profil",
    "btn_deposit": "💳 Deposit",
    "btn_support": "💬 Dukungan",
    "btn_back": "⬅️ Kembali",
    "btn_cancel_dep": "❌ Batalkan Deposit",
    "btn_wa": "🟢 WhatsApp",
    "btn_tg": "🔵 Telegram",
    "btn_dep_new": "💵 Deposit Baru",
    "btn_dep_hist": "📜 Riwayat",
    "btn_custom_amount": "✏️ Nominal Sendiri",
    "btn_i_paid": "✅ SUDAH BAYAR — Kirim TXID",
    "btn_get_otp": "📩 Ambil OTP",
    "btn_buy_now": "✅ Beli — ${price}",
    "kb_placeholder": "Pilih salah satu 👇",
    "menu_title": "🏠 <b>Menu Utama</b>",
    "menu_where": "👉 Mau ke mana selanjutnya?",
    "menu_footer": "✅ Selesai! Anda kembali ke Menu Utama 👇",
    "blocked": "🔒 <b>Akses diblokir</b>\nAkun ini tidak bisa memakai bot lagi.",
    "lang_pick_title": "🌐 <b>Pilih Bahasa Anda</b>",
    "lang_pick_hint": "👉 Ketuk bahasa Anda untuk lanjut",
    "lang_set_ok": "✅ Bahasa diatur: {lang}",
    "lang_current": "🌐 Bahasa saat ini: <b>{lang}</b>\nKetuk bahasa di bawah untuk mengganti.",
    "welcome_hi": "👋 <b>Hai {name}, selamat datang kembali!</b>",
    "welcome_tagline": "📱 Nomor WhatsApp &amp; Telegram premium\n⚡ Antar instan • Termasuk OTP",
    "welcome_balance": "💰 Saldo: <code>${bal}</code>",
    "welcome_stock": "📦 Stok: <code>{total}</code> nomor",
    "welcome_cta": "👉 Ketuk tombol di bawah untuk mulai",
    "profile_title": "👤 <b>Profil Anda</b>",
    "lbl_id": "🆔 ID:",
    "lbl_name": "📝 Nama:",
    "lbl_username": "🌐 Nama pengguna:",
    "prof_purchased": "🛒 Dibeli: <code>{n}</code>",
    "prof_spent": "💸 Belanja: <code>${amount}</code>",
    "prof_deposited": "🏦 Deposit: <code>${amount}</code>",
    "prof_otps": "📩 OTP: <code>{n} ({pct})</code>",
    "support_title": "💬 <b>Butuh Bantuan?</b>",
    "support_admin": "👨‍💻 Admin: {handle}",
    "support_time": "⚡ Waktu balas: biasanya hanya beberapa menit",
    "support_body": "Pembayaran, masalah OTP, pertanyaan stok — kirim pesan saja, kami siap membantu. 🙌",
    "buy_title": "🛒 <b>Beli Nomor</b>",
    "buy_wa_price": "🟢 WhatsApp — <code>${wa}</code>",
    "buy_tg_price": "🔵 Telegram — <code>${tg}</code>",
    "buy_pick": "👉 Pilih jenis untuk lanjut",
    "ctry_title": "🌍 <b>Pilih Negara</b>",
    "ctry_avail": "📱 Nomor {label} tersedia",
    "cta_select": "👉 Pilih di bawah",
    "confirm_title": "🧾 <b>Konfirmasi Pesanan</b>",
    "cf_type": "📱 Jenis: {label}",
    "cf_country": "🌍 Negara: {flag} {country}",
    "cf_price": "💵 Harga: <code>${rate}</code>",
    "cf_balance": "💰 Saldo Anda: <code>${bal}</code>",
    "cf_cta": "👉 Semua benar? Konfirmasi di bawah",
    "ps_title": "✅ <b>Pembelian Selesai!</b>",
    "ps_number": "📱 Nomor: <code>{number}</code>",
    "ps_label": "🏷️ {label} • {flag} {country}",
    "ps_paid": "💵 Dibayar: <code>${rate}</code>",
    "ps_order": "🧾 Pesanan: <code>{order}</code>",
    "ps_get_otp": "📩 Ketuk <b>Get OTP</b> di bawah kapan saja untuk ambil kode",
    "ps_copy": "📋 Ketuk nomor untuk menyalinnya",
    "ins_title": "⚠️ <b>Saldo Tidak Cukup</b>",
    "ins_price": "💵 Harga: <code>${rate}</code>",
    "ins_balance": "💰 Saldo: <code>${bal}</code>",
    "ins_need": "❗ Anda butuh: <code>${need}</code> lagi",
    "ins_cta": "👉 Isi saldo sekali ketuk",
    "oos_title": "❌ <b>Stok Habis</b>",
    "oos_label": "🏷️ {label} — {flag} {country}",
    "oos_cta": "👉 Coba negara lain, atau hubungi 💬 dukungan",
    "otp_received": "🎉 <b>OTP Diterima!</b>",
    "otp_waiting": "⏳ <b>Masih Menunggu OTP</b>",
    "otp_waiting_body": "SMS kadang butuh waktu — kami terus memeriksa di latar belakang. Kode akan otomatis muncul di sini. 👀",
    "otp_blocked": "🔒 <b>OTP Diblokir</b>",
    "otp_blocked_body": "Nomor ini sudah di-refund — OTP tidak akan pernah datang lagi di sini.",
    "toast_no_link": "ℹ️ Nomor ini tidak punya tautan OTP — hubungi dukungan",
    "otp_timeout": "⏳ <b>OTP Belum Datang dalam 10 Menit</b>",
    "otp_timeout_body": "SMS memang bisa telat. Ketuk 🔑 <b>Get OTP</b> di struk untuk cek lagi kapan saja.",
    "toast_not_yours": "❌ Ini bukan nomor Anda",
    "toast_not_found": "❌ Nomor tidak ditemukan",
    "dep_title": "💳 <b>Deposit</b>",
    "dep_min_line": "💵 Minimal: <code>${min}</code> • Terverifikasi TXID 🔐",
    "dep_min_only": "💵 Minimal: <code>${min}</code>",
    "cta_pick": "👉 Pilih salah satu",
    "dep_amt_title": "💰 <b>Pilih Nominal</b>",
    "dep_amt_hint": "👉 Ketuk nominal, atau ✏️ Sendiri",
    "dep_net_title": "🌐 <b>Pilih Jaringan</b>",
    "dep_net_amount": "💵 <code>${amount}</code> USDT",
    "dep_net_hint": "👉 Ketuk jaringan Anda",
    "dep_hist_title": "📜 <b>Riwayat Deposit</b>",
    "dep_hist_empty": "Belum ada deposit — deposit pertama Anda akan tampil di sini.",
    "dep_min_warn": "⚠️ Deposit minimal <code>${min}</code>\n👉 Pilih lagi di bawah",
    "custom_title": "✏️ <b>Tulis Nominal Anda</b>\n💵 Dalam USDT — minimal <code>${min}</code>\nContoh: <code>1.50</code>",
    "custom_err": "❌ Deposit minimal <code>${min}</code>\n💵 Tulis lagi nominal USDT\nContoh: <code>1.50</code>",
    "card_send": "💸 <b>Kirim ${amount} USDT</b>",
    "card_network": "🌐 Jaringan: <b>{net}</b>",
    "card_address": "📍 Alamat (ketuk untuk salin):",
    "card_warn": "⚠️ Hanya <b>{net}</b> — salah jaringan = dana hilang.",
    "card_paid": "✅ Sudah bayar? Ketuk <b>I PAID</b> → lalu kirim TXID Anda.",
    "card_expire": "🧾 <code>{dep_id}</code> • kedaluwarsa {expires} ⏳",
    "txid_title": "🔑 <b>Tempel TXID {net} Anda</b>",
    "txid_body": "📋 Hash transaksi pembayaran Anda.",
    "txid_format": "Format: <code>{fmt}</code>",
    "txid_ok_line": "✅ Terverifikasi → saldo langsung masuk",
    "txid_no_line": "❌ Tanpa TXID → tidak ada kredit",
    "dep_cancelled": "❌ <b>Deposit dibatalkan.</b>",
    "dep_expired_session": "ℹ️ Sesi berakhir.\nMulai deposit baru dari menu.",
    "dep_no_active": "ℹ️ Tidak ada pesanan deposit aktif.\nMulai deposit baru dari menu.",
    "dep_closed": "ℹ️ Pesanan deposit ini sudah ditutup.\nMulai yang baru dari menu.",
    "toast_bad_amount": "❌ Nominal tidak valid",
    "scr_needed": "❌ <b>Tidak perlu tangkapan layar.</b>\nSilakan kirim <b>TXID</b> (hash transaksi) Anda sebagai teks.",
    "txid_bad_fmt": "❌ <b>Format TXID salah</b>\n{net} butuh <code>{fmt}</code>. Salin hash lengkap dari dompet Anda.",
    "dep_checking": "⏳ Memeriksa transaksi {net} Anda...",
    "dep_locked": "🔒 Pesanan terkunci — terlalu banyak TXID salah.\nHubungi admin dengan ID pesanan <code>{order}</code>.",
    "txid_replay": "🔁 TXID ini sudah pernah dipakai.\nSatu TXID = satu pesanan. Kirim hash transaksi baru Anda.",
    "bin_pay_id": "🏦 <b>Binance Pay ID</b> - kirim KE ID ini:",
    "bin_card_hint": "⚠️ Bayar lewat <b>aplikasi Binance → Pay</b>\n💵 Kirim <b>USDT saja</b>, tepat sesuai jumlah di atas.\n❌ ID atau aset salah = uang hilang.",
    "bin_auto_line": "⚡ Pembayaran terverifikasi otomatis dalam ~1 menit.\nAtau tekan I PAID dan tempel Order ID.",
    "bin_txid_title": "🔑 <b>Tempel Order ID Binance Pay Anda</b>",
    "bin_txid_body": "📋 Aplikasi Binance → Pay → buka transfer Anda → salin <b>Order ID</b> dan tempel di sini.",
    "bin_bad_fmt": "❌ <b>Itu bukan Order ID Binance Pay.</b>\nBentuknya seperti <code>M_P_123456789012345678</code> - salin dari aplikasi Binance → Pay → detail transfer.",
    "bin_amt_mismatch": "❌ <b>Jumlah tidak cocok.</b>\nPembayaran menunjukkan <code>${got}</code>, pesanan butuh <code>${want}</code>.\nBayar jumlah yang tepat, lalu tempel Order ID-nya.",
    "bin_decline_pending": "⏳ Pembayaran untuk Order ID ini belum ditemukan.\nBayar dulu, periksa Order ID, dan kirim lagi dalam satu menit.",
    "bin_decline_stale": "❌ Order ID ini tidak bisa dipakai untuk pesanan ini.\nLebih lama dari pesanan atau sudah terpakai.\nBayar baru dan tempel Order ID baru.",
    "bin_decline_out": "❌ Itu transfer KELUAR (OUTGOING) - uang terkirim ke luar.\nTempel Order ID transfer yang Anda kirim KEPADA kami.",
    "dep_api_busy": "⏳ Verifikasi Binance sedang sibuk.\nPesanan Anda aman - coba lagi dalam satu menit.",
    "amt_mismatch": "❌ <b>Nominal tidak cocok.</b>\nTransaksi menunjukkan <code>${got}</code>, pesanan butuh <code>${want}</code>.\nKirim hash yang benar, atau mulai deposit baru.",
    "dep_already": "✅ Deposit ini sudah dikonfirmasi.\nSaldo Anda sudah diperbarui.",
    "dep_ok_title": "✅ <b>Deposit Terkonfirmasi!</b>",
    "dep_ok_credited": "💵 Masuk: <code>${amount}</code>",
    "dep_ok_balance": "💰 Saldo: <code>${bal}</code>",
    "dep_ok_cta": "🛒 Belanja nyaman — ketuk Buy di bawah!",
    "decline_pending": "⏳ Transaksi belum ditemukan di {net}.\nPeriksa TXID dan kirim lagi dalam satu menit.",
    "decline_failed": "❌ Transaksi gagal di rantai — dana tidak berpindah.\nKirim TXID baru yang berhasil.",
    "decline_token": "❌ Itu bukan transfer USDT di {net}.\nKirim USDT saja.",
    "decline_recipient": "❌ Penerima salah.\nTXID ini tidak mengirim USDT ke alamat {net} kami.",
    "dm_credited": "✅ Masuk <code>${amount}</code> • Saldo <code>${bal}</code>\n🧾 Pesanan <code>{order}</code>",
    "dm_dep_confirmed": "✅ <b>DEPOSIT KONFIRM</b>\n\n{div}\n💵 <b>Nominal:</b> ${amount}\n🧾 <b>Pesanan:</b> <code>{order}</code>\n{div}\n\n💰 <b>Saldo diperbarui! Belanja nyaman 🛒</b>",
    "dm_dep_rejected": "❌ <b>DEPOSIT DITOLAK</b>\n\n{div}\n🧾 <b>Pesanan:</b> <code>{order}</code>\n{div}\n\n💬 Hubungi dukungan jika Anda merasa ini keliru.",
    "help_title": "📖 <b>Bantuan Cepat</b>",
    "help_lines": "/start — buka menu utama\n/menu — tampilkan menu\n/language — ganti bahasa\n/admin — panel admin",
    "help_cta": "💡 Semuanya sekali ketuk lewat tombol di bawah.",
    "err_generic": "⚠️ <b>Terjadi kesalahan.</b>\nCoba lagi — atau tekan /start.",
    "toast_processing": "Memproses pembelian... ⏳",
    "toast_invalid": "Permintaan tidak valid",
    "toast_expired": "❌ Tombol ini kedaluwarsa — coba lagi",
    "btn_join_channel": "✉️ GABUNG CHANNEL",
    "btn_join_group": "✉️ GABUNG GRUP",
    "fj_title": "🔒 <b>Satu Langkah Lagi untuk Membuka</b>",
    "fj_body": "👉 Gabung channel kami di bawah untuk menggunakan bot.\n✅ Setelah gabung, ketuk <b>Verifikasi</b>.",
    "btn_fj_check": "✅ Verifikasi",
    "fj_toast_no": "❌ Kamu belum gabung — gabung dulu, lalu ketuk Verifikasi.",
    "fj_done": "✅ <b>Terverifikasi!</b>\n🎉 Selamat — menu utama kamu terbuka di bawah 👇",
    "fj_dm": "✅ <b>Join terverifikasi!</b>\n👋 Selamat — menu utama terbuka 👇",
    "btn_refer": "🎁 Refer & Hasilkan",
    "btn_active": "📱 Nomor Aktif",
    "btn_ubulk": "📦 Beli Massal",
    "ub_pick": "📦 <b>Beli Massal</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> tersedia • <code>${wa_rate}</code>/nomor\n🔵 Telegram — <code>{tg_n}</code> tersedia • <code>${tg_rate}</code>/nomor\n\n🎁 <b>{dmin}+ nomor = hemat ${damt} per nomor</b>\n\n👉 Pilih jenis:",
    "ub_qty": "📦 <b>Beli Massal — {label}</b>\n\n📱 Tersedia: <code>{n}</code>\n💵 Harga: <code>${rate}</code> per nomor\n💰 Saldo: <code>${bal}</code>\n\n🎁 {dmin}+ = <b>hemat ${damt} per nomor</b>\n\n👉 Ketik BERAPA nomor yang mau dibeli:",
    "ub_bad_qty": "❌ Tulis ANGKA saja (1 sampai {cap}).\n👉 Coba lagi:",
    "ub_stock_low": "⚠️ Hanya <code>{n}</code> tersedia saat ini.\n👉 Ketik jumlah lebih kecil:",
    "ub_no_bal": "⚠️ {n} nomor = <code>${total}</code>\n💰 Saldo: <code>${bal}</code>\n👉 Maksimal: <code>{maxn}</code> nomor. Ketik itu (atau kurang):",
    "ub_confirm": "🧾 <b>Konfirmasi Pesanan</b>\n\n{div}\n📱 Jenis: <b>{label}</b>\n🔢 Jumlah: <code>{n}</code>\n💵 Harga: <code>${unit}</code> per nomor {disc}\n💰 Total: <code>${total}</code>\n💰 Sisa saldo: <code>${after}</code>\n{div}\n\n👉 Konfirmasi di bawah — file .txt langsung dikirim.",
    "ub_disc": "(diskon {dmin}+ ✅)",
    "ub_expired": "⏳ Sesi kedaluwarsa — mulai lagi dari 📦 Beli Massal.",
    "ub_done": "✅ <b>Pesanan Massal Selesai!</b>\n\n{div}\n📱 Nomor terkirim: <code>{n}</code>\n💵 Dibayar: <code>${total}</code> (<code>${unit}</code>/nomor {disc})\n💰 Saldo: <code>${bal}</code>\n{div}\n\n📎 <code>{fname}</code> terlampir — setiap nomor dengan link API OTP.\n📩 Setiap OTP otomatis masuk ke chat ini.\n📱 Pantau kapan saja di 📱 Active Numbers.",
    "ub_partial": "⚠️ Stok bergerak cepat — hanya <code>{n}</code> tersedia. Anda hanya dibebankan untuk <code>{n}</code>.",
    "ub_none": "❌ <b>Stok habis</b> — tidak ada yang ditagih.",
    "ub_hint_file": "❌ Itu file — di sini butuh ANGKA.\n👉 Ketik BERAPA nomor yang mau dibeli:",
    "act_title": "📞 <b>Nomor Aktif Anda</b> ({n})",
    "act_none": "📭 Anda belum punya nomor aktif saat ini.\n🛒 Beli nomor — langsung muncul di sini.",
    "act_hint": "▶️ Ketuk nomor untuk menyalin, lalu kirim di sini — nomor terbuka dengan tombol Get OTP.",
    "act_more": "…dan {extra} lagi",
    "act_card_title": "🟢 <b>Nomor Aktif Anda</b>",
    "act_card_body": "📩 Tekan GET OTP kapan saja — kode sampai ke Anda begitu datang. Tanpa batas waktu.",
    "rfs_title": "🎉 <b>Refund Anda Berhasil</b>",
    "rfs_body": "🟢 <code>{number}</code>\n💰 <code>${amount}</code> ditambahkan ke saldo Anda",
    "ref_title": "🤝 <b>Refer &amp; Earn</b>",
    "ref_body": "Bagikan tautanmu — kamu dapat <b>${rate}</b> setiap kali temanmu membeli nomor. Selamanya.",
    "ref_link": "🔗 Tautan referral kamu:",
    "ref_stats": "👥 Referal: <b>{count}</b>\n💰 Total dihasilkan: <b>${earned}</b>",
    "ref_rate_line": "💵 Ratemu: <b>${rate}</b> per pembelian",
    "ref_vip_line": "👑 <b>Referer VIP</b> — tarif khusus <b>${rate}</b> per pembelian",
    "btn_ref_share": "📤 Bagikan Tautan",
    "ref_share_text": "🎁 Nomor WhatsApp & Telegram premium — OTP instan!",
    "ref_none_yet": "Belum ada referal — bagikan tautanmu untuk mulai menghasilkan 👇",
    "ref_earned_notif": "🎉 <b>Bonus Referal!</b>\n{div}\n👤 {name} membeli nomor\n💰 <b>+${amount}</b> ditambahkan ke saldo kamu\n💼 Saldo: <b>${bal}</b>\n{div}",
    "ref_new_ref": "👥 <b>Referal baru!</b>\n👤 {name} bergabung lewat tautanmu\n💰 Kamu dapat hasil dari setiap pembeliannya",
    "ref_paused": "⏸ Program referal sedang dijeda.\n💡 Cek lagi nanti!",
},

    "tr": {
    "btn_buy": "🛒 Numara Satın Al",
    "btn_profile": "👤 Profil",
    "btn_deposit": "💳 Bakiye Yükle",
    "btn_support": "💬 Destek",
    "btn_back": "⬅️ Geri",
    "btn_cancel_dep": "❌ Yükleme İptal",
    "btn_wa": "🟢 WhatsApp",
    "btn_tg": "🔵 Telegram",
    "btn_dep_new": "💵 Yeni Yükleme",
    "btn_dep_hist": "📜 Geçmiş",
    "btn_custom_amount": "✏️ Özel Tutar",
    "btn_i_paid": "✅ ÖDEDİM — TXID Gönder",
    "btn_get_otp": "📩 Kod Al",
    "btn_buy_now": "✅ Satın Al — ${price}",
    "kb_placeholder": "Bir seçenek seçin 👇",
    "menu_title": "🏠 <b>Ana Menü</b>",
    "menu_where": "👉 Şimdi nereye gitmek istersiniz?",
    "menu_footer": "✅ Tamam! Ana menüdesiniz 👇",
    "blocked": "🔒 <b>Erişim engellendi</b>\nBu hesap artık botu kullanamaz.",
    "lang_pick_title": "🌐 <b>Dilinizi Seçin</b>",
    "lang_pick_hint": "👉 Devam etmek için dilinize dokunun",
    "lang_set_ok": "✅ Dil ayarlandı: {lang}",
    "lang_current": "🌐 Mevcut dil: <b>{lang}</b>\nDeğiştirmek için aşağıdaki bir dile dokunun.",
    "welcome_hi": "👋 <b>Merhaba {name}, tekrar hoş geldiniz!</b>",
    "welcome_tagline": "📱 Premium WhatsApp ve Telegram numaraları\n⚡ Anında teslim • OTP dahil",
    "welcome_balance": "💰 Bakiye: <code>${bal}</code>",
    "welcome_stock": "📦 Stokta: <code>{total}</code> numara",
    "welcome_cta": "👉 Başlamak için aşağıdaki bir düğmeye dokunun",
    "profile_title": "👤 <b>Profiliniz</b>",
    "lbl_id": "🆔 ID:",
    "lbl_name": "📝 Ad:",
    "lbl_username": "🌐 Kullanıcı adı:",
    "prof_purchased": "🛒 Satın alınan: <code>{n}</code>",
    "prof_spent": "💸 Harcanan: <code>${amount}</code>",
    "prof_deposited": "🏦 Yüklenen: <code>${amount}</code>",
    "prof_otps": "📩 OTP: <code>{n} ({pct})</code>",
    "support_title": "💬 <b>Yardım mı lazım?</b>",
    "support_admin": "👨‍💻 Yönetici: {handle}",
    "support_time": "⚡ Yanıt süresi: genellikle birkaç dakika",
    "support_body": "Ödemeler, OTP sorunları, stok soruları — bize yazın, yanınızdayız. 🙌",
    "buy_title": "🛒 <b>Numara Satın Al</b>",
    "buy_wa_price": "🟢 WhatsApp — <code>${wa}</code>",
    "buy_tg_price": "🔵 Telegram — <code>${tg}</code>",
    "buy_pick": "👉 Devam etmek için bir tür seçin",
    "ctry_title": "🌍 <b>Ülke Seçin</b>",
    "ctry_avail": "📱 {label} numaraları mevcut",
    "cta_select": "👉 Aşağıdan seçin",
    "confirm_title": "🧾 <b>Siparişi Onaylayın</b>",
    "cf_type": "📱 Tür: {label}",
    "cf_country": "🌍 Ülke: {flag} {country}",
    "cf_price": "💵 Fiyat: <code>${rate}</code>",
    "cf_balance": "💰 Bakiyeniz: <code>${bal}</code>",
    "cf_cta": "👉 Her şey tamam mı? Aşağıda onaylayın",
    "ps_title": "✅ <b>Satın Alma Tamam!</b>",
    "ps_number": "📱 Numara: <code>{number}</code>",
    "ps_label": "🏷️ {label} • {flag} {country}",
    "ps_paid": "💵 Ödenen: <code>${rate}</code>",
    "ps_order": "🧾 Sipariş: <code>{order}</code>",
    "ps_get_otp": "📩 Kodunuzu almak için aşağıdaki <b>Get OTP</b>'ye istediğiniz zaman dokunun",
    "ps_copy": "📋 Kopyalamak için numaraya dokunun",
    "ins_title": "⚠️ <b>Bakiye Yetersiz</b>",
    "ins_price": "💵 Fiyat: <code>${rate}</code>",
    "ins_balance": "💰 Bakiye: <code>${bal}</code>",
    "ins_need": "❗ Gereken: <code>${need}</code> daha",
    "ins_cta": "👉 Tek dokunuşla bakiye yükle",
    "oos_title": "❌ <b>Stokta Yok</b>",
    "oos_label": "🏷️ {label} — {flag} {country}",
    "oos_cta": "👉 Başka bir ülke deneyin veya 💬 Destek'e yazın",
    "otp_received": "🎉 <b>OTP Alındı!</b>",
    "otp_waiting": "⏳ <b>OTP Hâlâ Bekleniyor</b>",
    "otp_waiting_body": "SMS biraz gecikebilir — arka planda kontrol etmeye devam ediyoruz. Kod kendiliğinden buraya düşecek. 👀",
    "otp_blocked": "🔒 <b>OTP Engellendi</b>",
    "otp_blocked_body": "Bu numara iade edildi — buraya bir daha asla OTP gelmez.",
    "toast_no_link": "ℹ️ Bu numarada OTP bağlantısı yok — desteğe başvurun",
    "otp_timeout": "⏳ <b>10 Dakikada OTP Gelmedi</b>",
    "otp_timeout_body": "SMS gecikebiliyor. Fişinizdeki 🔑 <b>Get OTP</b> düğmesine basıp istediğiniz an tekrar kontrol edin.",
    "toast_not_yours": "❌ Bu numara size ait değil",
    "toast_not_found": "❌ Numara bulunamadı",
    "dep_title": "💳 <b>Bakiye Yükle</b>",
    "dep_min_line": "💵 En az: <code>${min}</code> • TXID doğrulamalı 🔐",
    "dep_min_only": "💵 En az: <code>${min}</code>",
    "cta_pick": "👉 Bir seçenek seçin",
    "dep_amt_title": "💰 <b>Tutar Seçin</b>",
    "dep_amt_hint": "👉 Bir tutara dokunun veya ✏️ Özel",
    "dep_net_title": "🌐 <b>Ağ Seçin</b>",
    "dep_net_amount": "💵 <code>${amount}</code> USDT",
    "dep_net_hint": "👉 Ağınızı seçin",
    "dep_hist_title": "📜 <b>Yükleme Geçmişi</b>",
    "dep_hist_empty": "Henüz yükleme yok — ilk yüklemeniz burada görünecek.",
    "dep_min_warn": "⚠️ En düşük yükleme <code>${min}</code>\n👉 Aşağıdan yeniden seçin",
    "custom_title": "✏️ <b>Tutarınızı Yazın</b>\n💵 USDT cinsinden — en az <code>${min}</code>\nÖrnek: <code>1.50</code>",
    "custom_err": "❌ En düşük yükleme <code>${min}</code>\n💵 USDT tutarını tekrar yazın\nÖrnek: <code>1.50</code>",
    "card_send": "💸 <b>${amount} USDT gönderin</b>",
    "card_network": "🌐 Ağ: <b>{net}</b>",
    "card_address": "📍 Adres (kopyalamak için dokunun):",
    "card_warn": "⚠️ Yalnızca <b>{net}</b> — yanlış ağ = para kaybı.",
    "card_paid": "✅ Ödediniz mi? <b>I PAID</b>'e dokunun → sonra TXID'nizi gönderin.",
    "card_expire": "🧾 <code>{dep_id}</code> • bitiş {expires} ⏳",
    "txid_title": "🔑 <b>{net} TXID'nizi yapıştırın</b>",
    "txid_body": "📋 Ödemenizin işlem karması (hash).",
    "txid_format": "Biçim: <code>{fmt}</code>",
    "txid_ok_line": "✅ Doğrulandı → anında bakiye",
    "txid_no_line": "❌ TXID yok → bakiye yok",
    "dep_cancelled": "❌ <b>Yükleme iptal edildi.</b>",
    "dep_expired_session": "ℹ️ Oturum süresi doldu.\nMenüden yeni bir yükleme başlatın.",
    "dep_no_active": "ℹ️ Aktif yükleme siparişi bulunamadı.\nMenüden yeni bir yükleme başlatın.",
    "dep_closed": "ℹ️ Bu yükleme siparişi zaten kapandı.\nMenüden yenisini başlatın.",
    "toast_bad_amount": "❌ Geçersiz tutar",
    "scr_needed": "❌ <b>Ekran görüntüsü gerekmez.</b>\nLütfen <b>TXID</b>'nizi (işlem karması) metin olarak gönderin.",
    "txid_bad_fmt": "❌ <b>TXID biçimi geçersiz</b>\n{net} şunu ister: <code>{fmt}</code>. Cüzdanınızdan karmayı tam kopyalayın.",
    "dep_checking": "⏳ {net} işleminiz kontrol ediliyor...",
    "dep_locked": "🔒 Sipariş kilitli — çok fazla yanlış TXID.\nSipariş numarası <code>{order}</code> ile yönetime yazın.",
    "txid_replay": "🔁 Bu TXID daha önce kullanıldı.\nBir TXID = bir sipariş. Yeni işlem karmınızı gönderin.",
    "bin_pay_id": "🏦 <b>Binance Pay ID</b> - bu IDye GÖNDER:",
    "bin_card_hint": "⚠️ <b>Binance uygulaması → Pay</b> ile ödeyin\n💵 Sadece <b>USDT</b>, yukarıdaki tam tutarda gönderin.\n❌ Yanlış ID veya varlık = para kaybı.",
    "bin_auto_line": "⚡ Ödeme ~1 dakikada otomatik onaylanır.\nYa da I PAID butonuna basıp Order ID yapıştırın.",
    "bin_txid_title": "🔑 <b>Binance Pay Sipariş Numaranızı (Order ID) Yapıştırın</b>",
    "bin_txid_body": "📋 Binance uygulaması → Pay → transferinizi açın → <b>Order ID</b> bilgisini kopyalayıp buraya yapıştırın.",
    "bin_bad_fmt": "❌ <b>Bu bir Binance Pay Order ID değil.</b>\nŞuna benzer: <code>M_P_123456789012345678</code> - Binance uygulaması → Pay → transfer detayından kopyalayın.",
    "bin_amt_mismatch": "❌ <b>Tutar uyuşmuyor.</b>\nÖdeme <code>${got}</code> gösteriyor, sipariş <code>${want}</code> istiyor.\nTam tutarı ödeyin, sonra o Order ID bilgisini yapıştırın.",
    "bin_decline_pending": "⏳ Bu Order ID için henüz ödeme bulunamadı.\nÖnce ödeyin, Order ID bilgisini kontrol edin, bir dakika sonra tekrar gönderin.",
    "bin_decline_stale": "❌ Bu Order ID bu sipariş için kullanılamaz.\nSiparişten eski veya zaten kullanılmış.\nYeni ödeme yapıp yeni Order ID gönderin.",
    "bin_decline_out": "❌ Bu bir GİDEN (OUTGOING) transfer - para dışarı gitti.\nBize gönderdiğiniz transferin Order ID bilgisini yapıştırın.",
    "dep_api_busy": "⏳ Binance doğrulaması şu an meşgul.\nSiparişiniz güvende - bir dakika sonra tekrar deneyin.",
    "amt_mismatch": "❌ <b>Tutar uyuşmuyor.</b>\nİşlem <code>${got}</code> gösteriyor, sipariş <code>${want}</code> bekliyor.\nDoğru karmayı gönderin veya yeni yükleme başlatın.",
    "dep_already": "✅ Bu yükleme zaten onaylandı.\nBakiyeniz güncel.",
    "dep_ok_title": "✅ <b>Yükleme Onaylandı!</b>",
    "dep_ok_credited": "💵 Yüklendi: <code>${amount}</code>",
    "dep_ok_balance": "💰 Bakiye: <code>${bal}</code>",
    "dep_ok_cta": "🛒 İyi alışverişler — aşağıda Buy'a dokunun!",
    "decline_pending": "⏳ İşlem {net} üzerinde henüz görünmüyor.\nTXID'yi kontrol edip bir dakika sonra tekrar gönderin.",
    "decline_failed": "❌ İşlem zincirde başarısız — para hareket etmedi.\nYeni, başarılı bir TXID gönderin.",
    "decline_token": "❌ Bu, {net} üzerinde bir USDT transferi değildi.\nLütfen yalnızca USDT gönderin.",
    "decline_recipient": "❌ Alıcı yanlış.\nBu TXID, {net} adresimize USDT göndermemiş.",
    "dm_credited": "✅ Yüklendi <code>${amount}</code> • Bakiye <code>${bal}</code>\n🧾 Sipariş <code>{order}</code>",
    "dm_dep_confirmed": "✅ <b>YÜKLEME ONAYLANDI</b>\n\n{div}\n💵 <b>Tutar:</b> ${amount}\n🧾 <b>Sipariş:</b> <code>{order}</code>\n{div}\n\n💰 <b>Bakiye güncellendi! İyi alışverişler 🛒</b>",
    "dm_dep_rejected": "❌ <b>YÜKLEME REDDEDİLDİ</b>\n\n{div}\n🧾 <b>Sipariş:</b> <code>{order}</code>\n{div}\n\n💬 Hatalı olduğunu düşünüyorsanız Destek'e yazın.",
    "help_title": "📖 <b>Hızlı Yardım</b>",
    "help_lines": "/start — ana menüyü aç\n/menu — menüyü göster\n/language — dili değiştir\n/admin — yönetici paneli",
    "help_cta": "💡 Her şey aşağıdaki düğmelerle tek dokunuş uzağınızda.",
    "err_generic": "⚠️ <b>Bir şeyler ters gitti.</b>\nTekrar deneyin — veya /start'a basın.",
    "toast_processing": "Satın alma işleniyor... ⏳",
    "toast_invalid": "Geçersiz istek",
    "toast_expired": "❌ Bu düğmenin süresi doldu — tekrar deneyin",
    "btn_join_channel": "✉️ KANALA KATIL",
    "btn_join_group": "✉️ GRUBA KATIL",
    "fj_title": "🔒 <b>Açmak için Bir Adım Kaldı</b>",
    "fj_body": "👉 Botu kullanmak için aşağıdaki kanalımıza katılın.\n✅ Katıldıktan sonra <b>Doğrula</b> düğmesine dokunun.",
    "btn_fj_check": "✅ Doğrula",
    "fj_toast_no": "❌ Henüz katılmadınız — katılın, sonra Doğrula'ya dokunun.",
    "fj_done": "✅ <b>Doğrulandı!</b>\n🎉 Hoş geldiniz — ana menünüz aşağıda açıldı 👇",
    "fj_dm": "✅ <b>Katılım doğrulandı!</b>\n👋 Hoş geldiniz — ana menü açıldı 👇",
    "btn_refer": "🎁 Davet Et & Kazan",
    "btn_active": "📱 Aktif Numaralar",
    "btn_ubulk": "📦 Toplu Alım",
    "ub_pick": "📦 <b>Toplu Alım</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> stokta • tanesi <code>${wa_rate}</code>\n🔵 Telegram — <code>{tg_n}</code> stokta • tanesi <code>${tg_rate}</code>\n\n🎁 <b>{dmin}+ numara = numara başına ${damt} indirim</b>\n\n👉 Tür seç:",
    "ub_qty": "📦 <b>Toplu Alım — {label}</b>\n\n📱 Stokta: <code>{n}</code>\n💵 Fiyat: tanesi <code>${rate}</code>\n💰 Bakiye: <code>${bal}</code>\n\n🎁 {dmin}+ = tanesi <b>${damt} indirim</b>\n\n👉 KAÇ numara istediğinizi yazın:",
    "ub_bad_qty": "❌ Lütfen sadece SAYI yazın (1 ile {cap}).\n👉 Tekrar deneyin:",
    "ub_stock_low": "⚠️ şu an sadece <code>{n}</code> var.\n👉 Daha küçük bir miktar yazın:",
    "ub_no_bal": "⚠️ {n} numara = <code>${total}</code>\n💰 Bakiye: <code>${bal}</code>\n👉 Alabileceğiniz en fazla: <code>{maxn}</code>. Onu yazın:",
    "ub_confirm": "🧾 <b>Siparişi Onayla</b>\n\n{div}\n📱 Tür: <b>{label}</b>\n🔢 Adet: <code>{n}</code>\n💵 Fiyat: tanesi <code>${unit}</code> {disc}\n💰 Toplam: <code>${total}</code>\n💰 Sonra: <code>${after}</code>\n{div}\n\n👉 Aşağıda onaylayın — .txt dosyası anında gelir.",
    "ub_disc": "({dmin}+ indirim ✅)",
    "ub_expired": "⏳ Oturum süresi doldu — 📦 Toplu Alım\'dan tekrar başlayın.",
    "ub_done": "✅ <b>Toplu Sipariş Tamamlandı!</b>\n\n{div}\n📱 Teslim edilen: <code>{n}</code>\n💵 Ödenen: <code>${total}</code> (tanesi <code>${unit}</code> {disc})\n💰 Bakiye: <code>${bal}</code>\n{div}\n\n📎 <code>{fname}</code> eklendi — her numarayla OTP API linki.\n📩 Her OTP geldiğinde otomatik bu sohbete düşer.\n📱 📱 Aktif Numaralar\'dan istediğiniz zaman takip edin.",
    "ub_partial": "⚠️ Stok hızlı biti — sadece <code>{n}</code> vardı. Sadece <code>{n}</code> için ücret alındı.",
    "ub_none": "❌ <b>Stok yok</b> — hiç ücret alınmadı.",
    "ub_hint_file": "❌ Bu bir dosya — burada SAYI gerekiyor.\n👉 KAÇ numara istediğinizi yazın:",
    "act_title": "📞 <b>Aktif Numaralarınız</b> ({n})",
    "act_none": "📭 Şu anda aktif numaranız yok.\n🛒 Numara alın — anında burada görünür.",
    "act_hint": "▶️ Kopyalamak için bir numaraya dokunun, sonra buraya gönderin — numara Get OTP düğmesiyle açılır.",
    "act_more": "…ve {extra} daha",
    "act_card_title": "🟢 <b>Aktif Numaranız</b>",
    "act_card_body": "📩 İstediğiniz zaman GET OTP'ye basın — kod gelir gelmez size ulaşır. Süre sınırı yok.",
    "rfs_title": "🎉 <b>İadeniz Başarılı</b>",
    "rfs_body": "🟢 <code>{number}</code>\n💰 <code>${amount}</code> bakiyenize eklendi",
    "ref_title": "🤝 <b>Davet &amp; Kazanç</b>",
    "ref_body": "Linkini paylaş — arkadaşın her numara aldığında <b>${rate}</b> kazanırsın. Ömür boyu.",
    "ref_link": "🔗 Davet linkin:",
    "ref_stats": "👥 Davet edilen: <b>{count}</b>\n💰 Toplam kazanç: <b>${earned}</b>",
    "ref_rate_line": "💵 Oranınız: her alımda <b>${rate}</b>",
    "ref_vip_line": "👑 <b>VIP davetçi</b> — özel oran her alımda <b>${rate}</b>",
    "btn_ref_share": "📤 Linki Paylaş",
    "ref_share_text": "🎁 Premium WhatsApp ve Telegram numaraları — anında OTP!",
    "ref_none_yet": "Henüz davet yok — kazanmaya başlamak için linkini paylaş 👇",
    "ref_earned_notif": "🎉 <b>Davet bonusu!</b>\n{div}\n👤 {name} bir numara aldı\n💰 Bakiyene <b>+${amount}</b> eklendi\n💼 Bakiye: <b>${bal}</b>\n{div}",
    "ref_new_ref": "👥 <b>Yeni davet!</b>\n👤 {name} linkinle katıldı\n💰 Her alımından kazanç sağlayacaksın",
    "ref_paused": "⏸ Davet programı şu anda duraklatıldı.\n💡 Yakında tekrar bak!",
},

    "ru": {
    "btn_buy": "🛒 Купить номер",
    "btn_profile": "👤 Профиль",
    "btn_deposit": "💳 Пополнить",
    "btn_support": "💬 Поддержка",
    "btn_back": "⬅️ Назад",
    "btn_cancel_dep": "❌ Отменить пополнение",
    "btn_wa": "🟢 WhatsApp",
    "btn_tg": "🔵 Telegram",
    "btn_dep_new": "💵 Новое пополнение",
    "btn_dep_hist": "📜 История",
    "btn_custom_amount": "✏️ Своя сумма",
    "btn_i_paid": "✅ ОПЛАТИЛ — отправить TXID",
    "btn_get_otp": "📩 Получить OTP",
    "btn_buy_now": "✅ Купить — ${price}",
    "kb_placeholder": "Выберите вариант 👇",
    "menu_title": "🏠 <b>Главное меню</b>",
    "menu_where": "👉 Куда дальше?",
    "menu_footer": "✅ Готово! Вы снова в главном меню 👇",
    "blocked": "🔒 <b>Доступ закрыт</b>\nЭтот аккаунт больше не может пользоваться ботом.",
    "lang_pick_title": "🌐 <b>Выберите язык</b>",
    "lang_pick_hint": "👉 Нажмите свой язык, чтобы продолжить",
    "lang_set_ok": "✅ Язык установлен: {lang}",
    "lang_current": "🌐 Текущий язык: <b>{lang}</b>\nНажмите язык ниже, чтобы сменить.",
    "welcome_hi": "👋 <b>Привет, {name}, с возвращением!</b>",
    "welcome_tagline": "📱 Премиум-номера WhatsApp и Telegram\n⚡ Мгновенная выдача • OTP включён",
    "welcome_balance": "💰 Баланс: <code>${bal}</code>",
    "welcome_stock": "📦 В наличии: <code>{total}</code> номеров",
    "welcome_cta": "👉 Нажмите кнопку ниже, чтобы начать",
    "profile_title": "👤 <b>Ваш профиль</b>",
    "lbl_id": "🆔 ID:",
    "lbl_name": "📝 Имя:",
    "lbl_username": "🌐 Юзернейм:",
    "prof_purchased": "🛒 Куплено: <code>{n}</code>",
    "prof_spent": "💸 Потрачено: <code>${amount}</code>",
    "prof_deposited": "🏦 Пополнено: <code>${amount}</code>",
    "prof_otps": "📩 OTP: <code>{n} ({pct})</code>",
    "support_title": "💬 <b>Нужна помощь?</b>",
    "support_admin": "👨‍💻 Админ: {handle}",
    "support_time": "⚡ Время ответа: обычно пара минут",
    "support_body": "Платежи, проблемы с OTP, вопросы по стоку — просто напишите нам, мы на связи. 🙌",
    "buy_title": "🛒 <b>Купить номер</b>",
    "buy_wa_price": "🟢 WhatsApp — <code>${wa}</code>",
    "buy_tg_price": "🔵 Telegram — <code>${tg}</code>",
    "buy_pick": "👉 Выберите тип, чтобы продолжить",
    "ctry_title": "🌍 <b>Выберите страну</b>",
    "ctry_avail": "📱 Номера {label} в наличии",
    "cta_select": "👉 Выберите ниже",
    "confirm_title": "🧾 <b>Подтвердите заказ</b>",
    "cf_type": "📱 Тип: {label}",
    "cf_country": "🌍 Страна: {flag} {country}",
    "cf_price": "💵 Цена: <code>${rate}</code>",
    "cf_balance": "💰 Ваш баланс: <code>${bal}</code>",
    "cf_cta": "👉 Всё верно? Подтвердите ниже",
    "ps_title": "✅ <b>Покупка завершена!</b>",
    "ps_number": "📱 Номер: <code>{number}</code>",
    "ps_label": "🏷️ {label} • {flag} {country}",
    "ps_paid": "💵 Оплачено: <code>${rate}</code>",
    "ps_order": "🧾 Заказ: <code>{order}</code>",
    "ps_get_otp": "📩 Нажмите <b>Get OTP</b> ниже в любое время, чтобы получить код",
    "ps_copy": "📋 Нажмите на номер, чтобы скопировать",
    "ins_title": "⚠️ <b>Недостаточно средств</b>",
    "ins_price": "💵 Цена: <code>${rate}</code>",
    "ins_balance": "💰 Баланс: <code>${bal}</code>",
    "ins_need": "❗ Нужно ещё: <code>${need}</code>",
    "ins_cta": "👉 Пополнить в один тап",
    "oos_title": "❌ <b>Нет в наличии</b>",
    "oos_label": "🏷️ {label} — {flag} {country}",
    "oos_cta": "👉 Попробуйте другую страну или напишите в 💬 Поддержку",
    "otp_received": "🎉 <b>OTP получен!</b>",
    "otp_waiting": "⏳ <b>Ещё ждём OTP</b>",
    "otp_waiting_body": "SMS может прийти не сразу — мы проверяем в фоне. Код сам появится здесь. 👀",
    "otp_blocked": "🔒 <b>OTP заблокирован</b>",
    "otp_blocked_body": "Этот номер был возвращён — OTP сюда больше никогда не придёт.",
    "toast_no_link": "ℹ️ У этого номера нет OTP-ссылки — обратитесь в поддержку",
    "otp_timeout": "⏳ <b>OTP не пришёл за 10 минут</b>",
    "otp_timeout_body": "SMS иногда задерживается. Нажмите 🔑 <b>Get OTP</b> в квитанции, чтобы проверить снова в любой момент.",
    "toast_not_yours": "❌ Это не ваш номер",
    "toast_not_found": "❌ Номер не найден",
    "dep_title": "💳 <b>Пополнение</b>",
    "dep_min_line": "💵 Минимум: <code>${min}</code> • Проверка по TXID 🔐",
    "dep_min_only": "💵 Минимум: <code>${min}</code>",
    "cta_pick": "👉 Выберите вариант",
    "dep_amt_title": "💰 <b>Выберите сумму</b>",
    "dep_amt_hint": "👉 Нажмите сумму или ✏️ Своя",
    "dep_net_title": "🌐 <b>Выберите сеть</b>",
    "dep_net_amount": "💵 <code>${amount}</code> USDT",
    "dep_net_hint": "👉 Нажмите свою сеть",
    "dep_hist_title": "📜 <b>История пополнений</b>",
    "dep_hist_empty": "Пока нет пополнений — первое появится здесь.",
    "dep_min_warn": "⚠️ Минимальное пополнение <code>${min}</code>\n👉 Выберите снова ниже",
    "custom_title": "✏️ <b>Введите сумму</b>\n💵 В USDT — минимум <code>${min}</code>\nПример: <code>1.50</code>",
    "custom_err": "❌ Минимальное пополнение <code>${min}</code>\n💵 Введите сумму USDT ещё раз\nПример: <code>1.50</code>",
    "card_send": "💸 <b>Отправьте ${amount} USDT</b>",
    "card_network": "🌐 Сеть: <b>{net}</b>",
    "card_address": "📍 Адрес (нажмите, чтобы скопировать):",
    "card_warn": "⚠️ Только <b>{net}</b> — не та сеть = потеря средств.",
    "card_paid": "✅ Оплатили? Нажмите <b>I PAID</b> → затем отправьте свой TXID.",
    "card_expire": "🧾 <code>{dep_id}</code> • истекает {expires} ⏳",
    "txid_title": "🔑 <b>Вставьте свой TXID {net}</b>",
    "txid_body": "📋 Хэш транзакции вашей оплаты.",
    "txid_format": "Формат: <code>{fmt}</code>",
    "txid_ok_line": "✅ Проверено → мгновенный баланс",
    "txid_no_line": "❌ Нет TXID → нет зачисления",
    "dep_cancelled": "❌ <b>Пополнение отменено.</b>",
    "dep_expired_session": "ℹ️ Сессия истекла.\nНачните новое пополнение из меню.",
    "dep_no_active": "ℹ️ Активный заказ на пополнение не найден.\nНачните новое из меню.",
    "dep_closed": "ℹ️ Этот заказ уже закрыт.\nНачните новый из меню.",
    "toast_bad_amount": "❌ Неверная сумма",
    "scr_needed": "❌ <b>Скриншот не нужен.</b>\nПришлите свой <b>TXID</b> (хэш транзакции) текстом.",
    "txid_bad_fmt": "❌ <b>Неверный формат TXID</b>\nДля {net} нужен <code>{fmt}</code>. Скопируйте полный хэш из кошелька.",
    "dep_checking": "⏳ Проверяем вашу транзакцию {net}...",
    "dep_locked": "🔒 Заказ заблокирован — слишком много неверных TXID.\nСвяжитесь с админом, указав ID заказа <code>{order}</code>.",
    "txid_replay": "🔁 Этот TXID уже использовался.\nОдин TXID = один заказ. Отправьте хэш новой транзакции.",
    "bin_pay_id": "🏦 <b>Binance Pay ID</b> - отправьте НА этот ID:",
    "bin_card_hint": "⚠️ Оплатите через <b>приложение Binance → Pay</b>\n💵 Отправляйте <b>только USDT</b>, ровно сумму выше.\n❌ Неверный ID или актив = потеря денег.",
    "bin_auto_line": "⚡ Платёж подтверждается автоматически ~1 минуту.\nИли нажмите I PAID и вставьте Order ID.",
    "bin_txid_title": "🔑 <b>Вставьте ваш Binance Pay Order ID</b>",
    "bin_txid_body": "📋 Приложение Binance → Pay → откройте ваш перевод → скопируйте <b>Order ID</b> и вставьте сюда.",
    "bin_bad_fmt": "❌ <b>Это не Binance Pay Order ID.</b>\nВыглядит так: <code>M_P_123456789012345678</code> - скопируйте в приложении Binance → Pay → детали перевода.",
    "bin_amt_mismatch": "❌ <b>Сумма не совпадает.</b>\nПлатёж показывает <code>${got}</code>, заказ требует <code>${want}</code>.\nЗаплатите точную сумму и вставьте её Order ID.",
    "bin_decline_pending": "⏳ Платёж по этому Order ID пока не найден.\nСначала заплатите, проверьте Order ID и отправьте снова через минуту.",
    "bin_decline_stale": "❌ Этот Order ID нельзя использовать для этого заказа.\nОн старше заказа или уже потрачен.\nЗаплатите заново и вставьте новый Order ID.",
    "bin_decline_out": "❌ Это ИСХОДЯЩИЙ перевод - деньги ушли от вас.\nВставьте Order ID перевода, которым вы ОТПРАВИЛИ нам.",
    "dep_api_busy": "⏳ Проверка Binance сейчас занята.\nВаш заказ в безопасности - попробуйте через минуту.",
    "amt_mismatch": "❌ <b>Сумма не совпадает.</b>\nВ транзакции <code>${got}</code>, а заказ требует <code>${want}</code>.\nОтправьте правильный хэш или начните новое пополнение.",
    "dep_already": "✅ Это пополнение уже подтверждено.\nВаш баланс уже обновлён.",
    "dep_ok_title": "✅ <b>Пополнение подтверждено!</b>",
    "dep_ok_credited": "💵 Зачислено: <code>${amount}</code>",
    "dep_ok_balance": "💰 Баланс: <code>${bal}</code>",
    "dep_ok_cta": "🛒 Приятных покупок — нажмите Buy ниже!",
    "decline_pending": "⏳ Транзакция пока не найдена в {net}.\nПроверьте TXID и отправьте снова через минуту.",
    "decline_failed": "❌ Транзакция не прошла в блокчейне — деньги не перевелись.\nОтправьте новый, успешный TXID.",
    "decline_token": "❌ Это не перевод USDT в {net}.\nОтправляйте только USDT.",
    "decline_recipient": "❌ Неверный получатель.\nЭта транзакция не отправляла USDT на наш адрес {net}.",
    "dm_credited": "✅ Зачислено <code>${amount}</code> • Баланс <code>${bal}</code>\n🧾 Заказ <code>{order}</code>",
    "dm_dep_confirmed": "✅ <b>ПОПОЛНЕНИЕ ПОДТВЕРЖДЕНО</b>\n\n{div}\n💵 <b>Сумма:</b> ${amount}\n🧾 <b>Заказ:</b> <code>{order}</code>\n{div}\n\n💰 <b>Баланс обновлён! Приятных покупок 🛒</b>",
    "dm_dep_rejected": "❌ <b>ПОПОЛНЕНИЕ ОТКЛОНЕНО</b>\n\n{div}\n🧾 <b>Заказ:</b> <code>{order}</code>\n{div}\n\n💬 Считаете это ошибкой — напишите в Поддержку.",
    "help_title": "📖 <b>Быстрая помощь</b>",
    "help_lines": "/start — открыть главное меню\n/menu — показать меню\n/language — сменить язык\n/admin — панель админа",
    "help_cta": "💡 Всё в одном тапе на кнопках ниже.",
    "err_generic": "⚠️ <b>Что-то пошло не так.</b>\nПопробуйте снова — или нажмите /start.",
    "toast_processing": "Обрабатываем покупку... ⏳",
    "toast_invalid": "Неверный запрос",
    "toast_expired": "❌ Срок действия кнопки истёк — попробуйте снова",
    "btn_join_channel": "✉️ ПОДПИСАТЬСЯ НА КАНАЛ",
    "btn_join_group": "✉️ ВСТУПИТЬ В ГРУППУ",
    "fj_title": "🔒 <b>Один шаг до разблокировки</b>",
    "fj_body": "👉 Подпишитесь на наш канал ниже, чтобы пользоваться ботом.\n✅ После подписки нажмите <b>Проверить</b>.",
    "btn_fj_check": "✅ Проверить",
    "fj_toast_no": "❌ Вы ещё не подписались — подпишитесь и нажмите Проверить.",
    "fj_done": "✅ <b>Проверено!</b>\n🎉 Добро пожаловать — главное меню открыто ниже 👇",
    "fj_dm": "✅ <b>Подписка подтверждена!</b>\n👋 Добро пожаловать — главное меню открыто 👇",
    "btn_refer": "🎁 Приглашай и зарабатывай",
    "btn_active": "📱 Активные номера",
    "btn_ubulk": "📦 Оптовая покупка",
    "ub_pick": "📦 <b>Оптовая покупка</b>\n\n🟢 WhatsApp — доступно <code>{wa_n}</code> • по <code>${wa_rate}</code>\n🔵 Telegram — доступно <code>{tg_n}</code> • по <code>${tg_rate}</code>\n\n🎁 <b>{dmin}+ номеров = скидка ${damt} за номер</b>\n\n👉 Выберите тип:",
    "ub_qty": "📦 <b>Оптовая покупка — {label}</b>\n\n📱 Доступно: <code>{n}</code>\n💵 Цена: <code>${rate}</code> за номер\n💰 Баланс: <code>${bal}</code>\n\n🎁 {dmin}+ = <b>скидка ${damt} за номер</b>\n\n👉 Напишите СКОЛЬКО номеров нужно:",
    "ub_bad_qty": "❌ Напишите число (1 до {cap}).\n👉 Попробуйте ещё раз:",
    "ub_stock_low": "⚠️ Сейчас доступно только <code>{n}</code>.\n👉 Напишите меньше:",
    "ub_no_bal": "⚠️ {n} номеров = <code>${total}</code>\n💰 Баланс: <code>${bal}</code>\n👉 Максимум по балансу: <code>{maxn}</code>. Напишите его:",
    "ub_confirm": "🧾 <b>Подтвердите заказ</b>\n\n{div}\n📱 Тип: <b>{label}</b>\n🔢 Количество: <code>{n}</code>\n💵 Цена: <code>${unit}</code> за номер {disc}\n💰 Итого: <code>${total}</code>\n💰 После: <code>${after}</code>\n{div}\n\n👉 Подтвердите ниже — .txt файл придёт сразу.",
    "ub_disc": "(скидка {dmin}+ ✅)",
    "ub_expired": "⏳ Сессия истекла — начните снова через 📦 Оптовая покупка.",
    "ub_done": "✅ <b>Оптовый заказ выполнен!</b>\n\n{div}\n📱 Номеров: <code>{n}</code>\n💵 Оплачено: <code>${total}</code> (по <code>${unit}</code> {disc})\n💰 Баланс: <code>${bal}</code>\n{div}\n\n📎 Файл <code>{fname}</code> прикреплён — каждый номер с OTP API ссылкой.\n📩 Каждый OTP прийдёт сюда автоматически.\n📱 Следите в 📱 Активные номера.",
    "ub_partial": "⚠️ Сток ушёл быстро — было только <code>{n}</code>. Списали только за <code>{n}</code>.",
    "ub_none": "❌ <b>Нет стока</b> — ничего не списано.",
    "ub_hint_file": "❌ Это файл — здесь нужно ЧИСЛО.\n👉 Напишите СКОЛЬКО номеров нужно:",
    "act_title": "📞 <b>Ваши активные номера</b> ({n})",
    "act_none": "📭 У вас пока нет активных номеров.\n🛒 Купите номер — он сразу появится здесь.",
    "act_hint": "▶️ Нажмите на номер, чтобы скопировать, затем отправьте сюда — номер откроется с кнопкой Get OTP.",
    "act_more": "…и ещё {extra}",
    "act_card_title": "🟢 <b>Ваш активный номер</b>",
    "act_card_body": "📩 Нажимайте GET OTP в любой момент — код придёт, как только поступит. Без ограничения времени.",
    "rfs_title": "🎉 <b>Возврат выполнен успешно</b>",
    "rfs_body": "🟢 <code>{number}</code>\n💰 <code>${amount}</code> добавлено на ваш баланс",
    "ref_title": "🤝 <b>Реферальная программа</b>",
    "ref_body": "Поделитесь ссылкой — вы получаете <b>${rate}</b> с каждой покупки друга. Пожизненно.",
    "ref_link": "🔗 Ваша реферальная ссылка:",
    "ref_stats": "👥 Приглашено: <b>{count}</b>\n💰 Всего заработано: <b>${earned}</b>",
    "ref_rate_line": "💵 Ваша ставка: <b>${rate}</b> за покупку",
    "ref_vip_line": "👑 <b>VIP-реферер</b> — особая ставка <b>${rate}</b> за покупку",
    "btn_ref_share": "📤 Поделиться ссылкой",
    "ref_share_text": "🎁 Премиум номера WhatsApp и Telegram — мгновенный OTP!",
    "ref_none_yet": "Пока нет рефералов — поделитесь ссылкой и начните зарабатывать 👇",
    "ref_earned_notif": "🎉 <b>Реферальный бонус!</b>\n{div}\n👤 {name} купил номер\n💰 На ваш баланс зачислено <b>+${amount}</b>\n💼 Баланс: <b>${bal}</b>\n{div}",
    "ref_new_ref": "👥 <b>Новый реферал!</b>\n👤 {name} присоединился по вашей ссылке\n💰 Вы получаете с каждой его покупки",
    "ref_paused": "⏸ Реферальная программа временно приостановлена.\n💡 Загляните позже!",
},

    "fa": {
    "btn_buy": "🛒 خرید شماره",
    "btn_profile": "👤 پروفایل",
    "btn_deposit": "💳 شارژ حساب",
    "btn_support": "💬 پشتیبانی",
    "btn_back": "⬅️ بازگشت",
    "btn_cancel_dep": "❌ لغو شارژ",
    "btn_wa": "🟢 WhatsApp",
    "btn_tg": "🔵 Telegram",
    "btn_dep_new": "💵 شارژ جدید",
    "btn_dep_hist": "📜 تاریخچه",
    "btn_custom_amount": "✏️ مبلغ دلخواه",
    "btn_i_paid": "✅ پرداخت کردم — TXID را بفرست",
    "btn_get_otp": "📩 دریافت کد",
    "btn_buy_now": "✅ خرید — ${price}",
    "kb_placeholder": "یک گزینه انتخاب کن 👇",
    "menu_title": "🏠 <b>منوی اصلی</b>",
    "menu_where": "👉 حالا کجا می‌روی؟",
    "menu_footer": "✅ تمام! به منوی اصلی برگشتی 👇",
    "blocked": "🔒 <b>دسترسی مسدود شد</b>\nاین حساب دیگر نمی‌تواند از ربات استفاده کند.",
    "lang_pick_title": "🌐 <b>زبان خود را انتخاب کن</b>",
    "lang_pick_hint": "👉 برای ادامه روی زبان خودت بزن",
    "lang_set_ok": "✅ زبان تنظیم شد: {lang}",
    "lang_current": "🌐 زبان فعلی: <b>{lang}</b>\nبرای تغییر روی یکی از زبان‌های پایین بزن.",
    "welcome_hi": "👋 <b>سلام {name}، دوباره خوش آمدی!</b>",
    "welcome_tagline": "📱 شماره‌های پرمیوم WhatsApp و Telegram\n⚡ تحویل آنی • همراه با کد تأیید",
    "welcome_balance": "💰 موجودی: <code>${bal}</code>",
    "welcome_stock": "📦 موجود در انبار: <code>{total}</code> شماره",
    "welcome_cta": "👉 برای شروع روی دکمه پایین بزن",
    "profile_title": "👤 <b>پروفایل تو</b>",
    "lbl_id": "🆔 شناسه:",
    "lbl_name": "📝 نام:",
    "lbl_username": "🌐 نام کاربری:",
    "prof_purchased": "🛒 خریداری‌شده: <code>{n}</code>",
    "prof_spent": "💸 خرج‌شده: <code>${amount}</code>",
    "prof_deposited": "🏦 شارژ شده: <code>${amount}</code>",
    "prof_otps": "📩 کدها: <code>{n} ({pct})</code>",
    "support_title": "💬 <b>کمک لازم داری؟</b>",
    "support_admin": "👨‍💻 ادمین: {handle}",
    "support_time": "⚡ زمان پاسخ: معمولاً چند دقیقه",
    "support_body": "پرداخت، مشکل کد، سؤال انبار — فقط به ما پیام بده، ما کنارت هستیم. 🙌",
    "buy_title": "🛒 <b>خرید شماره</b>",
    "buy_wa_price": "🟢 WhatsApp — <code>${wa}</code>",
    "buy_tg_price": "🔵 Telegram — <code>${tg}</code>",
    "buy_pick": "👉 برای ادامه یک نوع انتخاب کن",
    "ctry_title": "🌍 <b>کشور را انتخاب کن</b>",
    "ctry_avail": "📱 شماره‌های {label} موجود است",
    "cta_select": "👉 از پایین انتخاب کن",
    "confirm_title": "🧾 <b>سفارش را تأیید کن</b>",
    "cf_type": "📱 نوع: {label}",
    "cf_country": "🌍 کشور: {flag} {country}",
    "cf_price": "💵 قیمت: <code>${rate}</code>",
    "cf_balance": "💰 موجودی تو: <code>${bal}</code>",
    "cf_cta": "👉 همه‌چیز درست است؟ پایین تأیید کن",
    "ps_title": "✅ <b>خرید کامل شد!</b>",
    "ps_number": "📱 شماره: <code>{number}</code>",
    "ps_label": "🏷️ {label} • {flag} {country}",
    "ps_paid": "💵 پرداخت‌شده: <code>${rate}</code>",
    "ps_order": "🧾 سفارش: <code>{order}</code>",
    "ps_get_otp": "📩 هر وقت خواستی روی <b>Get OTP</b> پایین بزن تا کدت را بگیری",
    "ps_copy": "📋 برای کپی کردن روی شماره بزن",
    "ins_title": "⚠️ <b>موجودی کافی نیست</b>",
    "ins_price": "💵 قیمت: <code>${rate}</code>",
    "ins_balance": "💰 موجودی: <code>${bal}</code>",
    "ins_need": "❗ باز لازم داری: <code>${need}</code>",
    "ins_cta": "👉 با یک لمس حساب را شارژ کن",
    "oos_title": "❌ <b>موجود نیست</b>",
    "oos_label": "🏷️ {label} — {flag} {country}",
    "oos_cta": "👉 کشور دیگری را امتحان کن یا به 💬 پشتیبانی بگو",
    "otp_received": "🎉 <b>کد تأیید رسید!</b>",
    "otp_waiting": "⏳ <b>هنوز منتظر کد هستیم</b>",
    "otp_waiting_body": "پیامک ممکن است کمی طول بکشد — در پس‌زمینه داریم چک می‌کنیم. کد خودش اینجا می‌رسد. 👀",
    "otp_blocked": "🔒 <b>کد مسدود شد</b>",
    "otp_blocked_body": "این شماره بازپرداخت شده — دیگر هیچ‌وقت کد به اینجا نمی‌رسد.",
    "toast_no_link": "ℹ️ این شماره لینک کد ندارد — با پشتیبانی تماس بگیر",
    "otp_timeout": "⏳ <b>کد بعد از ۱۰ دقیقه نرسید</b>",
    "otp_timeout_body": "پیامک گاهی دیر می‌رسد. روی 🔑 <b>Get OTP</b> در رسید بزن تا هر وقت خواستی دوباره چک کنی.",
    "toast_not_yours": "❌ این شماره مال تو نیست",
    "toast_not_found": "❌ شماره پیدا نشد",
    "dep_title": "💳 <b>شارژ حساب</b>",
    "dep_min_line": "💵 حداقل: <code>${min}</code> • تأیید با TXID 🔐",
    "dep_min_only": "💵 حداقل: <code>${min}</code>",
    "cta_pick": "👉 یک گزینه انتخاب کن",
    "dep_amt_title": "💰 <b>مبلغ را انتخاب کن</b>",
    "dep_amt_hint": "👉 روی مبلغ بزن، یا ✏️ دلخواه",
    "dep_net_title": "🌐 <b>شبکه را انتخاب کن</b>",
    "dep_net_amount": "💵 <code>${amount}</code> USDT",
    "dep_net_hint": "👉 روی شبکه‌ات بزن",
    "dep_hist_title": "📜 <b>تاریخچه شارژ</b>",
    "dep_hist_empty": "هنوز شارژی نداری — اولین شارژت اینجا نشان داده می‌شود.",
    "dep_min_warn": "⚠️ حداقل شارژ <code>${min}</code> است\n👉 دوباره از پایین انتخاب کن",
    "custom_title": "✏️ <b>مبلغت را بنویس</b>\n💵 به USDT — حداقل <code>${min}</code>\nمثال: <code>1.50</code>",
    "custom_err": "❌ حداقل شارژ <code>${min}</code> است\n💵 دوباره مبلغ USDT را بنویس\nمثال: <code>1.50</code>",
    "card_send": "💸 <b>${amount} USDT بفرست</b>",
    "card_network": "🌐 شبکه: <b>{net}</b>",
    "card_address": "📍 آدرس (برای کپی بزن):",
    "card_warn": "⚠️ فقط <b>{net}</b> — شبکه اشتباه = پول از دست می‌رود.",
    "card_paid": "✅ پرداختی؟ <b>I PAID</b> را بزن → بعد TXID را بفرست.",
    "card_expire": "🧾 <code>{dep_id}</code> • انقضا {expires} ⏳",
    "txid_title": "🔑 <b>TXID مربوط به {net} را بچسبان</b>",
    "txid_body": "📋 هش تراکنش پرداخت تو.",
    "txid_format": "قالب: <code>{fmt}</code>",
    "txid_ok_line": "✅ تأیید شد → موجودی فوری",
    "txid_no_line": "❌ بدون TXID → بدون شارژ",
    "dep_cancelled": "❌ <b>شارژ لغو شد.</b>",
    "dep_expired_session": "ℹ️ نشست منقضی شد.\nاز منو یک شارژ جدید شروع کن.",
    "dep_no_active": "ℹ️ سفارش شارژ فعالی پیدا نشد.\nاز منو یکی جدید شروع کن.",
    "dep_closed": "ℹ️ این سفارش شارژ قبلاً بسته شده.\nاز منو جدیدی شروع کن.",
    "toast_bad_amount": "❌ مبلغ نامعتبر",
    "scr_needed": "❌ <b>اسکرین‌شات لازم نیست.</b>\nلطفاً <b>TXID</b> (هش تراکنش) را به شکل متن بفرست.",
    "txid_bad_fmt": "❌ <b>قالب TXID غلط است</b>\n{net} نیاز دارد: <code>{fmt}</code>. هش کامل را از کیف پولت کپی کن.",
    "dep_checking": "⏳ در حال بررسی تراکنش {net} تو…",
    "dep_locked": "🔒 سفارش قفل شد — TXID غلط زیاد.\nبا شماره سفارش <code>{order}</code> به ادمین پیام بده.",
    "txid_replay": "🔁 این TXID قبلاً استفاده شده.\nهر TXID = یک سفارش. هش تراکنش جدیدت را بفرست.",
    "bin_pay_id": "🏦 <b>آیدی Binance Pay</b> - به این آیدی بفرستید:",
    "bin_card_hint": "⚠️ از <b>اپلیکیشن Binance → Pay</b> پرداخت کنید\n💵 فقط <b>USDT</b> و دقیقاً مبلغ بالا را بفرستید.\n❌ آیدی یا ارز اشتباه = از دست رفتن پول.",
    "bin_auto_line": "⚡ پرداخت حدود ۱ دقیقه بعد خودکار تایید می‌شود.\nیا I PAID را بزنید و Order ID را بفرستید.",
    "bin_txid_title": "🔑 <b>Order ID بایننس پی خود را ارسال کنید</b>",
    "bin_txid_body": "📋 اپلیکیشن Binance → Pay → تراکنش خود را باز کنید → <b>Order ID</b> را کپی و اینجا بفرستید.",
    "bin_bad_fmt": "❌ <b>این یک Order ID بایننس پی نیست.</b>\nشکل آن چنین است: <code>M_P_123456789012345678</code> - از اپلیکیشن Binance → Pay → جزئیات تراکنش کپی کنید.",
    "bin_amt_mismatch": "❌ <b>مبلغ مطابقت ندارد.</b>\nپرداخت <code>${got}</code> است، سفارش <code>${want}</code> می‌خواهد.\nدقیقاً همان مبلغ را بپردازید و Order ID همان را بفرستید.",
    "bin_decline_pending": "⏳ هنوز پرداختی برای این Order ID پیدا نشده است.\nاول پرداخت کنید، Order ID را بررسی کنید و یک دقیقه بعد دوباره بفرستید.",
    "bin_decline_stale": "❌ این Order ID برای این سفارش قابل استفاده نیست.\nقدیمی‌تر از سفارش است یا قبلاً استفاده شده است.\nپرداخت جدید انجام دهید و Order ID جدید بفرستید.",
    "bin_decline_out": "❌ این یک تراکنش خروجی (OUTGOING) است - پول از دست شما خارج شده است.\nOrder ID تراکنشی که به ما فرستادید را بفرستید.",
    "dep_api_busy": "⏳ تایید بایننس در حال حاضر شلوغ است.\nسفارش شما ایمن است - یک دقیقه بعد دوباره تلاش کنید.",
    "amt_mismatch": "❌ <b>مبلغ مطابقت ندارد.</b>\nتراکنش <code>${got}</code> نشان می‌دهد، سفارش <code>${want}</code> می‌خواهد.\nهش درست را بفرست یا شارژ جدیدی شروع کن.",
    "dep_already": "✅ این شارژ قبلاً تأیید شده.\nموجودی‌ات به‌روز است.",
    "dep_ok_title": "✅ <b>شارژ تأیید شد!</b>",
    "dep_ok_credited": "💵 واریز شد: <code>${amount}</code>",
    "dep_ok_balance": "💰 موجودی: <code>${bal}</code>",
    "dep_ok_cta": "🛒 خرید خوش — پایین روی Buy بزن!",
    "decline_pending": "⏳ تراکنش هنوز در {net} پیدا نشده.\nTXID را دوباره چک کن و یک دقیقه بعد بفرست.",
    "decline_failed": "❌ تراکنش در بلاک‌چین شکست خورد — پول جابه‌جا نشده.\nیک TXID جدیدِ موفق بفرست.",
    "decline_token": "❌ این یک انتقال USDT در {net} نبود.\nفقط USDT بفرست.",
    "decline_recipient": "❌ گیرنده اشتباه است.\nاین TXID به آدرس {net} ما USDT نفرستاده.",
    "dm_credited": "✅ واریز <code>${amount}</code> • موجودی <code>${bal}</code>\n🧾 سفارش <code>{order}</code>",
    "dm_dep_confirmed": "✅ <b>شارژ تأیید شد</b>\n\n{div}\n💵 <b>مبلغ:</b> ${amount}\n🧾 <b>سفارش:</b> <code>{order}</code>\n{div}\n\n💰 <b>موجودی به‌روز شد! خرید خوش 🛒</b>",
    "dm_dep_rejected": "❌ <b>شارژ رد شد</b>\n\n{div}\n🧾 <b>سفارش:</b> <code>{order}</code>\n{div}\n\n💬 فکر می‌کنی اشتباه است، با پشتیبانی تماس بگیر.",
    "help_title": "📖 <b>راهنمای سریع</b>",
    "help_lines": "/start — باز کردن منوی اصلی\n/menu — نمایش منو\n/language — تغییر زبان\n/admin — پنل ادمین",
    "help_cta": "💡 همه‌چیز با دکمه‌های پایین یک لمسی است.",
    "err_generic": "⚠️ <b>مشکلی پیش آمد.</b>\nدوباره تلاش کن — یا /start را بزن.",
    "toast_processing": "در حال انجام خرید… ⏳",
    "toast_invalid": "درخواست نامعتبر",
    "toast_expired": "❌ اعتبار این دکمه تمام شد — دوباره تلاش کن",
    "btn_join_channel": "✉️ عضویت در کانال",
    "btn_join_group": "✉️ عضویت در گروه",
    "fj_title": "🔒 <b>یک قدم تا باز شدن</b>",
    "fj_body": "👉 برای استفاده از ربات، در کانال ما عضو شوید.\n✅ بعد از عضویت روی <b>بررسی</b> بزنید.",
    "btn_fj_check": "✅ بررسی",
    "fj_toast_no": "❌ هنوز عضو نشده‌اید — اول عضو شوید، بعد بررسی را بزنید.",
    "fj_done": "✅ <b>تأیید شد!</b>\n🎉 خوش آمدید — منوی اصلی شما در پایین باز شد 👇",
    "fj_dm": "✅ <b>عضویت تأیید شد!</b>\n👋 خوش آمدید — منوی اصلی باز شد 👇",
    "btn_refer": "🎁 معرفی کن و درآمد بساز",
    "btn_active": "📱 شماره‌های فعال",
    "btn_ubulk": "📦 خرید عمده",
    "ub_pick": "📦 <b>خرید عمده</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> موجود • هر شماره <code>${wa_rate}</code>\n🔵 Telegram — <code>{tg_n}</code> موجود • هر شماره <code>${tg_rate}</code>\n\n🎁 <b>{dmin}+ شماره = تخفیف ${damt} در هر شماره</b>\n\n👉 نوع را انتخاب کنید:",
    "ub_qty": "📦 <b>خرید عمده — {label}</b>\n\n📱 موجود: <code>{n}</code>\n💵 قیمت: هر شماره <code>${rate}</code>\n💰 موجودی: <code>${bal}</code>\n\n🎁 {dmin}+ = هر شماره <b>${damt} تخفیف</b>\n\n👉 چند شماره می‌خواهید؟ بنویسید:",
    "ub_bad_qty": "❌ فقط عدد بنویسید (1 تا {cap})٤\n👉 دوباره تلاش کنید:",
    "ub_stock_low": "⚠️ فعلا فقط <code>{n}</code> موجود است٤\n👉 عدد کمتری بنویسید:",
    "ub_no_bal": "⚠️ {n} شماره = <code>${total}</code>\n💰 موجودی: <code>${bal}</code>\n👉 حداکثر <code>{maxn}</code> شماره می‌توانید. آن را بنویسید:",
    "ub_confirm": "🧾 <b>تأیید سفارش</b>\n\n{div}\n📱 نوع: <b>{label}</b>\n🔢 تعداد: <code>{n}</code>\n💵 قیمت: هر یک <code>${unit}</code> {disc}\n💰 جمع: <code>${total}</code>\n💰 بعد از خرید: <code>${after}</code>\n{div}\n\n👉 پایین تأیید کنید — فایل .txt فوراً می‌آید.",
    "ub_disc": "(تخفیف {dmin}+ ✅)",
    "ub_expired": "⏳ جلسه منقضی شد — دوباره از 📦 خرید عمده شروع کنید.",
    "ub_done": "✅ <b>سفارش عمده کامل شد!</b>\n\n{div}\n📱 تعداد: <code>{n}</code>\n💵 پرداخته: <code>${total}</code> (هر یک <code>${unit}</code> {disc})\n💰 موجودی: <code>${bal}</code>\n{div}\n\n📎 فایل <code>{fname}</code> پیوست شد — هر شماره با لینک OTP API.\n📩 هر OTP به‌محض رسیدن خودکار در این چت می‌آید.\n📱 پیگیری در 📱 شماره‌های فعال.",
    "ub_partial": "⚠️ انبار سریع تمام شد — فقط <code>{n}</code> موجود بود. فقط برای <code>{n}</code> کسر شد.",
    "ub_none": "❌ <b>انبار خالی</b> — چیزی کسر نشد.",
    "ub_hint_file": "❌ این فایل است — اینجا عدد لازم است.\n👉 چند شماره می‌خواهید؟ بنویسید:",
    "act_title": "📞 <b>شماره‌های فعال شما</b> ({n})",
    "act_none": "📭 در حال حاضر شماره فعالی ندارید.\n🛒 شماره بخرید — بلافاصله اینجا نمایش داده می‌شود.",
    "act_hint": "▶️ برای کپی روی هر شماره بزنید و بعد همین‌جا بفرستید — شماره با دکمه Get OTP باز می‌شود.",
    "act_more": "…و {extra} مورد دیگر",
    "act_card_title": "🟢 <b>شماره فعال شما</b>",
    "act_card_body": "📩 هر وقت خواستید GET OTP را بزنید — کد به محض رسیدن برای شما ارسال می‌شود. بدون محدودیت زمانی.",
    "rfs_title": "🎉 <b>بازپرداخت شما با موفقیت انجام شد</b>",
    "rfs_body": "🟢 <code>{number}</code>\n💰 <code>${amount}</code> به موجودی‌ات اضافه شد",
    "ref_title": "🤝 <b>معرفی و درآمد</b>",
    "ref_body": "لینک خود را به اشتراک بگذارید — با هر خریدِ هر دوستتان <b>${rate}</b> دریافت می‌کنید. مادام‌العمر.",
    "ref_link": "🔗 لینک معرفی شما:",
    "ref_stats": "👥 معرفی‌شده: <b>{count}</b>\n💰 کل درآمد: <b>${earned}</b>",
    "ref_rate_line": "💵 نرخ شما: به ازای هر خرید <b>${rate}</b>",
    "ref_vip_line": "👑 <b>معرف VIP</b> — نرخ ویژه هر خرید <b>${rate}</b>",
    "btn_ref_share": "📤 اشتراک‌گذاری لینک",
    "ref_share_text": "🎁 شماره‌های ممتاز WhatsApp و Telegram — OTP فوری!",
    "ref_none_yet": "هنوز معرفی ندارید — لینک خود را بفرستید تا کسب درآمد را شروع کنید 👇",
    "ref_earned_notif": "🎉 <b>پاداش معرفی!</b>\n{div}\n👤 {name} یک شماره خرید\n💰 <b>+${amount}</b> به موجودی شما اضافه شد\n💼 موجودی: <b>${bal}</b>\n{div}",
    "ref_new_ref": "👥 <b>معرفی جدید!</b>\n👤 {name} با لینک شما عضو شد\n💰 از هر خرید او درآمد خواهید داشت",
    "ref_paused": "⏸ برنامه معرفی فعلاً متوقف است.\n💡 بعداً دوباره سر بزنید!",
},
    "pt": {
    'btn_buy': '🛒 Comprar Número',
    'btn_profile': '👤 Perfil',
    'btn_deposit': '💳 Depósito',
    'btn_support': '💬 Suporte',
    'btn_back': '⬅️ Voltar',
    'btn_cancel_dep': '❌ Cancelar Depósito',
    'btn_wa': '🟢 WhatsApp',
    'btn_tg': '🔵 Telegram',
    'btn_dep_new': '💵 Novo Depósito',
    'btn_dep_hist': '📜 Histórico',
    'btn_custom_amount': '✏️ Valor Personalizado',
    'btn_i_paid': '✅ PAGUEI — Enviar TXID',
    'btn_get_otp': '📩 Receber OTP',
    'btn_buy_now': '✅ Comprar — ${price}',
    'kb_placeholder': 'Escolha uma opção 👇',
    'menu_title': '🏠 <b>Menu Principal</b>',
    'menu_where': '👉 Onde você quer ir agora?',
    'menu_footer': '✅ Pronto! Você está de volta ao menu principal 👇',
    'blocked': '🔒 <b>Acesso bloqueado</b>\nEsta conta não pode mais usar o bot.',
    'lang_pick_title': '🌐 <b>Escolha seu idioma</b>',
    'lang_pick_hint': '👉 Toque no seu idioma para continuar',
    'lang_set_ok': '✅ Idioma definido: {lang}',
    'lang_current': '🌐 Idioma atual: <b>{lang}</b>\nToque em um idioma abaixo para trocar.',
    'welcome_hi': '👋 <b>Olá {name}, bem-vindo de volta!</b>',
    'welcome_tagline': '📱 Números premium de WhatsApp &amp; Telegram\n⚡ Entrega instantânea • OTP incluído',
    'welcome_balance': '💰 Saldo: <code>${bal}</code>',
    'welcome_stock': '📦 Em estoque: <code>{total}</code> números',
    'welcome_cta': '👉 Toque em um botão abaixo para começar',
    'profile_title': '👤 <b>Seu Perfil</b>',
    'lbl_id': '🆔 ID:',
    'lbl_name': '📝 Nome:',
    'lbl_username': '🌐 Usuário:',
    'prof_purchased': '🛒 Comprados: <code>{n}</code>',
    'prof_spent': '💸 Gasto: <code>${amount}</code>',
    'prof_deposited': '🏦 Depositado: <code>${amount}</code>',
    'prof_otps': '📩 OTPs: <code>{n} ({pct})</code>',
    'support_title': '💬 <b>Precisa de ajuda?</b>',
    'support_admin': '👨\u200d💻 Admin: {handle}',
    'support_time': '⚡ Tempo de resposta: geralmente alguns minutos',
    'support_body': 'Pagamentos, problemas de OTP, dúvidas de estoque — é só nos chamar, estamos aqui. 🙌',
    'buy_title': '🛒 <b>Comprar um Número</b>',
    'buy_wa_price': '🟢 WhatsApp — <code>${wa}</code>',
    'buy_tg_price': '🔵 Telegram — <code>${tg}</code>',
    'buy_pick': '👉 Escolha um tipo para continuar',
    'ctry_title': '🌍 <b>Escolha um País</b>',
    'ctry_avail': '📱 Números {label} disponíveis',
    'cta_select': '👉 Selecione abaixo',
    'confirm_title': '🧾 <b>Confirme seu Pedido</b>',
    'cf_type': '📱 Tipo: {label}',
    'cf_country': '🌍 País: {flag} {country}',
    'cf_price': '💵 Preço: <code>${rate}</code>',
    'cf_balance': '💰 Seu Saldo: <code>${bal}</code>',
    'cf_cta': '👉 Tudo certo? Confirme abaixo',
    'ps_title': '✅ <b>Compra concluída!</b>',
    'ps_number': '📱 Número: <code>{number}</code>',
    'ps_label': '🏷️ {label} • {flag} {country}',
    'ps_paid': '💵 Pago: <code>${rate}</code>',
    'ps_order': '🧾 Pedido: <code>{order}</code>',
    'ps_get_otp': '📩 Toque em <b>Get OTP</b> abaixo quando quiser para receber seu código',
    'ps_copy': '📋 Toque no número para copiar',
    'ins_title': '⚠️ <b>Saldo Insuficiente</b>',
    'ins_price': '💵 Preço: <code>${rate}</code>',
    'ins_balance': '💰 Saldo: <code>${bal}</code>',
    'ins_need': '❗ Falta: <code>${need}</code>',
    'ins_cta': '👉 Recarregue com um toque',
    'oos_title': '❌ <b>Fora de Estoque</b>',
    'oos_label': '🏷️ {label} — {flag} {country}',
    'oos_cta': '👉 Tente outro país, ou fale com o 💬 Suporte',
    'otp_received': '🎉 <b>OTP Recebido!</b>',
    'otp_waiting': '⏳ <b>Ainda aguardando o OTP</b>',
    'otp_waiting_body': 'O SMS pode demorar um pouco — seguimos verificando em segundo plano. Ele chega aqui automaticamente. 👀',
    'otp_blocked': '🔒 <b>OTP Bloqueado</b>',
    'otp_blocked_body': 'Este número foi reembolsado — nenhum OTP chegará aqui novamente.',
    'toast_no_link': 'ℹ️ Sem link de OTP neste número — fale com o suporte',
    'otp_timeout': '⏳ <b>Sem OTP após 10 Minutos</b>',
    'otp_timeout_body': 'SMS pode atrasar. Toque em 🔑 <b>Get OTP</b> no recibo para verificar novamente quando quiser.',
    'toast_not_yours': '❌ Esse número não é seu',
    'toast_not_found': '❌ Número não encontrado',
    'dep_title': '💳 <b>Depósito</b>',
    'dep_min_line': '💵 Mín: <code>${min}</code> • Verificado por TXID 🔐',
    'dep_min_only': '💵 Mín: <code>${min}</code>',
    'cta_pick': '👉 Escolha uma opção',
    'dep_amt_title': '💰 <b>Escolha um Valor</b>',
    'dep_amt_hint': '👉 Toque em um valor, ou use ✏️ Personalizado',
    'dep_net_title': '🌐 <b>Escolha a Rede</b>',
    'dep_net_amount': '💵 <code>${amount}</code> USDT',
    'dep_net_hint': '👉 Toque na sua rede',
    'dep_hist_title': '📜 <b>Histórico de Depósitos</b>',
    'dep_hist_empty': 'Nenhum depósito ainda — o seu primeiro vai aparecer aqui.',
    'dep_min_warn': '⚠️ O depósito mínimo é <code>${min}</code>\n👉 Escolha novamente abaixo',
    'custom_title': '✏️ <b>Digite seu Valor</b>\n💵 Em USDT — mínimo <code>${min}</code>\nExemplo: <code>1.50</code>',
    'custom_err': '❌ O depósito mínimo é <code>${min}</code>\n💵 Digite o valor em USDT novamente\nExemplo: <code>1.50</code>',
    'card_send': '💸 <b>Envie ${amount} USDT</b>',
    'card_network': '🌐 Rede: <b>{net}</b>',
    'card_address': '📍 Endereço (toque para copiar):',
    'card_warn': '⚠️ Apenas <b>{net}</b> — rede errada = fundos perdidos.',
    'card_paid': '✅ Pagou? Toque em <b>I PAID</b> → depois envie seu TXID.',
    'card_expire': '🧾 <code>{dep_id}</code> • expira {expires} ⏳',
    'txid_title': '🔑 <b>Cole seu TXID da {net}</b>',
    'txid_body': '📋 O hash da transação do seu pagamento.',
    'txid_format': 'Formato: <code>{fmt}</code>',
    'txid_ok_line': '✅ Verificado → crédito instantâneo',
    'txid_no_line': '❌ Sem TXID → sem crédito',
    'dep_cancelled': '❌ <b>Depósito cancelado.</b>',
    'dep_expired_session': 'ℹ️ Sessão expirada.\nInicie um novo depósito pelo menu.',
    'dep_no_active': 'ℹ️ Nenhum pedido de depósito ativo.\nInicie um novo depósito pelo menu.',
    'dep_closed': 'ℹ️ Este pedido de depósito já está encerrado.\nInicie um novo pelo menu.',
    'toast_bad_amount': '❌ Valor inválido',
    'scr_needed': '❌ <b>Não precisa de print.</b>\nEnvie seu <b>TXID</b> (o hash da transação) como texto.',
    'txid_bad_fmt': '❌ <b>Formato de TXID inválido</b>\nA {net} exige <code>{fmt}</code>. Copie o hash completo da sua carteira.',
    'dep_checking': '⏳ Verificando sua transação na {net}...',
    'dep_locked': '🔒 Pedido bloqueado — muitos TXIDs errados.\nFale com o admin com o ID do pedido <code>{order}</code>.',
    'txid_replay': '🔁 Este TXID já foi usado.\nUm TXID = um pedido. Envie o hash da sua nova transação.',
    'bin_pay_id': '🏦 <b>Binance Pay ID</b> - envie PARA este ID:',
    'bin_card_hint': '⚠️ Pague pelo <b>app Binance → Pay</b>\n💵 Envie <b>somente USDT</b>, no valor exato acima.\n❌ ID ou ativo errado = dinheiro perdido.',
    'bin_auto_line': '⚡ O pagamento é verificado automaticamente em ~1 minuto.\nOu toque em I PAID e cole o Order ID.',
    'bin_txid_title': '🔑 <b>Cole o Order ID do seu Binance Pay</b>',
    'bin_txid_body': '📋 App Binance → Pay → abra sua transferência → copie o <b>Order ID</b> e cole aqui.',
    'bin_bad_fmt': '❌ <b>Isso não é um Order ID do Binance Pay.</b>\nTem a forma <code>M_P_123456789012345678</code> - copie no app Binance → Pay → detalhes da transferência.',
    'bin_amt_mismatch': '❌ <b>Valor não confere.</b>\nO pagamento mostra <code>${got}</code>, o pedido precisa de <code>${want}</code>.\nPague o valor exato e cole o Order ID correspondente.',
    'bin_decline_pending': '⏳ Nenhum pagamento encontrado para este Order ID ainda.\nPague primeiro, confira o Order ID e envie novamente em um minuto.',
    'bin_decline_stale': '❌ Este Order ID não pode ser usado neste pedido.\nÉ mais antigo que o pedido ou já foi usado.\nPague novamente e cole o novo Order ID.',
    'bin_decline_out': '❌ Essa é uma transferência de SAÍDA (OUTGOING) - o dinheiro saiu da sua conta.\nCole o Order ID da transferência que você nos ENVIOU.',
    'dep_api_busy': '⏳ A verificação do Binance está ocupada agora.\nSeu pedido está seguro - tente novamente em um minuto.',
    'amt_mismatch': '❌ <b>Valor divergente.</b>\nA transação mostra <code>${got}</code>, o pedido precisa de <code>${want}</code>.\nEnvie o hash correto ou inicie um novo depósito.',
    'dep_already': '✅ Este depósito já foi confirmado.\nSeu saldo já está atualizado.',
    'dep_ok_title': '✅ <b>Depósito Confirmado!</b>',
    'dep_ok_credited': '💵 Creditado: <code>${amount}</code>',
    'dep_ok_balance': '💰 Saldo: <code>${bal}</code>',
    'dep_ok_cta': '🛒 Boas compras — toque em Comprar abaixo!',
    'decline_pending': '⏳ Transação ainda não encontrada na {net}.\nConfira o TXID e envie novamente em um minuto.',
    'decline_failed': '❌ A transação falhou na blockchain — nenhum fundo foi movido.\nEnvie um novo TXID bem-sucedido.',
    'decline_token': '❌ Isso não foi uma transferência de USDT na {net}.\nEnvie apenas USDT.',
    'decline_recipient': '❌ Destinatário errado.\nEste TXID não enviou USDT para nosso endereço da {net}.',
    'dm_credited': '✅ Creditado <code>${amount}</code> • Saldo <code>${bal}</code>\n🧾 Pedido <code>{order}</code>',
    'dm_dep_confirmed': '✅ <b>DEPÓSITO CONFIRMADO</b>\n\n{div}\n💵 <b>Valor:</b> ${amount}\n🧾 <b>Pedido:</b> <code>{order}</code>\n{div}\n\n💰 <b>Saldo atualizado! Boas compras 🛒</b>',
    'dm_dep_rejected': '❌ <b>DEPÓSITO REJEITADO</b>\n\n{div}\n🧾 <b>Pedido:</b> <code>{order}</code>\n{div}\n\n💬 Fale com o Suporte se achar que é um erro.',
    'help_title': '📖 <b>Ajuda Rápida</b>',
    'help_lines': '/start — abrir o menu principal\n/menu — mostrar o menu\n/language — mudar o idioma\n/admin — painel admin',
    'help_cta': '💡 Está tudo a um toque de distância nos botões abaixo.',
    'err_generic': '⚠️ <b>Algo deu errado.</b>\nTente novamente — ou pressione /start.',
    'toast_processing': 'Processando sua compra... ⏳',
    'toast_invalid': 'Solicitação inválida',
    'toast_expired': '❌ Este botão expirou — tente novamente',
    'btn_join_channel': '✉️ ENTRAR NO CANAL',
    'btn_join_group': '✉️ ENTRAR NO GRUPO',
    'fj_title': '🔒 <b>Falta um Passo para Desbloquear</b>',
    'fj_body': '👉 Entre no nosso canal abaixo para usar o bot.\n✅ Depois de entrar, toque em <b>Verificar</b>.',
    'btn_fj_check': '✅ Verificar',
    'fj_toast_no': '❌ Você ainda não entrou — entre primeiro e toque em Verificar.',
    'fj_done': '✅ <b>Verificado!</b>\n🎉 Bem-vindo — seu menu principal está liberado abaixo 👇',
    'fj_dm': '✅ <b>Entrada verificada!</b>\n👋 Bem-vindo — menu principal liberado 👇',
    'btn_refer': '🎁 Indique e Ganhe',
    'btn_active': '📱 Números Ativos',
    'btn_ubulk': '📦 Compra em Massa',
    'ub_pick': '📦 <b>Compra em Massa</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> disponíveis • <code>${wa_rate}</code> cada\n🔵 Telegram — <code>{tg_n}</code> disponíveis • <code>${tg_rate}</code> cada\n\n🎁 <b>{dmin}+ números = ${damt} menos por número</b>\n\n👉 Escolha o tipo:',
    'ub_qty': '📦 <b>Compra em Massa — {label}</b>\n\n📱 Disponíveis: <code>{n}</code>\n💵 Preço: <code>${rate}</code> por número\n💰 Saldo: <code>${bal}</code>\n\n🎁 {dmin}+ = <b>${damt} menos por número</b>\n\n👉 Digite QUANTOS números você quer:',
    'ub_bad_qty': '❌ Digite apenas um NÚMERO (1 a {cap}).\n👉 Tente de novo:',
    'ub_stock_low': '⚠️ Só há <code>{n}</code> disponíveis agora.\n👉 Digite uma quantidade menor:',
    'ub_no_bal': '⚠️ {n} números = <code>${total}</code>\n💰 Saldo: <code>${bal}</code>\n👉 Máximo que pode pagar: <code>{maxn}</code> números. Digite isso (ou menos):',
    'ub_confirm': '🧾 <b>Confirmar Pedido</b>\n\n{div}\n📱 Tipo: <b>{label}</b>\n🔢 Números: <code>{n}</code>\n💵 Preço: <code>${unit}</code> cada {disc}\n💰 Total: <code>${total}</code>\n💰 Depois: <code>${after}</code>\n{div}\n\n👉 Confirme abaixo — o arquivo .txt chega na hora.',
    'ub_disc': '(desconto {dmin}+ ✅)',
    'ub_expired': '⏳ Sessão expirada — comece de novo em 📦 Compra em Massa.',
    'ub_done': '✅ <b>Pedido em Massa Concluído!</b>\n\n{div}\n📱 Números entregues: <code>{n}</code>\n💵 Pago: <code>${total}</code> (<code>${unit}</code> cada {disc})\n💰 Saldo: <code>${bal}</code>\n{div}\n\n📎 <code>{fname}</code> anexado — cada número com seu link de API de OTP.\n📩 Cada OTP chega neste chat automaticamente.\n📱 Acompanhe em 📱 Números Ativos.',
    'ub_partial': '⚠️ O estoque andou rápido — só havia <code>{n}</code>. Cobramos apenas por <code>{n}</code>.',
    'ub_none': '❌ <b>Sem estoque</b> — nada foi cobrado.',
    'ub_hint_file': '❌ Isso é um arquivo — aqui eu preciso de um NÚMERO.\n👉 Digite QUANTOS números você quer:',
    'act_title': '📞 <b>Seus Números Ativos</b> ({n})',
    'act_none': '📭 Você não tem números ativos agora.\n🛒 Compre um número — aparece aqui na hora.',
    'act_hint': '▶️ Toque em um número para copiar e envie aqui — o número abre com o botão Get OTP.',
    'act_more': '…e mais {extra}',
    'act_card_title': '🟢 <b>Seu Número Ativo</b>',
    'act_card_body': '📩 Toque em GET OTP quando quiser — o código chega até você no momento em que aparecer. Sem limite de tempo.',
    'rfs_title': '🎉 <b>Seu Reembolso foi Realizado</b>',
    'rfs_body': '🟢 <code>{number}</code>\n💰 <code>${amount}</code> adicionado ao seu saldo',
    'ref_title': '🤝 <b>Indique &amp; Ganhe</b>',
    'ref_body': 'Partilhe o seu link — ganha <b>${rate}</b> sempre que um amigo comprar um número. Para sempre.',
    'ref_link': '🔗 O seu link de indicação:',
    'ref_stats': '👥 Indicados: <b>{count}</b>\n💰 Total ganho: <b>${earned}</b>',
    'ref_rate_line': '💵 A sua taxa: <b>${rate}</b> por compra',
    'ref_vip_line': '👑 <b>Indicador VIP</b> — taxa especial de <b>${rate}</b> por compra',
    'btn_ref_share': '📤 Partilhar Link',
    'ref_share_text': '🎁 Números premium de WhatsApp e Telegram — OTP instantâneo!',
    'ref_none_yet': 'Ainda sem indicações — partilhe o seu link para começar a ganhar 👇',
    'ref_earned_notif': '🎉 <b>Bónus de indicação!</b>\n{div}\n👤 {name} comprou um número\n💰 <b>+${amount}</b> adicionados ao seu saldo\n💼 Saldo: <b>${bal}</b>\n{div}',
    'ref_new_ref': '👥 <b>Nova indicação!</b>\n👤 {name} entrou através do seu link\n💰 Ganha em cada compra dele',
    'ref_paused': '⏸ O programa de indicações está em pausa.\n💡 Volte em breve!',
    },
    "es": {
    'btn_buy': '🛒 Comprar Número',
    'btn_profile': '👤 Perfil',
    'btn_deposit': '💳 Depósito',
    'btn_support': '💬 Soporte',
    'btn_back': '⬅️ Atrás',
    'btn_cancel_dep': '❌ Cancelar Depósito',
    'btn_wa': '🟢 WhatsApp',
    'btn_tg': '🔵 Telegram',
    'btn_dep_new': '💵 Nuevo Depósito',
    'btn_dep_hist': '📜 Historial',
    'btn_custom_amount': '✏️ Monto Personalizado',
    'btn_i_paid': '✅ YA PAGUÉ — Enviar TXID',
    'btn_get_otp': '📩 Obtener OTP',
    'btn_buy_now': '✅ Comprar — ${price}',
    'kb_placeholder': 'Elige una opción 👇',
    'menu_title': '🏠 <b>Menú Principal</b>',
    'menu_where': '👉 ¿A dónde vamos ahora?',
    'menu_footer': '✅ ¡Listo! Ya estás de vuelta en el menú principal 👇',
    'blocked': '🔒 <b>Acceso bloqueado</b>\nEsta cuenta ya no puede usar el bot.',
    'lang_pick_title': '🌐 <b>Elige tu idioma</b>',
    'lang_pick_hint': '👉 Toca tu idioma para continuar',
    'lang_set_ok': '✅ Idioma establecido: {lang}',
    'lang_current': '🌐 Idioma actual: <b>{lang}</b>\nToca un idioma abajo para cambiar.',
    'welcome_hi': '👋 <b>¡Hola {name}, bienvenido de nuevo!</b>',
    'welcome_tagline': '📱 Números premium de WhatsApp &amp; Telegram\n⚡ Entrega instantánea • OTP incluido',
    'welcome_balance': '💰 Saldo: <code>${bal}</code>',
    'welcome_stock': '📦 En stock: <code>{total}</code> números',
    'welcome_cta': '👉 Toca un botón abajo para empezar',
    'profile_title': '👤 <b>Tu Perfil</b>',
    'lbl_id': '🆔 ID:',
    'lbl_name': '📝 Nombre:',
    'lbl_username': '🌐 Usuario:',
    'prof_purchased': '🛒 Comprados: <code>{n}</code>',
    'prof_spent': '💸 Gastado: <code>${amount}</code>',
    'prof_deposited': '🏦 Depositado: <code>${amount}</code>',
    'prof_otps': '📩 OTPs: <code>{n} ({pct})</code>',
    'support_title': '💬 <b>¿Necesitas ayuda?</b>',
    'support_admin': '👨\u200d💻 Admin: {handle}',
    'support_time': '⚡ Tiempo de respuesta: usualmente unos minutos',
    'support_body': 'Pagos, problemas de OTP, dudas de stock — solo escríbenos, aquí estamos. 🙌',
    'buy_title': '🛒 <b>Comprar un Número</b>',
    'buy_wa_price': '🟢 WhatsApp — <code>${wa}</code>',
    'buy_tg_price': '🔵 Telegram — <code>${tg}</code>',
    'buy_pick': '👉 Elige un tipo para continuar',
    'ctry_title': '🌍 <b>Elige un País</b>',
    'ctry_avail': '📱 Números {label} disponibles',
    'cta_select': '👉 Selecciona abajo',
    'confirm_title': '🧾 <b>Confirma tu Pedido</b>',
    'cf_type': '📱 Tipo: {label}',
    'cf_country': '🌍 País: {flag} {country}',
    'cf_price': '💵 Precio: <code>${rate}</code>',
    'cf_balance': '💰 Tu Saldo: <code>${bal}</code>',
    'cf_cta': '👉 ¿Todo bien? Confirma abajo',
    'ps_title': '✅ <b>¡Compra completada!</b>',
    'ps_number': '📱 Número: <code>{number}</code>',
    'ps_label': '🏷️ {label} • {flag} {country}',
    'ps_paid': '💵 Pagado: <code>${rate}</code>',
    'ps_order': '🧾 Pedido: <code>{order}</code>',
    'ps_get_otp': '📩 Toca <b>Get OTP</b> abajo cuando quieras para obtener tu código',
    'ps_copy': '📋 Toca el número para copiarlo',
    'ins_title': '⚠️ <b>Saldo Insuficiente</b>',
    'ins_price': '💵 Precio: <code>${rate}</code>',
    'ins_balance': '💰 Saldo: <code>${bal}</code>',
    'ins_need': '❗ Te falta: <code>${need}</code>',
    'ins_cta': '👉 Recarga con un toque',
    'oos_title': '❌ <b>Sin Stock</b>',
    'oos_label': '🏷️ {label} — {flag} {country}',
    'oos_cta': '👉 Prueba otro país, o escribe al 💬 Soporte',
    'otp_received': '🎉 <b>¡OTP Recibido!</b>',
    'otp_waiting': '⏳ <b>Todavía esperando el OTP</b>',
    'otp_waiting_body': 'El SMS puede tardar un poco — seguimos verificando en segundo plano. Llegará aquí automáticamente. 👀',
    'otp_blocked': '🔒 <b>OTP Bloqueado</b>',
    'otp_blocked_body': 'Este número fue reembolsado — ningún OTP llegará aquí de nuevo.',
    'toast_no_link': 'ℹ️ Sin link de OTP en este número — contacta al soporte',
    'otp_timeout': '⏳ <b>Sin OTP tras 10 Minutos</b>',
    'otp_timeout_body': 'El SMS a veces se retrasa. Toca 🔑 <b>Get OTP</b> en tu recibo para verificar de nuevo cuando quieras.',
    'toast_not_yours': '❌ Ese número no es tuyo',
    'toast_not_found': '❌ Número no encontrado',
    'dep_title': '💳 <b>Depósito</b>',
    'dep_min_line': '💵 Mín: <code>${min}</code> • Verificado por TXID 🔐',
    'dep_min_only': '💵 Mín: <code>${min}</code>',
    'cta_pick': '👉 Elige una opción',
    'dep_amt_title': '💰 <b>Elige un Monto</b>',
    'dep_amt_hint': '👉 Toca un monto, o usa ✏️ Personalizado',
    'dep_net_title': '🌐 <b>Elige la Red</b>',
    'dep_net_amount': '💵 <code>${amount}</code> USDT',
    'dep_net_hint': '👉 Toca tu red',
    'dep_hist_title': '📜 <b>Historial de Depósitos</b>',
    'dep_hist_empty': 'Aún no hay depósitos — el primero aparecerá aquí.',
    'dep_min_warn': '⚠️ El depósito mínimo es <code>${min}</code>\n👉 Elige de nuevo abajo',
    'custom_title': '✏️ <b>Escribe tu Monto</b>\n💵 En USDT — mínimo <code>${min}</code>\nEjemplo: <code>1.50</code>',
    'custom_err': '❌ El depósito mínimo es <code>${min}</code>\n💵 Escribe el monto en USDT otra vez\nEjemplo: <code>1.50</code>',
    'card_send': '💸 <b>Envía ${amount} USDT</b>',
    'card_network': '🌐 Red: <b>{net}</b>',
    'card_address': '📍 Dirección (toca para copiar):',
    'card_warn': '⚠️ Solo <b>{net}</b> — red equivocada = fondos perdidos.',
    'card_paid': '✅ ¿Pagaste? Toca <b>I PAID</b> → luego envía tu TXID.',
    'card_expire': '🧾 <code>{dep_id}</code> • expira {expires} ⏳',
    'txid_title': '🔑 <b>Pega tu TXID de {net}</b>',
    'txid_body': '📋 El hash de la transacción de tu pago.',
    'txid_format': 'Formato: <code>{fmt}</code>',
    'txid_ok_line': '✅ Verificado → crédito instantáneo',
    'txid_no_line': '❌ Sin TXID → sin crédito',
    'dep_cancelled': '❌ <b>Depósito cancelado.</b>',
    'dep_expired_session': 'ℹ️ Sesión expirada.\nInicia un depósito nuevo desde el menú.',
    'dep_no_active': 'ℹ️ No hay pedido de depósito activo.\nInicia uno nuevo desde el menú.',
    'dep_closed': 'ℹ️ Este pedido de depósito ya está cerrado.\nInicia uno nuevo desde el menú.',
    'toast_bad_amount': '❌ Monto inválido',
    'scr_needed': '❌ <b>No se necesita captura.</b>\nEnvía tu <b>TXID</b> (el hash de la transacción) como texto.',
    'txid_bad_fmt': '❌ <b>Formato de TXID inválido</b>\n{net} requiere <code>{fmt}</code>. Copia el hash completo desde tu wallet.',
    'dep_checking': '⏳ Verificando tu transacción en {net}...',
    'dep_locked': '🔒 Pedido bloqueado — demasiados TXIDs incorrectos.\nContacta al admin con el ID del pedido <code>{order}</code>.',
    'txid_replay': '🔁 Este TXID ya fue usado.\nUn TXID = un pedido. Envía el hash de tu nueva transacción.',
    'bin_pay_id': '🏦 <b>Binance Pay ID</b> - envía A este ID:',
    'bin_card_hint': '⚠️ Paga desde la <b>app de Binance → Pay</b>\n💵 Envía <b>solo USDT</b>, por el monto exacto de arriba.\n❌ ID o activo incorrecto = dinero perdido.',
    'bin_auto_line': '⚡ El pago se verifica automáticamente en ~1 minuto.\nO toca I PAID y pega el Order ID.',
    'bin_txid_title': '🔑 <b>Pega tu Order ID de Binance Pay</b>',
    'bin_txid_body': '📋 App de Binance → Pay → abre tu transferencia → copia el <b>Order ID</b> y pégalo aquí.',
    'bin_bad_fmt': '❌ <b>Eso no es un Order ID de Binance Pay.</b>\nTiene la forma <code>M_P_123456789012345678</code> - cópialo en la app de Binance → Pay → detalles de la transferencia.',
    'bin_amt_mismatch': '❌ <b>Monto incorrecto.</b>\nEl pago muestra <code>${got}</code>, el pedido necesita <code>${want}</code>.\nPaga el monto exacto y pega ese Order ID.',
    'bin_decline_pending': '⏳ Aún no se encontró ningún pago para este Order ID.\nPaga primero, revisa el Order ID y reenvíalo en un minuto.',
    'bin_decline_stale': '❌ Este Order ID no puede usarse para este pedido.\nEs anterior al pedido o ya fue usado.\nPaga de nuevo y pega el nuevo Order ID.',
    'bin_decline_out': '❌ Esa es una transferencia SALIENTE (OUTGOING) - enviaste el dinero fuera.\nPega el Order ID de la transferencia que nos ENVIASTE a nosotros.',
    'dep_api_busy': '⏳ La verificación de Binance está ocupada ahora.\nTu pedido está seguro - inténtalo de nuevo en un minuto.',
    'amt_mismatch': '❌ <b>Monto incorrecto.</b>\nLa transacción muestra <code>${got}</code>, el pedido necesita <code>${want}</code>.\nEnvía el hash correcto o inicia un depósito nuevo.',
    'dep_already': '✅ Este depósito ya fue confirmado.\nTu saldo ya está actualizado.',
    'dep_ok_title': '✅ <b>¡Depósito Confirmado!</b>',
    'dep_ok_credited': '💵 Acreditado: <code>${amount}</code>',
    'dep_ok_balance': '💰 Saldo: <code>${bal}</code>',
    'dep_ok_cta': '🛒 ¡Feliz compra — toca Comprar abajo!',
    'decline_pending': '⏳ Transacción aún no encontrada en {net}.\nRevisa el TXID y envíalo de nuevo en un minuto.',
    'decline_failed': '❌ La transacción falló en la blockchain — no se movieron fondos.\nEnvía un nuevo TXID exitoso.',
    'decline_token': '❌ Eso no fue una transferencia de USDT en {net}.\nPor favor envía solo USDT.',
    'decline_recipient': '❌ Destinatario equivocado.\nEste TXID no envió USDT a nuestra dirección de {net}.',
    'dm_credited': '✅ Acreditado <code>${amount}</code> • Saldo <code>${bal}</code>\n🧾 Pedido <code>{order}</code>',
    'dm_dep_confirmed': '✅ <b>DEPÓSITO CONFIRMADO</b>\n\n{div}\n💵 <b>Monto:</b> ${amount}\n🧾 <b>Pedido:</b> <code>{order}</code>\n{div}\n\n💰 <b>¡Saldo actualizado! Feliz compra 🛒</b>',
    'dm_dep_rejected': '❌ <b>DEPÓSITO RECHAZADO</b>\n\n{div}\n🧾 <b>Pedido:</b> <code>{order}</code>\n{div}\n\n💬 Contacta al Soporte si crees que es un error.',
    'help_title': '📖 <b>Ayuda Rápida</b>',
    'help_lines': '/start — abrir el menú principal\n/menu — mostrar el menú\n/language — cambiar el idioma\n/admin — panel admin',
    'help_cta': '💡 Todo está a un toque de distancia en los botones de abajo.',
    'err_generic': '⚠️ <b>Algo salió mal.</b>\nInténtalo de nuevo — o presiona /start.',
    'toast_processing': 'Procesando tu compra... ⏳',
    'toast_invalid': 'Solicitud inválida',
    'toast_expired': '❌ Este botón expiró — inténtalo de nuevo',
    'btn_join_channel': '✉️ UNIRSE AL CANAL',
    'btn_join_group': '✉️ UNIRSE AL GRUPO',
    'fj_title': '🔒 <b>Falta un Paso para Desbloquear</b>',
    'fj_body': '👉 Únete a nuestro canal de abajo para usar el bot.\n✅ Después de unirte, toca <b>Verificar</b>.',
    'btn_fj_check': '✅ Verificar',
    'fj_toast_no': '❌ Todavía no te has unido — únete primero y toca Verificar.',
    'fj_done': '✅ <b>¡Verificado!</b>\n🎉 Bienvenido — tu menú principal está desbloqueado abajo 👇',
    'fj_dm': '✅ <b>¡Unión verificada!</b>\n👋 Bienvenido — menú principal desbloqueado 👇',
    'btn_refer': '🎁 Invita y Gana',
    'btn_active': '📱 Números Activos',
    'btn_ubulk': '📦 Compra Masiva',
    'ub_pick': '📦 <b>Compra Masiva</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> disponibles • <code>${wa_rate}</code> c/u\n🔵 Telegram — <code>{tg_n}</code> disponibles • <code>${tg_rate}</code> c/u\n\n🎁 <b>{dmin}+ números = ${damt} menos por número</b>\n\n👉 Elige el tipo:',
    'ub_qty': '📦 <b>Compra Masiva — {label}</b>\n\n📱 Disponibles: <code>{n}</code>\n💵 Precio: <code>${rate}</code> por número\n💰 Saldo: <code>${bal}</code>\n\n🎁 {dmin}+ = <b>${damt} menos por número</b>\n\n👉 Escribe CUÁNTOS números quieres:',
    'ub_bad_qty': '❌ Escribe solo un NÚMERO (1 a {cap}).\n👉 Intenta de nuevo:',
    'ub_stock_low': '⚠️ Solo hay <code>{n}</code> disponibles ahora.\n👉 Escribe una cantidad menor:',
    'ub_no_bal': '⚠️ {n} números = <code>${total}</code>\n💰 Saldo: <code>${bal}</code>\n👉 Máximo que te alcanza: <code>{maxn}</code> números. Escribe eso (o menos):',
    'ub_confirm': '🧾 <b>Confirmar Pedido</b>\n\n{div}\n📱 Tipo: <b>{label}</b>\n🔢 Números: <code>{n}</code>\n💵 Precio: <code>${unit}</code> c/u {disc}\n💰 Total: <code>${total}</code>\n💰 Después: <code>${after}</code>\n{div}\n\n👉 Confirma abajo — el archivo .txt llega al instante.',
    'ub_disc': '(descuento {dmin}+ ✅)',
    'ub_expired': '⏳ Sesión expirada — empieza de nuevo en 📦 Compra Masiva.',
    'ub_done': '✅ <b>¡Pedido Masivo Completado!</b>\n\n{div}\n📱 Números entregados: <code>{n}</code>\n💵 Pagado: <code>${total}</code> (<code>${unit}</code> c/u {disc})\n💰 Saldo: <code>${bal}</code>\n{div}\n\n📎 <code>{fname}</code> adjunto — cada número con su enlace API de OTP.\n📩 Cada OTP llega a este chat automáticamente.\n📱 SíGUELOS en 📱 Números Activos.',
    'ub_partial': '⚠️ El stock se movió rápido — solo había <code>{n}</code>. Se cobró solo por <code>{n}</code>.',
    'ub_none': '❌ <b>Sin stock</b> — no se cobró nada.',
    'ub_hint_file': '❌ Eso es un archivo — aquí necesito un NÚMERO.\n👉 Escribe CUÁNTOS números quieres:',
    'act_title': '📞 <b>Tus Números Activos</b> ({n})',
    'act_none': '📭 Ahora mismo no tienes números activos.\n🛒 Compra un número — aparecerá aquí al instante.',
    'act_hint': '▶️ Toca un número para copiarlo y envíalo aquí — el número se abre con su botón Get OTP.',
    'act_more': '…y {extra} más',
    'act_card_title': '🟢 <b>Tu Número Activo</b>',
    'act_card_body': '📩 Pulsa GET OTP cuando quieras — el código te llega en cuanto entre. Sin límite de tiempo.',
    'rfs_title': '🎉 <b>Tu Reembolso fue Exitoso</b>',
    'rfs_body': '🟢 <code>{number}</code>\n💰 <code>${amount}</code> agregado a tu saldo',
    'ref_title': '🤝 <b>Invita y Gana</b>',
    'ref_body': 'Comparte tu enlace — ganas <b>${rate}</b> cada vez que un amigo compra un número. Para siempre.',
    'ref_link': '🔗 Tu enlace de referido:',
    'ref_stats': '👥 Referidos: <b>{count}</b>\n💰 Total ganado: <b>${earned}</b>',
    'ref_rate_line': '💵 Tu tarifa: <b>${rate}</b> por compra',
    'ref_vip_line': '👑 <b>Referidor VIP</b> — tarifa especial de <b>${rate}</b> por compra',
    'btn_ref_share': '📤 Compartir Enlace',
    'ref_share_text': '🎁 Números premium de WhatsApp y Telegram — ¡OTP al instante!',
    'ref_none_yet': 'Aún no tienes referidos — comparte tu enlace para empezar a ganar 👇',
    'ref_earned_notif': '🎉 <b>¡Bono de referido!</b>\n{div}\n👤 {name} compró un número\n💰 <b>+${amount}</b> añadidos a tu saldo\n💼 Saldo: <b>${bal}</b>\n{div}',
    'ref_new_ref': '👥 <b>¡Nuevo referido!</b>\n👤 {name} se unió con tu enlace\n💰 Ganas en cada compra que haga',
    'ref_paused': '⏸ El programa de referidos está en pausa.\n💡 ¡Vuelve pronto!',
    },
    "sw": {
    'btn_buy': '🛒 Nunua Namba',
    'btn_profile': '👤 Wasifu',
    'btn_deposit': '💳 Amana',
    'btn_support': '💬 Msaada',
    'btn_back': '⬅️ Rudi',
    'btn_cancel_dep': '❌ Ghairi Amana',
    'btn_wa': '🟢 WhatsApp',
    'btn_tg': '🔵 Telegram',
    'btn_dep_new': '💵 Amana Mpya',
    'btn_dep_hist': '📜 Historia',
    'btn_custom_amount': '✏️ Kiasi Maalum',
    'btn_i_paid': '✅ NIMELIPA — Tuma TXID',
    'btn_get_otp': '📩 Pata OTP',
    'btn_buy_now': '✅ Nunua — ${price}',
    'kb_placeholder': 'Chagua chaguo 👇',
    'menu_title': '🏠 <b>Menyu Kuu</b>',
    'menu_where': '👉 Unataka kwenda wapi sasa?',
    'menu_footer': '✅ Imekamilika! Umerudi menyu kuu 👇',
    'blocked': '🔒 <b>Ufikiaji umefungwa</b>\nAkaunti hii haiwezi kutumia bot tena.',
    'lang_pick_title': '🌐 <b>Chagua Lugha Yako</b>',
    'lang_pick_hint': '👉 Gusa lugha yako ili uendelee',
    'lang_set_ok': '✅ Lugha imewekwa: {lang}',
    'lang_current': '🌐 Lugha ya sasa: <b>{lang}</b>\nGusa lugha hapa chini kubadilisha.',
    'welcome_hi': '👋 <b>Habari {name}, karibu tena!</b>',
    'welcome_tagline': '📱 Namba premium za WhatsApp &amp; Telegram\n⚡ Uwasilisho wa papo hapo • OTP imejumuishwa',
    'welcome_balance': '💰 Salio: <code>${bal}</code>',
    'welcome_stock': '📦 Kwenye stoo: <code>{total}</code> namba',
    'welcome_cta': '👉 Gusa kitufe hapa chini ili uanze',
    'profile_title': '👤 <b>Wasifu Wako</b>',
    'lbl_id': '🆔 ID:',
    'lbl_name': '📝 Jina:',
    'lbl_username': '🌐 Jina la mtumiaji:',
    'prof_purchased': '🛒 Zilizonunuliwa: <code>{n}</code>',
    'prof_spent': '💸 Zilizotumika: <code>${amount}</code>',
    'prof_deposited': '🏦 Zilizowekwa: <code>${amount}</code>',
    'prof_otps': '📩 OTP: <code>{n} ({pct})</code>',
    'support_title': '💬 <b>Unahitaji Msaada?</b>',
    'support_admin': '👨\u200d💻 Msimamizi: {handle}',
    'support_time': '⚡ Muda wa kujibu: kwa kawaida dakika chache',
    'support_body': 'Malipo, matatizo ya OTP, maswali ya stoo — tuandikie tu, sisi hapa. 🙌',
    'buy_title': '🛒 <b>Nunua Namba</b>',
    'buy_wa_price': '🟢 WhatsApp — <code>${wa}</code>',
    'buy_tg_price': '🔵 Telegram — <code>${tg}</code>',
    'buy_pick': '👉 Chagua aina ili uendelee',
    'ctry_title': '🌍 <b>Chagua Nchi</b>',
    'ctry_avail': '📱 Namba za {label} zinapatikana',
    'cta_select': '👉 Chagua hapa chini',
    'confirm_title': '🧾 <b>Thibitisha Oda Yako</b>',
    'cf_type': '📱 Aina: {label}',
    'cf_country': '🌍 Nchi: {flag} {country}',
    'cf_price': '💵 Bei: <code>${rate}</code>',
    'cf_balance': '💰 Salio Lako: <code>${bal}</code>',
    'cf_cta': '👉 Kila kitu sawa? Thibitisha hapa chini',
    'ps_title': '✅ <b>Ununuzi Umekamilika!</b>',
    'ps_number': '📱 Namba: <code>{number}</code>',
    'ps_label': '🏷️ {label} • {flag} {country}',
    'ps_paid': '💵 Lililolipwa: <code>${rate}</code>',
    'ps_order': '🧾 Oda: <code>{order}</code>',
    'ps_get_otp': '📩 Gusa <b>Get OTP</b> hapa chini wakati wowote upate msimbo wako',
    'ps_copy': '📋 Gusa namba ili uinakili',
    'ins_title': '⚠️ <b>Salio si la kutosha</b>',
    'ins_price': '💵 Bei: <code>${rate}</code>',
    'ins_balance': '💰 Salio: <code>${bal}</code>',
    'ins_need': '❗ Unahitaji: <code>${need}</code> zaidi',
    'ins_cta': '👉 Jaza salio kwa mguso mmoja',
    'oos_title': '❌ <b>Stoo Imeisha</b>',
    'oos_label': '🏷️ {label} — {flag} {country}',
    'oos_cta': '👉 Jaribu nchi nyingine, au wasiliana na 💬 Msaada',
    'otp_received': '🎉 <b>OTP Imefika!</b>',
    'otp_waiting': '⏳ <b>Bado Tunasubiri OTP</b>',
    'otp_waiting_body': 'SMS inaweza kuchukua muda — bado tunakagua nyuma ya pazia. Itafika hapa yenyewe. 👀',
    'otp_blocked': '🔒 <b>OTP Imefungwa</b>',
    'otp_blocked_body': 'Namba hii imerejeshwa — OTP haiwezi kufika hapa tena.',
    'toast_no_link': 'ℹ️ Hakuna kiungo cha OTP kwenye namba hii — wasiliana na msaada',
    'otp_timeout': '⏳ <b>Hakuna OTP baada ya Dakika 10</b>',
    'otp_timeout_body': 'SMS huchelewa wakati mwingine. Gusa 🔑 <b>Get OTP</b> kwenye risiti kuangalia tena wakati wowote.',
    'toast_not_yours': '❌ Hiyo si namba yako',
    'toast_not_found': '❌ Namba haijatapatikana',
    'dep_title': '💳 <b>Amana</b>',
    'dep_min_line': '💵 Kidogo zaidi: <code>${min}</code> • Inathibitishwa kwa TXID 🔐',
    'dep_min_only': '💵 Kidogo zaidi: <code>${min}</code>',
    'cta_pick': '👉 Chagua chaguo',
    'dep_amt_title': '💰 <b>Chagua Kiasi</b>',
    'dep_amt_hint': '👉 Gusa kiasi, au chagua ✏️ Maalum',
    'dep_net_title': '🌐 <b>Chagua Mtandao</b>',
    'dep_net_amount': '💵 <code>${amount}</code> USDT',
    'dep_net_hint': '👉 Gusa mtandao wako',
    'dep_hist_title': '📜 <b>Historia ya Amana</b>',
    'dep_hist_empty': 'Hakuna amana bado — amana yako ya kwanza itaonekana hapa.',
    'dep_min_warn': '⚠️ Amana ndogo zaidi ni <code>${min}</code>\n👉 Chagua tena hapa chini',
    'custom_title': '✏️ <b>Andika Kiasi Chako</b>\n💵 Kwa USDT — kidogo zaidi <code>${min}</code>\nMfano: <code>1.50</code>',
    'custom_err': '❌ Amana ndogo zaidi ni <code>${min}</code>\n💵 Andika kiasi cha USDT tena\nMfano: <code>1.50</code>',
    'card_send': '💸 <b>Tuma ${amount} USDT</b>',
    'card_network': '🌐 Mtandao: <b>{net}</b>',
    'card_address': '📍 Anwani (gusa kunakili):',
    'card_warn': '⚠️ <b>{net}</b> pekee — mtandao mbaya = pesa zinapotea.',
    'card_paid': '✅ Umelipa? Gusa <b>I PAID</b> → kisha tuma TXID yako.',
    'card_expire': '🧾 <code>{dep_id}</code> • inaisha {expires} ⏳',
    'txid_title': '🔑 <b>Weka TXID Yako ya {net}</b>',
    'txid_body': '📋 Hash ya muamala wa malipo yako.',
    'txid_format': 'Muundo: <code>{fmt}</code>',
    'txid_ok_line': '✅ Imethibitishwa → salio papo hapo',
    'txid_no_line': '❌ Hakuna TXID → hakuna salio',
    'dep_cancelled': '❌ <b>Amana imeghairiwa.</b>',
    'dep_expired_session': 'ℹ️ Kipindi kimeisha.\nAnzisha amana mpya kutoka menyu.',
    'dep_no_active': 'ℹ️ Hakuna oda ya amana inayofanya kazi.\nAnzisha amana mpya kutoka menyu.',
    'dep_closed': 'ℹ️ Oda hii ya amana imefungwa tayari.\nAnzisha mpya kutoka menyu.',
    'toast_bad_amount': '❌ Kiasi batili',
    'scr_needed': '❌ <b>Picha ya skrini haihitajiki.</b>\nTafadhali tuma <b>TXID</b> yako (hash ya muamala) kama maandishi.',
    'txid_bad_fmt': '❌ <b>Muundo wa TXID ni batili</b>\n{net} inahitaji <code>{fmt}</code>. Nakili hash kamili kutoka pochi yako.',
    'dep_checking': '⏳ Tunakagua muamala wako wa {net}...',
    'dep_locked': '🔒 Oda imefungwa — TXID sahihi hazikuwahi kutumwa nyingi.\nWasiliana na msimamizi ukiwa na ID ya oda <code>{order}</code>.',
    'txid_replay': '🔁 TXID hii imetumika tayari.\nTXID moja = oda moja. Tuma hash ya muamala wako mpya.',
    'bin_pay_id': '🏦 <b>Binance Pay ID</b> - tumilia KWENDA kwenye ID hii:',
    'bin_card_hint': '⚠️ Lipia kwa <b>app ya Binance → Pay</b>\n💵 Tuma <b>USDT pekee</b>, kiasi halisi kilicho hapo juu.\n❌ ID au sarafu isiyo sahihi = pesa kupotea.',
    'bin_auto_line': '⚡ Malipo huthibitishwa kiotomatiki ndani ya dakika ~1.\nAu bonyeza I PAID kisha weka Order ID.',
    'bin_txid_title': '🔑 <b>Weka Order ID yako ya Binance Pay</b>',
    'bin_txid_body': '📋 App ya Binance → Pay → fungua uhamisho wako → nakili <b>Order ID</b> kisha weka hapa.',
    'bin_bad_fmt': '❌ <b>Hayo si Order ID ya Binance Pay.</b>\nInaonekana kama <code>M_P_123456789012345678</code> - inakili kwenye app ya Binance → Pay → maelezo ya uhamisho.',
    'bin_amt_mismatch': '❌ <b>Kiasi hakilingani.</b>\nMalipo yanaonyesha <code>${got}</code>, oda inahitaji <code>${want}</code>.\nLipa kiasi halisi kisha weka Order ID yake.',
    'bin_decline_pending': '⏳ Hakuna malipo yaliyopatikana kwa Order ID hii bado.\nLipa kwanza, kagua Order ID, na utume tena baada ya dakika moja.',
    'bin_decline_stale': '❌ Order ID hii haiwezi kutumika kwa oda hii.\nNi ya zamani kuliko oda au imetumika tayari.\nLipa mpya na utume Order ID mpya.',
    'bin_decline_out': '❌ Hicho ni uhamisho wa KUTUMA (OUTGOING) - pesa imetumwa nje.\nWeka Order ID ya uhamisho uliotuma KWETU.',
    'dep_api_busy': '⏳ Uthibitisho wa Binance una shughuli kwa sasa.\nOda yako iko salama - jaribu tena baada ya dakika moja.',
    'amt_mismatch': '❌ <b>Kiasi hakilingani.</b>\nMuamala unaonyesha <code>${got}</code>, oda inahitaji <code>${want}</code>.\nTuma hash sahihi, au anzisha amana mpya.',
    'dep_already': '✅ Amana hii imeshathibitishwa.\nSalio lako limeshasasishwa.',
    'dep_ok_title': '✅ <b>Amana Imethibitishwa!</b>',
    'dep_ok_credited': '💵 Imewekwa: <code>${amount}</code>',
    'dep_ok_balance': '💰 Salio: <code>${bal}</code>',
    'dep_ok_cta': '🛒 Nunua kwa furaha — gusa Buy hapa chini!',
    'decline_pending': '⏳ Muamala bado haujaonekana kwenye {net}.\nKagua TXID tena na uitume baada ya dakika moja.',
    'decline_failed': '❌ Muamala umeshindikana kwenye blockchain — pesa hazikusogea.\nTuma TXID mpya yenye mafanikio.',
    'decline_token': '❌ Hiyo haikuwa uhamisho wa USDT kwenye {net}.\nTafadhali tuma USDT pekee.',
    'decline_recipient': '❌ Mpokeaji si sahihi.\nTXID hii haikutuma USDT kwa anwani yetu ya {net}.',
    'dm_credited': '✅ Imewekwa <code>${amount}</code> • Salio <code>${bal}</code>\n🧾 Oda <code>{order}</code>',
    'dm_dep_confirmed': '✅ <b>AMANA IMETHIBITISHWA</b>\n\n{div}\n💵 <b>Kiasi:</b> ${amount}\n🧾 <b>Oda:</b> <code>{order}</code>\n{div}\n\n💰 <b>Salio limesasishwa! Nunua kwa furaha 🛒</b>',
    'dm_dep_rejected': '❌ <b>AMANA IMEKATALIWA</b>\n\n{div}\n🧾 <b>Oda:</b> <code>{order}</code>\n{div}\n\n💬 Wasiliana na Msaada ukihisi hili ni kosa.',
    'help_title': '📖 <b>Msaada wa Haraka</b>',
    'help_lines': '/start — fungua menyu kuu\n/menu — onyesha menyu\n/language — badilisha lugha\n/admin — paneli ya msimamizi',
    'help_cta': '💡 Kila kitu kiko umbali wa mguso mmoja kwenye vitufe hapa chini.',
    'err_generic': '⚠️ <b>Kitu kimekosekana.</b>\nJaribu tena — au bonyeza /start.',
    'toast_processing': 'Tunachakata ununuzi wako... ⏳',
    'toast_invalid': 'Ombi batili',
    'toast_expired': '❌ Kitufe hiki kimeisha — jaribu tena',
    'btn_join_channel': '✉️ JIUNGE NA CHANNEL',
    'btn_join_group': '✉️ JIUNGE NA GROUP',
    'fj_title': '🔒 <b>Hatua Moja ya Kufungua</b>',
    'fj_body': '👉 Jiunge na channel yetu hapa chini ili kutumia bot.\n✅ Baada ya kujiunga, bonyeza <b>Thibitisha</b>.',
    'btn_fj_check': '✅ Thibitisha',
    'fj_toast_no': '❌ Huja jiunga bado — jiunga kwanza, kisha bonyeza Thibitisha.',
    'fj_done': '✅ <b>Imethibitishwa!</b>\n🎉 Karibu — menyu yako kuu imefunguliwa hapa chini 👇',
    'fj_dm': '✅ <b>Uanachama umethibitishwa!</b>\n👋 Karibu — menyu kuu imefunguliwa 👇',
    'btn_refer': '🎁 Refer & Pata Pesa',
    'btn_active': '📱 Namba Hai',
    'btn_ubulk': '📦 Nunua kwa Wingi',
    'ub_pick': '📦 <b>Nunua kwa Wingi</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> zipo • <code>${wa_rate}</code> kila moja\n🔵 Telegram — <code>{tg_n}</code> zipo • <code>${tg_rate}</code> kila moja\n\n🎁 <b>Namba {dmin}+ = punguzo la ${damt} kwa kila namba</b>\n\n👉 Chagua aina:',
    'ub_qty': '📦 <b>Nunua kwa Wingi — {label}</b>\n\n📱 Zipo: <code>{n}</code>\n💵 Bei: <code>${rate}</code> kila namba\n💰 Salio: <code>${bal}</code>\n\n🎁 {dmin}+ = <b>${damt} punguzo kwa kila namba</b>\n\n👉 Andika NAMBA ngapi unataka:',
    'ub_bad_qty': '❌ Tafadhali andika NAMBA tu (1 hadi {cap}).\n👉 Jaribu tena:',
    'ub_stock_low': '⚠️ Kuna <code>{n}</code> tu kwa sasa.\n👉 Andika idadi ndogo zaidi:',
    'ub_no_bal': '⚠️ Namba {n} = <code>${total}</code>\n💰 Salio: <code>${bal}</code>\n👉 Unaweza nunua hadi <code>{maxn}</code>. Andika hivyo (au chini):',
    'ub_confirm': '🧾 <b>Thibitisha Oda</b>\n\n{div}\n📱 Aina: <b>{label}</b>\n🔢 Namba: <code>{n}</code>\n💵 Bei: <code>${unit}</code> kila moja {disc}\n💰 Jumla: <code>${total}</code>\n💰 Baadaye: <code>${after}</code>\n{div}\n\n👉 Thibitisha chini — faili la .txt linakuja mara moja.',
    'ub_disc': '(punguzo {dmin}+ ✅)',
    'ub_expired': '⏳ Kipindi kimeisha — anza tena kwa 📦 Nunua kwa Wingi.',
    'ub_done': '✅ <b>Oda ya Wingi Imekamilika!</b>\n\n{div}\n📱 Namba zilizotolewa: <code>{n}</code>\n💵 Zilizolipwa: <code>${total}</code> (<code>${unit}</code> kila moja {disc})\n💰 Salio: <code>${bal}</code>\n{div}\n\n📎 <code>{fname}</code> imeambatishwa — kila namba na kiungo chake cha OTP API.\n📩 Kila OTP inakuja kwenye mazungumzo hii moja kwa moja.\n📱 Fuatilia wakati wowote kwenye 📱 Active Numbers.',
    'ub_partial': '⚠️ Stokiliisha haraka — kuna <code>{n}</code> tu. Malipo yamefanywa kwa <code>{n}</code> tu.',
    'ub_none': '❌ <b>Hakuna stoki</b> — hakuna kilichokatwa.',
    'ub_hint_file': '❌ Hiyo ni faili — hapa nahitaji NAMBA.\n👉 Andika NAMBA ngapi unataka:',
    'act_title': '📞 <b>Namba Zako Hai</b> ({n})',
    'act_none': '📭 Huna namba hai kwa sasa.\n🛒 Nunua namba — itaonekana hapa mara moja.',
    'act_hint': '▶️ Gusa namba ili ku-copy, kisha itume hapa — namba itafunguka na kitufe cha Get OTP.',
    'act_more': '…na {extra} zaidi',
    'act_card_title': '🟢 <b>Namba Yako Hai</b>',
    'act_card_body': '📩 Bonyeza GET OTP wakati wowote — utapata code mara inapofika. Hakuna muda maalum.',
    'rfs_title': '🎉 <b>Marejesho Yamekamilika</b>',
    'rfs_body': '🟢 <code>{number}</code>\n💰 <code>${amount}</code> imeongezwa kwenye salio lako',
    'ref_title': '🤝 <b>Refer &amp; Pata Pesa</b>',
    'ref_body': 'Sambaza link yako — unapata <b>${rate}</b> kila mara rafiki yako anayenunua namba. Milele.',
    'ref_link': '🔗 Link yako ya refer:',
    'ref_stats': '👥 Walioreferiwa: <b>{count}</b>\n💰 Jumla uliyopata: <b>${earned}</b>',
    'ref_rate_line': '💵 Kiwango chako: <b>${rate}</b> kila ununuzi',
    'ref_vip_line': '👑 <b>Refer wa VIP</b> — kiwango maalum <b>${rate}</b> kila ununuzi',
    'btn_ref_share': '📤 Sambaza Link',
    'ref_share_text': '🎁 Namba bora za WhatsApp na Telegram — OTP ya papo hapo!',
    'ref_none_yet': 'Hakuna refer bado — sambaza link yako uanze kupata pesa 👇',
    'ref_earned_notif': '🎉 <b>Bonus ya Refer!</b>\n{div}\n👤 {name} alinunua namba\n💰 <b>+${amount}</b> zimeongezwa kwenye balansi yako\n💼 Balansi: <b>${bal}</b>\n{div}',
    'ref_new_ref': '👥 <b>Refer mpya!</b>\n👤 {name} alijiunga kwa link yako\n💰 Utapata faida kwa kila wanunuzi',
    'ref_paused': '⏸ Programu ya refer imeahirishwa kwa sasa.\n💡 Angalia tena baadaye!',
    },
    "hi": {
    'btn_buy': '🛒 नंबर खरीदें',
    'btn_profile': '👤 प्रोफ़ाइल',
    'btn_deposit': '💳 डिपोजिट',
    'btn_support': '💬 सपोर्ट',
    'btn_back': '⬅️ वापस',
    'btn_cancel_dep': '❌ डिपोजिट रद्द करें',
    'btn_wa': '🟢 WhatsApp',
    'btn_tg': '🔵 Telegram',
    'btn_dep_new': '💵 नया डिपोजिट',
    'btn_dep_hist': '📜 हिस्ट्री',
    'btn_custom_amount': '✏️ कस्टम अमाउंट',
    'btn_i_paid': '✅ पेमेंट हो गया — TXID भेजें',
    'btn_get_otp': '📩 OTP लें',
    'btn_buy_now': '✅ खरीदें — ${price}',
    'kb_placeholder': 'नीचे कोई विकल्प चुनें 👇',
    'menu_title': '🏠 <b>मेन मेन्यू</b>',
    'menu_where': '👉 आगे कहाँ जाना है?',
    'menu_footer': '✅ हो गया! आप वापस मेन मेन्यू पर हैं 👇',
    'blocked': '🔒 <b>एक्सेस बंद है</b>\nयह अकाउंट अब बॉट इस्तेमाल नहीं कर सकता।',
    'lang_pick_title': '🌐 <b>अपनी भाषा चुनें</b>',
    'lang_pick_hint': '👉 आगे बढ़ने के लिए अपनी भाषा दबाएँ',
    'lang_set_ok': '✅ भाषा सेट हो गई: {lang}',
    'lang_current': '🌐 मौजूदा भाषा: <b>{lang}</b>\nबदलने के लिए नीचे कोई भाषा दबाएँ।',
    'welcome_hi': '👋 <b>नमस्ते {name}, दोबारा स्वागत है!</b>',
    'welcome_tagline': '📱 प्रीमियम WhatsApp &amp; Telegram नंबर\n⚡ तुरंत डिलीवरी • OTP के साथ',
    'welcome_balance': '💰 बैलेंस: <code>${bal}</code>',
    'welcome_stock': '📦 स्टॉक में: <code>{total}</code> नंबर',
    'welcome_cta': '👉 शुरू करने के लिए नीचे कोई बटन दबाएँ',
    'profile_title': '👤 <b>आपकी प्रोफ़ाइल</b>',
    'lbl_id': '🆔 ID:',
    'lbl_name': '📝 नाम:',
    'lbl_username': '🌐 यूज़रनेम:',
    'prof_purchased': '🛒 खरीदे: <code>{n}</code>',
    'prof_spent': '💸 खर्च: <code>${amount}</code>',
    'prof_deposited': '🏦 डिपोजिट: <code>${amount}</code>',
    'prof_otps': '📩 OTP: <code>{n} ({pct})</code>',
    'support_title': '💬 <b>मदद चाहिए?</b>',
    'support_admin': '👨\u200d💻 एडमिन: {handle}',
    'support_time': '⚡ रिप्लाई टाइम: आमतौर पर सिर्फ कुछ मिनट',
    'support_body': 'पेमेंट, OTP समस्या, स्टॉक सवाल — बस हमें मैसेज करें, हम हैं ना। 🙌',
    'buy_title': '🛒 <b>नंबर खरीदें</b>',
    'buy_wa_price': '🟢 WhatsApp — <code>${wa}</code>',
    'buy_tg_price': '🔵 Telegram — <code>${tg}</code>',
    'buy_pick': '👉 आगे बढ़ने के लिए एक टाइप चुनें',
    'ctry_title': '🌍 <b>देश चुनें</b>',
    'ctry_avail': '📱 {label} नंबर उपलब्ध',
    'cta_select': '👉 नीचे से चुनें',
    'confirm_title': '🧾 <b>ऑर्डर कन्फर्म करें</b>',
    'cf_type': '📱 टाइप: {label}',
    'cf_country': '🌍 देश: {flag} {country}',
    'cf_price': '💵 कीमत: <code>${rate}</code>',
    'cf_balance': '💰 आपका बैलेंस: <code>${bal}</code>',
    'cf_cta': '👉 सब ठीक है? नीचे कन्फर्म करें',
    'ps_title': '✅ <b>खरीदारी पूरी!</b>',
    'ps_number': '📱 नंबर: <code>{number}</code>',
    'ps_label': '🏷️ {label} • {flag} {country}',
    'ps_paid': '💵 भुगतान: <code>${rate}</code>',
    'ps_order': '🧾 ऑर्डर: <code>{order}</code>',
    'ps_get_otp': '📩 जब चाहें नीचे <b>Get OTP</b> दबाकर अपना कोड लें',
    'ps_copy': '📋 नंबर कॉपी करने के लिए दबाएँ',
    'ins_title': '⚠️ <b>बैलेंस कम है</b>',
    'ins_price': '💵 कीमत: <code>${rate}</code>',
    'ins_balance': '💰 बैलेंस: <code>${bal}</code>',
    'ins_need': '❗ और चाहिए: <code>${need}</code>',
    'ins_cta': '👉 एक टैप में बैलेंस भरें',
    'oos_title': '❌ <b>स्टॉक खत्म</b>',
    'oos_label': '🏷️ {label} — {flag} {country}',
    'oos_cta': '👉 दूसरा देश आज़माएँ, या 💬 सपोर्ट को बताएँ',
    'otp_received': '🎉 <b>OTP आ गया!</b>',
    'otp_waiting': '⏳ <b>OTP का इंतज़ार जारी है</b>',
    'otp_waiting_body': 'SMS में थोड़ा टाइम लग सकता है — हम पीछे से चेक कर रहे हैं। यहीं अपने आप आ जाएगा। 👀',
    'otp_blocked': '🔒 <b>OTP ब्लॉक</b>',
    'otp_blocked_body': 'यह नंबर रिफंड हो चुका है — अब यहाँ OTP कभी नहीं आ सकता।',
    'toast_no_link': 'ℹ️ इस नंबर पर OTP लिंक नहीं है — सपोर्ट से बात करें',
    'otp_timeout': '⏳ <b>10 मिनट में OTP नहीं आया</b>',
    'otp_timeout_body': 'SMS में देरी हो जाती है। रिसीट पर 🔑 <b>Get OTP</b> दबाकर कभी भी दोबारा चेक करें।',
    'toast_not_yours': '❌ यह आपका नंबर नहीं है',
    'toast_not_found': '❌ नंबर नहीं मिला',
    'dep_title': '💳 <b>डिपोजिट</b>',
    'dep_min_line': '💵 कम से कम: <code>${min}</code> • TXID-वेरिफाइड 🔐',
    'dep_min_only': '💵 कम से कम: <code>${min}</code>',
    'cta_pick': '👉 कोई विकल्प चुनें',
    'dep_amt_title': '💰 <b>अमाउंट चुनें</b>',
    'dep_amt_hint': '👉 कोई अमाउंट दबाएँ, या ✏️ कस्टम चुनें',
    'dep_net_title': '🌐 <b>नेटवर्क चुनें</b>',
    'dep_net_amount': '💵 <code>${amount}</code> USDT',
    'dep_net_hint': '👉 अपना नेटवर्क दबाएँ',
    'dep_hist_title': '📜 <b>डिपोजिट हिस्ट्री</b>',
    'dep_hist_empty': 'अभी कोई डिपोजिट नहीं — आपका पहला डिपोजिट यहीं दिखेगा।',
    'dep_min_warn': '⚠️ कम से कम डिपोजिट <code>${min}</code> है\n👉 नीचे दोबारा चुनें',
    'custom_title': '✏️ <b>अपना अमाउंट लिखें</b>\n💵 USDT में — कम से कम <code>${min}</code>\nउदाहरण: <code>1.50</code>',
    'custom_err': '❌ कम से कम डिपोजिट <code>${min}</code> है\n💵 USDT अमाउंट दोबारा लिखें\nउदाहरण: <code>1.50</code>',
    'card_send': '💸 <b>${amount} USDT भेजें</b>',
    'card_network': '🌐 नेटवर्क: <b>{net}</b>',
    'card_address': '📍 एड्रेस (कॉपी करने के लिए दबाएँ):',
    'card_warn': '⚠️ सिर्फ <b>{net}</b> — गलत नेटवर्क = पैसे डूब जाएँगे।',
    'card_paid': '✅ पेमेंट हो गया? <b>I PAID</b> दबाएँ → फिर अपना TXID भेजें।',
    'card_expire': '🧾 <code>{dep_id}</code> • समय खत्म होगा {expires} ⏳',
    'txid_title': '🔑 <b>अपना {net} TXID पेस्ट करें</b>',
    'txid_body': '📋 आपके पेमेंट का ट्रांज़ेक्शन हैश।',
    'txid_format': 'फॉर्मैट: <code>{fmt}</code>',
    'txid_ok_line': '✅ वेरिफाई होते ही → तुरंत बैलेंस',
    'txid_no_line': '❌ TXID नहीं → बैलेंस नहीं',
    'dep_cancelled': '❌ <b>डिपोजिट रद्द हो गया।</b>',
    'dep_expired_session': 'ℹ️ सेशन एक्सपायर हो गया।\nमेन्यू से नया डिपोजिट शुरू करें।',
    'dep_no_active': 'ℹ️ कोई एक्टिव डिपोजिट ऑर्डर नहीं मिला।\nमेन्यू से नया डिपोजिट शुरू करें।',
    'dep_closed': 'ℹ️ यह डिपोजिट ऑर्डर पहले ही बंद हो चुका है।\nमेन्यू से नया शुरू करें।',
    'toast_bad_amount': '❌ गलत अमाउंट',
    'scr_needed': '❌ <b>स्क्रीनशॉट की ज़रूरत नहीं।</b>\nकृपया अपना <b>TXID</b> (ट्रांज़ेक्शन हैश) टेक्स्ट में भेजें।',
    'txid_bad_fmt': '❌ <b>TXID फॉर्मैट गलत</b>\n{net} को <code>{fmt}</code> चाहिए। अपने वॉलेट से पूरा हैश कॉपी करें।',
    'dep_checking': '⏳ आपका {net} ट्रांज़ेक्शन चेक हो रहा है...',
    'dep_locked': '🔒 ऑर्डर लॉक — बहुत ज़्यादा गलत TXID।\nऑर्डर ID <code>{order}</code> के साथ एडमिन से बात करें।',
    'txid_replay': '🔁 यह TXID पहले इस्तेमाल हो चुका है।\nएक TXID = एक ऑर्डर। अपना नया ट्रांज़ेक्शन हैश भेजें।',
    'bin_pay_id': '🏦 <b>Binance Pay ID</b> - इसी ID पर भेजें:',
    'bin_card_hint': '⚠️ <b>Binance app → Pay</b> से पेमेंट करें\n💵 सिर्फ <b>USDT</b> भेजें, ऊपर वाली exact रकम।\n❌ गलत ID या कॉइन = पैसे डूब जाएंगे।',
    'bin_auto_line': '⚡ पेमेंट ~1 मिनट में अपने आप verify हो जाता है।\nया I PAID दबाकर Order ID भेजें।',
    'bin_txid_title': '🔑 <b>अपनी Binance Pay Order ID पेस्ट करें</b>',
    'bin_txid_body': '📋 Binance app → Pay → अपना transfer खोलें → <b>Order ID</b> कॉपी करके यहाँ पेस्ट करें।',
    'bin_bad_fmt': '❌ <b>यह Binance Pay Order ID नहीं है।</b>\nऐसा दिखता है: <code>M_P_123456789012345678</code> - Binance app → Pay → transfer details से कॉपी करें।',
    'bin_amt_mismatch': '❌ <b>रकम मैच नहीं हुई।</b>\nपेमेंट <code>${got}</code> दिखा, ऑर्डर को <code>${want}</code> चाहिए।\nexact रकम भेजकर उसी की Order ID भेजें।',
    'bin_decline_pending': '⏳ इस Order ID का कोई पेमेंट नहीं मिला।\nपहले पेमेंट करें, Order ID जांचें, एक मिनट बाद फिर भेजें।',
    'bin_decline_stale': '❌ यह Order ID इस ऑर्डर के लिए इस्तेमाल नहीं हो सकता।\nयह ऑर्डर से पुराना है या पहले ही खर्च हो चुका है।\nनया पेमेंट करके नई Order ID भेजें।',
    'bin_decline_out': '❌ यह OUTGOING ट्रांसफ़र है - पैसा बाहर गया है।\nहमें भेजे गए ट्रांसफ़र की Order ID पेस्ट करें।',
    'dep_api_busy': '⏳ Binance वेरिफिकेशन अभी व्यस्त है।\nआपका ऑर्डर सुरक्षित है - एक मिनट बाद फिर कोशिश करें।',
    'amt_mismatch': '❌ <b>अमाउंट मैच नहीं।</b>\nट्रांज़ेक्शन में <code>${got}</code> है, ऑर्डर को <code>${want}</code> चाहिए।\nसही हैश भेजें, या नया डिपोजिट शुरू करें।',
    'dep_already': '✅ यह डिपोजिट पहले ही कन्फर्म हो चुका है।\nआपका बैलेंस पहले से अपडेट है।',
    'dep_ok_title': '✅ <b>डिपोजिट कन्फर्म!</b>',
    'dep_ok_credited': '💵 जमा: <code>${amount}</code>',
    'dep_ok_balance': '💰 बैलेंस: <code>${bal}</code>',
    'dep_ok_cta': '🛒 मस्त शॉपिंग करें — नीचे Buy दबाएँ!',
    'decline_pending': '⏳ {net} पर ट्रांज़ेक्शन अभी नहीं दिखा।\nTXID दोबारा चेक करें और एक मिनट में फिर भेजें।',
    'decline_failed': '❌ ट्रांज़ेक्शन चेन पर फेल — पैसे कहीं नहीं गए।\nनया, सफल TXID भेजें।',
    'decline_token': '❌ यह {net} पर USDT ट्रांसफर नहीं था।\nकृपया सिर्फ USDT भेजें।',
    'decline_recipient': '❌ गलत प्राप्तकर्ता।\nइस TXID में USDT हमारे {net} एड्रेस पर नहीं गया।',
    'dm_credited': '✅ <code>${amount}</code> जमा • बैलेंस <code>${bal}</code>\n🧾 ऑर्डर <code>{order}</code>',
    'dm_dep_confirmed': '✅ <b>डिपोजिट कन्फर्म</b>\n\n{div}\n💵 <b>अमाउंट:</b> ${amount}\n🧾 <b>ऑर्डर:</b> <code>{order}</code>\n{div}\n\n💰 <b>बैलेंस अपडेट! मस्त शॉपिंग 🛒</b>',
    'dm_dep_rejected': '❌ <b>डिपोजिट रिजेक्ट</b>\n\n{div}\n🧾 <b>ऑर्डर:</b> <code>{order}</code>\n{div}\n\n💬 गलती लगे तो सपोर्ट से बात करें।',
    'help_title': '📖 <b>क्विक हेल्प</b>',
    'help_lines': '/start — मेन मेन्यू खोलें\n/menu — मेन्यू दिखाएँ\n/language — भाषा बदलें\n/admin — एडमिन पैनल',
    'help_cta': '💡 सब कुछ नीचे के बटनों पर एक टैप दूर है।',
    'err_generic': '⚠️ <b>कुछ गड़बड़ हो गई।</b>\nदोबारा कोशिश करें — या /start दबाएँ।',
    'toast_processing': 'खरीदारी प्रोसेस हो रही है... ⏳',
    'toast_invalid': 'गलत रिक्वेस्ट',
    'toast_expired': '❌ यह बटन एक्सपायर हो गया — दोबारा कोशिश करें',
    'btn_join_channel': '✉️ चैनल जॉइन करें',
    'btn_join_group': '✉️ ग्रुप जॉइन करें',
    'fj_title': '🔒 <b>अनलॉक करने के लिए एक कदम बाकी</b>',
    'fj_body': '👉 बॉट इस्तेमाल करने के लिए नीचे दिए चैनल को जॉइन करें।\n✅ जॉइन करने के बाद <b>वेरिफाई</b> दबाएँ।',
    'btn_fj_check': '✅ वेरिफाई',
    'fj_toast_no': '❌ आपने अभी जॉइन नहीं किया — पहले जॉइन करें, फिर वेरिफाई दबाएँ।',
    'fj_done': '✅ <b>वेरिफाई हो गया!</b>\n🎉 स्वागत है — आपका मेन मेनू नीचे खुल गया 👇',
    'fj_dm': '✅ <b>जॉइन वेरिफाई हो गया!</b>\n👋 स्वागत है — मेन मेनू खुल गया 👇',
    'btn_refer': '🎁 रेफर करें, कमाएँ',
    'btn_active': '📱 एक्टिव नंबर',
    'btn_ubulk': '📦 बल्क खरीद',
    'ub_pick': '📦 <b>बल्क खरीद</b>\n\n🟢 WhatsApp — <code>{wa_n}</code> उपलब्ध • प्रति <code>${wa_rate}</code>\n🔵 Telegram — <code>{tg_n}</code> उपलब्ध • प्रति <code>${tg_rate}</code>\n\n🎁 <b>{dmin}+ नंबर = प्रति नंबर ${damt} छूट</b>\n\n👉 टाइप चुनें:',
    'ub_qty': '📦 <b>बल्क खरीद — {label}</b>\n\n📱 उपलब्ध: <code>{n}</code>\n💵 रेट: प्रति नंबर <code>${rate}</code>\n💰 बैलेन्स: <code>${bal}</code>\n\n🎁 {dmin}+ = प्रति नंबर <b>${damt} छूट</b>\n\n👉 कितने नंबर चाहिए लिखें:',
    'ub_bad_qty': '❌ सिर्फ नंबर लिखें (1 से {cap})।\n👉 फिर कोशिश करें:',
    'ub_stock_low': '⚠️ अभी सिर्फ <code>{n}</code> उपलब्ध हैं।\n👉 छोटी संख्या लिखें:',
    'ub_no_bal': '⚠️ {n} नंबर = <code>${total}</code>\n💰 बैलेन्स: <code>${bal}</code>\n👉 अधिकतम <code>{maxn}</code> नंबर ले सकते हैं। उतने लिखें:',
    'ub_confirm': '🧾 <b>ऑर्डर कन्फार्म करें</b>\n\n{div}\n📱 टाइप: <b>{label}</b>\n🔢 नंबर: <code>{n}</code>\n💵 रेट: प्रति <code>${unit}</code> {disc}\n💰 कुल: <code>${total}</code>\n💰 बाद में: <code>${after}</code>\n{div}\n\n👉 नीचे कन्फार्म करें — .txt फ़ाइल तुरंत आएगी।',
    'ub_disc': '({dmin}+ छूट ✅)',
    'ub_expired': '⏳ सेशन समाप्त — 📦 बल्क खरीद से फिर शुरू करें।',
    'ub_done': '✅ <b>बल्क ऑर्डर पूर्ण!</b>\n\n{div}\n📱 नंबर मिले: <code>{n}</code>\n💵 भुगतान: <code>${total}</code> (प्रति <code>${unit}</code> {disc})\n💰 बैलेन्स: <code>${bal}</code>\n{div}\n\n📎 <code>{fname}</code> अट्याच्षित — हर नंबर के साथ OTP API लिंक।\n📩 हर OTP आते ही इस चैट में अपने आप आ जाएगा।\n📱 📱 Active Numbers में कभी भी ट्रैक करें।',
    'ub_partial': '⚠️ स्टॉक ङीरी खत्म — सिर्फ <code>{n}</code> थे। सिर्फ <code>{n}</code> का ही चार्ज लगा।',
    'ub_none': '❌ <b>स्टॉक नहीं</b> — कुछ भी चार्ज नहीं लगा।',
    'ub_hint_file': '❌ ये फ़ाइल है — यहाँ नंबर चाहिए।\n👉 कितने नंबर चाहिए लिखें:',
    'act_title': '📞 <b>आपके एक्टिव नंबर</b> ({n})',
    'act_none': '📭 अभी आपका कोई एक्टिव नंबर नहीं है।\n🛒 नंबर खरीदें — यहाँ तुरंत दिखेगा।',
    'act_hint': '▶️ कॉपी करने के लिए किसी नंबर पर टैप करें, फिर यहाँ भेजें — नंबर Get OTP बटन के साथ खुल जाएगा।',
    'act_more': '…और {extra} और',
    'act_card_title': '🟢 <b>आपका एक्टिव नंबर</b>',
    'act_card_body': '📩 जब चाहें GET OTP दबाएं — OTP आते ही आपको मिल जाएगा। कोई टाइम लिमिट नहीं।',
    'rfs_title': '🎉 <b>आपका रिफंड सफल</b>',
    'rfs_body': '🟢 <code>{number}</code>\n💰 <code>${amount}</code> आपके बैलेंस में जुड़ गया',
    'ref_title': '🤝 <b>रेफर एंड अर्न</b>',
    'ref_body': 'अपना लिंक शेयर करें — दोस्त के हर नंबर खरीदने पर आपको <b>${rate}</b> मिलेगा। ज़िंदगी भर।',
    'ref_link': '🔗 आपका रेफरल लिंक:',
    'ref_stats': '👥 रेफर किए: <b>{count}</b>\n💰 कुल कमाई: <b>${earned}</b>',
    'ref_rate_line': '💵 आपका रेट: हर खरीद पर <b>${rate}</b>',
    'ref_vip_line': '👑 <b>VIP रेफरर</b> — स्पेशल रेट हर खरीद पर <b>${rate}</b>',
    'btn_ref_share': '📤 लिंक शेयर करें',
    'ref_share_text': '🎁 प्रीमियम WhatsApp और Telegram नंबर — तुरंत OTP!',
    'ref_none_yet': 'अभी कोई रेफर नहीं — कमाई शुरू करने के लिए अपना लिंक शेयर करें 👇',
    'ref_earned_notif': '🎉 <b>रेफरल बोनस!</b>\n{div}\n👤 {name} ने एक नंबर खरीदा\n💰 आपके बैलेंस में <b>+${amount}</b> जुड़े\n💼 बैलेंस: <b>${bal}</b>\n{div}',
    'ref_new_ref': '👥 <b>नया रेफरल!</b>\n👤 {name} आपके लिंक से जुड़ा\n💰 उसकी हर खरीद पर आपको कमाई होगी',
    'ref_paused': '⏸ रेफरल प्रोग्राम फिलहाल बंद है।\n💡 जल्द फिर देखें!',
    },
}

del __LANGS_SRC__


# --------------------------------------------------------------------------- #
#  v9.17 PREMIUM EMOJI LAYER
#  - 47 owner-supplied premium custom-emoji IDs render inside every user-side
#    message, in ALL 13 languages, through one render-time wrapper (pem()).
#  - Buttons / callback toasts / input placeholder keep NORMAL emojis:
#    Telegram does not support custom-emoji entities there (platform rule).
#  - The emoji inside <tg-emoji ...> is a hidden fallback for old clients;
#    exactly ONE emoji is ever displayed (never two).
#  - Boot self-test DMs the owner all 47 premium emojis; if Telegram ever
#    rejects one, the layer auto-disables and normal emojis continue.
#  - Admin texts / group posts / wallets / numbers / rates: same text.
#  - v9.18: admin BUTTONS get premium icons too (BUTTON ICONS block).
# --------------------------------------------------------------------------- #
_PEMOJI_SPEC = (
    ("\U0001F447",  "5406745015365943482"),   # 1  point down
    ("\U0001F3E0",  "5395831812704452001"),   # 2  house / main menu
    ("\U0001F449",  "6269290077512274929"),   # 3  point right (hints)
    ("\u2705",      "6269163801178804220"),   # 4  check mark
    ("\U0001F512",  "5206432422194849059"),   # 5  lock / blocked
    ("\U0001F310",  "5395558210402807000"),   # 6  globe
    ("\U0001F44B",  "5458904472598095631"),   # 7  waving hand
    ("\U0001F4F1",  "6264546492292273861"),   # 8  mobile phone
    ("\u26A1",      "5224607267797606837"),   # 9  lightning
    ("\U0001F4B0",  "6158813773378360152"),   # 10 money bag
    ("\U0001F4E6",  "6023639019290630537"),   # 11 package / stock
    ("\U0001F464",  "5287521623786694265"),   # 12 person / profile
    ("\U0001F194",  "5463131021065097215"),   # 13 ID
    ("\U0001F4DD",  "5562024498481332233"),   # 14 memo / name
    ("\U0001F6D2",  "6073131976141840544"),   # 15 cart / buy
    ("\U0001F4B8",  "5201873447554145566"),   # 16 money with wings
    ("\U0001F3E6",  "5332455502917949981"),   # 17 bank / deposited
    ("\U0001F4E9",  "5944769808984709885"),   # 18 envelope / OTP
    ("\U0001F4AC",  "6073446711345291938"),   # 19 speech / support
    ("\U0001F468\u200D\U0001F4BB", "5204435863697649763"),  # 20 dev admin
    ("\U0001F64C",  "5336885546935427008"),   # 21 raised hands
    ("\U0001F7E2",  "5334998226636390258"),   # 22 green circle (WA)
    ("\U0001F535",  "5330237710655306682"),   # 23 blue circle (TG)
    ("\U0001F30D",  "6084845507304229827"),   # 24 globe / country
    ("\U0001F9FE",  "5444856076954520455"),   # 25 receipt / order
    ("\U0001F4B5",  "5197434882321567830"),   # 26 dollar / price
    ("\U0001F3F7\uFE0F", "6170104177247654767"),            # 27 label
    ("\U0001F4CB",  "5165830112070863167"),   # 28 clipboard / copy
    ("\u26A0\uFE0F", "6267000941547885720"),                # 29 warning
    ("\u2757",      "4956368164817470478"),   # 30 exclamation
    ("\u274C",      "6267039884016358504"),   # 31 cross / errors
    ("\U0001F389",  "5193018401810822951"),   # 32 party / OTP got
    ("\u23F3",      "6267229004311303657"),   # 33 hourglass / waiting
    ("\U0001F440",  "5116599934203724812"),   # 34 eyes
    ("\u2139\uFE0F", "6069045379184206363"),                # 35 info
    ("\U0001F511",  "4916090902113420509"),   # 36 key / get OTP
    ("\U0001F4B3",  "6069045215975448549"),   # 37 card / deposit
    ("\U0001F510",  "5197288647275071607"),   # 38 locked / verified
    ("\u270F\uFE0F", "5116512467194741904"),                # 39 pencil
    ("\U0001F4DC",  "5845724624733608381"),   # 40 scroll / history
    ("\U0001F4CD",  "5240147597640876449"),   # 41 pin / address
    ("\u2192",      "5372917041193828849"),   # 42 right arrow
    ("\U0001F501",  "5935950110822242301"),   # 43 repeat / txid replay
    ("\U0001F4D6",  "6052914628776697272"),   # 44 book / help
    ("\U0001F4A1",  "5945066071533820120"),   # 45 bulb / tip
    ("\u2190",      "5165824283800241035"),   # 46 left arrow (RTL)
    ("\u2B1C",      "5447472837319221129"),   # 47 white square (RTL)
)
_PEMOJI = {tok: eid for tok, eid in _PEMOJI_SPEC}
_PEMO_ORDER = [tok for tok, _e in _PEMOJI_SPEC]
# bare forms (no variation selector) map to the same premium id - safety net
for _fe, _bare in (("\U0001F3F7\uFE0F", "\U0001F3F7"), ("\u26A0\uFE0F", "\u26A0"),
                   ("\u2139\uFE0F", "\u2139"), ("\u270F\uFE0F", "\u270F")):
    if _fe in _PEMOJI:
        _PEMOJI.setdefault(_bare, _PEMOJI[_fe])
# U+2192/U+2190 are TEXT arrows, not Unicode emoji: Telegram rejects them as
# <tg-emoji> content (ENTITY_TEXT_INVALID). Their tag fallback is the valid
# emoji twin; the premium custom id (owner's) stays untouched.
_PEM_ALT = {"\u2192": "\u27A1\uFE0F", "\u2190": "\u2B05\uFE0F"}
# keys that must NEVER be premium-wrapped: callback toasts + kb placeholder
_PEM_PLAIN = {
    "kb_placeholder", "lang_set_ok",
    "toast_invalid", "toast_processing", "toast_expired",
    "toast_bad_amount",
    "toast_no_link", "toast_not_found", "toast_not_yours",
    "fj_toast_no",   # v9.23: callback toasts never get premium tags
    "ref_share_text",   # v9.24: goes into a t.me/share URL, never HTML
}
_PEM_ACTIVE = True
# v9.36 SELF-HEALING PREMIUM LAYER (owner bug: "ek baar fix kiya tha,
# 2 din baad phir se normal ho gaya" - the old design flipped the WHOLE
# layer OFF, permanently, on ONE dead ID at boot or ONE runtime reject;
# only a restart with a clean probe ever brought it back).
#  - _PEM_DEAD: per-ID graveyard. A dead/rotated ID is skipped alone;
#    every still-alive ID keeps rendering premium.
#  - _PEM_COOLDOWN_UNTIL: short cooldown instead of a permanent OFF.
#    While it lasts pem() stays plain; when it expires premium is
#    retried automatically - the layer HEALS itself (e.g. the moment
#    the owner's Telegram Premium / pack is back, no restart needed).
#  - the 30-min heal loop (_pem_heal_loop) re-probes read-only and
#    revives/prunes IDs while the bot runs.
_PEM_DEAD = set()
_PEM_COOLDOWN_UNTIL = 0.0
_PEM_COOLDOWN_S = 600           # v9.37: 10 min (was 1800) - faster self-heal
_PEM_RE = re.compile("(" + "|".join(re.escape(e) for e in
                                    sorted(_PEMOJI, key=len, reverse=True)) + ")")
_PEM_CODE_SPLIT = re.compile(r"(<code>.*?</code>|<pre>.*?</pre>)", re.S)
_PEM_TAG_RE = re.compile(r'<tg-emoji emoji-id="\d+">(.*?)</tg-emoji>', re.S)


def _pem_cool(reason: str):
    """v9.37: 10-min premium cooldown (was: permanent layer OFF)."""
    global _PEM_COOLDOWN_UNTIL
    _PEM_COOLDOWN_UNTIL = time.monotonic() + _PEM_COOLDOWN_S
    logger.warning("premium emoji cooldown %ss (%s) - normal emojis "
                   "continue, auto-retry after cooldown",
                   _PEM_COOLDOWN_S, str(reason)[:90])


def _pem_hot() -> bool:
    """True while the premium layer may wrap (active + not cooling)."""
    return _PEM_ACTIVE and time.monotonic() >= _PEM_COOLDOWN_UNTIL


def pem(s: str) -> str:
    """Wrap known emojis in premium <tg-emoji> tags.
    Idempotent, code-span safe, instantly off when _PEM_ACTIVE is False.
    v9.36: dead IDs are skipped per-ID (never a global kill) and a
    cooldown pauses wrapping without ending the layer."""
    if not s or "<tg-emoji" in s or not _PEM_RE.search(s):
        return s
    if not _pem_hot():
        return s
    parts = _PEM_CODE_SPLIT.split(s)
    out = []
    for p in parts:
        if p.startswith(("<code", "<pre")):
            out.append(p)
        else:
            out.append(_PEM_RE.sub(
                lambda m: (_PEM_ALT.get(m.group(1)) or m.group(1))
                if _PEMOJI.get(m.group(1)) in _PEM_DEAD
                else '<tg-emoji emoji-id="%s">%s</tg-emoji>'
                     % (_PEMOJI[m.group(1)],
                        _PEM_ALT.get(m.group(1), m.group(1))), p))
    return "".join(out)


def pem_strip(s: str) -> str:
    """Remove premium tags, keep the fallback emoji (safe downgrade)."""
    return _PEM_TAG_RE.sub(r"\1", s)


def _pem_tag(e: str) -> str:
    """One premium tag (v9.33: boot no longer sends the numbered card -
    the helper stays for tooling/tests)."""
    return '<tg-emoji emoji-id="%s">%s</tg-emoji>' % (
        _PEMOJI[e], _PEM_ALT.get(e, e))


async def _pemoji_selftest(bot) -> bool:
    """v9.36 SILENT boot check - sends NOTHING. Every premium ID is
    validated through the READ-ONLY getCustomEmojiStickers API.
    v9.36 HEALING SEMANTICS (owner bug: one dead ID used to kill the
    WHOLE layer until the next clean restart):
      - some IDs dead  -> only those are pruned into _PEM_DEAD, the
        layer STAYS ON with the still-alive IDs;
      - every ID dead  -> layer OFF (the heal loop can revive it later);
      - API hiccup / empty response -> NOT a verdict, layer unchanged.
    The runtime net in _pem_send stays as the second line of defence."""
    global _PEM_ACTIVE
    ids = [i for i in dict.fromkeys(_PEMOJI.values()) if i]
    if not ids:
        _PEM_ACTIVE = False
        return False
    try:
        got = await bot.get_custom_emoji_stickers(custom_emoji_ids=ids)
        alive = {getattr(s, "custom_emoji_id", None)
                 for s in (got or [])
                 if getattr(s, "custom_emoji_id", None)}
    except Exception as e:
        # API hiccup / a bot stub without the method: keep the layer ON -
        # the runtime net handles any real rejection later.
        logger.info("premium emoji check skipped (no send): %s", str(e)[:80])
        return True
    if not alive:
        # empty/odd response (test stub, or the API returned nothing
        # usable) is NOT a verdict - keep the layer unchanged; the
        # runtime net stays the final authority on real sends.
        logger.info("premium emoji check: no sticker data - layer "
                    "unchanged (no send)")
        return True
    dead = [i for i in ids if i not in alive]
    _PEM_DEAD.clear()
    _PEM_DEAD.update(dead)
    if len(dead) == len(ids):
        _PEM_ACTIVE = False
        logger.warning("premium emoji: ALL %d ids dead -> layer OFF "
                       "(heal loop will re-probe every %ss)",
                       len(ids), _PEM_COOLDOWN_S)
        return False
    if dead:
        logger.warning("premium emoji: %d/%d ids dead (e.g. %s) -> only "
                       "those pruned, layer STAYS ON with %d alive ids",
                       len(dead), len(ids), str(dead[0])[:20],
                       len(alive))
    _PEM_ACTIVE = True
    return True


async def _pem_heal_loop(app):
    """v9.36 SELF-HEAL: every _PEM_COOLDOWN_S a READ-ONLY re-probe of
    every premium ID. Dead IDs come back to life (owner renewed Premium,
    pack restored) -> revived instantly, NO restart needed; alive IDs
    turned dead -> pruned mid-run. Silent: no message is ever sent."""
    global _PEM_ACTIVE, _PEM_COOLDOWN_UNTIL, _BICONS_COOLDOWN_UNTIL
    while True:
        try:
            await asyncio.sleep(_PEM_COOLDOWN_S)
            ids = [i for i in dict.fromkeys(_PEMOJI.values()) if i]
            if not ids:
                continue
            got = await app.bot.get_custom_emoji_stickers(
                custom_emoji_ids=ids)
            alive = {getattr(s, "custom_emoji_id", None)
                     for s in (got or [])
                     if getattr(s, "custom_emoji_id", None)}
            if not alive:
                continue            # empty/odd response is NOT a verdict
            dead = {i for i in ids if i not in alive}
            prev_dead, was_active = set(_PEM_DEAD), _PEM_ACTIVE
            _PEM_DEAD.clear()
            _PEM_DEAD.update(dead)
            _PEM_ACTIVE = True      # at least one alive -> premium is on
            # v9.37: a healthy probe REVIVES EVERYTHING - the message
            # layer AND button icons leave their cooldowns at once,
            # so premium self-restores mid-run without any restart.
            _PEM_COOLDOWN_UNTIL = 0.0
            _BICONS_COOLDOWN_UNTIL = 0.0
            if dead != prev_dead or not was_active:
                logger.info("premium emoji heal: %d/%d ids alive, %d "
                            "pruned -> layer refreshed (was %s)",
                            len(alive), len(ids), len(dead),
                            "OFF" if not was_active else "ON")
        except asyncio.CancelledError:
            raise
        except Exception as e:
            logger.info("premium emoji heal skipped: %s", str(e)[:80])


def _pem_verify_entities(resp, text: str):
    """v9.36 STRIP DETECTOR (zero extra sends): after a real send of a
    tg-emoji text, the RETURNED Message object tells the truth - if the
    accepted message carries NO custom_emoji entity, Telegram silently
    stripped the premium tags (bot eligibility / dead IDs) and we open a
    cooldown instead of retrying premium on every single send.
    Odd/unknown response objects (True, None, stubs) give no verdict."""
    if "<tg-emoji" not in text:
        return
    if time.monotonic() < _PEM_COOLDOWN_UNTIL:
        return
    ents = list(getattr(resp, "entities", None) or [])
    if not ents:
        return                       # unknown/stub response -> no verdict
    if not any(getattr(e, "type", "") == "custom_emoji" for e in ents):
        _pem_cool("Telegram stripped premium entities on send - bot may "
                  "lack custom-emoji eligibility (Fragment username / "
                  "owner Premium); auto-retries later")


async def _pem_send(sendfn, text: str, **kw):
    """v9.36 safety net: send/edit; on ANY rejection of a premium-tagged
    text, retry once with the tags stripped - the user ALWAYS gets the
    message. The old matcher only recognised parse/entity errors, so a
    raw "CUSTOM_EMOJI_INVALID" rejection re-raised, crashed the handler
    AND took down the err_generic card with it -> users saw NOTHING
    (owner bug: ~40% of users dead on /start). Cooldown replaces the
    old permanent layer OFF; the returned Message is also checked for
    silently-stripped entities (v9.36 eligibility detector)."""
    global _BICONS_ACTIVE
    try:
        resp = await sendfn(text=text, **kw)
        _pem_verify_entities(resp, text)
        return resp
    except BadRequest as e:
        emsg = str(e).lower()
        rm = kw.get("reply_markup")
        if ("reply_markup" in kw and rm is not None and _bicons_on()
                and _markup_has_icons(rm)
                and ("markup" in emsg or "icon" in emsg
                     or ("parse" in emsg and "<tg-emoji" not in text))):
            _bicons_cool(str(e))    # v9.37: cooldown, never permanent
            logger.warning("button icons rejected (%s) -> icons cooldown, "
                           "plain buttons continue", str(e)[:80])
            kw = dict(kw, reply_markup=strip_button_icons(rm))
            return await sendfn(text=text, **kw)
        if "<tg-emoji" in text:
            # v9.37: the message must NEVER be lost to a premium tag ->
            # strip + retry on ANY rejection. Cooldown ONLY when the
            # error itself is emoji/entity-caused (a real premium-layer
            # problem); any other BadRequest (chat, markup, flood...)
            # strips this one message and leaves the layer hot - an
            # unrelated error can never flatten every premium emoji
            # again (owner bug: "sare premium emoji hatt gaye").
            if any(w in emsg for w in ("custom_emoji", "emoji",
                                       "entity", "parse")):
                _pem_cool(str(e))
            return await sendfn(text=pem_strip(text), **kw)
        raise


# --------------------------------------------------------------------------- #
#  v9.18 PREMIUM BUTTON ICONS (Bot API 9.4+ icon_custom_emoji_id)
#  OFFICIAL TELEGRAM RULE (core.telegram.org/api/bots/buttons, verified
#  live 2026-09): a button icon_custom_emoji_id renders only when the bot
#  "purchased additional usernames on Fragment, or the bot's owner has an
#  active Telegram Premium subscription" - and the viewer needs a recent
#  Telegram app. The server ACCEPTS the send either way; old clients /
#  old PTB builds degrade to the plain Unicode label, so the boot
#  self-test below now says LOUDLY which side is off (v9.31 diagnosis).
#  - Official field on KeyboardButton AND InlineKeyboardButton: the owner's
#    premium custom emoji renders BEFORE the button text for premium
#    viewers; everyone else sees the button exactly as before.
#  - Icons reuse the SAME 47-ID owner pack as the messages, plus one alias:
#    the emoji Back-arrow (U+2B05) shows the owner's left-arrow icon (#46).
#  - Attached centrally inside _kb() / _ikb() -> EVERY keyboard in the bot
#    (user + admin, reply + inline) is covered; button TEXTS never change,
#    so text routing and menu matching stay 100% identical.
#  - v9.33 SILENT BOOT: nothing is sent to anyone at boot - the layer
#    state comes from read-only API probes (see _bicons_selftest); any
#    runtime Telegram rejection flips _BICONS_ACTIVE off -> plain
#    buttons, zero user-facing errors.
# --------------------------------------------------------------------------- #
_BICON_ALIAS = {"\u2B05\uFE0F": "5165824283800241035"}  # Back -> owner arrow #46
_BICON = dict(_PEMOJI)
_BICON.update(_BICON_ALIAS)
_BICON_RE = re.compile("(" + "|".join(re.escape(e) for e in
                                      sorted(_BICON, key=len, reverse=True)) + ")")

# --------------------------------------------------------------------------- #
#  v9.19 PER-BUTTON OWNER ICON MAP (88 buttons, owner-assigned IDs)
#  Numbering = the owner's A-to-Z 88-button inventory worksheet.
#  Resolution order per button (see _resolve_bicon):
#    1. callback EXACT   (language picker lang:xx)
#    2. callback PREFIX  (deposit amount presets dep:amt:*)
#    3. keyboard map FULL TEXT (admin English labels, e.g. both 💰 buttons)
#    4. keyboard map LEADING EMOJI (i18n safe - works in all 13 languages)
#    5. message-pack fallback (_BICON) - never breaks older screens
#  Per-keyboard maps let the same label carry different icons on different
#  screens (two "Admin Panel" backs, Telegram buy vs Telegram stock).
# --------------------------------------------------------------------------- #
_BIC_BACK  = "5352759161945867747"   # 23-25,41-43,46,47,60,69,72,75 ALL Back
_BIC_X     = "5976657231033146983"   # 37-39,61,63,77,86,88 Cancel/Reject/Keep
_BIC_OK    = "6336882627844251006"   # 22,36,76 Buy / I PAID / Approve
_BIC_WA    = "5334998226636390258"   # 19,67,70 green WhatsApp (all screens)
_BIC_TG    = "6237748318726790570"   # 20,71 Telegram buy-type + set-rate
_BIC_TGST  = "5330237710655306682"   # 68 Telegram Stock (Add-Stock picker)
_BIC_USD   = "5197434882321567830"   # 28-31 $ amount presets
_BIC_MREF  = "5201691993775818138"   # 45,59 Refund + Manage Refund
_BIC_RESET = "5445267414562389170"   # 83,85,87 Reset/Continue/DELETE NOW

# 1-5 + refer: user main menu (reply) - i18n labels, leading-emoji keys
_BIC_MAIN = {
    "\U0001F6D2": "5440841102871517055",            # 1  Buy Number
    "\U0001F464": "5287521623786694265",            # 2  Profile
    "\U0001F4B3": "5287538468648424441",            # 3  Deposit
    "\U0001F4AC": "5289784010694762962",            # 4  Support
    "\U0001F4F1": "6264546492292273861",            # 8  Active Numbers (v9.27)
    "\U0001F6E0\uFE0F": "6255693594032605539",      # 5  Admin Panel (main menu)
    "\U0001F381": REFER_EMOJI_ID,                   # v9.24 Refer & Earn
    "\U0001F4E6": "6023639019290630537",            # v9.34 Bulk Buy (top row, box icon)
}
# 6-18: language picker - resolved by callback_data exact match
_BIC_CB_EXACT = {
    "lang:en": "5293993521026453119",               # 6  English
    "lang:bn": "5291824687096027834",               # 7  Bangla
    "lang:ur": "5291825606219029010",               # 8  Urdu
    "lang:zh": "5294068833277990704",               # 9  Chinese
    "lang:ar": "5294163983983463099",               # 10 Arabic
    "lang:id": "5433884376838454074",               # 11 Indonesia
    "lang:tr": "5293993400767367408",               # 12 Turkce
    "lang:ru": "5294335323113807278",               # 13 Russian
    "lang:fa": "5294220170745630736",               # 14 Farsi
    "lang:pt": "5294436555492973610",               # 15 Portugues
    "lang:es": "5294513087515216901",               # 16 Espanol
    "lang:sw": "5292111852904416801",               # 17 Kiswahili
    "lang:hi": "5291933173674957761",               # 18 Hindi
}
_BIC_CB_PRE = (("dep:amt:", _BIC_USD),)             # 28-31 $ presets
# 19-25: buy flow (inline, i18n labels)
_BIC_BUY_TYPE = {
    "\U0001F7E2": _BIC_WA,                          # 19  WhatsApp
    "\U0001F535": _BIC_TG,                          # 20  Telegram
    "\u2B05\uFE0F": _BIC_BACK,                      # 23  Back (buy type)
}
_BIC_COUNTRY = {
    "\U0001F1FA\U0001F1F8": "5224321781321442532",  # 21  USA (user + admin)
    "\u2B05\uFE0F": _BIC_BACK,                      # 24  Back (country)
}
_BIC_BUY_CONFIRM = {
    "\u2705": _BIC_OK,                              # 22  Buy — $X.XX
    "\u2B05\uFE0F": _BIC_BACK,                      # 25  Back (confirm)
}
# 26-43: deposit flow (inline, i18n labels)
_BIC_DEP_MENU = {
    "\U0001F4B5": "5285220062481894208",            # 26  New Deposit
    "\U0001F4DC": "5411090199419580352",            # 27  History
    "\u2B05\uFE0F": _BIC_BACK,                      # 41  Back (dep menu)
}
_BIC_DEP_AMT = {
    "\u270F\uFE0F": "6071226479541230640",          # 32  Custom Amount
    "\u2B05\uFE0F": _BIC_BACK,                      # 42  Back (amount)
}
_BIC_DEP_NET = {
    "\U0001F3E6": "5420232672964275159",            # v9.32 Binance Pay (owner emoji ID)
    "\U0001F7E1": "5190735192901325809",            # 35  USDT BEP-20
    "\u2B05\uFE0F": _BIC_BACK,                      # 43  Back (network)
}
_BIC_DEP_WAIT = {
    "\u2705": _BIC_OK,                              # 36  I PAID — Send TXID
    "\u274C": _BIC_X,                               # 37  Cancel Deposit
}
_BIC_DEP_CANCEL = {"\u274C": _BIC_X}                # 38,39 Cancel Deposit
_BIC_NAV = {"\u2B05\uFE0F": _BIC_BACK}              # 47  generic inline Back
_BIC_INSUF = {
    "\U0001F4B3": "5316953080456057649",            # 40  Deposit (insufficient)
    "\u2B05\uFE0F": _BIC_BACK,                      # 47  Back
}
# 44-47: OTP receipt (inline, i18n labels)
_BIC_OTP = {
    "\U0001F4E9": "6275811074818184964",            # 44  Get OTP
    "\u2B05\uFE0F": _BIC_BACK,                      # 46  Back (receipt)
}
# 48-60: admin panel (reply, English BTN_* labels) - text keys first so the
# two 💰 buttons (Pending Deposits / Total Deposit) keep their own icons
_BIC_ADMIN = {
    BTN_CHANNELS: "5947490155370650280",            # v9.23 Manage Channels
    BTN_PENDING: "5976827006795389445",             # 50  Pending Deposits
    BTN_ALL_BAL: "5285220062481894208",             # v9.38 All User Balance (owner pack, live)
    "\U0001F4E6": "6023639019290630537",            # 48  Add Stock (+ v9.34 Bulk Manage - same box icon)
    "\U0001F4CA": "5203993413346680064",            # 49  Stock Stats
    "\u270F\uFE0F": "6219707811111115716",          # 52  Modify User
    "\U0001F4C8": "4956599758044005301",            # 53  Statistics
    "\u2699\uFE0F": "6098399122715318470",          # 54  Set Rate
    "\U0001F4E3": "5947490155370650280",            # 55  Broadcast
    "\U0001F511": "6068898860669870535",            # 56  Set Wallet
    "\U0001F512": "5852487725051023314",            # 58  Ban/Unban
    "\U0001F4B8": _BIC_MREF,                        # 59  Manage Refund
    "\u2B05\uFE0F": _BIC_BACK,                      # 60  Back (panel exit)
    BTN_REFER_MGMT: REFER_EMOJI_ID,                 # v9.24 Manage Reffer
}
# 61-66: admin input + refund menus (reply, English labels)
_BIC_ADMIN_INPUT = {
    "\u274C": _BIC_X,                               # 61  Cancel (input)
    "\U0001F6E0\uFE0F": "5019276890104398625",      # 62  Admin Panel (input)
}
# v9.27 refund hub (reply, English labels) - icons reuse the owner pack
_BIC_ADMIN_REFUND = {
    "\U0001F522": "6068689511078960547",            # Check Number (65)
    "\U0001F4B8": _BIC_MREF,                        # Refund Send / Manage Refund
    "\U0001F501": "6136198451282581752",            # Chek Number & Refund (66)
    "\u274C": _BIC_X,                               # Cancel (refund hub)
    "\U0001F6E0\uFE0F": "5354837664124153264",      # Admin Panel (refund hub)
}
# 67-88: admin inline pickers / cards / report / reset
_BIC_ADD_TYPE = {
    "\U0001F7E2": _BIC_WA,                          # 67  WhatsApp Stock
    "\U0001F535": _BIC_TGST,                        # 68  Telegram Stock
    "\u2B05\uFE0F": _BIC_BACK,                      # 69  Back (Add Stock)
}
_BIC_RATE = {
    "\U0001F7E2": _BIC_WA,                          # 70  WhatsApp — $rate
    "\U0001F535": _BIC_TG,                          # 71  Telegram — $rate
    "\u2B05\uFE0F": _BIC_BACK,                      # 72  Back (Set Rate)
}
_BIC_BAN = {
    "\U0001F512": "5852487725051023314",            # 73  Ban User
    "\U0001F513": "5852849902463225394",            # 74  Unban User
    "\u2B05\uFE0F": _BIC_BACK,                      # 75  Back (Ban)
}
_BIC_APPROVE = {
    "\u2705": _BIC_OK,                              # 76  Approve
    "\u274C": _BIC_X,                               # 77  Reject
}
_BIC_USER = {
    "\U0001F4B5": "6156816141139319335",            # 78  Modify Balance
    "\u2B05\uFE0F": "5967814249852965678",          # 79  Admin Panel (user card)
}
_BIC_REPORT = {
    "\U0001F4C5": "5287606810168028257",            # 80  Today
    "\U0001F555": "5017179932451668652",            # 81  Yesterday
    "\U0001F5D3\uFE0F": "5028418466000930064",      # 82  Last 7 Days
    "\u267B\uFE0F": _BIC_RESET,                     # 83  Reset History
    "\u2B05\uFE0F": "5116599934203724812",          # 84  Admin Panel (report)
}
_BIC_RESET_KB = {
    "\u267B\uFE0F": _BIC_RESET,                     # 85,87 Continue / DELETE NOW
    "\u274C": _BIC_X,                               # 86,88 Keep Data (both steps)
}
# v9.23: force-join (user) + Manage Channels (admin) icon maps
_BIC_FJOIN = {
    "\u2709\uFE0F": JOIN_EMOJI_ID,                 # JOIN CHANNEL / JOIN GROUP
    "\u2705": _BIC_OK,                             # Verify
}
_BIC_CH_TYPE = {
    "\U0001F4E3": "5947490155370650280",           # Public (owner megaphone)
    "\U0001F512": "5206432422194849059",           # Private (owner lock)
    "\u2B05\uFE0F": _BIC_BACK,                    # Back
}
_BIC_CHANNELS = {
    BTN_CH_ADD: "6023639019290630537",              # Add Channel
    BTN_CH_REMOVE: "6267039884016358504",           # Remove Channel
    BTN_CH_LIST: "5165830112070863167",             # List Channels
    "\U0001F6E0\uFE0F": "5354837664124153264",     # Admin Panel (exit)
    "\u274C": _BIC_X,                              # Cancel
}
# v9.24: Manage Reffer (admin) icon map - same clean icon-text mode
_BIC_REFER = {
    BTN_REFER_MGMT: REFER_EMOJI_ID,                 # Manage Reffer (panel row)
    BTN_REF_PRICE: _BIC_USD,                        # Set Reffer Price ($ icon)
    BTN_REF_VIP: "5287521623786694265",             # Manage VIP (person icon)
    BTN_REF_VIP_ADD: "6023639019290630537",         # Add VIP (package/add icon)
    BTN_REF_VIP_REM: "6267039884016358504",         # Remove VIP (cross icon)
    BTN_REF_VIP_LIST: "5165830112070863167",        # VIP List (clipboard icon)
    "\U0001F504": "5935950110822242301",           # ON/OFF toggle (repeat icon)
    "\u274C": _BIC_X,                              # Cancel
    "\U0001F6E0\uFE0F": "5354837664124153264",     # Admin Panel (exit)
}
_BIC_ALL_MAPS = (_BIC_MAIN, _BIC_BUY_TYPE, _BIC_COUNTRY, _BIC_BUY_CONFIRM,
                 _BIC_DEP_MENU, _BIC_DEP_AMT, _BIC_DEP_NET, _BIC_DEP_WAIT,
                 _BIC_DEP_CANCEL, _BIC_NAV, _BIC_INSUF, _BIC_OTP,
                 _BIC_ADMIN, _BIC_ADMIN_INPUT, _BIC_ADMIN_REFUND,
                 _BIC_ADD_TYPE, _BIC_RATE, _BIC_BAN, _BIC_APPROVE,
                 _BIC_USER, _BIC_REPORT, _BIC_RESET_KB,
                 _BIC_FJOIN, _BIC_CH_TYPE, _BIC_CHANNELS, _BIC_REFER)
# leading-emoji regex = message pack + every per-keyboard emoji key
_BIC_KEY_SET = set(_BICON)
for _m in _BIC_ALL_MAPS:
    for _k in _m:
        if len(_k) <= 4:          # emoji keys only (text keys are longer)
            _BIC_KEY_SET.add(_k)
_BIC_KEY_RE = re.compile("(" + "|".join(re.escape(e) for e in
                                        sorted(_BIC_KEY_SET, key=len,
                                               reverse=True)) + ")")

# --------------------------------------------------------------------------- #
#  v9.22 ICON-TEXT MODE: a button that carries the owner's custom icon
#  shows that icon INSTEAD of its normal unicode emoji (no double emoji).
#  _LEAD_EMOJI_RE matches ONE leading emoji cluster (flag pair / SMP
#  pictograph / BMP arrow-or-symbol + VS16, skin tones, ZWJ sequences).
#  _bt() strips it from a label; btn_eq() compares button labels
#  emoji-tolerantly so BOTH keyboards route 100% correctly:
#    - new icon keyboards (stripped labels, e.g. "Buy Number")
#    - old emoji keyboards still on screen (e.g. "🛒 Buy Number")
#  in every one of the 13 languages.
# --------------------------------------------------------------------------- #
_LEAD_EMOJI_RE = re.compile(
    "^(?:"
    "[\U0001F1E6-\U0001F1FF]{2}"                        # flag pair
    "|[\U0001F000-\U0001FAFF]"                          # SMP pictographs
    "|[\u2190-\u2BFF\u3030\u303D\u3297\u3299]"          # BMP arrows/symbols
    ")[\uFE0E\uFE0F]?(?:[\U0001F3FB-\U0001F3FF])?"      # VS + skin tone
    "(?:\u200D(?:[\U0001F000-\U0001FAFF]"
    "|[\u2190-\u2BFF\u3030\u303D\u3297\u3299])"
    "[\uFE0E\uFE0F]?(?:[\U0001F3FB-\U0001F3FF])?)*"     # ZWJ sequence
)


def _bt(s: str) -> str:
    """Button label without ONE leading emoji cluster (v9.22 icon-text).
    Labels that do not start with an emoji are returned unchanged."""
    return _LEAD_EMOJI_RE.sub("", s or "", count=1).strip()


def btn_eq(text: str, label: str) -> bool:
    """Emoji-tolerant button-text equality (v9.22, icon-text safe).
    True when `text` is the label exactly OR equals it once both sides
    lose their leading emoji - so stripped-icon keyboards and old
    emoji keyboards both keep working everywhere."""
    if not text or not label:
        return False
    if text == label:
        return True
    return _bt(text) == _bt(label)


def _ptb_version() -> str:
    """python-telegram-bot version string (v9.31 icon diagnosis - the
    module object is not bound at top level, so import lazily)."""
    try:
        import telegram as _tg_mod
        return str(getattr(_tg_mod, "__version__", "?"))
    except Exception:
        return "?"


def _bicons_supported() -> bool:
    """PTB feature detect: does this build accept the 9.4 icon field?"""
    try:
        InlineKeyboardButton("t", callback_data="c", icon_custom_emoji_id="1")
        KeyboardButton("t", icon_custom_emoji_id="1")
        return True
    except Exception:
        return False


_BICONS_ACTIVE = _bicons_supported()
# v9.37: button icons can NEVER die permanently either. A runtime
# rejection now opens a COOLDOWN (auto-retried after _PEM_COOLDOWN_S
# and cleared by the heal loop) instead of the old permanent flag
# flip - one bad event can no longer flatten every menu icon in the
# bot until a restart (owner bug: "sare premium emoji hatt gaye").
_BICONS_COOLDOWN_UNTIL = 0.0


def _bicons_cool(reason: str):
    """v9.37: 10-min button-icon cooldown (was: permanent OFF)."""
    global _BICONS_COOLDOWN_UNTIL
    _BICONS_COOLDOWN_UNTIL = time.monotonic() + _PEM_COOLDOWN_S
    logger.warning("button icons cooldown %ss (%s) - plain buttons "
                   "continue, auto-retry after cooldown",
                   _PEM_COOLDOWN_S, str(reason)[:90])


def _bicons_on() -> bool:
    """True while button icons may attach (capability + not cooling)."""
    return _BICONS_ACTIVE and time.monotonic() >= _BICONS_COOLDOWN_UNTIL


def _resolve_bicon(btn, icons=None):
    """v9.19 owner icon for ONE button.
    Order: callback-exact (lang picker) > callback-prefix (amount presets)
    > keyboard map full-text (admin labels) > keyboard map leading emoji
    (i18n safe) > message-pack fallback (_BICON).
    v9.36: an ID sitting in the dead-graveyard resolves to None - that
    ONE button shows its plain unicode emoji, the rest stay premium."""
    if not _bicons_on():          # v9.37: capability + cooldown gate
        return None
    iid = _resolve_bicon_raw(btn, icons)
    if iid and iid in _PEM_DEAD:
        return None
    return iid


def _resolve_bicon_raw(btn, icons=None):
    """The ID chain without the dead-check (kept separate so the
    graveyard filter in _resolve_bicon can never be bypassed)."""
    cb = getattr(btn, "callback_data", None)
    if cb:
        got = _BIC_CB_EXACT.get(cb)
        if got:
            return got
        for _pre, _iid in _BIC_CB_PRE:
            if cb.startswith(_pre):
                return _iid
    text = getattr(btn, "text", None)
    if not text:
        return None
    ts = text.strip()
    if icons:
        got = icons.get(ts)
        if got:
            return got
    m = _BIC_KEY_RE.match(ts)
    if not m:
        return None
    e = m.group(1)
    if icons:
        got = icons.get(e)
        if got:
            return got
    return _BICON.get(e)


def _attach_button_icons(rows, icons=None):
    """Attach icon_custom_emoji_id per button (v9.19 owner 88-ID map).
    v9.22 ICON-TEXT MODE: when an icon is attached, the button's normal
    leading unicode emoji is REMOVED from the label - the premium icon
    replaces it, so a button never shows two emojis.
    Called from _kb()/_ikb() only.
    PTB buttons are frozen, so a matching button is REBUILT via to_dict()."""
    global _BICONS_ACTIVE
    if not _bicons_on() or not rows:   # v9.37: cooldown-aware gate
        return
    for ri, row in enumerate(rows):
        if not row:
            continue
        new_row = []
        for btn in row:
            try:
                icon = _resolve_bicon(btn, icons)
            except Exception:
                icon = None
            if icon and not getattr(btn, "icon_custom_emoji_id", None):
                try:
                    d = btn.to_dict()
                    d["icon_custom_emoji_id"] = icon
                    _nt = _bt(d.get("text") or "")   # v9.22: strip old emoji
                    if _nt:
                        d["text"] = _nt   # empty -> keep original (never blank)
                    btn = btn.__class__(**d)
                except Exception:
                    _bicons_cool("button rebuild failed")   # v9.37
                    return
            new_row.append(btn)
        rows[ri] = new_row


def _kb_rows(markup):
    """Button rows of either markup type."""
    return (markup.inline_keyboard if isinstance(markup, InlineKeyboardMarkup)
            else getattr(markup, "keyboard", None))


def _markup_has_icons(markup) -> bool:
    try:
        for row in (_kb_rows(markup) or ()):
            for b in row or ():
                if getattr(b, "icon_custom_emoji_id", None):
                    return True
    except Exception:
        pass
    return False


def strip_button_icons(markup):
    """Rebuild a markup without icon fields (safety-net downgrade)."""
    try:
        rows = _kb_rows(markup)
        if rows is None:
            return None
        new_rows = []
        for row in rows:
            nr = []
            for b in row or ():
                d = b.to_dict()
                d.pop("icon_custom_emoji_id", None)
                nr.append(b.__class__(**d))
            new_rows.append(nr)
        if isinstance(markup, InlineKeyboardMarkup):
            return InlineKeyboardMarkup(new_rows)
        return ReplyKeyboardMarkup(
            new_rows, resize_keyboard=True, is_persistent=False,
            input_field_placeholder=getattr(markup,
                                            "input_field_placeholder", None))
    except Exception:
        return None


def _bicon_test_inline_kb() -> InlineKeyboardMarkup:  # kept: test_button_icons asserts these IDs via the SAME builder
    return _ikb([
        [InlineKeyboardButton(BTN_BUY, callback_data="nav:home",
                              style=KeyboardButtonStyle.SUCCESS),
         InlineKeyboardButton(BTN_DEPOSIT, callback_data="nav:home",
                              style=KeyboardButtonStyle.PRIMARY)],
        [InlineKeyboardButton(BTN_BACK, callback_data="nav:home",
                              style=KeyboardButtonStyle.DANGER)],
    ], dict(_BIC_MAIN, **{"\u2B05\uFE0F": _BIC_BACK}))


def _bicon_test_reply_kb() -> ReplyKeyboardMarkup:
    """v9.33: boot no longer SENDS these - the builders survive only as
    icon-map regression fixtures for test_button_icons."""
    return _kb(
        [[KeyboardButton(BTN_PROFILE, style=KeyboardButtonStyle.PRIMARY),
          KeyboardButton(BTN_SUPPORT, style=KeyboardButtonStyle.PRIMARY)]],
        "Premium button icon test", _BIC_MAIN,
    )


async def _bicons_selftest(bot) -> bool:
    """v9.36 SILENT boot check - sends NOTHING. Two read-only probes
    decide the layer:
      1) capability: _BICONS_ACTIVE was set at import from the PTB
         feature probe (does this build accept icon_custom_emoji_id?)
      2) liveness: every mapped icon ID must resolve through the
         READ-ONLY getCustomEmojiStickers API.
    v9.36 HEALING SEMANTICS (same as the message layer): SOME ids dead
    -> only those pruned into _PEM_DEAD, icons stay ON for the alive
    ones; ALL ids dead -> icons OFF; empty/odd response -> no verdict.
    The runtime net in _pem_send stays the final authority on real
    sends - a Telegram rejection there auto-strips icons silently."""
    global _BICONS_ACTIVE
    if not _BICONS_ACTIVE:
        logger.warning("button icons OFF: PTB %s lacks the icon field - "
                       "fix once on the VPS: pip3 install "
                       "--break-system-packages "
                       "'python-telegram-bot[job-queue]==22.8'",
                       _ptb_version())
        return False
    ids = [i for i in dict.fromkeys(_BICON.values()) if i]
    if not ids:
        return True
    try:
        got = await bot.get_custom_emoji_stickers(custom_emoji_ids=ids)
        alive = {getattr(s, "custom_emoji_id", None)
                 for s in (got or [])
                 if getattr(s, "custom_emoji_id", None)}
    except Exception as e:
        # API hiccup / a bot stub without the method: keep icons ON -
        # the runtime net handles any real rejection later.
        logger.info("button icon check skipped (no send): %s", str(e)[:80])
        return True
    if not alive:
        # empty/odd response (test stub, or the API returned nothing
        # usable) is NOT a verdict - keep icons unchanged; the runtime
        # net stays the final authority on real sends.
        logger.info("button icon check: no sticker data - icons "
                    "unchanged (no send)")
        return True
    dead = [i for i in ids if i not in alive]
    _PEM_DEAD.update(dead)          # v9.36: per-ID graveyard (shared)
    if len(dead) == len(ids):
        _bicons_cool("ALL %d icon ids dead" % len(ids))   # v9.37
        return False
    if dead:
        logger.warning("button icons: %d/%d icon ids dead (e.g. %s) -> "
                       "only those pruned, icons STAY ON for %d alive",
                       len(dead), len(ids), str(dead[0])[:20], len(alive))
    return True


_LANG_CACHE = {}   # telegram_id -> lang code (set_user_lang keeps it fresh)


def lang_of(user) -> str:
    """Language of a user ROW dict (None/'' -> English)."""
    try:
        return (user or {}).get("lang") or DEFAULT_LANG
    except Exception:
        return DEFAULT_LANG


def t(lng: str, key: str, **kw) -> str:
    """Translate one string. Unknown lang/key -> EN -> key. Safe format.
    First arg named `lng` so a {lang} placeholder can never collide."""
    d = LANGS.get(lng) or LANGS[DEFAULT_LANG]
    s = d.get(key) or LANGS[DEFAULT_LANG].get(key) or key
    if kw:
        try:
            s = s.format(**kw)
        except Exception:
            pass
    if key not in _PEM_PLAIN and not key.startswith("btn_"):
        s = pem(s)   # v9.17: premium emojis on every user-side message
    return s


async def get_user_lang(uid) -> str:
    """Cached language lookup (one DB read per user, then memory-fast)."""
    if uid in _LANG_CACHE:
        return _LANG_CACHE[uid]
    row = await get_user(uid)
    lang = (row or {}).get("lang") or DEFAULT_LANG
    if len(_LANG_CACHE) > 60000:
        _LANG_CACHE.clear()
    _LANG_CACHE[uid] = lang
    return lang


async def set_user_lang(uid, lang: str):
    """Persist the user's language + refresh the cache instantly."""
    if lang not in LANG_CODES:
        lang = DEFAULT_LANG
    async with adb() as db:
        await db.execute(
            "UPDATE users SET lang=?, updated_at=datetime('now') "
            "WHERE telegram_id=?", (lang, uid))
    _LANG_CACHE[uid] = lang


def lang_picker_kb() -> InlineKeyboardMarkup:
    """Language picker: flag + native-name buttons, 2 per row (lang:<code>)."""
    rows, pair = [], []
    for code, name, flag in LANGUAGES:
        pair.append(InlineKeyboardButton(f"{flag} {name}",
                                         callback_data=f"lang:{code}"))
        if len(pair) == 2:
            rows.append(pair)
            pair = []
    if pair:
        rows.append(pair)
    return _ikb(rows)


def lang_pick_text() -> str:
    """Picker screen: title + hint (English base, buttons self-explain)."""
    return (f"{t(DEFAULT_LANG, 'lang_pick_title')}\n"
            f"{DIV}\n"
            f"{t(DEFAULT_LANG, 'lang_pick_hint')}")


# States where any non-button text is treated as user input.
# NOTE: menu buttons are handled BEFORE these states, which fixes the old
# bug where a menu tap was saved as TX hash / phone / URL etc.
INPUT_STATES = {
    "awaiting_txid",
    "dep_custom",
    "admin_add_phone",
    "admin_add_url",
    "admin_set_rate",
    "admin_broadcast",
    "admin_ban",
    "admin_set_wallet",
    "admin_modify_user",
    "admin_modbal",
    "admin_ch_add",   # v9.23: channel link/ID/forward input
    "admin_ref_price",        # v9.24: new per-buy commission input
    "admin_ref_vip_add_id",   # v9.24: VIP referrer chat ID input
    "admin_ref_vip_add_rate", # v9.24: VIP referrer special rate input
    "admin_bulkmanage_min",   # v9.34: bulk discount min-quantity input
    "admin_bulkmanage_disc",  # v9.34: bulk per-number discount input
    "user_bulkbuy",           # v9.31: user-side Bulk Buy quantity input
    "admin_adm",              # v9.41: Manage Admin submenu (btns+input)
    "admin_adm_add",          # v9.41: Add Admin -> ID input
    "admin_adm_rm",           # v9.41: Remove Admin -> ID input
}


def is_admin(user_id: int) -> bool:
    if user_id in ADMIN_IDS:
        return True
    # v9.41: dynamic extra admins (Manage Admin) - sync cache, boot +
    # har add/remove pe refresh hota hai.
    return user_id in _EXTRA_ADMINS


def _is_private(update) -> bool:
    """v9.23 GROUP SILENCE guard: True only for private (DM) chats.
    In groups/channels the bot never talks - no menu, no commands,
    no replies. The ONLY thing it ever posts there is an admin
    broadcast (copy_message straight into managed chats)."""
    try:
        c = update.effective_chat
        # a missing type (legacy fake updates / edge transports) counts
        # as private - real Telegram chats ALWAYS carry a type
        return c is None or getattr(c, "type", "private") == "private"
    except Exception:
        return True


def flag_of(country: str) -> str:
    for n, f in COUNTRIES:
        if n == country:
            return f
    return "\U0001F30D"


def _utcnow():
    """Naive UTC datetime (DB stores UTC) without the deprecated utcnow()."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


def country_from_button(text: str):
    """Return the country name if `text` matches a country button label.
    v9.22: emoji-tolerant - icon-stripped labels (and plain typed names)
    match too, old flag labels still match exactly."""
    s = (text or "").strip()
    if not s:
        return None
    for name, flag in COUNTRIES:
        if s == f"{flag} {name}" or s == _bt(f"{flag} {name}") or s == name:
            return name
    return None


# Track last bot messages per user so we can clean up stale menu messages
def _track_msg(context, uid, msg):
    if "bot_msgs" not in context.bot_data:
        context.bot_data["bot_msgs"] = {}
    store = context.bot_data["bot_msgs"].setdefault(uid, [])
    store.append(msg.message_id)
    if len(store) > 20:
        del store[: len(store) - 20]


async def _send_tracked(update, context, text, reply_markup, parse_mode=None):
    """Render a screen. NEVER deletes any previous message.

    - Normal text update -> reply with the given markup.
    - Inline button tap  -> EDIT the button message in place when the new
      markup is an inline keyboard (classic single-message navigation);
      otherwise send a fresh message so nothing is lost.
    """
    uid = update.effective_user.id
    pm = parse_mode or ParseMode.HTML

    if update.callback_query:
        q = update.callback_query
        if isinstance(reply_markup, InlineKeyboardMarkup):
            try:
                await _pem_send(
                    lambda text, reply_markup=None: q.edit_message_text(
                        text, parse_mode=pm, reply_markup=reply_markup),
                    text, reply_markup=reply_markup)
                _track_msg(context, uid, q.message)
                return q.message
            except BadRequest as e:
                if "not modified" in str(e).lower():
                    return q.message
                # anything else (photo message etc.) -> fall through & send
            except Exception:
                pass
        msg = await _pem_send(
            lambda text, reply_markup=None: context.bot.send_message(
                chat_id=update.effective_chat.id, text=text, parse_mode=pm,
                reply_markup=reply_markup),
            text, reply_markup=reply_markup)
        _track_msg(context, uid, msg)
        return msg

    msg = await _pem_send(
        lambda text, reply_markup=None: update.message.reply_text(
            text, parse_mode=pm, reply_markup=reply_markup),
        text, reply_markup=reply_markup)
    _track_msg(context, uid, msg)
    return msg


# --------------------------------------------------------------------------- #
#  v9.14 PERFORMANCE CORE
#  - ONE shared aiohttp session (TCP/TLS reuse for OTP poll + RPC)
#  - ONE shared SQLite connection (WAL) via adb() - keeps the old
#    `async with ... as db:` call-shape, never closes the shared conn,
#    commits on exit so a write can never be silently lost
#  - tiny TTL cache for settings reads, invalidated on admin save
# --------------------------------------------------------------------------- #
_HTTP = None              # shared aiohttp.ClientSession (lazy)
_DB_CONN = None           # shared aiosqlite.Connection (lazy)
_DB_CONN_LOOP = None
_DB_CONN_PATH = None
_SET_CACHE = {}           # settings key -> (value, monotonic ts)
_SET_CACHE_TTL = 2.0      # seconds
_TX_LOCKS = {}            # running loop -> asyncio.Lock (atomic txs)


# aiosqlite 0.22 runs its worker on a NON-daemon thread, and CPython
# joins non-daemon threads BEFORE atexit - a long-lived shared connection
# would therefore hang the process at exit. Daemonize aiosqlite's worker
# thread creation (graceful close still happens in post_shutdown /
# _release_shared_resources; the atexit hook stays as the polite path).
import aiosqlite.core as _asql_core
import threading as _threading


class _DaemonThread(_threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True


if getattr(_asql_core.Thread, "__name__", "") != "_DaemonThread":
    _asql_core.Thread = _DaemonThread


async def http_session():
    """Process-wide aiohttp session - reused everywhere, closed on shutdown."""
    global _HTTP
    if _HTTP is None or _HTTP.closed:
        _HTTP = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            connector=aiohttp.TCPConnector(
                limit=30, ttl_dns_cache=600, enable_cleanup_closed=True),
            headers={"User-Agent": "OTPHUB/9.14"},
        )
    return _HTTP


async def close_http_session():
    global _HTTP
    if _HTTP is not None and not _HTTP.closed:
        try:
            await _HTTP.close()
        except Exception:
            pass
    _HTTP = None


async def _get_shared_db():
    """The one aiosqlite connection for the whole process (WAL mode).
    Recycles automatically if the event loop or DB_PATH changed
    (keeps test harnesses and hot reloads safe)."""
    global _DB_CONN, _DB_CONN_LOOP, _DB_CONN_PATH
    loop = asyncio.get_running_loop()
    if _DB_CONN is not None and (
            _DB_CONN_LOOP is not loop or _DB_CONN_PATH != DB_PATH):
        try:
            await asyncio.wait_for(_DB_CONN.close(), timeout=1.0)
        except Exception:
            pass
        _DB_CONN = None
    if _DB_CONN is None:
        # v9.32 FIX: isolation_level=None = FULL AUTOCOMMIT. The default
        # ("") opens an implicit transaction on every write that stays
        # open until the shim's commit - and with concurrent_updates two
        # users racing (the exact "2 phones at once" load) could hit
        # "cannot start a transaction within a transaction" when one
        # coroutine's implicit transaction overlapped another's
        # BEGIN IMMEDIATE (purchase / bulk / credit engine). Autocommit
        # makes every single statement self-contained, the shim's commit
        # a harmless no-op, and the lock-protected BEGIN IMMEDIATE
        # transactions always legal - atomicity now lives exactly where
        # it was designed: inside the _tx_lock + rowcount guards.
        _DB_CONN = await aiosqlite.connect(DB_PATH, isolation_level=None)
        # v9.20: Row factory set ONCE here - every query gets name/index
        # access and interleaved coroutines can never see a bare tuple
        # row (the atomic buy used to depend on handler call order).
        _DB_CONN.row_factory = aiosqlite.Row
        await _DB_CONN.execute("PRAGMA journal_mode=WAL")
        await _DB_CONN.execute("PRAGMA synchronous=NORMAL")
        await _DB_CONN.execute("PRAGMA busy_timeout=5000")
        _DB_CONN_LOOP = loop
        _DB_CONN_PATH = DB_PATH
        _SET_CACHE.clear()
    return _DB_CONN


class _SharedDB:
    """async-with shim yielding the shared connection (never closes it)."""

    __slots__ = ()

    async def __aenter__(self):
        return await _get_shared_db()

    async def __aexit__(self, exc_type, exc, tb):
        # v9.32 FIX: never commit while an EXPLICIT transaction is open.
        # In full-autocommit mode every single statement commits itself,
        # so this commit only ever did one thing: stomp an in-flight
        # BEGIN IMMEDIATE of another concurrent coroutine (two phones
        # depositing/buying at the same moment could end each other's
        # atomic transaction mid-flight). in_transaction-gated = the
        # atomic engines own their transaction start-to-finish.
        conn = _DB_CONN
        if conn is not None and not conn.in_transaction:
            try:
                await conn.commit()
            except Exception:
                pass
        return False


def adb():
    """Drop-in replacement for a per-call connect, reusing one connection:
    `async with adb() as db:` keeps every existing call-site unchanged."""
    return _SharedDB()


def _tx_lock():
    """Serialises multi-statement transactions (BEGIN IMMEDIATE) per loop;
    single-statement reads/writes stay fully concurrent."""
    loop = asyncio.get_running_loop()
    lk = _TX_LOCKS.get(loop)
    if lk is None:
        lk = _TX_LOCKS[loop] = asyncio.Lock()
    return lk


def _atexit_release_shared_db():
    """Interpreter-exit safety net: stop the shared DB worker thread even
    when post_shutdown never ran (test harnesses, crash paths).
    aiosqlite 0.22 runs a NON-daemon worker thread - without this the
    process can hang forever at exit."""
    conn = _DB_CONN
    if conn is None:
        return
    try:
        conn.stop()          # sync: queues sqlite close + worker stop
    except Exception:
        pass


atexit.register(_atexit_release_shared_db)


async def _release_shared_resources():
    """Best-effort release of shared HTTP + DB resources (used by the
    supervisor crash path, where no event loop is running anymore)."""
    global _DB_CONN, _DB_CONN_LOOP, _DB_CONN_PATH
    await close_http_session()
    if _DB_CONN is not None:
        try:
            await asyncio.wait_for(_DB_CONN.close(), timeout=2.0)
        except Exception:
            pass
    _DB_CONN = None
    _DB_CONN_LOOP = None
    _DB_CONN_PATH = None


async def get_setting(key: str) -> str:
    now = time.monotonic()
    hit = _SET_CACHE.get(key)
    if hit is not None and now - hit[1] < _SET_CACHE_TTL:
        return hit[0]
    async with adb() as db:
        cur = await db.execute("SELECT value FROM settings WHERE key=?", (key,))
        row = await cur.fetchone()
        await cur.close()
        val = row[0] if row else DEFAULT_SETTINGS.get(key, "")
    _SET_CACHE[key] = (val, time.monotonic())
    return val


async def set_setting(key: str, value: str):
    _SET_CACHE.pop(key, None)   # admin edits apply on the very next read
    async with adb() as db:
        await db.execute(
            "INSERT INTO settings(key,value,updated_at) VALUES(?,?,datetime('now')) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=datetime('now')",
            (key, str(value)),
        )

async def bulk_disc_params():
    """v9.34: owner-configurable bulk discount (Admin Panel > Bulk
    Manage). Reads the settings (admin-set, cache-busting on write),
    falls back to the built-in defaults when unset/invalid.
    Returns (min_qty, per_number_off)."""
    mn, dp = BULK_DISCOUNT_MIN, BULK_DISCOUNT
    try:
        v = str(await get_setting("bulk_disc_min") or "").strip()
        if v:
            iv = int(float(v))
            if 2 <= iv <= 100000:
                mn = iv
    except Exception:
        pass
    try:
        v = str(await get_setting("bulk_disc_per") or "").strip()
        if v:
            fv = float(v)
            if math.isfinite(fv) and 0.0 <= fv <= 10.0:
                dp = round(fv, 4)
    except Exception:
        pass
    return mn, dp


# --------------------------------------------------------------------------- #
#  DATABASE
# --------------------------------------------------------------------------- #
async def init_db():
    # v9.32: isolation_level=None (autocommit) on this one-shot migration
    # connection too - every CREATE/ALTER commits itself, nothing can be
    # lost when the connection closes (the shimmed shared-conn commits
    # are gone by design; see _get_shared_db for the full story).
    async with aiosqlite.connect(DB_PATH, isolation_level=None) as db:
        await db.execute("PRAGMA journal_mode=WAL;")
        await db.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE NOT NULL,
                username TEXT,
                first_name TEXT,
                balance REAL DEFAULT 0.0,
                total_deposit REAL DEFAULT 0.0,
                total_spent REAL DEFAULT 0.0,
                total_purchased INTEGER DEFAULT 0,
                total_otp INTEGER DEFAULT 0,
                is_banned INTEGER DEFAULT 0,
                is_admin INTEGER DEFAULT 0,
                lang TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                updated_at TEXT DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT NOT NULL,
                otp_url TEXT NOT NULL,
                number_type TEXT NOT NULL,
                country TEXT DEFAULT 'USA',
                status TEXT DEFAULT 'available',
                otp_status TEXT DEFAULT 'pending',
                otp_code TEXT,
                added_by INTEGER,
                sold_to INTEGER,
                created_at TEXT DEFAULT (datetime('now')),
                sold_at TEXT,
                otp_fetched_at TEXT,
                refund_state TEXT,
                otp_blocked INTEGER DEFAULT 0,
                baseline_codes TEXT
            );
            CREATE TABLE IF NOT EXISTS deposits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                deposit_id TEXT UNIQUE NOT NULL,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                usdt_address TEXT,
                tx_hash TEXT,
                screenshot_file_id TEXT,
                network TEXT DEFAULT 'TRC20',
                status TEXT DEFAULT 'pending',
                group_message_id INTEGER,
                expires_at TEXT,
                confirmed_by INTEGER,
                created_at TEXT DEFAULT (datetime('now')),
                confirmed_at TEXT
            );
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id TEXT UNIQUE NOT NULL,
                user_id INTEGER NOT NULL,
                number_type TEXT NOT NULL,
                country TEXT,
                total_amount REAL NOT NULL,
                quantity INTEGER NOT NULL,
                numbers TEXT NOT NULL,
                rate_at_purchase REAL NOT NULL,
                status TEXT DEFAULT 'completed',
                created_at TEXT DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TEXT DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS rate_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rate_type TEXT,
                old_rate REAL,
                new_rate REAL,
                changed_by INTEGER,
                changed_at TEXT DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS user_states (
                user_id INTEGER PRIMARY KEY,
                state TEXT,
                data TEXT,
                updated_at TEXT DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS usdt_seen (
                hash TEXT PRIMARY KEY,
                ts INTEGER,
                value REAL,
                matched INTEGER DEFAULT 0,
                seen_at TEXT DEFAULT (datetime('now'))
            );
            """
        )
        # Safe column adds for older DBs
        for col, typedef in [("total_purchased", "INTEGER DEFAULT 0"),
                             ("total_otp", "INTEGER DEFAULT 0"),
                             ("lang", "TEXT"),
                             ("adm_modified",   # v9.39: balance was
                              "INTEGER DEFAULT 0")]:  # admin-set
            try:
                await db.execute(f"ALTER TABLE users ADD COLUMN {col} {typedef};")
            except Exception:
                pass
        try:
            await db.execute("ALTER TABLE stock ADD COLUMN country TEXT DEFAULT 'USA';")
        except Exception:
            pass
        for col, typedef in [
            ("refund_state", "TEXT"),
            ("otp_blocked", "INTEGER DEFAULT 0"),
            ("baseline_codes", "TEXT"),
            ("order_id", "TEXT"),   # v9.27: links the stock to its order
        ]:
            try:
                await db.execute(f"ALTER TABLE stock ADD COLUMN {col} {typedef};")
            except Exception:
                pass
        for col, typedef in [
            ("pay_amount", "REAL"),
            ("created_ts", "INTEGER"),
            ("verified_at", "TEXT"),
            ("match_mode", "TEXT"),
            ("attempts", "INTEGER DEFAULT 0"),
        ]:
            try:
                await db.execute(f"ALTER TABLE deposits ADD COLUMN {col} {typedef};")
            except Exception:
                pass
        # Seed default settings
        for k, v in DEFAULT_SETTINGS.items():
            await db.execute(
                "INSERT OR IGNORE INTO settings(key,value) VALUES(?,?)", (k, v)
            )
        # v9.10: enforce the new minimum deposit on old databases
        await db.execute(
            "UPDATE settings SET value='0.15' WHERE key='min_deposit' "
            "AND CAST(value AS REAL) < 0.15")
        # v9.12: deposit audit trail (append-only)
        await db.execute(
            "CREATE TABLE IF NOT EXISTS deposit_trace("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "ts INTEGER NOT NULL, deposit_id TEXT, user_id INTEGER,"
            "network TEXT, txid TEXT, event TEXT NOT NULL, detail TEXT)")
        await db.execute(
            "CREATE INDEX IF NOT EXISTS idx_deptrace_dep "
            "ON deposit_trace(deposit_id)")
        # v9.23: managed channels (force-join + broadcast targets)
        # and per-user join states (public=live membership,
        # private=join REQUEST unlocks, never approved)
        await db.execute(
            "CREATE TABLE IF NOT EXISTS channels("
            "chat_id INTEGER PRIMARY KEY,"
            "title TEXT, username TEXT, ctype TEXT, privacy TEXT,"
            "invite_link TEXT, added_by INTEGER,"
            "added_at TEXT DEFAULT (datetime('now')))")
        await db.execute(
            "CREATE TABLE IF NOT EXISTS channel_joins("
            "user_id INTEGER NOT NULL, chat_id INTEGER NOT NULL,"
            "state TEXT DEFAULT 'pending', ts INTEGER,"
            "PRIMARY KEY(user_id, chat_id))")
        await db.execute(
            "CREATE INDEX IF NOT EXISTS idx_cj_user "
            "ON channel_joins(user_id)")
        # v9.24 REFERRAL SYSTEM: buyers carry referred_by, referrers get
        # one UNIQUE-per-order earning row, VIP referrers a custom rate.
        try:
            await db.execute(
                "ALTER TABLE users ADD COLUMN referred_by INTEGER;")
        except Exception:
            pass   # column already exists (idempotent upgades)
        await db.execute(
            "CREATE TABLE IF NOT EXISTS ref_earnings("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "order_id TEXT UNIQUE NOT NULL,"
            "buyer_id INTEGER NOT NULL,"
            "referrer_id INTEGER NOT NULL,"
            "amount REAL NOT NULL,"
            "status TEXT DEFAULT 'paid',"
            "created_at TEXT DEFAULT (datetime('now')))")
        await db.execute(
            "CREATE INDEX IF NOT EXISTS idx_refearn_ref "
            "ON ref_earnings(referrer_id, id)")
        await db.execute(
            "CREATE INDEX IF NOT EXISTS idx_refearn_buyer "
            "ON ref_earnings(buyer_id)")
        await db.execute(
            "CREATE TABLE IF NOT EXISTS ref_vip("
            "user_id INTEGER PRIMARY KEY,"
            "rate REAL NOT NULL,"
            "added_at TEXT DEFAULT (datetime('now')))")
        await db.execute(
            "CREATE INDEX IF NOT EXISTS idx_users_refby "
            "ON users(referred_by)")
        # v9.14: hot-path indexes (browse counts, histories, admin lists)
        for _idx_sql in (
            "CREATE INDEX IF NOT EXISTS idx_stock_avail "
            "ON stock(number_type, country, status)",
            "CREATE INDEX IF NOT EXISTS idx_stock_soldto ON stock(sold_to)",
            "CREATE INDEX IF NOT EXISTS idx_dep_user ON deposits(user_id, id)",
            "CREATE INDEX IF NOT EXISTS idx_dep_status ON deposits(status, id)",
            "CREATE INDEX IF NOT EXISTS idx_ord_user ON orders(user_id, id)",
            # v9.27 refund-hub hot paths (url matching, sell batches, active numbers)
            "CREATE INDEX IF NOT EXISTS idx_stock_otpurl ON stock(otp_url)",
            "CREATE INDEX IF NOT EXISTS idx_stock_status_id ON stock(status, id)",
            "CREATE INDEX IF NOT EXISTS idx_refearn_order ON ref_earnings(order_id)",
        ):
            await db.execute(_idx_sql)
        # v9.27: the old refund system is fully retired - the legacy
        # refunds table is dropped on boot (the refund hub matches on
        # live stock rows only; no second data model may exist).
        try:
            await db.execute("DROP TABLE IF EXISTS refunds")
        except Exception:
            pass
        # v9.12: rotate any leftover RETIRED wallet -> new wallet
        for _wk, _rot in WALLET_ROTATE.items():
            cur = await db.execute(
                "SELECT value FROM settings WHERE key=?", (_wk,))
            _wrow = await cur.fetchone()
            await cur.close()
            _wold = (str(_wrow[0]) if _wrow and _wrow[0] else "").strip()
            _wnew = None
            for _o, _n in _rot.items():
                if _wold == _o or _wold.lower() == _o.lower():
                    _wnew = _n
                    break
            if _wnew:
                await db.execute(
                    "UPDATE settings SET value=? WHERE key=?",
                    (_wnew, _wk))
                await db.execute(
                    "INSERT INTO deposit_trace(ts,deposit_id,user_id,"
                    "network,txid,event,detail) VALUES(?,?,?,?,?,?,?)",
                    (int(_utcnow().timestamp()), "-", 0, _wk, "-",
                     "wallet_rotated",
                     "retired %s... -> new %s..."
                     % (_wold[:10], _wnew[:10])))
                logger.info("Wallet rotated for %s - old address retired",
                            _wk)
        # v9.9: migrate placeholder/TRC20 wallet -> BEP20 auto-verify wallet
        cur = await db.execute(
            "SELECT value FROM settings WHERE key='usdt_wallet_address'")
        _row = await cur.fetchone()
        await cur.close()
        _old = (str(_row[0]) if _row and _row[0] else "").strip()
        if not _old.lower().startswith("0x"):
            await db.execute(
                "UPDATE settings SET value=? WHERE key='usdt_wallet_address'",
                (USDT_BEP20_WALLET,))
            await db.execute(
                "UPDATE settings SET value='BEP20' WHERE key='usdt_network'")
            logger.info("Migrated deposit wallet to BEP20 auto-verify")
        # v9.9.1: arm the BscScan API key on DBs created before it
        cur = await db.execute(
            "SELECT value FROM settings WHERE key='bscscan_api_key'")
        _krow = await cur.fetchone()
        await cur.close()
        _key = (str(_krow[0]) if _krow and _krow[0] else "").strip()
        if not _key and BSCSCAN_API_KEY_ENV:
            await db.execute(
                "UPDATE settings SET value=? "
                "WHERE key='bscscan_api_key'",
                (BSCSCAN_API_KEY_ENV,))
            logger.info("BscScan API key armed (auto-verify fully active)")
        # Mark admin(s) - v9.25: every owner-admin in ADMIN_IDS gets the
        # DB crown too (covers the second admin even if his user row
        # already existed with is_admin=0).
        for _aid in ADMIN_IDS:
            await db.execute(
                "UPDATE users SET is_admin=1 WHERE telegram_id=?", (_aid,)
            )
        # v9.41: dynamic extra admins -> sync is_admin cache (boot load)
        try:
            _ex = await get_extra_admins()
            _EXTRA_ADMINS.clear()
            _EXTRA_ADMINS.update(_ex)
            if _ex:
                logger.info("Extra admins loaded: %s", sorted(_ex))
        except Exception as _e:
            logger.warning("extra admin cache load failed: %s", _e)
    logger.info("Database ready at %s", DB_PATH)


# --------------------------------------------------------------------------- #
#  CRUD
# --------------------------------------------------------------------------- #
async def get_or_create_user(telegram_id, username=None, first_name=None):
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM users WHERE telegram_id=?", (telegram_id,)
        )
        row = await cur.fetchone()
        await cur.close()
        if row is None:
            is_adm = 1 if telegram_id in ADMIN_IDS else 0
            cur = await db.execute(
                "INSERT INTO users(telegram_id,username,first_name,is_admin) "
                "VALUES(?,?,?,?)",
                (telegram_id, username, first_name, is_adm),
            )
            uid = cur.lastrowid
            cur2 = await db.execute("SELECT * FROM users WHERE id=?", (uid,))
            row = await cur2.fetchone()
            await cur2.close()
        return dict(row)


async def get_user(telegram_id):
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM users WHERE telegram_id=?", (telegram_id,)
        )
        row = await cur.fetchone()
        await cur.close()
        return dict(row) if row else None


async def deduct_balance(telegram_id, amount):
    async with adb() as db:
        await db.execute(
            "UPDATE users SET balance=balance-?, total_spent=total_spent+?, "
            "total_purchased=total_purchased+1, updated_at=datetime('now') "
            "WHERE telegram_id=?",
            (amount, amount, telegram_id),
        )


async def increment_otp_count(telegram_id):
    async with adb() as db:
        await db.execute(
            "UPDATE users SET total_otp=total_otp+1 WHERE telegram_id=?",
            (telegram_id,),
        )


async def set_ban(telegram_id, banned: bool):
    async with adb() as db:
        await db.execute(
            "UPDATE users SET is_banned=? WHERE telegram_id=?",
            (1 if banned else 0, telegram_id),
        )


async def set_balance(telegram_id, amount: float):
    """v9.39: admin balance writes mark the user adm_modified=1
    - that balance is admin money and is EXCLUDED from the All
    User Balance screen (real deposits only). This is the SINGLE
    admin balance write path (audited), so the flag can never be
    forgotten."""
    async with adb() as db:
        await db.execute(
            "UPDATE users SET balance=?, adm_modified=1, "
            "updated_at=datetime('now') "
            "WHERE telegram_id=?",
            (round(float(amount), 2), telegram_id),
        )


async def get_broadcast_targets():
    """v9.20: ids of every non-banned user (40k-safe, tiny memory).
    Banned users never receive broadcasts."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT telegram_id FROM users WHERE is_banned=0")
        rows = await cur.fetchall()
        await cur.close()
        return [r[0] for r in rows]


# ------------------------------------------------------------------------- #
#  v9.23 MANAGED CHANNELS - CRUD + force-join state
# ------------------------------------------------------------------------- #
async def add_channel(chat_id, title, username, ctype, privacy,
                      invite_link, added_by):
    async with adb() as db:
        await db.execute(
            "INSERT OR REPLACE INTO channels(chat_id,title,username,"
            "ctype,privacy,invite_link,added_by) VALUES(?,?,?,?,?,?,?)",
            (int(chat_id), title, username, ctype, privacy, invite_link,
             int(added_by)))
    _CH_CACHE["ids"] = None


async def remove_channel(chat_id):
    async with adb() as db:
        await db.execute("DELETE FROM channels WHERE chat_id=?",
                         (int(chat_id),))
    _CH_CACHE["ids"] = None


async def list_channels():
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM channels ORDER BY added_at, chat_id")
        rows = [dict(r) for r in await cur.fetchall()]
        await cur.close()
        return rows


async def get_channel(chat_id):
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM channels WHERE chat_id=?", (int(chat_id),))
        row = await cur.fetchone()
        await cur.close()
        return dict(row) if row else None


async def count_channels():
    async with adb() as db:
        cur = await db.execute("SELECT COUNT(*) FROM channels")
        n = (await cur.fetchone())[0]
        await cur.close()
        return n


_CH_CACHE = {"ids": None, "ts": 0.0}   # managed chat-id cache (60s)


async def managed_channel_ids():
    """Cached frozenset of managed chat ids (force-join + broadcast).
    40k-safe: one cached read per minute, invalidated on add/remove."""
    now = time.monotonic()
    if _CH_CACHE["ids"] is not None and now - _CH_CACHE["ts"] < 60.0:
        return _CH_CACHE["ids"]
    ids = frozenset(int(r["chat_id"]) for r in await list_channels())
    _CH_CACHE["ids"] = ids
    _CH_CACHE["ts"] = now
    return ids


async def mark_join(user_id, chat_id, state):
    """Upsert a join state: pending | requested | joined."""
    async with adb() as db:
        await db.execute(
            "INSERT INTO channel_joins(user_id,chat_id,state,ts) "
            "VALUES(?,?,?,?) ON CONFLICT(user_id,chat_id) "
            "DO UPDATE SET state=excluded.state, ts=excluded.ts",
            (int(user_id), int(chat_id), state,
             int(_utcnow().timestamp())))


async def get_join_row(user_id, chat_id):
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM channel_joins WHERE user_id=? AND chat_id=?",
            (int(user_id), int(chat_id)))
        row = await cur.fetchone()
        await cur.close()
        return dict(row) if row else None


async def pending_force_join(user_id):
    """Channel rows this user has NOT unlocked yet. Both 'requested'
    (private join request arrived) and 'joined' unlock. Admin check
    is the caller's job. v9.36: chats marked broken (bot kicked,
    chat deleted - see probe_managed_chats) NEVER trap a user; they
    are filtered out everywhere."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT c.chat_id, c.title, c.username, c.ctype, c.privacy, "
            "c.invite_link, COALESCE(j.state,'pending') AS jstate "
            "FROM channels c LEFT JOIN channel_joins j "
            "ON j.user_id=? AND j.chat_id=c.chat_id "
            "WHERE j.state IS NULL OR j.state "
            "NOT IN ('joined','requested') "
            "ORDER BY c.added_at, c.chat_id",
            (int(user_id),))
        rows = [dict(r) for r in await cur.fetchall()]
        await cur.close()
        if _FJ_BROKEN:
            rows = [r for r in rows if int(r["chat_id"]) not in _FJ_BROKEN]
        return rows


# v9.36: managed chats the bot can no longer see (kicked/deleted) -
# the force-join gate auto-passes them instead of locking users forever
_FJ_BROKEN = set()


def _fj_chat_unreachable_err(msg: str) -> bool:
    """Classify a getChatMember failure: chat-level (bot kicked, chat
    deleted) vs user-level (user simply has not joined yet)."""
    m = (msg or "").lower()
    if "user" in m and ("not found" in m or "participant" in m
                        or "not a member" in m):
        return False        # the USER has not joined - chat itself is fine
    return ("not a member" in m or "not a participant" in m
            or "chat not found" in m or "channel not found" in m
            or "chat_id invalid" in m or "peer id invalid" in m
            or "invalid chat" in m)


async def probe_managed_chats(bot):
    """v9.36 boot sanity: READ-ONLY probe of every managed chat (sends
    NOTHING). A chat the bot can no longer reach lands in _FJ_BROKEN so
    the force-join gate auto-passes it instead of trapping users on the
    join screen forever (owner bug: users stuck - start 'crash')."""
    bid = getattr(bot, "id", None)
    if not bid:
        return
    try:
        chats = list(await managed_channel_ids())
    except Exception:
        return
    for cid in chats:
        try:
            await bot.get_chat_member(int(cid), bid)
        except Exception as e:
            if _fj_chat_unreachable_err(str(e)):
                _FJ_BROKEN.add(int(cid))
                logger.warning("managed chat %s unreachable at boot (%s) "
                               "-> force-join gate auto-passes it",
                               cid, str(e)[:80])


# --------------------------------------------------------------------------- #
#  v9.24 REFERRAL SYSTEM — helpers
#  Loot-proof rules baked into the data layer:
#  - a buyer is bound to a referrer ONCE (first deep-link start wins,
#    WHERE referred_by IS NULL), self-binding is impossible;
#  - the commission row is UNIQUE per order id (INSERT OR IGNORE +
#    rowcount check) - a double payout can never exist;
#  - VIP rates override the global rate per referrer;
#  - a refunded order reverses its earning (status='reversed') and
#    deducts from the referrer, never below 0.
# --------------------------------------------------------------------------- #
_REF_ON = True          # in-process mirror of settings.ref_enabled (fast sync)
_BOT_USERNAME = ""      # set in post_init -> referral deep links


def ref_is_on() -> bool:
    """SYNC check used by main_menu_kb (40k-safe: no awaits, no I/O)."""
    return _REF_ON


async def ref_enabled() -> bool:
    """Async truth: reads the setting (2s TTL cache) and refreshes the
    sync mirror so the very next menu render agrees with it."""
    global _REF_ON
    _REF_ON = (await get_setting("ref_enabled")) == "1"
    return _REF_ON


async def get_ref_rate() -> float:
    """Global per-buy commission (default $0.005)."""
    try:
        v = float(await get_setting("ref_rate"))
    except (TypeError, ValueError):
        v = 0.005
    if not math.isfinite(v) or v < 0:
        v = 0.005
    return v


def _fmt_amt(x: float) -> str:
    """$0.005 -> '0.005', $2.50 -> '2.50' (trailing zeros trimmed)."""
    s = f"{float(x):.4f}".rstrip("0").rstrip(".")
    return s if s else "0"


async def bind_referral(buyer_id: int, referrer_id: int) -> bool:
    """Bind a BRAND-NEW buyer to the referrer from their deep link.
    - self-referral blocked;
    - referrer must exist;
    - WHERE referred_by IS NULL -> under a race the FIRST binder wins
      and a user can never be re-bound (no commission farming)."""
    if not referrer_id or int(buyer_id) == int(referrer_id):
        return False
    ru = await get_user(int(referrer_id))
    if ru is None:
        return False
    async with adb() as db:
        cur = await db.execute(
            "UPDATE users SET referred_by=? "
            "WHERE telegram_id=? AND referred_by IS NULL",
            (int(referrer_id), int(buyer_id)))
        return cur.rowcount == 1


async def ref_vip_rate(referrer_id: int):
    """VIP commission for this referrer, or None when not VIP."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT rate FROM ref_vip WHERE user_id=?", (int(referrer_id),))
        row = await cur.fetchone()
        await cur.close()
        return float(row[0]) if row and row[0] is not None else None


async def ref_vip_set(user_id: int, rate: float):
    async with adb() as db:
        await db.execute(
            "INSERT INTO ref_vip(user_id,rate) VALUES(?,?) "
            "ON CONFLICT(user_id) DO UPDATE SET rate=excluded.rate",
            (int(user_id), float(rate)))


async def ref_vip_del(user_id: int) -> bool:
    async with adb() as db:
        cur = await db.execute(
            "DELETE FROM ref_vip WHERE user_id=?", (int(user_id),))
        return cur.rowcount == 1


async def ref_vip_list():
    """VIP rows joined with the users table (name + username)."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT v.user_id, v.rate, u.first_name, u.username "
            "FROM ref_vip v LEFT JOIN users u "
            "ON u.telegram_id=v.user_id ORDER BY v.added_at, v.user_id")
        rows = [dict(r) for r in await cur.fetchall()]
        await cur.close()
        return rows


async def ref_stats_for(referrer_id: int):
    """(referred_count, total_earned_paid) for one referrer."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT COUNT(*) FROM users WHERE referred_by=?",
            (int(referrer_id),))
        cnt = (await cur.fetchone())[0]
        await cur.close()
        cur = await db.execute(
            "SELECT COALESCE(SUM(amount),0) FROM ref_earnings "
            "WHERE referrer_id=? AND status='paid'",
            (int(referrer_id),))
        earned = float((await cur.fetchone())[0] or 0.0)
        await cur.close()
    return int(cnt), earned


async def ref_recent_earnings(referrer_id: int, limit: int = 5):
    """Last `limit` paid earnings with the buyer's name for the screen."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT e.amount, e.created_at, u.first_name, u.username "
            "FROM ref_earnings e LEFT JOIN users u "
            "ON u.telegram_id=e.buyer_id "
            "WHERE e.referrer_id=? AND e.status='paid' "
            "ORDER BY e.id DESC LIMIT ?",
            (int(referrer_id), int(limit)))
        rows = [dict(r) for r in await cur.fetchall()]
        await cur.close()
        return rows


async def notify_referral_earned(context, referrer_id: int, amount: float,
                                 buyer_name: str, order_id: str):
    """Beautiful, localized 'you earned' card to the referrer."""
    lang = await get_user_lang(referrer_id)
    u = await get_user(referrer_id)
    bal = float(u.get("balance", 0.0) or 0.0) if u else 0.0
    try:
        await context.bot.send_message(
            chat_id=referrer_id,
            text=t(lang, "ref_earned_notif",
                   name=html_escape(buyer_name or "?"),
                   amount=_fmt_amt(amount), bal=f"{bal:.2f}",
                   div=DIV) + f"\n\U0001F194 <code>{html_escape(order_id)}</code>",
            parse_mode=ParseMode.HTML)
    except Exception:
        pass   # referrer blocked the bot - commission already credited


async def add_stock(phone, otp_url, ntype, country, added_by):
    async with adb() as db:
        await db.execute(
            "INSERT INTO stock(phone_number,otp_url,number_type,country,added_by) "
            "VALUES(?,?,?,?,?)",
            (phone, otp_url, ntype, country, added_by),
        )


async def phone_in_stock_any(phone):
    """True if the phone exists in stock in ANY state (sold/refunded too)."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT COUNT(*) FROM stock WHERE phone_number=?", (phone,)
        )
        n = (await cur.fetchone())[0]
        await cur.close()
        return n > 0


async def phones_in_stock_set(phones, only_available=False):
    """v9.20: ONE chunked query for a whole phone list (bulk add fast path).
    Returns the set of phones that exist in stock."""
    out = set()
    phones = [p for p in phones if p]
    for i in range(0, len(phones), 500):
        chunk = phones[i:i + 500]
        q = ("SELECT DISTINCT phone_number FROM stock WHERE "
             "phone_number IN (%s)" % ",".join("?" * len(chunk)))
        if only_available:
            q += " AND status='available'"
        async with adb() as db:
            cur = await db.execute(q, chunk)
            rows = await cur.fetchall()
            await cur.close()
        out.update(r[0] for r in rows)
    return out


async def add_stock_many(entries, ntype, country, added_by):
    """v9.20: bulk insert [(phone, url), ...] in ONE executemany/commit."""
    if not entries:
        return 0
    db_type = "whatsapp" if ntype == "wa" else "telegram"
    async with adb() as db:
        await db.executemany(
            "INSERT INTO stock(phone_number,otp_url,number_type,country,added_by) "
            "VALUES(?,?,?,?,?)",
            [(p, u or "", db_type, country, added_by) for p, u in entries])
    return len(entries)


async def get_available_stock(ntype=None, country=None):
    async with adb() as db:
        q = "SELECT * FROM stock WHERE status='available'"
        params = []
        if ntype:
            q += " AND number_type=?"
            params.append(ntype)
        if country:
            q += " AND country=?"
            params.append(country)
        q += " ORDER BY id LIMIT 1"
        cur = await db.execute(q, params)
        row = await cur.fetchone()
        await cur.close()
        return dict(row) if row else None


async def get_stock_counts():
    async with adb() as db:
        counts = {}
        for nt in ("whatsapp", "telegram"):
            cur = await db.execute(
                "SELECT country, COUNT(*) c FROM stock WHERE status='available' "
                "AND number_type=? GROUP BY country",
                (nt,),
            )
            rows = await cur.fetchall()
            await cur.close()
            counts[nt] = {r[0]: r[1] for r in rows}
        cur = await db.execute(
            "SELECT COUNT(*) FROM stock WHERE status='available'"
        )
        total = (await cur.fetchone())[0]
        await cur.close()
        return counts, total


async def mark_stock_sold(stock_id, sold_to):
    async with adb() as db:
        await db.execute(
            "UPDATE stock SET status='sold', sold_to=?, sold_at=datetime('now') "
            "WHERE id=?",
            (sold_to, stock_id),
        )


async def get_stock_item(stock_id):
    async with adb() as db:
        cur = await db.execute("SELECT * FROM stock WHERE id=?", (stock_id,))
        row = await cur.fetchone()
        await cur.close()
        return dict(row) if row else None


async def update_otp_for_stock(stock_id, otp_code):
    """v9.21: atomic OTP claim - returns True only when THIS caller won
    the right to deliver (otp_code was still empty). The 10-minute
    poller and the Get OTP button can race each other; exactly one of
    them notifies the user and the OTP counter can never double-count.
    Re-delivery attempts never overwrite a stored code.
    v9.28 RACE FIX: the claim also requires the row to still be a live
    SOLD number. Before this, a refund that won the race between the
    caller's fresh-check and this UPDATE could still lose the claim
    race -> the buyer received the OTP AND the refund money (double
    payout). Now a refunded/blocked row can never claim an OTP."""
    async with adb() as db:
        cur = await db.execute(
            "UPDATE stock SET otp_code=?, otp_status='used', "
            "otp_fetched_at=datetime('now') "
            "WHERE id=? AND (otp_code IS NULL OR otp_code='') "
            "AND status='sold' AND COALESCE(otp_blocked,0)=0 "
            "AND (refund_state IS NULL OR refund_state NOT IN "
            "('requested','approved'))",
            (otp_code, stock_id),
        )
        won = cur.rowcount == 1
        await cur.close()
    return won


async def get_stock_baseline(stock_id):
    """Codes that were already on the number's API at purchase time.
    v9.26 LOSS FIX: returns (captured, codes_set) -
      captured=False -> baseline was NEVER captured (no row yet)
      captured=True  -> baseline IS captured, possibly EMPTY: an empty
    set means 'fresh bulk number, no old SMS' and every code seen from
    now on belongs to the buyer. The old version returned [] for BOTH
    states, so callers re-baselined on the next fetch and a fast
    OTP swallowed itself as 'old SMS' - never delivered (the
    3-number loss)."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT baseline_codes FROM stock WHERE id=?", (stock_id,)
        )
        row = await cur.fetchone()
        await cur.close()
    if not row or row[0] is None or not str(row[0]).strip():
        return (False, set())
    try:
        return (True, set(json.loads(row[0]) or []))
    except Exception:
        # corrupted row -> read it as captured-empty: the OWNER-SAFE
        # direction (the waiting buyer gets their code, no silent loss)
        return (True, set())


async def save_stock_baseline(stock_id, codes):
    async with adb() as db:
        await db.execute(
            "UPDATE stock SET baseline_codes=? WHERE id=?",
            (json.dumps(list(codes or [])), stock_id),
        )


async def mark_stock_refunded(stock_id):
    """v9.27 ATOMIC REFUND GUARD: marks the stock refunded ONLY while it
    is still sold AND no OTP has landed. The rowcount tells the caller
    whether THIS call won the refund - a number whose OTP arrived in a
    race can never be refunded, and the refund can never run twice.
    DATA WIPE: otp_url and sold_to are cleared - once refunded the row
    can never be matched by a URL again (re-sending the same file is a
    mathematical no-op), the number is dead (otp_blocked) forever."""
    async with adb() as db:
        cur = await db.execute(
            "UPDATE stock SET status='refunded', refund_state='approved', "
            "otp_blocked=1, otp_url='', sold_to=NULL "
            "WHERE id=? AND status='sold' "
            "AND (otp_code IS NULL OR otp_code='')",
            (stock_id,),
        )
        won = cur.rowcount == 1
        await cur.close()
    return won


async def find_active_numbers(uid):
    """v9.27: the user's ACTIVE numbers - sold to them, OTP not yet
    arrived, not refunded/blocked. Newest first (Active Numbers menu)."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT id, phone_number, number_type, country, sold_at "
            "FROM stock WHERE sold_to=? AND status='sold' "
            "AND (otp_code IS NULL OR otp_code='') "
            "AND COALESCE(otp_blocked,0)=0 ORDER BY id DESC",
            (uid,),
        )
        rows = await cur.fetchall()
        await cur.close()
        return [dict(r) for r in rows]


async def find_active_stock(uid, phone):
    """v9.27: the user's ONE active stock row for an exact phone number
    (Active Numbers -> send the number -> open its Get OTP screen)."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM stock WHERE sold_to=? AND phone_number=? "
            "AND status='sold' AND (otp_code IS NULL OR otp_code='') "
            "AND COALESCE(otp_blocked,0)=0 ORDER BY id DESC LIMIT 1",
            (uid, phone),
        )
        row = await cur.fetchone()
        await cur.close()
        return dict(row) if row else None


async def find_sold_stock_by_url(url):
    """v9.27 REFUND MATCH: the CURRENT owner of an otp_url. Only a sold
    number with a live owner and no OTP yet can match; a refunded row
    (url wiped, owner NULL, status refunded) can never match again."""
    u = normalize_url(url)
    if not u:
        return None
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM stock WHERE status='sold' "
            "AND sold_to IS NOT NULL "
            "AND (otp_code IS NULL OR otp_code='') "
            "AND COALESCE(otp_blocked,0)=0 "
            "AND otp_url=? ORDER BY id DESC LIMIT 1",
            (u,),
        )
        row = await cur.fetchone()
        await cur.close()
        return dict(row) if row else None


async def get_max_stock_id():
    async with adb() as db:
        cur = await db.execute("SELECT COALESCE(MAX(id),0) FROM stock")
        val = (await cur.fetchone())[0]
        await cur.close()
        return int(val or 0)


async def find_undelivered_sold(limit=300, max_age_hours=None, offset=0):
    """v9.28 OTP SWEEPER candidates: sold to someone, OTP not yet stored,
    not refunded/blocked, still carrying a live URL. Newest first.
    max_age_hours limits how old the sale may be (None = no limit).
    offset pages through the whole backlog so the sweeper eventually
    reaches EVERY waiting number, not only the newest ones."""
    q = ("SELECT id, phone_number, otp_url, sold_to, order_id, sold_at "
         "FROM stock WHERE status='sold' "
         "AND (otp_code IS NULL OR otp_code='') "
         "AND COALESCE(otp_blocked,0)=0 "
         "AND (refund_state IS NULL OR refund_state NOT IN "
         "('requested','approved')) "
         "AND otp_url IS NOT NULL AND otp_url != '' ")
    args = []
    if max_age_hours is not None:
        q += ("AND sold_at IS NOT NULL AND sold_at >= "
              "datetime('now', ?) ")
        args.append(f"-{int(max_age_hours)} hours")
    q += "ORDER BY id DESC LIMIT ? OFFSET ?"
    args.extend([int(limit), int(offset)])
    async with adb() as db:
        cur = await db.execute(q, args)
        rows = await cur.fetchall()
        await cur.close()
        return [dict(r) for r in rows]


async def cancel_pending_referral(order_id):
    """v9.27: a refunded number's commission never exists - the pending
    referral row is cancelled before any money could move."""
    if not order_id:
        return False
    async with adb() as db:
        cur = await db.execute(
            "UPDATE ref_earnings SET status='cancelled' "
            "WHERE order_id=? AND status='pending'",
            (str(order_id),),
        )
        hit = cur.rowcount > 0
        await cur.close()
    return hit


async def pay_pending_referral(context, order_id):
    """v9.27 REFERRAL ON SUCCESS: the commission is credited the moment
    the buyer's OTP actually arrives - never at purchase. The atomic
    UPDATE..WHERE status='pending' means a race (poller + Get OTP) pays
    EXACTLY once; a cancelled (refunded) row can never be paid."""
    if not order_id:
        return None
    async with adb() as db:
        cur = await db.execute(
            "SELECT id, referrer_id, amount FROM ref_earnings "
            "WHERE order_id=? AND status='pending' LIMIT 1",
            (str(order_id),))
        row = await cur.fetchone()
        if row is None:
            await cur.close()
            return None
        cur2 = await db.execute(
            "UPDATE ref_earnings SET status='paid' WHERE id=? AND status='pending'",
            (row["id"],))
        paid = cur2.rowcount == 1
        await cur2.close()
        if paid:
            await db.execute(
                "UPDATE users SET balance=balance+?, "
                "updated_at=datetime('now') WHERE telegram_id=?",
                (float(row["amount"]), int(row["referrer_id"])))
        await cur.close()
    if not paid:
        return None
    info = {"referrer": int(row["referrer_id"]), "amount": float(row["amount"])}
    try:
        await notify_referral_earned(context, info["referrer"], info["amount"],
                                     "", str(order_id))
    except Exception:
        pass
    return info


async def credit_refund_balance(telegram_id, amount):
    async with adb() as db:
        await db.execute(
            "UPDATE users SET balance=balance+?, updated_at=datetime('now') "
            "WHERE telegram_id=?",
            (amount, telegram_id),
        )


async def get_order_amount_for(uid, phone):
    """(amount, order_id) of the order that contained this phone, or (None, None)."""
    async with adb() as db:
        cur = await db.execute(
            "SELECT total_amount, order_id FROM orders "
            "WHERE user_id=? AND numbers LIKE ? ORDER BY id DESC LIMIT 1",
            (uid, f'%"{phone}"%'),
        )
        row = await cur.fetchone()
        await cur.close()
        if row and row[0] is not None:
            return float(row[0]), row[1]
        return None, None


def normalize_url(u):
    return (u or "").strip().rstrip("/")


async def create_order(user_id, ntype, country, amount, numbers, rate):
    order_id = f"ORD{uuid.uuid4().hex[:8].upper()}"
    async with adb() as db:
        await db.execute(
            "INSERT INTO orders(order_id,user_id,number_type,country,total_amount,"
            "quantity,numbers,rate_at_purchase) VALUES(?,?,?,?,?,?,?,?)",
            (order_id, user_id, ntype, country, amount, 1, json.dumps(numbers), rate),
        )
    return order_id


async def create_deposit(user_id, amount, network="bep20",
                         pay_amount=None):
    """v9.35: pay_amount overrides the stored pay amount - Binance orders
    charge the EXACT picked amount (the unique-cent bump is retired);
    the sweep credits only unambiguous amounts, shared ones go through
    the submitter-bound Order-ID path."""
    deposit_id = f"DEP{uuid.uuid4().hex[:8].upper()}"
    mins = int(await get_setting("deposit_expiry_minutes"))
    expires = (_utcnow() + timedelta(minutes=mins)).strftime(
        "%Y-%m-%d %H:%M UTC"
    )
    created_ts = int(_utcnow().timestamp())
    wallet = await network_wallet(network)   # v9.12: bind to order
    pay_amt = amount if pay_amount is None else pay_amount
    async with adb() as db:
        await db.execute(
            "INSERT INTO deposits(deposit_id,user_id,amount,pay_amount,"
            "network,usdt_address,created_ts,expires_at) "
            "VALUES(?,?,?,?,?,?,?,?)",
            (deposit_id, user_id, amount, pay_amt, network, wallet,
             created_ts, expires),
        )
    detail = "$%.2f wallet=%s" % (amount, wallet)
    if pay_amt != amount:
        detail += " pay=$%.2f" % pay_amt
    await trace_deposit(deposit_id, user_id, network, "",
                        "order_created", detail)
    return deposit_id, expires


async def get_deposit(deposit_id):
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM deposits WHERE deposit_id=?", (deposit_id,)
        )
        row = await cur.fetchone()
        await cur.close()
        return dict(row) if row else None


async def update_deposit_tx(deposit_id, tx_hash, screenshot_file_id):
    async with adb() as db:
        await db.execute(
            "UPDATE deposits SET tx_hash=?, screenshot_file_id=? WHERE deposit_id=?",
            (tx_hash, screenshot_file_id, deposit_id),
        )


async def cancel_pending_deposit(uid, deposit_id):
    async with adb() as db:
        await db.execute(
            "UPDATE deposits SET status='cancelled' "
            "WHERE deposit_id=? AND user_id=? AND status='pending'",
            (deposit_id, uid),
        )


async def get_pending_deposits():
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM deposits WHERE status='pending' AND tx_hash IS NOT NULL "
            "ORDER BY id DESC"
        )
        rows = await cur.fetchall()
        await cur.close()
        return [dict(r) for r in rows]


async def confirm_deposit(deposit_id, admin_id):
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM deposits WHERE deposit_id=? AND status='pending'",
            (deposit_id,),
        )
        dep = await cur.fetchone()
        await cur.close()
        if not dep:
            return None
        dep = dict(dep)
        cur = await db.execute(
            "UPDATE deposits SET status='confirmed', confirmed_by=?, "
            "confirmed_at=datetime('now') WHERE deposit_id=? AND status='pending'",
            (admin_id, deposit_id),
        )
        if cur.rowcount == 0:   # decided between the two queries - no double pay
            return None
        await db.execute(
            "UPDATE users SET balance=balance+?, total_deposit=total_deposit+?, "
            "updated_at=datetime('now') WHERE telegram_id=?",
            (dep["amount"], dep["amount"], dep["user_id"]),
        )
        return dep


async def reject_deposit(deposit_id, admin_id):
    """Reject ONLY a still-pending deposit (double-tap safe)."""
    async with adb() as db:
        cur = await db.execute(
            "UPDATE deposits SET status='rejected', confirmed_by=?, "
            "confirmed_at=datetime('now') WHERE deposit_id=? AND status='pending'",
            (admin_id, deposit_id),
        )
        return cur.rowcount > 0


async def get_statistics():
    async with adb() as db:
        cur = await db.execute("SELECT COUNT(*) FROM users")
        users = (await cur.fetchone())[0]; await cur.close()
        cur = await db.execute("SELECT COUNT(*) FROM stock WHERE status='available'")
        avail = (await cur.fetchone())[0]; await cur.close()
        cur = await db.execute("SELECT COUNT(*) FROM stock WHERE status='sold'")
        sold = (await cur.fetchone())[0]; await cur.close()
        cur = await db.execute("SELECT COUNT(*) FROM deposits WHERE status='pending'")
        pend = (await cur.fetchone())[0]; await cur.close()
        cur = await db.execute("SELECT COALESCE(SUM(total_deposit),0) FROM users")
        tot_dep = (await cur.fetchone())[0]; await cur.close()
        cur = await db.execute("SELECT COALESCE(SUM(total_spent),0) FROM users")
        tot_spend = (await cur.fetchone())[0]; await cur.close()
        return {
            "users": users, "available": avail, "sold": sold,
            "pending_deposits": pend, "total_deposit": tot_dep,
            "total_spent": tot_spend,
        }


async def set_user_state(user_id, state, data=None):
    async with adb() as db:
        await db.execute(
            "INSERT INTO user_states(user_id,state,data,updated_at) "
            "VALUES(?,?,?,datetime('now')) "
            "ON CONFLICT(user_id) DO UPDATE SET state=excluded.state, "
            "data=excluded.data, updated_at=datetime('now')",
            (user_id, state, json.dumps(data) if data else None),
        )


async def get_user_state(user_id):
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM user_states WHERE user_id=?", (user_id,)
        )
        row = await cur.fetchone()
        await cur.close()
        if not row:
            return None, None
        return row["state"], (json.loads(row["data"]) if row["data"] else None)


async def clear_user_state(user_id):
    async with adb() as db:
        await db.execute("DELETE FROM user_states WHERE user_id=?", (user_id,))


# --------------------------------------------------------------------------- #
#  OTP FETCH  (backend fetches secret URL, user never sees URL)
# --------------------------------------------------------------------------- #
async def fetch_sms_text(url, session=None, timeout: int = 15):
    """GET the OTP API URL and return the raw response text (or None)."""
    if not url or not str(url).strip():
        return None
    try:
        if session is not None:
            async with session.get(
                url, timeout=aiohttp.ClientTimeout(total=timeout)
            ) as resp:
                return await resp.text()
        sess = await http_session()
        async with sess.get(
            url, timeout=aiohttp.ClientTimeout(total=timeout)
        ) as resp:
            return await resp.text()
    except Exception as e:
        logger.warning("SMS API fetch failed: %s", e)
        return None


def _otp_codes(text):
    """Extract OTP-looking codes from an API response, best candidates first.
    Priority: 6-digit > 123-456 style > 5-digit > 4-digit.
    v9.26 LOSS FIX: the provider's /sms/ page is a styled HTML document.
    Matching the RAW HTML used to return pure CSS junk (#16213e hex
    colors -> '16213', layout values -> '64748') while the real code was
    NOT in the server-rendered page at all. Script/style blocks and all
    tags are now stripped BEFORE matching, and entities are unescaped -
    only real text nodes can yield a code."""
    if not text:
        return []
    text = str(text)
    if "<" in text:
        text = re.sub(r"(?is)<(script|style)\b[^>]*>.*?</\1\s*>", " ", text)
        text = re.sub(r"(?is)<[^>]+>", " ", text)
        text = html_unescape(text)
    out = []
    for pat in (
        r"(?<!\d)(\d{6})(?!\d)",
        r"(?<!\d)(\d{3})[-\s](\d{3})(?!\d)",
        r"(?<!\d)(\d{5})(?!\d)",
        r"(?<!\d)(\d{4})(?!\d)",
    ):
        for m in re.finditer(pat, text):
            code = "".join(g for g in m.groups() if g)
            if code and code not in out:
                out.append(code)
        if out:
            break  # never mix weaker patterns once a stronger one matched
    return out


async def _fetch_api_sms(api_url, session, timeout: int = 10):
    """v9.26: GET with an HTTP-status check. Returns the body text only
    on a real 200 - a 404/500 page (or network error) means 'this
    provider has no machine endpoint', never 'no code'."""
    try:
        if session is not None:
            async with session.get(
                api_url, timeout=aiohttp.ClientTimeout(total=timeout)
            ) as resp:
                if resp.status != 200:
                    return None
                return await resp.text()
        sess = await http_session()
        async with sess.get(
            api_url, timeout=aiohttp.ClientTimeout(total=timeout)
        ) as resp:
            if resp.status != 200:
                return None
            return await resp.text()
    except Exception as e:
        logger.info("api/sms probe failed (falling back): %s", str(e)[:80])
        return None


async def fetch_sms_text_smart(url, session=None):
    """v9.26 LOSS FIX: read the OTP from the provider's MACHINE endpoint
    first (/api/sms/ - answers pure digits when a code exists, plain
    WAITING text when not). The pretty /sms/ page is rendered by
    JavaScript inside the buyer's browser: server-side it can sit on
    'WAITING...' forever while the real code is already live at
    /api/sms/ (proven live: page said WAITING, /api/sms/ returned
    869870 - three numbers were lost to exactly this). The /sms/ page
    is only used as a fallback when the machine endpoint is missing
    (non-200) - and _otp_codes then parses it HTML-safe."""
    u = (url or "").strip()
    if not u:
        return None
    api = api_sms_endpoint(u)
    if api != u:
        txt = await _fetch_api_sms(api, session)
        if txt is not None and str(txt).strip():
            return txt
    return await fetch_sms_text(u, session, 15)


def api_sms_endpoint(otp_url: str) -> str:
    """Seller-style clean probe endpoint: /sms/ -> /api/sms/.
    That endpoint answers pure digits when an OTP exists and plain
    text (WAITING / expiry notice) otherwise."""
    u = (otp_url or "").strip()
    if "/api/sms/" in u:
        return u
    if "/sms/" in u:
        return u.replace("/sms/", "/api/sms/", 1)
    return u


LIVE_CODE_RE = re.compile(r"^\d{3,10}$")


async def check_live_otp(otp_url: str, timeout: int = 12):
    """Live OTP probe using the seller's own rule: ONLY a pure-digit
    response proves a code exists (WAITING / errors prove nothing).
    Returns ("otp", code) | ("waiting", None) | ("unknown", None)."""
    if not otp_url:
        return ("unknown", None)
    # v9.26: status-checked probe - a 404 page must read as 'unknown',
    # never as 'waiting' (refund decisions depend on this difference).
    text = await _fetch_api_sms(api_sms_endpoint(otp_url), None, timeout)
    if text is None:
        return ("unknown", None)
    t = str(text).strip()
    if t and LIVE_CODE_RE.match(t):
        return ("otp", t)
    return ("waiting", None)


# --------------------------------------------------------------------------- #
#  STOCK PARSER  ("+14133525884 | http://otp-api")  — auto-fixes bad formats
# --------------------------------------------------------------------------- #
PHONE_RE = re.compile(r"\+?\d{10,15}")
URL_RE = re.compile(r"https?://[^\s|;,<>]+", re.IGNORECASE)
BARE_IP_RE = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}:\d{2,5}/\S+")


def normalize_phone(raw: str):
    digits = re.sub(r"\D", "", raw or "")
    if not (10 <= len(digits) <= 15):
        return None
    return "+" + digits


def parse_stock_line(line: str):
    """Parse one stock line.
    Returns ((phone, url), None) on success or ((None, None), reason)."""
    line = (line or "").strip()
    if not line:
        return (None, None), "empty"

    url = ""
    rest = line
    m = URL_RE.search(line)
    if m:
        url = m.group(0).rstrip(".,;)")
        rest = line[: m.start()] + " " + line[m.end():]
    else:
        m2 = BARE_IP_RE.search(rest)  # forgot http:// but it's an IP link
        if m2:
            url = "http://" + m2.group(0)
            rest = rest.replace(m2.group(0), " ", 1)

    # separators the admin might use instead of |
    rest = rest.replace("|", " ").replace(";", " ").replace(",", " ")
    rest = rest.replace("\t", " ")
    # drop phone-formatting punctuation, then glue everything together
    rest = re.sub(r"[()\u2013\u2014.\-]", " ", rest)
    rest = re.sub(r"\s+", "", rest)

    pm = PHONE_RE.search(rest)
    if not pm:
        return (None, None), "no phone number found"
    phone = normalize_phone(pm.group(0))
    if not phone:
        return (None, None), "invalid number length"
    return (phone, url), None


def parse_stock_lines(text: str):
    """Parse a multi-line stock dump.
    Returns (entries, errors):
      entries = [(phone, url), ...]
      errors  = [(line_no, sample, reason), ...]
    """
    entries, errors = [], []
    for i, line in enumerate((text or "").splitlines(), 1):
        res, err = parse_stock_line(line)
        if err == "empty":
            continue
        if err:
            errors.append((i, line.strip()[:48], err))
        else:
            entries.append(res)
    return entries, errors


# --------------------------------------------------------------------------- #
#  KEYBOARDS
#  MAIN MENU + ADMIN PANEL + TEXT-INPUT PROMPTS -> bottom REPLY keyboard
#  ALL SUB-MENUS -> INLINE keyboards on the message (classic edit-in-place)
#  The reply keyboard is NOT persistent: Telegram closes it after every
#  button tap, so submenus stay clean. Top-level screens (main menu /
#  admin panel / input prompts) re-attach it -> it pops back up.
# --------------------------------------------------------------------------- #
def _kb(rows, placeholder, icons=None):
    _attach_button_icons(rows, icons)   # v9.19 per-button owner icons
    return ReplyKeyboardMarkup(
        rows, resize_keyboard=True, is_persistent=False,
        input_field_placeholder=placeholder,
    )


def _ikb(rows, icons=None):
    _attach_button_icons(rows, icons)   # v9.19 per-button owner icons
    return InlineKeyboardMarkup(rows)


def _inline_nav_row(back_cb=None, lang="en"):
    """Single inline Back row (v9.15/v9.16): goes one step back when a
    back target exists, otherwise straight to the main menu."""
    return [InlineKeyboardButton(t(lang, "btn_back"),
                                 callback_data=back_cb or "nav:home",
                                 style=KeyboardButtonStyle.DANGER)]


def main_menu_kb(is_adm: bool = False, lang: str = "en") -> ReplyKeyboardMarkup:
    """v9.34 owner layout: Buy Number + Bulk Buy on the TOP row, then
    Deposit + Profile, then Support + Active Numbers, then Refer &
    Earn - with the Admin Panel button RIGHT BESIDE Refer & Earn for
    admins (own row when the referral system is OFF).
    v9.24: Refer & Earn appears ONLY while the referral system is ON.
    v9.27: Active Numbers (the user's live, OTP-less numbers)."""
    rows = [
        [KeyboardButton(t(lang, "btn_buy"), style=KeyboardButtonStyle.SUCCESS),
         KeyboardButton(t(lang, "btn_ubulk"),    # v9.31 user-side Bulk Buy
                        style=KeyboardButtonStyle.SUCCESS)],
        [KeyboardButton(t(lang, "btn_deposit"), style=KeyboardButtonStyle.PRIMARY),
         KeyboardButton(t(lang, "btn_profile"), style=KeyboardButtonStyle.PRIMARY)],
        [KeyboardButton(t(lang, "btn_support"), style=KeyboardButtonStyle.PRIMARY),
         KeyboardButton(t(lang, "btn_active"), style=KeyboardButtonStyle.SUCCESS)],
    ]
    if ref_is_on():
        ref_row = [KeyboardButton(t(lang, "btn_refer"),
                                  style=KeyboardButtonStyle.SUCCESS)]
        if is_adm:   # v9.34: Admin Panel beside Refer & Earn
            ref_row.append(KeyboardButton(BTN_ADMIN,
                                          style=KeyboardButtonStyle.SUCCESS))
        rows.append(ref_row)
    elif is_adm:
        rows.append([KeyboardButton(BTN_ADMIN, style=KeyboardButtonStyle.SUCCESS)])
    return _kb(rows, t(lang, "kb_placeholder"), _BIC_MAIN)


def home_only_kb(lang="en") -> InlineKeyboardMarkup:
    return _ikb([_inline_nav_row(None, lang)], _BIC_NAV)


def back_home_kb(lang="en") -> InlineKeyboardMarkup:
    return _ikb([_inline_nav_row("nav:back", lang)], _BIC_NAV)


def buy_type_kb(lang="en") -> InlineKeyboardMarkup:
    return _ikb(
        [
            [InlineKeyboardButton(t(lang, "btn_wa"), callback_data="buy:wa",
                                  style=KeyboardButtonStyle.SUCCESS),
             InlineKeyboardButton(t(lang, "btn_tg"), callback_data="buy:tg",
                                  style=KeyboardButtonStyle.PRIMARY)],
            _inline_nav_row(None, lang),
        ], _BIC_BUY_TYPE
    )


def country_kb(prefix: str = "buy", ntype: str = "wa",
               lang: str = "en") -> InlineKeyboardMarkup:
    back_cb = "buy:back_type" if prefix == "buy" else "adst:back"
    rows, pair = [], []
    for name, flag in COUNTRIES:
        pair.append(InlineKeyboardButton(f"{flag} {name}",
                                         callback_data=f"{prefix}:{ntype}:{name}",
                                         style=KeyboardButtonStyle.PRIMARY))
        if len(pair) == 2:
            rows.append(pair)
            pair = []
    if pair:
        rows.append(pair)
    rows.append([InlineKeyboardButton(t(lang, "btn_back"),
                                      callback_data=back_cb,
                                      style=KeyboardButtonStyle.DANGER)])
    return _ikb(rows, _BIC_COUNTRY)


def buy_confirm_kb(price: float, ntype: str = "wa",
                   country: str = "USA", lang: str = "en") -> InlineKeyboardMarkup:
    return _ikb(
        [
            [InlineKeyboardButton(t(lang, "btn_buy_now", price=f"{price:.2f}"),
                                  callback_data=f"buy:do:{ntype}:{country}",
                                  style=KeyboardButtonStyle.SUCCESS)],
            [InlineKeyboardButton(t(lang, "btn_back"),
                                  callback_data=f"buy:back_ctry:{ntype}",
                                  style=KeyboardButtonStyle.DANGER)],
        ], _BIC_BUY_CONFIRM
    )


def deposit_menu_kb(lang="en") -> InlineKeyboardMarkup:
    return _ikb(
        [
            [InlineKeyboardButton(t(lang, "btn_dep_new"), callback_data="dep:new",
                                  style=KeyboardButtonStyle.SUCCESS)],
            [InlineKeyboardButton(t(lang, "btn_dep_hist"), callback_data="dep:hist",
                                  style=KeyboardButtonStyle.PRIMARY)],
            [InlineKeyboardButton(t(lang, "btn_back"), callback_data="nav:back",
                                  style=KeyboardButtonStyle.DANGER)],
        ], _BIC_DEP_MENU
    )


def deposit_amount_kb(lang="en") -> InlineKeyboardMarkup:
    rows = []
    row = []
    for v in DEPOSIT_AMOUNT_PRESETS:
        label = f"${v:g}"
        row.append(InlineKeyboardButton(label, callback_data=f"dep:amt:{v:g}",
                                        style=KeyboardButtonStyle.PRIMARY))
        if len(row) == 3:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([InlineKeyboardButton(t(lang, "btn_custom_amount"),
                                     callback_data="dep:custom",
                                     style=KeyboardButtonStyle.SUCCESS)])
    rows.append([InlineKeyboardButton(t(lang, "btn_back"), callback_data="dep:back",
                                      style=KeyboardButtonStyle.DANGER)])
    return _ikb(rows, _BIC_DEP_AMT)


def deposit_network_kb(lang="en") -> InlineKeyboardMarkup:
    # FRIEND EDITION: only 2 networks - Binance Pay + USDT BEP-20
    return _ikb(
        [[InlineKeyboardButton("\U0001F3E6 Binance Pay",
                               callback_data="dep:net:binance",
                               style=KeyboardButtonStyle.SUCCESS),
          InlineKeyboardButton("\U0001F7E1 USDT BEP-20",
                               callback_data="dep:net:bep20",
                               style=KeyboardButtonStyle.SUCCESS)],
         [InlineKeyboardButton(t(lang, "btn_back"), callback_data="dep:back",
                               style=KeyboardButtonStyle.DANGER)],
        ], _BIC_DEP_NET
    )


def deposit_wait_kb(deposit_id=None, lang="en") -> InlineKeyboardMarkup:
    """ADDRESS screen: pay, then I PAID -> TXID prompt. Cancel only."""
    cb = f"dep:cancel:{deposit_id}" if deposit_id else "dep:cancel"
    pid = f"dep:paid:{deposit_id}" if deposit_id else "dep:paid"
    return _ikb(
        [[InlineKeyboardButton(t(lang, "btn_i_paid"),
                               callback_data=pid,
                               style=KeyboardButtonStyle.SUCCESS)],
         [InlineKeyboardButton(t(lang, "btn_cancel_dep"), callback_data=cb,
                               style=KeyboardButtonStyle.DANGER)]],
        _BIC_DEP_WAIT,
    )


def deposit_custom_kb(lang="en") -> InlineKeyboardMarkup:
    """CUSTOM AMOUNT screen: the user only types an amount here."""
    return _ikb(
        [[InlineKeyboardButton(t(lang, "btn_cancel_dep"), callback_data="dep:cancel",
                               style=KeyboardButtonStyle.DANGER)]],
        _BIC_DEP_CANCEL,
    )


def txid_input_kb(deposit_id=None, lang="en") -> InlineKeyboardMarkup:
    """TXID screen: only the TXID matters here. Cancel only."""
    cb = f"dep:cancel:{deposit_id}" if deposit_id else "dep:cancel"
    return _ikb(
        [[InlineKeyboardButton(t(lang, "btn_cancel_dep"), callback_data=cb,
                               style=KeyboardButtonStyle.DANGER)]],
        _BIC_DEP_CANCEL,
    )


def back_only_kb(lang="en") -> InlineKeyboardMarkup:
    return _ikb(
        [[InlineKeyboardButton(t(lang, "btn_back"), callback_data="nav:back",
                               style=KeyboardButtonStyle.DANGER)]],
        _BIC_NAV,
    )


def insufficient_kb(lang="en") -> InlineKeyboardMarkup:
    return _ikb(
        [[InlineKeyboardButton(t(lang, "btn_deposit"), callback_data="nav:dep",
                               style=KeyboardButtonStyle.SUCCESS)],
         _inline_nav_row(None, lang)],
        _BIC_INSUF,
    )


def admin_panel_kb() -> ReplyKeyboardMarkup:
    """v9.22/v9.24: TWO buttons per row (owner order) - cleaner admin
    keyboard. v9.24 adds Manage Reffer next to Manage Channels.
    v9.34: Users button REMOVED (owner order), Bulk Buy -> Bulk
    Manage (live discount config). v9.38: full-width All User
    Balance row (live money screen)."""
    return _kb(
        [
            [KeyboardButton(BTN_ADD_STOCK, style=KeyboardButtonStyle.SUCCESS),
             KeyboardButton(BTN_STOCK_STATS, style=KeyboardButtonStyle.PRIMARY)],
            [KeyboardButton(BTN_PENDING, style=KeyboardButtonStyle.PRIMARY),
             KeyboardButton(BTN_BULK_MANAGE, style=KeyboardButtonStyle.SUCCESS)],
            [KeyboardButton(BTN_MODIFY_USER, style=KeyboardButtonStyle.SUCCESS),
             KeyboardButton(BTN_STATS, style=KeyboardButtonStyle.PRIMARY)],
            [KeyboardButton(BTN_SET_RATE, style=KeyboardButtonStyle.PRIMARY),
             KeyboardButton(BTN_BROADCAST, style=KeyboardButtonStyle.PRIMARY)],
            [KeyboardButton(BTN_SET_WALLET, style=KeyboardButtonStyle.PRIMARY)],
            [KeyboardButton(BTN_ALL_BAL, style=KeyboardButtonStyle.SUCCESS)],   # v9.38 live money screen
            [KeyboardButton(BTN_BAN, style=KeyboardButtonStyle.DANGER),
             KeyboardButton(BTN_MANAGE_REFUND, style=KeyboardButtonStyle.DANGER)],
            [KeyboardButton(BTN_REFER_MGMT, style=KeyboardButtonStyle.SUCCESS),
             KeyboardButton(BTN_CHANNELS, style=KeyboardButtonStyle.PRIMARY)],
            [KeyboardButton(BTN_MANAGE_ADMINS, style=KeyboardButtonStyle.DANGER)],
            [KeyboardButton(BTN_HOME, style=KeyboardButtonStyle.DANGER)],
        ],
        "Select an action \U0001F447", _BIC_ADMIN,
    )


# --------------------------------------------------------------------------- #
#  v9.41 MANAGE ADMIN (MAIN admin only) - add / remove / list extra admins.
#  Extra admins = FULL admin access, par deposit notice + Manage Admin
#  MAIN-admin-only rehte hain. Storage: settings('extra_admins') JSON list;
#  _EXTRA_ADMINS = sync cache jise is_admin() check karta hai (boot load +
#  har add/remove pe refresh).
# --------------------------------------------------------------------------- #
_EXTRA_ADMINS: set = set()


def _adma_is_main(uid: int) -> bool:
    return uid == ADMIN_ID


async def get_extra_admins() -> list:
    try:
        arr = json.loads(await get_setting("extra_admins") or "[]")
        if isinstance(arr, list):
            return [int(x) for x in arr]
    except Exception:
        pass
    return []


async def set_extra_admins(ids: list) -> None:
    clean = sorted({int(x) for x in ids})
    await set_setting("extra_admins", json.dumps(clean))
    _EXTRA_ADMINS.clear()
    _EXTRA_ADMINS.update(clean)


def admin_manage_kb() -> ReplyKeyboardMarkup:
    return _kb(
        [
            [KeyboardButton(BTN_ADMA_ADD, style=KeyboardButtonStyle.SUCCESS),
             KeyboardButton(BTN_ADMA_REM, style=KeyboardButtonStyle.DANGER)],
            [KeyboardButton(BTN_ADMA_LIST, style=KeyboardButtonStyle.PRIMARY)],
            [KeyboardButton(BTN_HOME, style=KeyboardButtonStyle.DANGER)],
        ],
        "Manage Admin \U0001F447", _BIC_ADMIN,
    )


async def show_admin_manage(update, context):
    uid = update.effective_user.id
    if not _adma_is_main(uid):
        await clear_user_state(uid)
        return await _send_tracked(update, context,
                                   "\u26D4 <b>Manage Admin sirf MAIN admin "
                                   "ke liye hai.</b>", admin_panel_kb())
    extras = await get_extra_admins()
    txt = (f"\U0001F465 <b>MANAGE ADMIN</b>\n\n{DIV}\n"
           f"\U0001F451 Admin: <code>{ADMIN_ID}</code>\n"
           f"\u2022 Extra admins: <b>{len(extras)}</b>\n"
           f"{DIV}\n\n\U0001F447 <b>Select an action</b>")
    await set_user_state(uid, "admin_adm")
    return await _send_tracked(update, context, txt, admin_manage_kb())


async def prompt_admin_add(update, context):
    uid = update.effective_user.id
    if not _adma_is_main(uid):
        await clear_user_state(uid)
        return await show_admin_panel(update, context)
    await set_user_state(uid, "admin_adm_add")
    return await _send_tracked(update, context,
                               "\u2795 <b>ADD ADMIN</b>\n\nNaye admin ka "
                               "numeric Telegram user ID bhejo:",
                               admin_input_kb())


async def prompt_admin_remove(update, context):
    uid = update.effective_user.id
    if not _adma_is_main(uid):
        await clear_user_state(uid)
        return await show_admin_panel(update, context)
    await set_user_state(uid, "admin_adm_rm")
    return await _send_tracked(update, context,
                               "\u2796 <b>REMOVE ADMIN</b>\n\nJo admin "
                               "hatana hai uska numeric Telegram user ID "
                               "bhejo:", admin_input_kb())


async def show_admin_list(update, context):
    uid = update.effective_user.id
    if not _adma_is_main(uid):
        await clear_user_state(uid)
        return await show_admin_panel(update, context)
    extras = await get_extra_admins()
    ids = [ADMIN_ID] + sorted(extras)
    lines = [f"{i}. <code>{a}</code>" for i, a in enumerate(ids, 1)]
    if not extras:
        lines.append("(\u2014 koi extra admin nahi)")
    txt = ("\U0001F4CB <b>ADMINS</b>\n\n" + DIV + "\n" + "\n".join(lines)
           + f"\n{DIV}\nTotal: <b>{1 + len(extras)}</b>")
    await set_user_state(uid, "admin_adm")
    return await _send_tracked(update, context, txt, admin_manage_kb())


async def handle_admin_manage_input(update, context, uid, state, text):
    """v9.41: admin_adm_add / admin_adm_rm ID inputs (MAIN admin only)."""
    if not _adma_is_main(uid):
        await clear_user_state(uid)
        return await show_admin_panel(update, context)
    try:
        target = int((text or "").strip())
    except ValueError:
        target = 0
    if target <= 0:
        return await _send_tracked(update, context,
                                   "\u274C <b>Invalid ID.</b> Numeric "
                                   "Telegram user ID bhejo:",
                                   admin_input_kb())
    extras = await get_extra_admins()
    if state == "admin_adm_add":
        if target == ADMIN_ID:
            await clear_user_state(uid)
            return await _send_tracked(update, context,
                                       "\u26A0\uFE0F <b>Ye MAIN admin "
                                       "already hai.</b>", admin_manage_kb())
        if target in extras:
            await clear_user_state(uid)
            return await _send_tracked(update, context,
                                       f"\u26A0\uFE0F <code>{target}"
                                       "</code> already admin hai.",
                                       admin_manage_kb())
        extras.append(target)
        await set_extra_admins(extras)
        try:
            async with adb() as db:
                await db.execute("UPDATE users SET is_admin=1 "
                                 "WHERE telegram_id=?", (target,))
        except Exception:
            pass
        await clear_user_state(uid)
        return await _send_tracked(update, context,
                                   f"\u2705 <b>Admin added:</b> "
                                   f"<code>{target}</code>\nFULL admin "
                                   "access mil gaya.",
                                   admin_manage_kb())
    # ---- remove flow ----
    if target == ADMIN_ID:
        await clear_user_state(uid)
        return await _send_tracked(update, context,
                                   "\u26D4 <b>MAIN admin remove nahi ho "
                                   "sakta.</b>", admin_manage_kb())
    if target not in extras:
        await clear_user_state(uid)
        return await _send_tracked(update, context,
                                   f"\u26A0\uFE0F <code>{target}</code> "
                                   "admin list me nahi hai.",
                                   admin_manage_kb())
    extras.remove(target)
    await set_extra_admins(extras)
    try:
        async with adb() as db:
            await db.execute("UPDATE users SET is_admin=0 "
                             "WHERE telegram_id=?", (target,))
    except Exception:
        pass
    await clear_user_state(uid)
    return await _send_tracked(update, context,
                               f"\u2705 <b>Admin removed:</b> "
                               f"<code>{target}</code>",
                               admin_manage_kb())


def admin_input_kb() -> ReplyKeyboardMarkup:
    return _kb(
        [[KeyboardButton(BTN_CANCEL, style=KeyboardButtonStyle.DANGER),
          KeyboardButton(BTN_ADMIN, style=KeyboardButtonStyle.PRIMARY)]],
        "Type your input, or Cancel", _BIC_ADMIN_INPUT,
    )


def admin_refund_kb() -> ReplyKeyboardMarkup:
    """v9.40 MANAGE REFUND hub: Check / Refund / one-tap Chek
    & Refund (Sell Number Send removed v9.40)."""
    return _kb(
        [[KeyboardButton(BTN_CHECK_NUMBER, style=KeyboardButtonStyle.PRIMARY),
          KeyboardButton(BTN_REFUND_SEND, style=KeyboardButtonStyle.SUCCESS)],
         [KeyboardButton(BTN_CHECK_REFUND, style=KeyboardButtonStyle.SUCCESS)],
         [KeyboardButton(BTN_CANCEL, style=KeyboardButtonStyle.DANGER),
          KeyboardButton(BTN_ADMIN, style=KeyboardButtonStyle.PRIMARY)]],
        "Manage refund \U0001F447", _BIC_ADMIN_REFUND,
    )


def admin_add_type_kb() -> InlineKeyboardMarkup:
    """Number-type picker for Add Stock (inline, edit-in-place)."""
    return _ikb(
        [
            [InlineKeyboardButton(BTN_WA_STOCK, callback_data="adst:wa",
                                  style=KeyboardButtonStyle.SUCCESS),
             InlineKeyboardButton(BTN_TG_STOCK, callback_data="adst:tg",
                                  style=KeyboardButtonStyle.PRIMARY)],
            [InlineKeyboardButton("\u2b05\ufe0f Back", callback_data="nav:back",
                                  style=KeyboardButtonStyle.DANGER)],
        ], _BIC_ADD_TYPE
    )


def admin_rate_pick_kb(wa: str, tg: str) -> InlineKeyboardMarkup:
    return _ikb(
        [
            [InlineKeyboardButton(f"🟢 WhatsApp — ${wa}",
                                  callback_data="adrt:wa",
                                  style=KeyboardButtonStyle.SUCCESS)],
            [InlineKeyboardButton(f"🔵 Telegram — ${tg}",
                                  callback_data="adrt:tg",
                                  style=KeyboardButtonStyle.PRIMARY)],
            [InlineKeyboardButton("⬅️ Back", callback_data="nav:back",
                                  style=KeyboardButtonStyle.DANGER)],
        ], _BIC_RATE
    )


def admin_ban_pick_kb() -> InlineKeyboardMarkup:
    return _ikb(
        [
            [InlineKeyboardButton(BTN_BAN_USER, callback_data="adbn:ban",
                                  style=KeyboardButtonStyle.DANGER),
             InlineKeyboardButton(BTN_UNBAN_USER, callback_data="adbn:unban",
                                  style=KeyboardButtonStyle.SUCCESS)],
            [InlineKeyboardButton("⬅️ Back", callback_data="nav:back",
                                  style=KeyboardButtonStyle.DANGER)],
        ], _BIC_BAN
    )


def admin_channels_kb() -> ReplyKeyboardMarkup:
    """v9.23: Manage Channels home keyboard (2 per row)."""
    return _kb(
        [[KeyboardButton(BTN_CH_ADD, style=KeyboardButtonStyle.SUCCESS),
          KeyboardButton(BTN_CH_REMOVE, style=KeyboardButtonStyle.DANGER)],
         [KeyboardButton(BTN_CH_LIST, style=KeyboardButtonStyle.PRIMARY),
          KeyboardButton(BTN_ADMIN, style=KeyboardButtonStyle.PRIMARY)]],
        "Manage channels \U0001F447", _BIC_CHANNELS)


def admin_ch_type_kb() -> InlineKeyboardMarkup:
    """v9.23: public/private picker for Add Channel."""
    return _ikb(
        [[InlineKeyboardButton("\U0001F4E3 Public", callback_data="adch:pub",
                               style=KeyboardButtonStyle.SUCCESS),
          InlineKeyboardButton("\U0001F512 Private", callback_data="adch:priv",
                               style=KeyboardButtonStyle.PRIMARY)],
         [InlineKeyboardButton("\u2b05\ufe0f Back", callback_data="nav:back",
                               style=KeyboardButtonStyle.DANGER)]],
        _BIC_CH_TYPE)


def admin_ch_remove_kb(rows) -> InlineKeyboardMarkup:
    """v9.23: one tap-to-remove button per managed chat (2 per row)."""
    out, pair = [], []
    for r in rows:
        pair.append(InlineKeyboardButton(
            f"\U0001F5D1 {r.get('title') or r.get('chat_id')}",
            callback_data=f"adchr:{r.get('chat_id')}"))
        if len(pair) == 2:
            out.append(pair)
            pair = []
    if pair:
        out.append(pair)
    out.append([InlineKeyboardButton("\u2b05\ufe0f Back",
                                     callback_data="nav:back",
                                     style=KeyboardButtonStyle.DANGER)])
    return _ikb(out, _BIC_CHANNELS)


# --------------------------------------------------------------------------- #
#  v9.24 MANAGE REFFER keyboards (admin, 2 buttons per row)
# --------------------------------------------------------------------------- #
def admin_refer_kb(on: bool) -> ReplyKeyboardMarkup:
    """Manage Reffer home: Set Price / VIP / live ON-OFF toggle / exit."""
    toggle = BTN_REF_TOGGLE_ON if on else BTN_REF_TOGGLE_OFF
    return _kb(
        [[KeyboardButton(BTN_REF_PRICE, style=KeyboardButtonStyle.PRIMARY),
          KeyboardButton(BTN_REF_VIP, style=KeyboardButtonStyle.PRIMARY)],
         [KeyboardButton(toggle,
                         style=(KeyboardButtonStyle.SUCCESS if on
                                else KeyboardButtonStyle.DANGER)),
          KeyboardButton(BTN_ADMIN, style=KeyboardButtonStyle.PRIMARY)]],
        "Manage Reffer \U0001F447", _BIC_REFER)


def admin_ref_vip_kb() -> ReplyKeyboardMarkup:
    return _kb(
        [[KeyboardButton(BTN_REF_VIP_ADD, style=KeyboardButtonStyle.SUCCESS),
          KeyboardButton(BTN_REF_VIP_REM, style=KeyboardButtonStyle.DANGER)],
         [KeyboardButton(BTN_REF_VIP_LIST, style=KeyboardButtonStyle.PRIMARY),
          KeyboardButton(BTN_ADMIN, style=KeyboardButtonStyle.PRIMARY)]],
        "Manage VIP \U0001F447", _BIC_REFER)


def admin_vip_remove_kb(rows) -> InlineKeyboardMarkup:
    """One tap-to-remove button per VIP referrer (2 per row)."""
    out, pair = [], []
    for r in rows:
        nm = (r.get("first_name")
              or (f"@{r.get('username')}" if r.get("username") else "-"))
        label = f"\U0001F5D1 {html_escape(str(nm))[:20]} \u2022 ${_fmt_amt(r.get('rate') or 0)}"
        pair.append(InlineKeyboardButton(
            label, callback_data=f"adrfr:del:{r.get('user_id')}"))
        if len(pair) == 2:
            out.append(pair)
            pair = []
    if pair:
        out.append(pair)
    out.append([InlineKeyboardButton("\u2b05\ufe0f Back",
                                     callback_data="nav:back",
                                     style=KeyboardButtonStyle.DANGER)])
    return _ikb(out, _BIC_REFER)


def force_join_text(rows, lang="en") -> str:
    """v9.23: the locked screen text (fully translated, 13 languages)."""
    names = "\n".join(
        f"\u2022 {html_escape(str(r.get('title') or r.get('chat_id') or '-'))}"
        for r in rows[:8])
    more = f"\n(+{len(rows) - 8} more)" if len(rows) > 8 else ""
    return (f"{t(lang, 'fj_title')}\n"
            f"{DIV}\n"
            f"{t(lang, 'fj_body')}\n\n"
            f"{names}{more}\n"
            f"{DIV}")


def force_join_kb(rows, lang="en") -> InlineKeyboardMarkup:
    """v9.23: JOIN CHANNEL / JOIN GROUP url buttons (owner envelope icon
    JOIN_EMOJI_ID) + Verify. Label per chat type, i18n in 13 languages."""
    b_rows = []
    for r in rows:
        url = r.get("invite_link") or (
            "https://t.me/%s" % r["username"] if r.get("username") else None)
        if not url:
            continue
        key = ("btn_join_group" if (r.get("ctype") or "") == "group"
               else "btn_join_channel")
        b_rows.append([InlineKeyboardButton(t(lang, key), url=url)])
    b_rows.append([InlineKeyboardButton(t(lang, "btn_fj_check"),
                                        callback_data="fjv:1",
                                        style=KeyboardButtonStyle.SUCCESS)])
    return _ikb(b_rows, _BIC_FJOIN)


def otp_kb(stock_id: int, lang: str = "en") -> InlineKeyboardMarkup:
    """Receipt keyboard (v9.27): Get OTP + Back. The old Refund button
    is gone - refunds are admin-driven now (Manage Refund hub)."""
    return _ikb(
        [
            [InlineKeyboardButton(t(lang, "btn_get_otp"), callback_data=f"otp:{stock_id}",
                                  style=KeyboardButtonStyle.SUCCESS)],
            [InlineKeyboardButton(t(lang, "btn_back"), callback_data="nav:home",
                                  style=KeyboardButtonStyle.PRIMARY)],
        ], _BIC_OTP
    )


def admin_deposit_approve_kb(deposit_id: str) -> InlineKeyboardMarkup:
    return _ikb(
        [[InlineKeyboardButton("\u2705 Approve", callback_data=f"admdep:ok:{deposit_id}",
                               style=KeyboardButtonStyle.SUCCESS),
          InlineKeyboardButton("\u274C Reject", callback_data=f"admdep:no:{deposit_id}",
                               style=KeyboardButtonStyle.DANGER)]],
        _BIC_APPROVE,
    )


# --------------------------------------------------------------------------- #
#  MESSAGES  (2026 premium card design)
# --------------------------------------------------------------------------- #
def menu_info_text(lang="en") -> str:
    return (
        f"{t(lang, 'menu_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'menu_where')}"
    )


def menu_footer_text(lang="en") -> str:
    return t(lang, "menu_footer")


async def welcome_text(first_name: str, user: dict, lang: str = "en") -> str:
    bot_name = await get_setting("bot_name")
    safe_name = html_escape(first_name or "User")
    bal = (user or {}).get("balance", 0.0) or 0.0
    _, total = await get_stock_counts()
    return (
        f"{t(lang, 'welcome_hi', name=safe_name)}\n"
        f"{DIV}\n"
        f"\U0001F48E <b>{html_escape(bot_name)}</b>\n"
        f"{t(lang, 'welcome_tagline')}\n\n"
        f"{t(lang, 'welcome_balance', bal=f'{bal:.2f}')}\n"
        f"{t(lang, 'welcome_stock', total=total)}\n"
        f"{DIV}\n"
        f"{t(lang, 'welcome_cta')}"
    )


def profile_text(user: dict, lang: str = "en") -> str:
    uid = user["telegram_id"]
    uname = f"@{html_escape(user['username'])}" if user.get("username") else "\u2014"
    name = html_escape(user.get("first_name") or "\u2014")
    bal = user.get("balance", 0.0) or 0.0
    purchased = user.get("total_purchased", 0) or 0
    spent = user.get("total_spent", 0.0) or 0.0
    deposit = user.get("total_deposit", 0.0) or 0.0
    otp = user.get("total_otp", 0) or 0
    ratio = f"{(otp/purchased*100):.0f}%" if purchased else "0%"
    return (
        f"{t(lang, 'profile_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'lbl_id')} <code>{uid}</code>\n"
        f"{t(lang, 'lbl_name')} {name}\n"
        f"{t(lang, 'lbl_username')} {uname}\n"
        f"{DIV}\n"
        f"{t(lang, 'welcome_balance', bal=f'{bal:.2f}')}\n"
        f"{t(lang, 'prof_purchased', n=purchased)}\n"
        f"{t(lang, 'prof_spent', amount=f'{spent:.2f}')}\n"
        f"{t(lang, 'prof_deposited', amount=f'{deposit:.2f}')}\n"
        f"{t(lang, 'prof_otps', n=otp, pct=ratio)}\n"
        f"{DIV}"
    )


def support_text(lang="en") -> str:
    return (
        f"{t(lang, 'support_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'support_admin', handle=SUPPORT_USERNAME)}\n"
        f"{t(lang, 'support_time')}\n"
        f"{DIV}\n"
        f"{t(lang, 'support_body')}"
    )


async def buy_intro_text(lang: str = "en") -> str:
    wa = float(await get_setting("whatsapp_rate"))
    tg = float(await get_setting("telegram_rate"))
    return (
        f"{t(lang, 'buy_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'buy_wa_price', wa=f'{wa:.2f}')}\n"
        f"{t(lang, 'buy_tg_price', tg=f'{tg:.2f}')}\n"
        f"{DIV}\n"
        f"{t(lang, 'buy_pick')}"
    )


def buy_country_text(ntype: str, lang: str = "en") -> str:
    label = "WhatsApp" if ntype == "wa" else "Telegram"
    return (
        f"{t(lang, 'ctry_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'ctry_avail', label=label)}\n"
        f"{DIV}\n"
        f"{t(lang, 'cta_select')}"
    )


async def buy_confirm_text(ntype: str, country: str, balance: float,
                           lang: str = "en") -> str:
    rate = float(await get_setting("whatsapp_rate" if ntype == "wa" else "telegram_rate"))
    label = "WhatsApp" if ntype == "wa" else "Telegram"
    flag = flag_of(country)
    return (
        f"{t(lang, 'confirm_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'cf_type', label=label)}\n"
        f"{t(lang, 'cf_country', flag=flag, country=country)}\n"
        f"{t(lang, 'cf_price', rate=f'{rate:.2f}')}\n"
        f"{t(lang, 'cf_balance', bal=f'{balance:.2f}')}\n"
        f"{DIV}\n"
        f"{t(lang, 'cf_cta')}"
    )


def purchase_success_text(number: str, label: str, country: str,
                          rate: float, order_id: str,
                          lang: str = "en") -> str:
    flag = flag_of(country)
    return (
        f"{t(lang, 'ps_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'ps_number', number=html_escape(number))}\n"
        f"{t(lang, 'ps_label', label=label, flag=flag, country=country)}\n"
        f"{t(lang, 'ps_paid', rate=f'{rate:.2f}')}\n"
        f"{t(lang, 'ps_order', order=order_id)}\n"
        f"{DIV}\n"
        f"{t(lang, 'ps_get_otp')}\n"
        f"{t(lang, 'ps_copy')}"
    )


def insufficient_text(rate: float, bal: float, need: float,
                      lang: str = "en") -> str:
    return (
        f"{t(lang, 'ins_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'ins_price', rate=f'{rate:.2f}')}\n"
        f"{t(lang, 'ins_balance', bal=f'{bal:.2f}')}\n"
        f"{t(lang, 'ins_need', need=f'{need:.2f}')}\n"
        f"{DIV}\n"
        f"{t(lang, 'ins_cta')}"
    )


def out_of_stock_text(label: str, country: str, lang: str = "en") -> str:
    flag = flag_of(country)
    return (
        f"{t(lang, 'oos_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'oos_label', label=label, flag=flag, country=country)}\n"
        f"{DIV}\n"
        f"{t(lang, 'oos_cta')}"
    )


async def deposit_intro_text(lang: str = "en") -> str:
    min_dep = float(await get_setting("min_deposit"))
    return (
        f"{t(lang, 'dep_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'dep_min_line', min=f'{min_dep:.2f}')}\n"
        f"{DIV}\n"
        f"{t(lang, 'cta_pick')}"
    )


def txid_prompt_text(dep_id: str, network: str = "bep20",
                     lang: str = "en") -> str:
    """DEP-07: shown after I PAID - asks for the TXID."""
    meta = DEPOSIT_NETWORKS.get(network) or DEPOSIT_NETWORKS["bep20"]
    fmt = ("64 hex characters, no 0x" if network == "trc20"
           else "0x + 64 hex characters")
    if network == "binance":     # v9.32: Order ID prompt (not a TXID)
        return (
            f"{t(lang, 'bin_txid_title')}\n"
            f"{DIV}\n"
            f"{t(lang, 'bin_txid_body')}\n"
            f"{DIV}\n"
            f"{t(lang, 'txid_ok_line')}\n"
            f"{t(lang, 'txid_no_line')}\n"
            f"\U0001F9FE <code>{dep_id}</code>"
        )
    return (
        f"{t(lang, 'txid_title', net=meta['short'])}\n"
        f"{DIV}\n"
        f"{t(lang, 'txid_body')}\n"
        f"{t(lang, 'txid_format', fmt=fmt)}\n"
        f"{DIV}\n"
        f"{t(lang, 'txid_ok_line')}\n"
        f"{t(lang, 'txid_no_line')}\n"
        f"\U0001F9FE <code>{dep_id}</code>"
    )


async def network_wallet(network: str) -> str:
    meta = DEPOSIT_NETWORKS.get(network) or DEPOSIT_NETWORKS["bep20"]
    w = (await get_setting(meta["wallet_key"]) or "").strip()
    return w or (meta["default"] or "")


def deposit_card_text(network: str, amount: float, wallet: str,
                      deposit_id: str, expires: str,
                      lang: str = "en") -> str:
    meta = DEPOSIT_NETWORKS.get(network) or DEPOSIT_NETWORKS["bep20"]
    if network == "binance":     # v9.32: Pay ID card (not a wallet address)
        return (
            f"{t(lang, 'card_send', amount=f'{amount:.2f}')}\n"
            f"{t(lang, 'card_network', net=meta['short'])}\n"
            f"{DIV}\n"
            f"{t(lang, 'bin_pay_id')}\n"
            f"<code>{html_escape(wallet)}</code>\n"
            f"{DIV}\n"
            f"{t(lang, 'bin_card_hint')}\n"
            f"{t(lang, 'bin_auto_line')}\n"
            f"{t(lang, 'card_paid')}\n"
            f"{t(lang, 'card_expire', dep_id=deposit_id, expires=expires)}"
        )
    return (
        f"{t(lang, 'card_send', amount=f'{amount:.2f}')}\n"
        f"{t(lang, 'card_network', net=meta['short'])}\n"
        f"{DIV}\n"
        f"{t(lang, 'card_address')}\n"
        f"<code>{html_escape(wallet)}</code>\n"
        f"{DIV}\n"
        f"{t(lang, 'card_warn', net=meta['short'])}\n"
        f"{t(lang, 'card_paid')}\n"
        f"{t(lang, 'card_expire', dep_id=deposit_id, expires=expires)}"
    )


def deposit_history_text(rows, lang: str = "en") -> str:
    if not rows:
        return (
            f"{t(lang, 'dep_hist_title')}\n"
            f"{DIV}\n"
            f"{t(lang, 'dep_hist_empty')}\n"
            f"{DIV}"
        )
    lines = [
        f"{t(lang, 'dep_hist_title')}\n{DIV}"
    ]
    for r in rows[:10]:
        st = {"pending": "\u23F3", "confirmed": "\u2705",
              "rejected": "\u274C", "cancelled": "\u26D4"}.get(r["status"], "\u23F3")
        lines.append(f"{st} <code>{r['deposit_id']}</code> \u2014 ${r['amount']:.2f}")
    lines.append(DIV)
    return "\n".join(lines)

# --------------------------------------------------------------------------- #
#  SCREEN RENDERERS
#  Every screen: (1) sets the user state  ->  state memory / phone-back fix
#                (2) sends message + BOTTOM reply keyboard
# --------------------------------------------------------------------------- #
async def show_main_menu(update, context):
    uid = update.effective_user.id
    user = await get_user(uid)
    if user is None:
        user = await get_or_create_user(uid)
    lang = (user or {}).get("lang") or ""
    await clear_user_state(uid)
    if not lang:
        # v9.16 onboarding contract: no language picked -> picker first
        # (state is cleared FIRST so a stale screen can never trap anyone)
        return await _send_tracked(update, context, lang_pick_text(),
                                   lang_picker_kb())
    # v9.23 FORCE JOIN: every managed chat must be joined first
    # (admins always pass; no channels configured = fully open bot)
    if not is_admin(uid) and await managed_channel_ids():
        pend = await pending_force_join(uid)
        if pend:
            return await show_force_join(update, context, pend, lang)
    await _send_tracked(update, context,
                        menu_info_text(lang),
                        main_menu_kb(is_admin(uid), lang))


async def show_profile(update, context):
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await clear_user_state(uid)
    u = await get_or_create_user(uid)
    await _send_tracked(update, context, profile_text(u, lang), home_only_kb(lang))


# --------------------------------------------------------------------------- #
#  v9.24 REFER & EARN (user side): personal deep link, live stats,
#  recent earnings and a one-tap native share. Hidden instantly when
#  the owner turns the system OFF.
# --------------------------------------------------------------------------- #
def refer_link(uid: int) -> str:
    return (f"https://t.me/{_BOT_USERNAME or 'Tbh_Virtual_SMS_Bot'}"
            f"?start=ref{int(uid)}")


def refer_screen_text(uid, count, earned, rate, vip_rate, recent,
                      lang: str = "en") -> str:
    link = refer_link(uid)
    parts = [t(lang, "ref_title"), DIV]
    if vip_rate is not None:
        parts.append(t(lang, "ref_vip_line", rate=_fmt_amt(vip_rate)))
    else:
        parts.append(t(lang, "ref_body", rate=_fmt_amt(rate)))
    parts.append(DIV)
    parts.append(t(lang, "ref_link"))
    parts.append(f"<code>{html_escape(link)}</code>")
    parts.append("")
    parts.append(t(lang, "ref_stats", count=count, earned=_fmt_amt(earned)))
    parts.append(DIV)
    if recent:
        for r in recent[:5]:
            nm = (r.get("first_name")
                  or (f"@{r['username']}" if r.get("username") else "?"))
            parts.append(f"\u2795 <b>${_fmt_amt(r.get('amount') or 0)}</b> "
                         f"\u2022 {html_escape(str(nm))}")
        parts.append(DIV)
    else:
        parts.append(t(lang, "ref_none_yet"))
        parts.append(DIV)
    parts.append(t(lang, "welcome_cta"))
    return "\n".join(parts)


def refer_kb(lang: str = "en", link: str = "") -> InlineKeyboardMarkup:
    """Native one-tap share (URL button) + Back. The share text is
    URL-encoded so the owner's emoji ride along to any chat."""
    url = ("https://t.me/share/url?url=" + url_quote(link or refer_link(0))
           + "&text=" + url_quote(t(lang, "ref_share_text")))
    return _ikb(
        [[InlineKeyboardButton(t(lang, "btn_ref_share"), url=url,
                               style=KeyboardButtonStyle.SUCCESS)],
         _inline_nav_row(None, lang)],
        _BIC_NAV)


async def show_refer(update, context):
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await clear_user_state(uid)
    if not await ref_enabled():
        # Owner switched OFF: the button should already be gone from the
        # menu - re-sync the keyboard so it disappears right now.
        return await _send_tracked(update, context, t(lang, "ref_paused"),
                                   main_menu_kb(is_admin(uid), lang))
    count, earned = await ref_stats_for(uid)
    rate = await get_ref_rate()
    vip = await ref_vip_rate(uid)
    recent = await ref_recent_earnings(uid, 5)
    await _send_tracked(update, context,
                        refer_screen_text(uid, count, earned, rate, vip,
                                          recent, lang),
                        refer_kb(lang, refer_link(uid)))


async def show_support(update, context):
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await clear_user_state(uid)
    await _send_tracked(update, context, support_text(lang), home_only_kb(lang))


# --------------------------------------------------------------------------- #
#  v9.27 ACTIVE NUMBERS (user menu): live numbers, tap-to-copy, resend the
#  number to open its Get OTP screen exactly like after the purchase.
# --------------------------------------------------------------------------- #
ACTIVE_SHOW_LIMIT = 60   # max numbers rendered in one list message


async def show_active_numbers(update, context):
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await clear_user_state(uid)
    rows = await find_active_numbers(uid)
    if not rows:
        await _send_tracked(update, context,
                            t(lang, "act_none"),
                            main_menu_kb(is_admin(uid), lang))
        return
    lines = [t(lang, "act_title", n=len(rows)), DIV]
    shown = rows[:ACTIVE_SHOW_LIMIT]
    for i, r in enumerate(shown, 1):
        lines.append(f"{i}. <code>{html_escape(r['phone_number'])}</code>")
    if len(rows) > len(shown):
        lines.append(t(lang, "act_more", extra=len(rows) - len(shown)))
    lines.append(DIV)
    lines.append(t(lang, "act_hint"))
    await _send_tracked(update, context, "\n".join(lines),
                        main_menu_kb(is_admin(uid), lang))


async def open_active_number(update, context, uid, stock):
    """Re-open a purchased number's screen (Get OTP + Back). The 10-minute
    live poller restarts with it, so the code auto-arrives on its own."""
    lang = await get_user_lang(uid)
    start_otp_poller(context, uid, stock)
    txt = (
        f"{t(lang, 'act_card_title')}\n"
        f"{DIV}\n"
        f"\U0001F7E2 <code>{html_escape(stock['phone_number'])}</code>\n"
        f"{DIV}\n"
        f"{t(lang, 'act_card_body')}"
    )
    await _send_tracked(update, context, txt, otp_kb(stock["id"], lang))


async def show_buy_type(update, context):
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await set_user_state(uid, "buy_type")
    await _send_tracked(update, context, await buy_intro_text(lang),
                        buy_type_kb(lang))


async def show_buy_country(update, context, ntype):
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await set_user_state(uid, "buy_country", {"ntype": ntype})
    await _send_tracked(update, context, buy_country_text(ntype, lang),
                        country_kb("buy", ntype, lang))


async def show_buy_confirm(update, context, ntype, country):
    uid = update.effective_user.id
    user = await get_user(uid)
    bal = (user or {}).get("balance", 0.0) or 0.0
    lang = await get_user_lang(uid)
    rate = float(await get_setting("whatsapp_rate" if ntype == "wa" else "telegram_rate"))
    await set_user_state(uid, "buy_confirm", {"ntype": ntype, "country": country})
    await _send_tracked(update, context,
                        await buy_confirm_text(ntype, country, bal, lang),
                        buy_confirm_kb(rate, ntype, country, lang))


async def show_dep_menu(update, context):
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await set_user_state(uid, "dep_menu")
    await _send_tracked(update, context, await deposit_intro_text(lang),
                        deposit_menu_kb(lang))


async def show_dep_amount(update, context):
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await set_user_state(uid, "dep_amount")
    min_dep = float(await get_setting("min_deposit"))
    await _send_tracked(update, context,
                        f"{t(lang, 'dep_amt_title')}\n"
                        f"{DIV}\n"
                        f"{t(lang, 'dep_min_only', min=f'{min_dep:.2f}')}\n"
                        f"{DIV}\n"
                        f"{t(lang, 'dep_amt_hint')}",
                        deposit_amount_kb(lang))


async def show_dep_networks(update, context, amount):
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await set_user_state(uid, "dep_net",
                         {"amount": amount})
    await _send_tracked(update, context,
                        f"{t(lang, 'dep_net_title')}\n"
                        f"{DIV}\n"
                        f"{t(lang, 'dep_net_amount', amount=f'{amount:.2f}')}\n"
                        f"{DIV}\n"
                        f"{t(lang, 'dep_net_hint')}",
                        deposit_network_kb(lang))


async def show_dep_history(update, context):
    uid = update.effective_user.id
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM deposits WHERE user_id=? ORDER BY id DESC LIMIT 10", (uid,)
        )
        rows = await cur.fetchall()
        await cur.close()
    # Back from history returns to the deposit menu
    lang = await get_user_lang(uid)
    await set_user_state(uid, "dep_hist")
    await _send_tracked(update, context, deposit_history_text(rows, lang),
                        back_only_kb(lang))


async def show_admin_panel(update, context):
    await clear_user_state(update.effective_user.id)
    s = await get_statistics()
    txt = (
        f"\U0001F6E0\uFE0F <b>ADMIN PANEL</b>\n\n"
        f"{DIV}\n"
        f"\U0001F465 {s['users']} users \u2022 \U0001F4E6 {s['available']} stock\n"
        f"\u23F3 {s['pending_deposits']} pending deposits\n"
        f"{DIV}\n\n"
        f"\U0001F447 <b>Select an action</b>"
    )
    await _send_tracked(update, context, txt, admin_panel_kb())


# --------------------------------------------------------------------------- #
#  v9.39 ADMIN: ALL USER BALANCE (REAL DEPOSIT ONLY - owner order)
#  One tap: every user's balance at once - but ONLY real money.
#  Users whose balance was ever modified from the admin panel
#  (adm_modified=1, set by set_balance) are EXCLUDED from every
#  tier and every total; their money shows on one shield line
#  instead. Holders ABOVE $100 and ABOVE $50 are listed SEPARATELY
#  (never merged into the combined figure); the rest shows as one
#  combined live total; grand total of the real-deposit users at
#  the end. Every open re-reads the DB - live, zero cache.
# --------------------------------------------------------------------------- #
_ALLBAL_HIGH = 100.0    # "100$ se jayda" tier (strictly more)
_ALLBAL_MID = 50.0      # "50$ se jayda" tier (strictly more, up to 100)
_ALLBAL_CAP = 25        # per-tier list cap - card can never hit 4096


def admin_allbal_kb() -> ReplyKeyboardMarkup:
    """v9.38 ALL USER BALANCE screen: live Refresh + back to panel."""
    return _kb(
        [[KeyboardButton(BTN_ALLBAL_REFRESH,
                         style=KeyboardButtonStyle.PRIMARY),
          KeyboardButton(BTN_ADMIN, style=KeyboardButtonStyle.DANGER)]],
        "All user balance (live)", _BIC_ADMIN_INPUT,
    )


def _allbal_list(entries, cap=_ALLBAL_CAP):
    """v9.38: numbered per-user lines for one tier (capped, with an
    honest '+N more' note - the 4096-char limit can never be hit)."""
    out = []
    for i, (uid, bal, banned) in enumerate(entries[:cap], 1):
        out.append(f"  {i}. <code>{uid}</code> \u2014 <b>${bal:.2f}</b>"
                   + (" \U0001F6AB" if banned else ""))
    if len(entries) > cap:
        out.append(f"  ... +{len(entries) - cap} more")
    return out


async def all_user_balance_text() -> str:
    """v9.39 the live money card - REAL DEPOSITS ONLY. Users whose
    balance was ever modified from the admin panel (adm_modified=1)
    are EXCLUDED from every tier and every total - that is admin
    money, not a real deposit (owner rule). Tiers (owner rule "se
    jayda" = strictly more; float noise killed by _MONEY_EPS):
      ABOVE $100   -> listed one-by-one + subtotal
      $50 - $100   -> listed one-by-one + subtotal
      $50 or below -> ONE combined figure (the "baki" live money)
      COMBINED     -> total WITHOUT the above-$50 holders
      GRAND TOTAL  -> real-deposit users only
    Banned users still count (their money is real) and are flagged."""
    async with adb() as db:
        cur = await db.execute("SELECT COUNT(*) FROM users")
        n_users = (await cur.fetchone())[0]
        await cur.close()
        cur = await db.execute(
            "SELECT telegram_id, balance, is_banned FROM users "
            "WHERE balance > 0 AND COALESCE(adm_modified,0)=0 "
            "ORDER BY balance DESC, telegram_id ASC")
        rows = await cur.fetchall()
        await cur.close()
        # v9.39: the admin-modified money kept OUT of every figure
        cur = await db.execute(
            "SELECT COUNT(*), COALESCE(SUM(balance),0.0) FROM users "
            "WHERE balance > 0 AND COALESCE(adm_modified,0)=1")
        adm_n, adm_sum = await cur.fetchone()
        await cur.close()
    if not rows:
        head = (
            "\U0001F4B5 <b>ALL USER BALANCE</b> \u2014 LIVE "
            "(REAL DEPOSIT)\n\n"
            f"{DIV}\n"
            f"\U0001F465 Total users: <b>{n_users}</b>\n"
        )
        if adm_n:
            head += (
                f"\U0001F6E1 Admin-modified: <b>{adm_n}</b> user "
                f"\u2014 <b>${adm_sum:.2f}</b> \u2014 EXCLUDED "
                "(total me add NAHI hota)\n\n")
        head += (
            "\U0001F4AD Abhi kisi ke paas balance nahi "
            "(sab $0.00 \u2014 live check).")
        return head
    hi = [r for r in rows if r[1] > _ALLBAL_HIGH + _MONEY_EPS]
    mid = [r for r in rows
           if _ALLBAL_MID + _MONEY_EPS < r[1] <= _ALLBAL_HIGH + _MONEY_EPS]
    low = [r for r in rows if r[1] <= _ALLBAL_MID + _MONEY_EPS]
    hi_sum = sum(r[1] for r in hi)
    mid_sum = sum(r[1] for r in mid)
    low_sum = sum(r[1] for r in low)
    holders_sum = hi_sum + mid_sum
    grand = holders_sum + low_sum
    out = [
        "\U0001F4B5 <b>ALL USER BALANCE</b> \u2014 LIVE "
        "(REAL DEPOSIT)",
        "",
        DIV,
        f"\U0001F465 Users: <b>{n_users}</b> \u2022 balance wale: "
        f"<b>{len(rows) + adm_n}</b> \u2022 zero: "
        f"<b>{n_users - len(rows) - adm_n}</b>",
    ]
    if adm_n:
        out.append(
            f"\U0001F6E1 Admin-modified: <b>{adm_n}</b> user \u2014 "
            f"<b>${adm_sum:.2f}</b> \u2014 EXCLUDED (admin paise, "
            "total me add NAHI hota)")
    out.append("")
    if hi:
        out.append(f"\U0001F534 <b>ABOVE ${_ALLBAL_HIGH:.0f} \u2014 "
                   f"{len(hi)} user \u2014 ${hi_sum:.2f}</b>")
        out.extend(_allbal_list(hi))
        out.append("")
    if mid:
        out.append(f"\U0001F7E1 <b>${_ALLBAL_MID:.0f}\u2013"
                   f"${_ALLBAL_HIGH:.0f} \u2014 "
                   f"{len(mid)} user \u2014 ${mid_sum:.2f}</b>")
        out.extend(_allbal_list(mid))
        out.append("")
    if holders_sum > 0:
        out.append(f"\u26A0\uFE0F Above-$50 holders ka total: "
                   f"<b>${holders_sum:.2f}</b> \u2014 ye UPAR list me "
                   "hai, neeche combined me ADD NAHI hota")
        out.append("")
    out.append(f"\U0001F7E2 <b>BAKI SAB (\u2264 ${_ALLBAL_MID:.0f}) "
               f"\u2014 {len(low)} user \u2014 combined:</b> "
               f"${low_sum:.2f}")
    out.append("")
    out.append(DIV)
    out.append(f"\U0001F4B0 <b>COMBINED (bina above-$50 holders ke):"
               f"</b> ${low_sum:.2f}")
    out.append(f"\U0001F48E <b>GRAND TOTAL (real deposit users):</b> "
               f"${grand:.2f}")
    out.append("")
    out.append("\U0001F6E1 Sirf REAL deposit wale users gine gaye "
               "\u2014 jo balance admin panel se modify hua wo "
               "EXCLUDED hai.")
    out.append("\U0001F504 Har tap par fresh DB read \u2014 "
               "100% live, koi cache nahi.")
    return "\n".join(out)


async def show_admin_allbal(update, context):
    """v9.38: the ALL USER BALANCE screen (admin-only; routed in
    on_text; view-only - no input state, Refresh re-reads live)."""
    if not is_admin(update.effective_user.id):
        return
    await clear_user_state(update.effective_user.id)
    await _send_tracked(update, context,
                        await all_user_balance_text(),
                        admin_allbal_kb())


async def show_admin_add_type(update, context):
    await set_user_state(update.effective_user.id, "admin_add_type")
    await _send_tracked(update, context,
                        "\U0001F4E6 <b>ADD STOCK</b>\n\n"
                        f"{DIV}\n\U0001F447 <b>Select number type</b>",
                        admin_add_type_kb())


async def show_admin_add_country(update, context, ntype):
    await set_user_state(update.effective_user.id, "admin_add_country", {"ntype": ntype})
    label = "WhatsApp" if ntype == "wa" else "Telegram"
    await _send_tracked(update, context,
                        f"\U0001F4E6 <b>ADD {label.upper()} STOCK</b>\n\n"
                        f"{DIV}\n\U0001F447 <b>Select country</b>",
                        country_kb("adstc", ntype))


async def prompt_admin_add_phone(update, context, ntype, country):
    await set_user_state(update.effective_user.id, "admin_add_phone",
                         {"ntype": ntype, "country": country})
    label = "WhatsApp" if ntype == "wa" else "Telegram"
    await _send_tracked(update, context,
                        f"\U0001F4E6 <b>ADD {label.upper()} STOCK \u2014 "
                        f"{flag_of(country)} {country}</b>\n\n"
                        + stock_format_hint(),
                        admin_input_kb())


def admin_bulkmanage_kb() -> InlineKeyboardMarkup:
    """v9.34 BULK MANAGE picker: set the USER bulk-buy discount."""
    return _ikb(
        [
            [InlineKeyboardButton("\U0001F522 Min Qty",
                                  callback_data="bulkm:min",
                                  style=KeyboardButtonStyle.PRIMARY),
             InlineKeyboardButton("\U0001F4B0 Discount",
                                  callback_data="bulkm:disc",
                                  style=KeyboardButtonStyle.SUCCESS)],
            [InlineKeyboardButton("\u2b05\ufe0f Back",
                                  callback_data="bulkm:back",
                                  style=KeyboardButtonStyle.DANGER)],
        ], _BIC_NAV,
    )


def bulk_manage_text(dmin, damt) -> str:
    """v9.34: the Bulk Manage card body (admin-only, English)."""
    save = round(damt * dmin, 2)
    return (
        "\U0001F4E6 <b>BULK MANAGE</b>\n\n"
        f"{DIV}\n"
        "\U0001F381 <b>User Bulk Buy discount</b> (live):\n"
        f"\U0001F522 Min quantity: <code>{dmin}+</code> numbers\n"
        f"\U0001F4B0 Discount: <code>${damt:.2f}</code> per number\n"
        f"\U0001F465 Example: {dmin} numbers \u2192 user saves "
        f"<code>${save:.2f}</code>\n"
        f"{DIV}\n"
        "\u2699\ufe0f <b>Tap a button to change:</b>\n"
        "\U0001F522 <b>Min Qty</b> \u2014 discount kitne numbers se shuru ho\n"
        "\U0001F4B0 <b>Discount</b> \u2014 per number kitna $ off (0 = OFF)"
    )


async def show_admin_bulkmanage(update, context):
    """v9.34 BULK MANAGE (replaces the v9.30 admin Bulk Buy): set the
    USER bulk-buy discount - minimum quantity + per-number $ off.
    Stored in settings, applied live everywhere on the next read."""
    await set_user_state(update.effective_user.id, "admin_bulkmanage")
    dmin, damt = await bulk_disc_params()
    await _send_tracked(update, context, bulk_manage_text(dmin, damt),
                        admin_bulkmanage_kb())


async def prompt_bulkmanage_min(update, context):
    dmin, _damt = await bulk_disc_params()
    await set_user_state(update.effective_user.id, "admin_bulkmanage_min")
    await _send_tracked(
        update, context,
        "\U0001F522 <b>BULK MANAGE \u2014 MIN QUANTITY</b>\n\n"
        f"{DIV}\n"
        "Type the <b>MINIMUM numbers</b> a user must buy for the "
        "discount to apply (e.g. 30).\n"
        f"Current: <code>{dmin}</code>\n\n"
        "\u274C <b>Cancel</b> to stop.",
        admin_input_kb(),
    )


async def prompt_bulkmanage_disc(update, context):
    _dmin, damt = await bulk_disc_params()
    await set_user_state(update.effective_user.id, "admin_bulkmanage_disc")
    await _send_tracked(
        update, context,
        "\U0001F4B0 <b>BULK MANAGE \u2014 DISCOUNT</b>\n\n"
        f"{DIV}\n"
        "Type the <b>PER-NUMBER discount</b> in $ (e.g. 0.02). "
        "<b>0 = discount OFF</b>.\n"
        f"Current: <code>${damt:.2f}</code>\n\n"
        "\u274C <b>Cancel</b> to stop.",
        admin_input_kb(),
    )


async def admin_bulkmanage_callback(update, context):
    """v9.34 inline router: bulkm:min / bulkm:disc / bulkm:back."""
    q = update.callback_query
    uid = q.from_user.id
    if not is_admin(uid):
        try:
            await q.answer("Admin only", show_alert=True)
        except Exception:
            pass
        return
    action = q.data.split(":", 1)[1] if ":" in q.data else ""
    if action == "min":
        await _safe_answer(q)
        return await prompt_bulkmanage_min(update, context)
    if action == "disc":
        await _safe_answer(q)
        return await prompt_bulkmanage_disc(update, context)
    if action == "back":
        await _safe_answer(q)
        return await show_admin_panel(update, context)
    try:
        await q.answer("Expired", show_alert=True)
    except Exception:
        pass



async def show_admin_set_rate(update, context):
    wa = await get_setting("whatsapp_rate")
    tg = await get_setting("telegram_rate")
    await set_user_state(update.effective_user.id, "admin_set_rate_pick")
    await _send_tracked(update, context,
                        f"\u2699\uFE0F <b>SET RATE</b>\n\n"
                        f"{DIV}\n\U0001F447 <b>Select which rate to change</b>",
                        admin_rate_pick_kb(wa, tg))


async def prompt_admin_set_rate(update, context, ntype):
    label = "WhatsApp" if ntype == "wa" else "Telegram"
    await set_user_state(update.effective_user.id, "admin_set_rate", {"ntype": ntype})
    await _send_tracked(update, context,
                        f"\u2699\uFE0F <b>SET {label.upper()} RATE</b>\n\n"
                        f"{DIV}\n\U0001F4B0 <b>Send new price</b> <i>(e.g. 2.50)</i>",
                        admin_input_kb())


async def show_admin_ban_pick(update, context):
    await set_user_state(update.effective_user.id, "admin_ban_pick")
    await _send_tracked(update, context,
                        f"\U0001F512 <b>BAN / UNBAN</b>\n\n"
                        f"{DIV}\n\U0001F447 <b>Select action</b>",
                        admin_ban_pick_kb())


async def prompt_admin_ban(update, context, action):
    await set_user_state(update.effective_user.id, "admin_ban", {"action": action})
    label = "BAN" if action == "ban" else "UNBAN"
    await _send_tracked(update, context,
                        f"\U0001F512 <b>{label} USER</b>\n\n"
                        f"{DIV}\n\U0001F194 <b>Send the Telegram user ID</b>",
                        admin_input_kb())


async def show_admin_modify_user(update, context):
    await set_user_state(update.effective_user.id, "admin_modify_user")
    await _send_tracked(update, context,
                        "\u270f\ufe0f <b>MODIFY USER</b>\n\n"
                        f"{DIV}\n\U0001F194 <b>Send the user's chat ID</b>\n"
                        f"<i>e.g. 1234567890</i>",
                        admin_input_kb())


def admin_user_kb(target: int) -> InlineKeyboardMarkup:
    return _ikb(
        [
            [InlineKeyboardButton("\U0001F4B5 Modify Balance",
                                  callback_data=f"admuser:bal:{target}",
                                  style=KeyboardButtonStyle.SUCCESS)],
            [InlineKeyboardButton("\u2B05\uFE0F Admin Panel",
                                  callback_data="admuser:back",
                                  style=KeyboardButtonStyle.DANGER)],
        ], _BIC_USER
    )


async def admin_user_details(update, context, target, note=None):
    """Full user card for the admin: balance, purchases, OTPs, orders..."""
    u = await get_user(target)
    if not u:
        await _send_tracked(update, context,
                            "\u26a0\ufe0f <b>User not found.</b> "
                            "Send another chat ID:",
                            admin_input_kb())
        return
    async with adb() as db:
        cur = await db.execute(
            "SELECT COUNT(*) AS c, COALESCE(SUM(total_amount),0) AS s "
            "FROM orders WHERE user_id=?", (target,))
        o = await cur.fetchone()
        await cur.close()
    uname = f"@{u['username']}" if u.get("username") else "\u2014"
    name = html_escape(u.get("first_name") or "\u2014")
    banned = "\U0001F6AB YES" if u.get("is_banned") else "\u2705 No"
    is_adm = "\U0001F451 YES" if u.get("is_admin") else "\u274c No"
    txt = (
        "\u270f\ufe0f <b>USER DETAILS</b>\n\n"
        f"{DIV}\n"
        f"\U0001F464 <b>Name:</b> {name}\n"
        f"\U0001F465 <b>Username:</b> {uname}\n"
        f"\U0001F194 <b>Chat ID:</b> <code>{target}</code>\n"
        f"{DIV}\n"
        f"\U0001F4B0 <b>Balance:</b> ${u.get('balance', 0.0) or 0.0:.2f}\n"
        f"\U0001F4B5 <b>Total Deposit:</b> ${u.get('total_deposit', 0.0) or 0.0:.2f}\n"
        f"\U0001F4B8 <b>Total Spent:</b> ${u.get('total_spent', 0.0) or 0.0:.2f}\n"
        f"{DIV}\n"
        f"\U0001F6D2 <b>Numbers Bought:</b> {u.get('total_purchased', 0) or 0}\n"
        f"\U0001F4E9 <b>OTPs Received:</b> {u.get('total_otp', 0) or 0}\n"
        f"\U0001F9FE <b>Orders:</b> {o['c']} (USDT {o['s']:.2f})\n"
        f"{DIV}\n"
        f"\U0001F6AB <b>Banned:</b> {banned}\n"
        f"\U0001F451 <b>Admin:</b> {is_adm}\n"
        f"\U0001F4C5 <b>Joined:</b> {u.get('created_at', '?')}\n"
        f"{DIV}\n\n"
        f"\U0001F447 <b>Use the button on the card</b>"
    )
    if note:
        txt = f"{note}\n\n{txt}"
    await set_user_state(update.effective_user.id, "admin_user_view",
                         {"target": target})
    await _send_tracked(update, context, txt, admin_user_kb(target))


async def prompt_admin_modbal(update, context, target):
    u = await get_user(target)
    cur_bal = (u or {}).get("balance", 0.0) or 0.0
    await set_user_state(update.effective_user.id, "admin_modbal",
                         {"target": target})
    await _send_tracked(update, context,
                        "\U0001F4B5 <b>MODIFY BALANCE</b>\n\n"
                        f"{DIV}\n"
                        f"\U0001F464 <b>User:</b> <code>{target}</code>\n"
                        f"\U0001F4B0 <b>Current:</b> ${cur_bal:.2f}\n"
                        f"{DIV}\n\n"
                        f"\U0001F449 <b>Send the new balance:</b>\n"
                        f"\u2022 <code>10.50</code> \u2014 set exactly\n"
                        f"\u2022 <code>+5</code> \u2014 add $5\n"
                        f"\u2022 <code>-2</code> \u2014 deduct $2",
                        admin_input_kb())


async def show_admin_broadcast(update, context):
    await set_user_state(update.effective_user.id, "admin_broadcast")
    await _send_tracked(update, context,
                        f"\U0001F4E3 <b>BROADCAST</b>\n\n"
                        f"{DIV}\n"
                        "\U0001F449 <b>Send ANY message to broadcast — "
                        "text, photo, video, file (APK), audio, GIF</b>\n"
                        "<i>Copied SAME-TO-SAME — premium custom emojis "
                        "stay premium.</i>\n"
                        "<i>Every managed channel/group receives it "
                        "too.</i>",
                        admin_input_kb())


# --------------------------------------------------------------------------- #
#  v9.23 MANAGE CHANNELS (admin): Add / Remove / List
#  Fully advanced input: @username, t.me link, -100 ID or a FORWARDED
#  message - the bot auto-detects everything and refuses a chat where it
#  is not already admin. Private chats get a bot-created join-REQUEST
#  link (users can only send a request; the bot never approves).
# --------------------------------------------------------------------------- #
_CH_ID_RE = re.compile(r"^-100\d{6,}$")
_CH_USER_RE = re.compile(r"^(?:@|(?:https?://)?(?:t|telegram)\.me/)"
                         r"([A-Za-z0-9_]{4,64})/?$")
_CH_INVITE_RE = re.compile(r"^(?:https?://)?t\.me/(?:\+|joinchat/)")


async def show_admin_channels(update, context):
    n = await count_channels()
    await set_user_state(update.effective_user.id, "admin_channels")
    await _send_tracked(
        update, context,
        f"\U0001F4E1 <b>MANAGE CHANNELS</b>\n\n"
        f"{DIV}\n"
        f"\U0001F4E1 Managed chats: <b>{n}</b>\n"
        f"\U0001F510 Users must join before they can use the bot\n"
        f"\U0001F4E3 Broadcasts are copied to every managed chat\n"
        f"{DIV}\n\n"
        f"\U0001F447 <b>Select an action</b>",
        admin_channels_kb())


async def show_admin_ch_type(update, context):
    await set_user_state(update.effective_user.id, "admin_ch_add_type")
    await _send_tracked(
        update, context,
        f"\U0001F4E1 <b>ADD CHANNEL</b>\n\n"
        f"{DIV}\n"
        "\U0001F4E3 <b>Public</b> — has a @username / t.me link\n"
        "\U0001F512 <b>Private</b> — joins via invite link / ID\n\n"
        "\U0001F449 <b>Which one are you adding?</b>",
        admin_ch_type_kb())


async def show_admin_ch_add(update, context, privacy):
    await set_user_state(update.effective_user.id, "admin_ch_add",
                         {"privacy": privacy})
    if privacy == "private":
        hint = ("\U0001F512 <b>PRIVATE</b> — send the chat ID "
                "(<code>-100…</code>) or <b>forward any message</b> from "
                "that channel/group.\n"
                "<i>Invite links can't be resolved by the API — a forward "
                "or an ID works instantly.</i>")
    else:
        hint = ("\U0001F4E3 <b>PUBLIC</b> — send <code>@username</code>, a "
                "<code>t.me</code> link, the ID, or <b>forward any "
                "message</b> from that channel/group.")
    await _send_tracked(
        update, context,
        f"\U0001F4E1 <b>ADD CHANNEL</b>\n\n"
        f"{DIV}\n{hint}\n{DIV}\n"
        "\U0001F916 The bot auto-detects everything (title, type, link) "
        "and checks it is ALREADY ADMIN there — if not, the chat is "
        "refused.\n\n"
        "\u274C <b>Cancel</b> to stop.",
        admin_input_kb())


async def show_admin_ch_remove(update, context):
    rows = await list_channels()
    await set_user_state(update.effective_user.id, "admin_ch_remove")
    if not rows:
        await _send_tracked(update, context,
                            "\U0001F5D1 <b>REMOVE CHANNEL</b>\n\n"
                            f"{DIV}\n"
                            "No channels yet — add one first.",
                            admin_ch_remove_kb(rows))
        return
    await _send_tracked(update, context,
                        f"\U0001F5D1 <b>REMOVE CHANNEL</b>\n\n"
                        f"{DIV}\n"
                        f"\U0001F4E1 {len(rows)} managed — tap the one to "
                        "remove:",
                        admin_ch_remove_kb(rows))


async def show_admin_ch_list(update, context):
    rows = await list_channels()
    await set_user_state(update.effective_user.id, "admin_channels")
    if not rows:
        txt = "\U0001F4CB No channels yet — tap <b>Add Channel</b>."
    else:
        lines = []
        for i, r in enumerate(rows, 1):
            uname = (f"@{r['username']}" if r.get("username")
                     else str(r.get("chat_id")))
            ctype = "Channel" if (r.get("ctype") or "channel") == "channel" \
                else "Group"
            lines.append(
                f"{i}. <b>{html_escape(str(r.get('title') or '-'))}</b>\n"
                f"&nbsp;&nbsp;&nbsp;\U0001F517 {html_escape(uname)} \u2022 "
                f"{ctype} \u2022 "
                f"{str(r.get('privacy') or 'public').title()}")
        txt = ("\U0001F4CB <b>MANAGED CHANNELS</b>\n\n" + DIV + "\n"
               + "\n".join(lines) + "\n" + DIV)
    await _send_tracked(update, context, txt, admin_channels_kb())


async def resolve_and_add_channel(update, context, uid, text, d=None):
    """Auto-detect @user / link / ID / forward -> verify the bot is
    admin there -> build the right join link -> store the channel."""
    bot = context.bot
    d = d or {}
    want = d.get("privacy") or "public"
    chat = None
    err = None
    fwd = getattr(update.message, "forward_from_chat", None)
    if fwd is not None and getattr(fwd, "id", None):
        chat = fwd                       # forwarded from the chat itself
    else:
        s = (text or "").strip()
        if _CH_INVITE_RE.match(s):
            err = ("\u274C <b>Invite links can't be resolved by the "
                   "API.</b>\nForward any message from that private "
                   "channel/group here — or send its "
                   "<code>-100…</code> ID.")
        elif _CH_ID_RE.match(s):
            try:
                chat = await bot.get_chat(int(s))
            except Exception as e:
                err = ("\u274C <b>Can't resolve that ID.</b>\nMake the "
                       "bot an <b>ADMIN</b> there first, then send it "
                       "again.\n"
                       f"<code>{html_escape(str(e)[:80])}</code>")
        else:
            m = _CH_USER_RE.match(s)
            if m:
                try:
                    chat = await bot.get_chat("@" + m.group(1))
                except Exception as e:
                    err = ("\u274C <b>Chat not found.</b> Check the "
                           "username/link.\n"
                           f"<code>{html_escape(str(e)[:80])}</code>")
            else:
                err = ("\u274C <b>Unrecognized format.</b>\nSend "
                       "<code>@username</code>, a <code>t.me</code> link, "
                       "a <code>-100…</code> ID, or forward a message "
                       "from the chat.")
    if chat is None:
        await _send_tracked(update, context, err, admin_input_kb())
        return
    ctype = getattr(chat, "type", "")
    if ctype not in ("channel", "supergroup", "group"):
        await _send_tracked(update, context,
                            "\u274C <b>That's not a channel or group.</b>\n"
                            "Send a channel/group link or ID.",
                            admin_input_kb())
        return
    # OWNER RULE: the bot must ALREADY be admin in that chat
    try:
        me = await bot.get_chat_member(chat.id, bot.id)
        st = getattr(me, "status", "")
    except Exception:
        st = ""
    if st not in ("administrator", "creator"):
        _t = str(getattr(chat, "title", "") or "that chat")
        await _send_tracked(update, context,
                            f"\U0001F6AB <b>Bot is NOT admin in "
                            f"{html_escape(_t)}.</b>\n"
                            "Make the bot an <b>admin</b> there first, "
                            "then send it again. The chat was NOT added.",
                            admin_input_kb())
        return
    # Public/private auto-detect + the right join link
    username = getattr(chat, "username", None)
    if username:
        privacy = "public"
        link = f"https://t.me/{username}"
    else:
        privacy = "private"
        link = getattr(chat, "invite_link", None)
        if not link:
            try:
                il = await bot.create_chat_invite_link(
                    chat.id, creates_join_request=True)
                link = il.invite_link
            except Exception:
                await _send_tracked(update, context,
                                    "\u274C <b>Bot needs the <i>Invite "
                                    "users via link</i> admin right</b> to "
                                    "build a private join-request link.\n"
                                    "Grant it and send the chat again.",
                                    admin_input_kb())
                return
    title = str(getattr(chat, "title", "") or
                (f"@{username}" if username else str(chat.id)))
    ctype_s = "channel" if ctype == "channel" else "group"
    await add_channel(chat.id, title, username, ctype_s, privacy, link, uid)
    note = ""
    if want == "private" and privacy == "public":
        note = ("\n\u2139\uFE0F <i>It has a @username — stored as "
                "PUBLIC.</i>")
    elif want == "public" and privacy == "private":
        note = ("\n\u2139\uFE0F <i>No @username — stored as PRIVATE "
                "(join-request link created).</i>")
    await set_user_state(uid, "admin_channels")
    await _send_tracked(update, context,
                        f"\u2705 <b>CHANNEL ADDED</b>\n\n"
                        f"{DIV}\n"
                        f"\U0001F4E1 <b>{html_escape(title)}</b>\n"
                        f"\U0001F194 <code>{chat.id}</code>\n"
                        f"\U0001F517 {html_escape(link)}\n"
                        f"\U0001F4C1 Type: "
                        f"{'Channel' if ctype_s == 'channel' else 'Group'}"
                        f" \u2022 {str(privacy).title()}{note}\n"
                        f"{DIV}\n\n"
                        "\U0001F510 Users must join before they can use "
                        "the bot.",
                        admin_channels_kb())


async def channels_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """v9.23 admin inline: adch:pub|priv (add type), adchr:<id> (remove)."""
    q = update.callback_query
    uid = q.from_user.id
    if not is_admin(uid):
        await _safe_answer(q, "Admins only", show_alert=True)
        return
    parts = (q.data or "").split(":")
    act = parts[1] if len(parts) > 1 else ""
    if act in ("pub", "priv"):
        await _safe_answer(q)
        return await show_admin_ch_add(
            update, context, "public" if act == "pub" else "private")
    if parts[0] == "adchr" and len(parts) >= 2:
        # adchr:<chat_id> - remove one managed chat
        try:
            chat_id = int(parts[1])
        except ValueError:
            await _safe_answer(q, "Invalid channel", show_alert=True)
            return
        await remove_channel(chat_id)
        await _safe_answer(q, "Channel removed")
        return await show_admin_ch_remove(update, context)
    await _safe_answer(q)
    return await show_admin_channels(update, context)


# --------------------------------------------------------------------------- #
#  v9.24 MANAGE REFFER (admin): dashboard, Set Reffer Price, VIP
#  add/remove/list and the system-wide ON/OFF switch (one tap per flip).
#  OFF = every commission stops (VIP + normal) and the user-side
#  Refer & Earn button disappears from every menu until re-enabled.
# --------------------------------------------------------------------------- #
async def show_admin_refer(update, context):
    await ref_enabled()                       # refresh the fast mirror
    rate = await get_ref_rate()
    vips = await ref_vip_list()
    on = ref_is_on()
    await set_user_state(update.effective_user.id, "admin_refer")
    state = ("\u2705 ON \u2014 commissions active + button live"
             if on else
             "\u26D4 OFF \u2014 commissions stopped + button hidden")
    await _send_tracked(
        update, context,
        f"\U0001F91D <b>MANAGE REFFER</b>\n\n"
        f"{DIV}\n"
        f"\U0001F4B5 Commission per buy: <b>${_fmt_amt(rate)}</b>\n"
        f"\U0001F451 VIP referrers: <b>{len(vips)}</b>\n"
        f"\U0001F504 System: <b>{state}</b>\n"
        f"{DIV}\n\n"
        f"\U0001F449 <b>Select an action</b>",
        admin_refer_kb(on))


async def prompt_admin_ref_price(update, context):
    uid = update.effective_user.id
    rate = await get_ref_rate()
    await set_user_state(uid, "admin_ref_price")
    await _send_tracked(
        update, context,
        f"\U0001F4B5 <b>SET REFFER PRICE</b>\n\n"
        f"{DIV}\n"
        f"Current commission: <b>${_fmt_amt(rate)}</b> per buy\n\n"
        f"\U0001F449 <b>Send the new commission</b>\n"
        f"<i>Example: <code>0.005</code> or <code>0.01</code></i>\n"
        f"{DIV}\n"
        "\u274C <b>Cancel</b> to keep the current price.",
        admin_input_kb())


async def show_admin_ref_vip(update, context):
    vips = await ref_vip_list()
    await set_user_state(update.effective_user.id, "admin_ref_vip")
    txt = (f"\U0001F451 <b>MANAGE VIP</b>\n\n"
           f"{DIV}\n"
           f"\U0001F451 VIP referrers earn their <b>own special rate</b> "
           f"per buy \u2014 only the chat IDs you add here.\n"
           f"Currently: <b>{len(vips)}</b> VIP\n"
           f"{DIV}\n\n"
           f"\U0001F447 <b>Select an action</b>")
    await _send_tracked(update, context, txt, admin_ref_vip_kb())


async def prompt_admin_vip_id(update, context):
    uid = update.effective_user.id
    await set_user_state(uid, "admin_ref_vip_add_id")
    await _send_tracked(
        update, context,
        f"\u2795 <b>ADD VIP REFERRER</b>\n\n"
        f"{DIV}\n"
        f"\U0001F194 <b>Send the user's chat ID</b>\n"
        f"<i>e.g. 1234567890</i>\n"
        f"{DIV}\n"
        "\u274C <b>Cancel</b> to stop.",
        admin_input_kb())


async def prompt_admin_vip_rate(update, context, target):
    uid = update.effective_user.id
    rate = await get_ref_rate()
    await set_user_state(uid, "admin_ref_vip_add_rate", {"target": int(target)})
    await _send_tracked(
        update, context,
        f"\u2795 <b>ADD VIP REFERRER</b>\n\n"
        f"{DIV}\n"
        f"\U0001F194 Chat ID: <code>{int(target)}</code>\n"
        f"\U0001F4B5 Normal rate: <b>${_fmt_amt(rate)}</b>\n"
        f"{DIV}\n"
        f"\U0001F449 <b>Send this VIP's special rate</b>\n"
        f"<i>Example: <code>0.010</code></i>\n"
        f"{DIV}\n"
        "\u274C <b>Cancel</b> to stop.",
        admin_input_kb())


async def show_admin_vip_remove(update, context):
    rows = await ref_vip_list()
    await set_user_state(update.effective_user.id, "admin_ref_vip_remove")
    if not rows:
        await _send_tracked(update, context,
                            f"\U0001F5D1 <b>REMOVE VIP</b>\n\n"
                            f"{DIV}\n"
                            "No VIP referrers yet \u2014 add one first.",
                            admin_vip_remove_kb(rows))
        return
    await _send_tracked(update, context,
                        f"\U0001F5D1 <b>REMOVE VIP</b>\n\n"
                        f"{DIV}\n"
                        f"\U0001F451 {len(rows)} VIP \u2014 tap the one to "
                        "remove:",
                        admin_vip_remove_kb(rows))


async def show_admin_vip_list(update, context):
    rows = await ref_vip_list()
    if not rows:
        txt = ("\U0001F4CB <b>VIP LIST</b>\n\n" + DIV + "\n"
               "No VIP referrers yet \u2014 tap <b>Add VIP</b>.\n"
               "Normal referrers still earn the standard commission.")
    else:
        lines = []
        for i, r in enumerate(rows, 1):
            nm = (r.get("first_name")
                  or (f"@{r.get('username')}" if r.get("username") else "-"))
            lines.append(
                f"{i}. \U0001F451 <b>{html_escape(str(nm))}</b> \u2014 "
                f"<code>{r.get('user_id')}</code> \u2014 "
                f"<b>${_fmt_amt(r.get('rate') or 0)}</b>/buy")
        txt = ("\U0001F4CB <b>VIP LIST</b>\n\n" + DIV + "\n"
               + "\n".join(lines) + "\n" + DIV)
    await set_user_state(update.effective_user.id, "admin_ref_vip")
    await _send_tracked(update, context, txt, admin_ref_vip_kb())


async def toggle_ref_system(update, context):
    """One tap flips the whole referral program ON <-> OFF.
    2s cooldown: a double-tap can never flip it twice."""
    global _REF_ON
    uid = update.effective_user.id
    now = time.monotonic()
    if now - (context.bot_data.get("ref_toggle_cd") or 0.0) < 2.0:
        return   # double-tap absorbed - state stays consistent
    context.bot_data["ref_toggle_cd"] = now
    new_state = not ref_is_on()
    await set_setting("ref_enabled", "1" if new_state else "0")
    _REF_ON = new_state
    if new_state:
        rate = await get_ref_rate()
        body = (f"\U0001F504 <b>REFFER SYSTEM TURNED ON</b>\n\n"
                f"{DIV}\n"
                f"\u2705 <b>Refer &amp; Earn button is LIVE</b> in every "
                f"user menu\n"
                f"\U0001F4B5 Commission per buy: <b>${_fmt_amt(rate)}</b>\n"
                f"\U0001F451 VIP rates stay untouched\n"
                f"{DIV}")
    else:
        body = (f"\U0001F504 <b>REFFER SYSTEM TURNED OFF</b>\n\n"
                f"{DIV}\n"
                f"\u26D4 <b>Refer &amp; Earn button HIDDEN</b> from every "
                f"menu\n"
                f"\u26D4 Commissions stopped \u2014 VIP + normal, until you "
                f"turn it back on\n"
                f"\u2139\uFE0F Existing VIP list and price are saved\n"
                f"{DIV}")
    await _send_tracked(update, context, body, admin_refer_kb(new_state))


async def admin_refer_callback(update: Update,
                               context: ContextTypes.DEFAULT_TYPE):
    """v9.24 admin inline: adrfr:del:<user_id> (remove one VIP)."""
    q = update.callback_query
    uid = q.from_user.id
    if not is_admin(uid):
        await _safe_answer(q, "Admins only", show_alert=True)
        return
    parts = (q.data or "").split(":")
    if len(parts) >= 3 and parts[1] == "del":
        try:
            target = int(parts[2])
        except ValueError:
            await _safe_answer(q, "Invalid ID", show_alert=True)
            return
        if await ref_vip_del(target):
            await _safe_answer(q, "VIP removed")
        else:
            await _safe_answer(q, "Already removed")
        return await show_admin_vip_remove(update, context)
    await _safe_answer(q)
    return await show_admin_ref_vip(update, context)


async def show_admin_set_wallet(update, context):
    w_bep = await get_setting("usdt_wallet_address")
    w_trc = await get_setting("trc20_wallet_address")
    w_pol = await get_setting("polygon_wallet_address")
    await set_user_state(update.effective_user.id, "admin_set_wallet")
    await _send_tracked(update, context,
                        f"\U0001F511 <b>WALLETS</b>\n\n"
                        f"{DIV}\n"
                        f"\U0001F7E2 BEP-20 (BSC):\n<code>{html_escape(w_bep or '-')}</code>\n\n"
                        f"\U0001F7E0 TRC-20 (Tron):\n<code>{html_escape(w_trc or '-')}</code>\n\n"
                        f"\U0001F7E3 Polygon:\n<code>{html_escape(w_pol or '-')}</code>\n"
                        f"{DIV}\n\n"
                        f"\U0001F449 <b>Send new address</b> to change the "
                        f"BEP-20 wallet\n"
                        f"\U0001F310 <code>0x...</code> = BEP20 \u2192 "
                        f"\U0001F916 auto-verify <b>ON</b>\n"
                        f"\u26A0\uFE0F Other formats = manual approval only",
                        admin_input_kb())


# --------------------------------------------------------------------------- #
#  BACK NAVIGATION  (smart Back: knows which screen you came from)
# --------------------------------------------------------------------------- #
async def go_back(update, context, state, sdata):
    d = sdata or {}
    if state == "awaiting_txid" and d.get("deposit_id"):
        # v9.22: Back from the TXID prompt re-opens the ADDRESS card of the
        # SAME pending deposit - state and deposit stay consistent, the user
        # can resume with I PAID or Cancel. A dead deposit clears cleanly.
        dep = await get_deposit(d["deposit_id"])
        if dep and dep.get("status") == "pending":
            uid0 = update.effective_user.id
            _lng = await get_user_lang(uid0)
            try:
                _amt = float(dep.get("amount") or 0.0)
            except (TypeError, ValueError):
                _amt = 0.0
            if dep.get("network") == "binance" and dep.get("pay_amount"):
                try:
                    _amt = float(dep["pay_amount"])   # v9.35 exact amount
                except (TypeError, ValueError):
                    pass
            return await _send_tracked(
                update, context,
                deposit_card_text(dep.get("network") or "bep20",
                                  _amt,
                                  dep.get("usdt_address") or "",
                                  d["deposit_id"],
                                  dep.get("expires_at") or "-", _lng),
                deposit_wait_kb(d["deposit_id"], _lng))
        await clear_user_state(update.effective_user.id)
        return await show_main_menu(update, context)
    if state == "buy_confirm":
        return await show_buy_country(update, context, d.get("ntype", "wa"))
    if state == "buy_country":
        return await show_buy_type(update, context)
    if state in ("dep_amount", "dep_custom"):
        return await show_dep_menu(update, context)
    if state == "dep_net":
        return await show_dep_amount(update, context)
    if state == "dep_hist":
        return await show_dep_menu(update, context)
    if state == "admin_add_country":
        return await show_admin_add_type(update, context)
    if state == "admin_set_rate":
        return await show_admin_set_rate(update, context)
    if state == "admin_ban":
        return await show_admin_ban_pick(update, context)
    if state in ("admin_add_type", "admin_add_phone", "admin_add_url",
                 "admin_set_rate_pick", "admin_ban_pick",
                 "admin_broadcast", "admin_set_wallet",
                 "admin_modify_user", "admin_modbal", "admin_user_view",
                 "admin_channels", "admin_ch_add_type",
                 "admin_ch_add", "admin_ch_remove",
                 "admin_ref_price", "admin_ref_vip",
                 "admin_ref_vip_add_id", "admin_ref_vip_add_rate",
                 "admin_ref_vip_remove",
                 "admin_refund_menu", "admin_check_number",
                 "admin_refund_send", "admin_check_refund",
                 "admin_bulkmanage", "admin_bulkmanage_min",
                 "admin_bulkmanage_disc"):
        return await show_admin_panel(update, context)
    # buy_type / dep_menu / awaiting_tx / admin_panel / None / unknown
    return await show_main_menu(update, context)


async def reshow_state(update, context, state, sdata):
    """Re-render the CURRENT screen (keyboard re-sync when unexpected text arrives)."""
    d = sdata or {}
    if state == "buy_type":
        return await show_buy_type(update, context)
    if state == "buy_country":
        return await show_buy_country(update, context, d.get("ntype", "wa"))
    if state == "buy_confirm":
        return await show_buy_confirm(update, context, d.get("ntype", "wa"), d.get("country"))
    if state == "dep_menu":
        return await show_dep_menu(update, context)
    if state == "dep_hist":
        return await show_dep_history(update, context)
    if state == "dep_net":
        # v9.22: re-open the NETWORK screen with the SAME amount
        # (state stays dep_net - no more main-menu/state mismatch)
        try:
            _amt = float(d.get("amount") or 0.0)
        except (TypeError, ValueError):
            _amt = 0.0
        if _amt > 0:
            return await show_dep_networks(update, context, _amt)
        return await show_dep_menu(update, context)
    if state == "dep_amount":
        return await show_dep_amount(update, context)
    if state == "admin_add_type":
        return await show_admin_add_type(update, context)
    if state == "admin_add_country":
        return await show_admin_add_country(update, context, d.get("ntype", "wa"))
    if state == "admin_set_rate_pick":
        return await show_admin_set_rate(update, context)
    if state == "admin_ban_pick":
        return await show_admin_ban_pick(update, context)
    if state == "admin_modify_user":
        return await show_admin_modify_user(update, context)
    if state == "admin_modbal":
        return await prompt_admin_modbal(update, context, (d or {}).get("target"))
    if state == "admin_user_view":
        return await admin_user_details(update, context, (d or {}).get("target"))
    if state == "admin_refund_menu":
        return await show_manage_refund(update, context)
    if state == "admin_check_refund":
        return await show_check_refund(update, context)
    if state == "admin_channels":
        return await show_admin_channels(update, context)
    if state == "admin_ch_add_type":
        return await show_admin_ch_type(update, context)
    if state == "admin_ch_add":
        return await show_admin_ch_add(update, context,
                                       (d or {}).get("privacy")
                                       or "public")
    if state == "admin_ch_remove":
        return await show_admin_ch_remove(update, context)
    if state == "admin_refer":
        return await show_admin_refer(update, context)
    if state == "admin_ref_price":
        return await prompt_admin_ref_price(update, context)
    if state == "admin_ref_vip":
        return await show_admin_ref_vip(update, context)
    if state == "admin_ref_vip_add_id":
        return await prompt_admin_vip_id(update, context)
    if state == "admin_ref_vip_add_rate":
        target = (d or {}).get("target")
        if not target:
            return await prompt_admin_vip_id(update, context)
        return await prompt_admin_vip_rate(update, context, target)
    if state == "admin_ref_vip_remove":
        return await show_admin_vip_remove(update, context)
    if state == "dep_custom":
        return await prompt_custom_amount(update, context,
                                          update.effective_user.id)
    return await show_main_menu(update, context)


# --------------------------------------------------------------------------- #
#  COMMAND HANDLERS
# --------------------------------------------------------------------------- #
async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_private(update):
        return      # v9.23 group silence
    user = update.effective_user
    # v9.24 REFERRAL: deep link  t.me/<bot>?start=ref<id>  binds a
    # BRAND-NEW user to the referrer once and forever (no re-bind,
    # no self-referral, no farming - see bind_referral).
    ref_from = None
    _arg = ((context.args or [""])[0] or "").strip()
    if _arg[:3].lower() == "ref" and _arg[3:].isdigit() and len(_arg) <= 16:
        try:
            ref_from = int(_arg[3:])
        except ValueError:
            ref_from = None
    if ref_from == user.id:
        ref_from = None
    pre_existing = await get_user(user.id) if ref_from else None
    rec = await get_or_create_user(user.id, user.username, user.first_name)
    if ref_from and pre_existing is None:
        try:
            if await bind_referral(user.id, ref_from):
                ru = await get_user(ref_from)
                if ru and not ru.get("is_banned"):
                    _rlang = await get_user_lang(ref_from)
                    try:
                        await context.bot.send_message(
                            chat_id=ref_from,
                            text=t(_rlang, "ref_new_ref",
                                   name=html_escape(user.first_name
                                                    or str(user.id))),
                            parse_mode=ParseMode.HTML)
                    except Exception:
                        pass
        except Exception:
            logger.warning("referral bind failed user=%s ref=%s",
                           user.id, ref_from, exc_info=True)
    if rec.get("is_banned"):
        await update.message.reply_text(
            t(lang_of(rec), "blocked"), parse_mode=ParseMode.HTML)
        return
    lang = (rec.get("lang") or "").strip()
    if not lang:
        # v9.16: first visit -> one-time language onboarding, then menu
        await _send_tracked(update, context, lang_pick_text(), lang_picker_kb())
        return
    # v9.23 FORCE JOIN: language done -> join gate before the menu
    if not is_admin(user.id) and await managed_channel_ids():
        pend = await pending_force_join(user.id)
        if pend:
            return await show_force_join(update, context, pend, lang)
    await _send_tracked(update, context,
                        await welcome_text(user.first_name, rec, lang),
                        main_menu_kb(is_admin(user.id), lang))


async def menu_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_private(update):
        return      # v9.23 group silence
    await show_main_menu(update, context)


async def language_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """v9.16: /language — reopen the language picker anytime."""
    if not _is_private(update):
        return      # v9.23 group silence
    user = update.effective_user
    rec = await get_or_create_user(user.id, user.username, user.first_name)
    if rec.get("is_banned"):
        await update.message.reply_text(
            t(lang_of(rec), "blocked"), parse_mode=ParseMode.HTML)
        return
    lang = (rec.get("lang") or "").strip()
    text = (t(lang, "lang_current", lang=LANG_NAMES.get(lang, lang))
            if lang else lang_pick_text())
    await _send_tracked(update, context, text, lang_picker_kb())


async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """v9.16: user tapped a language on the picker -> save + main menu."""
    q = update.callback_query
    code = (q.data or "").split(":")[-1]
    if code not in LANG_CODES:
        code = DEFAULT_LANG
    uid = q.from_user.id
    user = await get_user(uid)
    if user and user.get("is_banned"):
        await _send_tracked(update, context, t(lang_of(user), "blocked"), None)
        return
    await get_or_create_user(uid, q.from_user.username, q.from_user.first_name)
    await set_user_lang(uid, code)
    await _safe_answer(q, t(code, "lang_set_ok", lang=LANG_NAMES[code]))
    # v9.23 FORCE JOIN: right after the language step, the join gate
    if not is_admin(uid) and await managed_channel_ids():
        pend = await pending_force_join(uid)
        if pend:
            return await show_force_join(update, context, pend, code)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=menu_info_text(code), parse_mode=ParseMode.HTML,
        reply_markup=main_menu_kb(is_admin(uid), code),
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_private(update):
        return      # v9.23 group silence
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    # v9.23 FORCE JOIN: help stays locked until joined
    if not is_admin(uid) and await managed_channel_ids():
        pend = await pending_force_join(uid)
        if pend:
            return await show_force_join(update, context, pend, lang)
    txt = (
        f"{t(lang, 'help_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'help_lines')}\n"
        f"{DIV}\n"
        f"{t(lang, 'help_cta')}"
    )
    await _send_tracked(update, context, txt,
                        main_menu_kb(is_admin(uid), lang))


def _mask_addr(a: str) -> str:
    """Short form for logs: 0x8374...f426a"""
    a = (a or "").strip()
    return "%s\u2026%s" % (a[:12], a[-6:]) if len(a) > 20 else (a or "-")


async def trace_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin: /trace [DEPID] - full deposit audit trail."""
    if not _is_private(update):
        return      # v9.23 group silence
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("\U0001F6AB Admins only.")
        return
    arg = ((context.args or [""])[0] or "").strip().upper()
    async with adb() as db:
        if arg:
            cur = await db.execute(
                "SELECT * FROM deposit_trace WHERE deposit_id=? "
                "ORDER BY id", (arg,))
            head = f"\U0001F50D <b>TRACE {html_escape(arg)}</b>"
        else:
            cur = await db.execute(
                "SELECT * FROM deposit_trace ORDER BY id DESC LIMIT 25")
            head = "\U0001F50D <b>DEPOSIT TRACE</b> \u2014 last 25"
        rows = await cur.fetchall()
        await cur.close()
    if not rows:
        await update.message.reply_text(head + "\n\nNo events yet.",
                                        parse_mode=ParseMode.HTML)
        return
    icon = {"credited": "\u2705", "order_created": "\U0001F195",
            "amount_mismatch": "\u274C", "txid_replay": "\U0001F501",
            "locked": "\U0001F512", "wallet_changed": "\U0001F511",
            "wallet_rotated": "\U0001F504"}
    lines = [head, DIV]
    for r in rows:
        d = dict(r)
        t = time.strftime("%d %b %H:%M UTC", time.gmtime(d.get("ts") or 0))
        ev = d.get("event") or "?"
        lines.append(
            f"{icon.get(ev, '\u2022')} <code>{d.get('deposit_id')}</code> "
            f"{html_escape(ev)} \u2014 {t}\n"
            f"&nbsp;&nbsp;net={html_escape(str(d.get('network')))} "
            f"user=<code>{d.get('user_id')}</code>"
            + (f"\n&nbsp;&nbsp;{html_escape(d['detail'])}"
               if d.get("detail") else ""))
    await update.message.reply_text("\n".join(lines[:90]),
                                    parse_mode=ParseMode.HTML)


async def admin_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_private(update):
        return      # v9.23 group silence
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("\U0001F6AB Admins only.")
        return
    await show_admin_panel(update, context)


# --------------------------------------------------------------------------- #
#  v9.23 FORCE JOIN ENGINE
#  start -> language -> JOIN (mandatory) -> main menu. Nothing works before
#  the user joins every managed chat. Public chats verify live membership;
#  private chats unlock the moment the user's JOIN REQUEST arrives (the
#  bot NEVER approves it - owner rule). Leaving a public chat re-locks.
# --------------------------------------------------------------------------- #
async def show_force_join(update, context, rows=None, lang=None):
    """The locked screen: JOIN CHANNEL / JOIN GROUP buttons + Verify.
    User state is NOT cleared - a running deposit survives the gate."""
    uid = update.effective_user.id
    if lang is None:
        lang = await get_user_lang(uid)
    if rows is None:
        rows = await pending_force_join(uid)
    if not rows:
        return await show_main_menu(update, context)
    await _send_tracked(update, context,
                        force_join_text(rows, lang),
                        force_join_kb(rows, lang))


async def _fj_unlock(update, context, q, lang):
    """All chats joined: welcome card replaces the join screen + menu."""
    uid = q.from_user.id
    await _safe_answer(q)
    await clear_user_state(uid)
    try:
        await q.edit_message_text(pem(t(lang, "fj_done")),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=None)
    except Exception:
        pass
    try:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=menu_info_text(lang), parse_mode=ParseMode.HTML,
            reply_markup=main_menu_kb(is_admin(uid), lang))
    except Exception:
        pass


async def fj_verify_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """JOIN screen Verify button: live re-check of every still-pending
    chat, unlock the moment all are met. Single-answer, spam-cooled."""
    q = update.callback_query
    uid = q.from_user.id
    user = await get_user(uid)
    if user and user.get("is_banned"):
        await _safe_answer(q, t(lang_of(user), "blocked"))
        return
    lang = lang_of(user)
    lock = f"fjv:{uid}"
    now = time.monotonic()
    if now - (context.bot_data.get(lock) or 0.0) < 2.0:
        await _safe_answer(q)
        return
    context.bot_data[lock] = now
    rows = await pending_force_join(uid)
    if not rows:
        return await _fj_unlock(update, context, q, lang)
    for r in rows:                    # public chats: live membership check
        try:
            m = await context.bot.get_chat_member(r["chat_id"], uid)
            if getattr(m, "status", "") in (
                    "member", "administrator", "creator", "restricted"):
                await mark_join(uid, r["chat_id"], "joined")
        except Exception as e:
            # v9.36: a chat the BOT itself can no longer reach (kicked,
            # deleted) must never lock the user forever. Probe the bot's
            # own membership: also unreachable -> chat is broken, the
            # gate auto-passes it for this user (and pending_force_join
            # filters it for everyone from now on).
            try:
                _bid = getattr(context.bot, "id", None)
                if not _bid:
                    continue          # stub bot in tests - no verdict
                await context.bot.get_chat_member(int(r["chat_id"]), _bid)
            except Exception as e2:
                if _fj_chat_unreachable_err(str(e2)):
                    _FJ_BROKEN.add(int(r["chat_id"]))
                    await mark_join(uid, r["chat_id"], "joined")
                    logger.warning("force-join chat %s unreachable for "
                                   "the bot (%s / %s) -> gate auto-passed "
                                   "for user %s", r["chat_id"],
                                   str(e)[:60], str(e2)[:60], uid)
    rows = await pending_force_join(uid)
    if not rows:
        return await _fj_unlock(update, context, q, lang)
    await _safe_answer(q, t(lang, "fj_toast_no"))


async def on_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """PRIVATE chats: the user can only SEND A REQUEST. The request
    itself IS the verification - the bot never approves it (owner rule).
    The moment the request arrives the user is auto-verified."""
    req = update.chat_join_request
    if req is None:
        return
    chat_id = int(req.chat.id)
    if chat_id not in await managed_channel_ids():
        return
    uid = int(req.from_user.id)
    await mark_join(uid, chat_id, "requested")
    user = await get_user(uid)
    if user and not user.get("is_banned") and not is_admin(uid) \
            and (user.get("lang") or "").strip():
        rows = await pending_force_join(uid)
        if not rows:
            lang = user.get("lang")
            try:
                await context.bot.send_message(
                    chat_id=uid, text=pem(t(lang, "fj_dm")),
                    parse_mode=ParseMode.HTML,
                    reply_markup=main_menu_kb(False, lang))
            except Exception:
                pass


async def on_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Real-time membership tracker for managed chats (bot is admin
    there, so Telegram streams chat_member updates):
    joined -> verified + auto menu, left/kicked -> locked again."""
    cmu = update.chat_member
    if cmu is None:
        return
    chat_id = int(cmu.chat.id)
    if chat_id not in await managed_channel_ids():
        return
    new = cmu.new_chat_member
    uid = getattr(getattr(new, "user", None), "id", None)
    if not uid:
        return
    st = getattr(new, "status", "")
    if st in ("member", "administrator", "creator", "restricted"):
        await mark_join(uid, chat_id, "joined")
        user = await get_user(uid)
        if user and not user.get("is_banned") and not is_admin(uid) \
                and (user.get("lang") or "").strip():
            rows = await pending_force_join(uid)
            if not rows:
                lang = user.get("lang")
                try:
                    await context.bot.send_message(
                        chat_id=uid, text=pem(t(lang, "fj_dm")),
                        parse_mode=ParseMode.HTML,
                        reply_markup=main_menu_kb(False, lang))
                except Exception:
                    pass
    elif st in ("left", "kicked"):
        row = await get_join_row(uid, chat_id)
        if row and (row.get("state") or "") in ("joined", "requested"):
            await mark_join(uid, chat_id, "pending")


# --------------------------------------------------------------------------- #
#  TEXT ROUTER  (the heart of the bot)
# #  Priority: 1) global buttons  2) Back  3) flow buttons  4) admin buttons
#            5) text-input states  6) unknown text -> keyboard re-sync
# --------------------------------------------------------------------------- #
async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_private(update):
        return          # v9.23 GROUP SILENCE: never talk in groups/channels
    msg = update.message or update.edited_message
    if msg is None or not msg.text:
        return          # stale/queued non-text update - nothing to route
    text = msg.text.strip()
    uid = update.effective_user.id
    user = await get_user(uid)
    if user is None:
        # v9.20: a user who never ran /start still gets a DB row, so
        # states, balances and stats work from the very first message.
        user = await get_or_create_user(
            uid, update.effective_user.username,
            update.effective_user.first_name)
    if user.get("is_banned"):
        await msg.reply_text(
            t(lang_of(user), "blocked"), parse_mode=ParseMode.HTML)
        return

    L = lang_of(user)   # v9.16: this user's language (EN fallback)
    state, sdata = await get_user_state(uid)
    adm = is_admin(uid)

    # v9.23 FORCE JOIN: the strongest gate - before ANY routing. Until
    # every managed chat is joined, NOTHING else is reachable.
    if not adm and await managed_channel_ids():
        pend = await pending_force_join(uid)
        if pend:
            return await show_force_join(update, context, pend, L)

    # ---------- 1) Global buttons: ALWAYS work (cancel any pending input) ----------
    # v9.22: btn_eq matches icon-stripped keyboards AND old emoji keyboards
    if btn_eq(text, t(L, "btn_back")):
        return await show_main_menu(update, context)
    if btn_eq(text, t(L, "btn_buy")):
        return await show_buy_type(update, context)
    if btn_eq(text, t(L, "btn_profile")):
        return await show_profile(update, context)
    if btn_eq(text, t(L, "btn_deposit")):
        return await show_dep_menu(update, context)
    if btn_eq(text, t(L, "btn_support")):
        return await show_support(update, context)
    if btn_eq(text, t(L, "btn_refer")) and ref_is_on():
        return await show_refer(update, context)   # v9.24 Refer & Earn
    if btn_eq(text, t(L, "btn_active")):
        return await show_active_numbers(update, context)   # v9.27
    if btn_eq(text, t(L, "btn_ubulk")):
        return await show_user_bulkbuy(update, context)   # v9.31
    if btn_eq(text, BTN_ADMIN) and adm:
        return await show_admin_panel(update, context)

    # ---------- 2) Back / Cancel ----------
    if btn_eq(text, BTN_BACK):
        return await go_back(update, context, state, sdata)

    if btn_eq(text, BTN_CANCEL):
        if state == "awaiting_txid" and \
                (sdata or {}).get("deposit_id"):
            await cancel_pending_deposit(uid, sdata["deposit_id"])
        if adm and state and state.startswith("admin"):
            return await show_admin_panel(update, context)
        return await show_main_menu(update, context)

    # ---------- 3) BUY flow ----------
    if state == "buy_type":
        if btn_eq(text, t(L, "btn_wa")):
            return await show_buy_country(update, context, "wa")
        if btn_eq(text, t(L, "btn_tg")):
            return await show_buy_country(update, context, "tg")

    if state == "buy_country":
        ctry = country_from_button(text)
        if ctry:
            return await show_buy_confirm(update, context, (sdata or {}).get("ntype", "wa"), ctry)

    if state == "buy_confirm" and \
            _bt(text).startswith(_bt(t(L, "btn_buy_now", price=""))) \
            and _bt(text):
        d = sdata or {}
        return await do_purchase(update, context, uid, d.get("ntype", "wa"), d.get("country"))

    # ---------- 4) DEPOSIT flow ----------
    if state == "dep_menu" and btn_eq(text, t(L, "btn_dep_new")):
        return await show_dep_amount(update, context)

    if state == "dep_menu" and btn_eq(text, t(L, "btn_dep_hist")):
        return await show_dep_history(update, context)

    if btn_eq(text, t(L, "btn_cancel_dep")) and state == "awaiting_txid":
        dep_id = (sdata or {}).get("deposit_id")
        if dep_id:
            await cancel_pending_deposit(uid, dep_id)
        await clear_user_state(uid)
        return await _send_tracked(update, context,
                                   t(L, "dep_cancelled"),
                                   main_menu_kb(adm, L))

    # ---------- 5) ADMIN panel buttons + admin flow buttons ----------
    if adm:
        if btn_eq(text, BTN_ADD_STOCK):
            return await show_admin_add_type(update, context)
        if btn_eq(text, BTN_BULK_MANAGE):
            return await show_admin_bulkmanage(update, context)   # v9.34
        if btn_eq(text, BTN_STOCK_STATS):
            return await admin_stock_stats(update, context)
        if btn_eq(text, BTN_PENDING):
            return await admin_pending_deposits(update, context)
        if btn_eq(text, BTN_STATS):
            return await admin_statistics(update, context)
        if btn_eq(text, BTN_SET_RATE):
            return await show_admin_set_rate(update, context)
        if btn_eq(text, BTN_BROADCAST):
            return await show_admin_broadcast(update, context)
        if btn_eq(text, BTN_SET_WALLET):
            return await show_admin_set_wallet(update, context)
        if btn_eq(text, BTN_BAN):
            return await show_admin_ban_pick(update, context)
        if btn_eq(text, BTN_MODIFY_USER):
            return await show_admin_modify_user(update, context)
        if btn_eq(text, BTN_MANAGE_REFUND):
            return await show_manage_refund(update, context)   # v9.27 hub
        if btn_eq(text, BTN_ALL_BAL):
            return await show_admin_allbal(update, context)   # v9.38
        if btn_eq(text, BTN_ALLBAL_REFRESH):
            return await show_admin_allbal(update, context)   # v9.38 live refresh
        if btn_eq(text, BTN_CHANNELS):
            return await show_admin_channels(update, context)
        if btn_eq(text, BTN_REFER_MGMT):
            return await show_admin_refer(update, context)
        if btn_eq(text, BTN_MANAGE_ADMINS):
            return await show_admin_manage(update, context)   # v9.41

        if state == "admin_refer":
            if btn_eq(text, BTN_REF_PRICE):
                return await prompt_admin_ref_price(update, context)
            if btn_eq(text, BTN_REF_VIP):
                return await show_admin_ref_vip(update, context)
            if btn_eq(text, BTN_REF_TOGGLE_ON) or btn_eq(text, BTN_REF_TOGGLE_OFF):
                return await toggle_ref_system(update, context)

        if state == "admin_ref_vip":
            if btn_eq(text, BTN_REF_VIP_ADD):
                return await prompt_admin_vip_id(update, context)
            if btn_eq(text, BTN_REF_VIP_REM):
                return await show_admin_vip_remove(update, context)
            if btn_eq(text, BTN_REF_VIP_LIST):
                return await show_admin_vip_list(update, context)

        if state == "admin_channels":
            if btn_eq(text, BTN_CH_ADD):
                return await show_admin_ch_type(update, context)
            if btn_eq(text, BTN_CH_REMOVE):
                return await show_admin_ch_remove(update, context)
            if btn_eq(text, BTN_CH_LIST):
                return await show_admin_ch_list(update, context)

        if state == "admin_refund_menu":
            if btn_eq(text, BTN_CHECK_NUMBER):
                return await show_check_number(update, context)
            if btn_eq(text, BTN_REFUND_SEND):
                return await show_refund_send(update, context)
            if btn_eq(text, BTN_CHECK_REFUND):
                return await show_check_refund(update, context)

        if state == "admin_check_number":
            if URL_RE.search(text) or "|" in text:
                return await run_check_number(update, context, uid, text)
            # any other text -> re-show the screen (stay in state)
            return await show_check_number(update, context)

        if state == "admin_refund_send":
            if URL_RE.search(text) or "|" in text:
                return await run_refund_send(update, context, uid, text)
            return await show_refund_send(update, context)

        if state == "admin_check_refund":
            return await run_check_and_refund(update, context, uid, text)

        if state == "admin_add_type":
            if btn_eq(text, BTN_WA_STOCK):
                return await show_admin_add_country(update, context, "wa")
            if btn_eq(text, BTN_TG_STOCK):
                return await show_admin_add_country(update, context, "tg")

        if state == "admin_add_country":
            ctry = country_from_button(text)
            if ctry:
                return await prompt_admin_add_phone(
                    update, context, (sdata or {}).get("ntype", "wa"), ctry)

        if state == "admin_set_rate_pick":
            if _bt(text).startswith("WhatsApp \u2014"):
                return await prompt_admin_set_rate(update, context, "wa")
            if _bt(text).startswith("Telegram \u2014"):
                return await prompt_admin_set_rate(update, context, "tg")

        if state == "admin_ban_pick":
            if btn_eq(text, BTN_BAN_USER):
                return await prompt_admin_ban(update, context, "ban")
            if btn_eq(text, BTN_UNBAN_USER):
                return await prompt_admin_ban(update, context, "unban")

    # ---------- 6) Text-input states (button taps never reach here) ----------
    if state in INPUT_STATES:
        return await handle_state_text(update, context, state, sdata, text)

    # ---------- 7) v9.27: a bare phone number opens its Get OTP screen -----
    # Active Numbers flow: tap a number to copy, send it back here and
    # the number opens exactly like the post-purchase receipt (Get OTP;
    # the background poller restarts too - no time limit on the code).
    if not state:
        ph = normalize_phone(text)
        if ph:
            stock = await find_active_stock(uid, ph)
            if stock:
                return await open_active_number(update, context, uid, stock)

    # ---------- 8) Unknown text -> re-sync keyboard for the current screen ----------
    if state:
        return await reshow_state(update, context, state, sdata)
    return await show_main_menu(update, context)

# --------------------------------------------------------------------------- #
#  BUY FLOW  (purchase)
# --------------------------------------------------------------------------- #
async def do_purchase(update, context, uid, ntype, country):
    """In-flight lock: a double-tap on Buy can never charge twice."""
    lock = f"buying:{uid}"
    if context.bot_data.get(lock):
        if update.callback_query:
            try:
                await update.callback_query.answer(
                    t(await get_user_lang(uid), "toast_processing"),
                    show_alert=True)
            except Exception:
                pass
        return
    context.bot_data[lock] = True
    try:
        return await _do_purchase_impl(update, context, uid, ntype, country)
    finally:
        context.bot_data.pop(lock, None)


async def purchase_number(uid, ntype, country, rate,
                          ref_on=False, ref_rate=0.0):
    """ATOMIC purchase (v9.14, v9.24 referral-aware).
    Balance check, stock claim, balance deduct, order insert AND the
    referrer's commission run in ONE BEGIN IMMEDIATE transaction. The
    stock row is claimed with a status='available' guard (two buyers can
    never receive the same number) and the deduct has a balance>=? guard
    (balance can never go negative). The per-loop lock serialises only
    this transaction; everything else in the bot stays fully concurrent.
    REFERRAL (v9.27): when the buyer came from a referral link, a
    PENDING commission row (VIP rate if the referrer is VIP, else the
    global rate) is recorded INSIDE the same transaction and the earning
    row is UNIQUE per order id - no double row, no loot. The money moves
    only when the OTP arrives (pay_pending_referral).
    Returns {ok, err('no_balance'|'no_stock'), stock, order_id, balance,
    ref:{referrer,amount}|None}."""
    conn = await _get_shared_db()
    db_type = "whatsapp" if ntype == "wa" else "telegram"
    async with _tx_lock():
        await conn.execute("BEGIN IMMEDIATE")
        try:
            cur = await conn.execute(
                "SELECT balance, referred_by FROM users "
                "WHERE telegram_id=?", (uid,))
            row = await cur.fetchone()
            await cur.close()
            bal = float(row[0]) if row and row[0] is not None else 0.0
            ref_by = None
            if row and row[1] is not None:
                try:
                    ref_by = int(row[1])
                except (TypeError, ValueError):
                    ref_by = None
            if ref_by == uid:
                ref_by = None   # belt-and-braces: never pay yourself
            if bal + _MONEY_EPS < rate:   # v9.35: epsilon (float noise)
                await conn.execute("ROLLBACK")
                return {"ok": False, "err": "no_balance", "balance": bal}

            stock = None
            cur = await conn.execute(
                "SELECT id, phone_number, otp_url, otp_blocked, "
                "refund_state FROM stock "
                "WHERE status='available' AND number_type=? AND country=? "
                "ORDER BY id LIMIT 5", (db_type, country))
            cands = await cur.fetchall()
            await cur.close()
            for c in cands:
                cur = await conn.execute(
                    "UPDATE stock SET status='sold', sold_to=?, "
                    "sold_at=datetime('now') "
                    "WHERE id=? AND status='available'", (uid, c["id"]))
                claimed = cur.rowcount == 1
                await cur.close()
                if claimed:
                    # v9.28 CRITICAL FIX: the dict MUST carry otp_url -
                    # it used to hold only id + phone, so start_otp_poller
                    # hit 'No OTP URL on stock' and SKIPPED every fresh
                    # purchase: no poller ever ran, the buyer could only
                    # press Get OTP manually and a code landing while he
                    # waited silently never arrived (real money loss).
                    stock = {"id": c["id"],
                             "phone_number": c["phone_number"],
                             "otp_url": c["otp_url"],
                             "otp_blocked": c["otp_blocked"],
                             "refund_state": c["refund_state"]}
                    break
            if stock is None:
                await conn.execute("ROLLBACK")
                return {"ok": False, "err": "no_stock"}

            cur = await conn.execute(
                "UPDATE users SET balance=balance-?, "
                "total_spent=total_spent+?, "
                "total_purchased=total_purchased+1, "
                "updated_at=datetime('now') "
                "WHERE telegram_id=? AND balance>=?",
                # v9.35: epsilon - float-noise balance still affords
                (rate, rate, uid, rate - _MONEY_EPS))
            paid = cur.rowcount == 1
            await cur.close()
            if not paid:
                await conn.execute("ROLLBACK")
                return {"ok": False, "err": "no_balance", "balance": bal}

            order_id = f"ORD{uuid.uuid4().hex[:8].upper()}"
            await conn.execute(
                "INSERT INTO orders(order_id,user_id,number_type,country,"
                "total_amount,quantity,numbers,rate_at_purchase) "
                "VALUES(?,?,?,?,?,?,?,?)",
                (order_id, uid, ntype, country, rate, 1,
                 json.dumps([stock["phone_number"]]), rate))
            # v9.27: link the stock row to its order - the referral
            # payout (on OTP arrival) and the refund cancel both read it.
            await conn.execute(
                "UPDATE stock SET order_id=? WHERE id=?",
                (order_id, stock["id"]))

            # ---- v9.27 REFERRAL COMMISSION (PENDING, pays on OTP) -----
            # The commission is RECORDED here but NEVER credited at
            # purchase: the row stays 'pending' and pay_pending_referral
            # credits the referrer only when the buyer's OTP actually
            # arrives. A refunded number's row is cancelled instead -
            # commission exists ONLY for numbers that delivered.
            ref = None
            if ref_on and ref_rate > 0 and ref_by:
                vip_amt = None
                cur = await conn.execute(
                    "SELECT rate FROM ref_vip WHERE user_id=?", (ref_by,))
                _v = await cur.fetchone()
                await cur.close()
                if _v and _v[0] is not None:
                    try:
                        _f = float(_v[0])
                        if math.isfinite(_f) and _f >= 0:
                            vip_amt = _f
                    except (TypeError, ValueError):
                        vip_amt = None
                amt = vip_amt if vip_amt is not None else float(ref_rate)
                if amt > 0:
                    cur = await conn.execute(
                        "INSERT OR IGNORE INTO ref_earnings"
                        "(order_id,buyer_id,referrer_id,amount,status) "
                        "VALUES(?,?,?,?, 'pending')",
                        (order_id, uid, ref_by, amt))
                    earned = cur.rowcount == 1
                    await cur.close()
                    if earned:
                        ref = {"referrer": ref_by, "amount": amt,
                               "pending": True}

            cur = await conn.execute(
                "SELECT balance FROM users WHERE telegram_id=?", (uid,))
            row = await cur.fetchone()
            await cur.close()
            new_bal = float(row[0]) if row and row[0] is not None else 0.0
            await conn.commit()
            return {"ok": True, "stock": stock, "order_id": order_id,
                    "balance": new_bal, "ref": ref}
        except Exception:
            try:
                await conn.execute("ROLLBACK")
            except Exception:
                pass
            raise


def bulk_unit_rate(rate, n, disc_min=BULK_DISCOUNT_MIN,
                   disc_per=BULK_DISCOUNT):
    """v9.31: per-number rate for a USER bulk order - at `disc_min` or
    more numbers the buyer gets `disc_per` $ OFF per number, never
    below zero. v9.34: threshold + amount are owner-configurable
    (Admin Panel > Bulk Manage). Pure function so the discount math
    is directly testable."""
    try:
        r = float(rate)
    except (TypeError, ValueError):
        r = 0.0
    if not math.isfinite(r) or r < 0:
        r = 0.0
    if int(n) >= disc_min:
        r = max(r - disc_per, 0.0)
    return round(r, 4)


async def bulk_purchase(uid, ntype, n, unit,
                        ref_on=False, ref_rate=0.0):
    """v9.31 USER BULK BUY ENGINE (mirror of purchase_number for many
    numbers at once). ONE BEGIN IMMEDIATE transaction:
      * balance check against the FULL expected total,
      * claim up to n rows with the status='available' guard (a
        concurrent buyer can never share a number - rows lost to a race
        are simply not charged),
      * guarded deduct (balance>=total -> can never go negative),
      * ONE order row PER NUMBER (quantity=1, rate_at_purchase=unit) -
        the owner's Refund Send / Check Number / OTP-price lookups then
        work on bulk numbers EXACTLY like on single buys,
      * stock.order_id link per row (poller + sweeper + refund wire-up),
      * PENDING referral commission per order (pays on OTP arrival,
        cancelled on refund - identical to single-buy semantics).
    Returns {ok, err, balance, rows:[{id, phone_number, otp_url,
    order_id, otp_blocked, refund_state, country}], unit, total}."""
    conn = await _get_shared_db()
    db_type = "whatsapp" if ntype == "wa" else "telegram"
    n = max(0, int(n))
    async with _tx_lock():
        await conn.execute("BEGIN IMMEDIATE")
        try:
            cur = await conn.execute(
                "SELECT balance, referred_by FROM users "
                "WHERE telegram_id=?", (uid,))
            row = await cur.fetchone()
            await cur.close()
            bal = float(row[0]) if row and row[0] is not None else 0.0
            ref_by = None
            if row and row[1] is not None:
                try:
                    ref_by = int(row[1])
                except (TypeError, ValueError):
                    ref_by = None
            if ref_by == uid:
                ref_by = None   # belt-and-braces: never pay yourself

            cur = await conn.execute(
                "SELECT id, phone_number, otp_url, otp_blocked, "
                "refund_state, country FROM stock "
                "WHERE status='available' AND number_type=? "
                "AND COALESCE(otp_url,'')!='' ORDER BY id LIMIT ?",
                (db_type, n))
            cands = await cur.fetchall()
            await cur.close()
            claimed = []
            for c in cands:
                cur = await conn.execute(
                    "UPDATE stock SET status='sold', sold_to=?, "
                    "sold_at=datetime('now') "
                    "WHERE id=? AND status='available'", (uid, c["id"]))
                won = cur.rowcount == 1
                await cur.close()
                if won:
                    claimed.append(c)
                if len(claimed) >= n:
                    break
            if not claimed:
                await conn.execute("ROLLBACK")
                return {"ok": False, "err": "no_stock", "balance": bal}

            total = round(unit * len(claimed), 2)
            cur = await conn.execute(
                "UPDATE users SET balance=balance-?, "
                "total_spent=total_spent+?, "
                "total_purchased=total_purchased+?, "
                "updated_at=datetime('now') "
                "WHERE telegram_id=? AND balance>=?",
                (total, total, len(claimed), uid,
                 total - _MONEY_EPS))   # v9.35: epsilon
            paid = cur.rowcount == 1
            await cur.close()
            if not paid:
                await conn.execute("ROLLBACK")
                return {"ok": False, "err": "no_balance", "balance": bal}

            # one pending referral amount decided ONCE (VIP rate first)
            ref_amt = 0.0
            if ref_on and ref_rate > 0 and ref_by:
                vip_amt = None
                cur = await conn.execute(
                    "SELECT rate FROM ref_vip WHERE user_id=?", (ref_by,))
                _v = await cur.fetchone()
                await cur.close()
                if _v and _v[0] is not None:
                    try:
                        _f = float(_v[0])
                        if math.isfinite(_f) and _f >= 0:
                            vip_amt = _f
                    except (TypeError, ValueError):
                        vip_amt = None
                ref_amt = vip_amt if vip_amt is not None else float(ref_rate)

            rows = []
            for c in claimed:
                order_id = f"ORD{uuid.uuid4().hex[:8].upper()}"
                await conn.execute(
                    "INSERT INTO orders(order_id,user_id,number_type,"
                    "country,total_amount,quantity,numbers,"
                    "rate_at_purchase) VALUES(?,?,?,?,?,1,?,?)",
                    (order_id, uid, ntype,
                     (c["country"] or "USA"), unit,
                     json.dumps([c["phone_number"]]), unit))
                await conn.execute(
                    "UPDATE stock SET order_id=? WHERE id=?",
                    (order_id, c["id"]))
                if ref_amt > 0:
                    await conn.execute(
                        "INSERT OR IGNORE INTO ref_earnings"
                        "(order_id,buyer_id,referrer_id,amount,status) "
                        "VALUES(?,?,?,?, 'pending')",
                        (order_id, uid, ref_by, ref_amt))
                rows.append({"id": c["id"],
                             "phone_number": c["phone_number"],
                             "otp_url": c["otp_url"],
                             "otp_blocked": c["otp_blocked"],
                             "refund_state": c["refund_state"],
                             "country": c["country"],
                             "order_id": order_id})

            cur = await conn.execute(
                "SELECT balance FROM users WHERE telegram_id=?", (uid,))
            new_bal = float((await cur.fetchone())[0] or 0.0)
            await cur.close()
            await conn.commit()
            return {"ok": True, "rows": rows, "balance": new_bal,
                    "unit": unit, "total": total}
        except Exception:
            try:
                await conn.execute("ROLLBACK")
            except Exception:
                pass
            raise


async def _do_purchase_impl(update, context, uid, ntype, country):
    rate = float(await get_setting(
        "whatsapp_rate" if ntype == "wa" else "telegram_rate"))
    # v9.24: referral switch + global rate read BEFORE the transaction
    ref_on = await ref_enabled()
    ref_rate = await get_ref_rate() if ref_on else 0.0
    res = await purchase_number(uid, ntype, country, rate,
                                ref_on=ref_on, ref_rate=ref_rate)
    label = "WhatsApp" if ntype == "wa" else "Telegram"
    lang = await get_user_lang(uid)

    if not res["ok"]:
        if res["err"] == "no_balance":
            bal = res.get("balance") or 0.0
            await clear_user_state(uid)
            await _send_tracked(update, context,
                                insufficient_text(rate, bal, rate - bal, lang),
                                insufficient_kb(lang))
        else:
            # Back returns to the country list so the user can pick another
            await set_user_state(uid, "buy_country", {"ntype": ntype})
            await _send_tracked(update, context,
                                out_of_stock_text(label, country, lang),
                                back_home_kb(lang))
        return

    stock = res["stock"]
    order_id = res["order_id"]
    await clear_user_state(uid)

    # Receipt is sent as a FRESH message — it is NEVER edited or deleted,
    # so the user can always come back to the Get OTP button later.
    receipt_txt = purchase_success_text(stock["phone_number"], label, country,
                                        rate, order_id, lang)
    if update.callback_query:
        try:
            await update.callback_query.edit_message_text(
                receipt_txt, parse_mode=ParseMode.HTML,
                reply_markup=otp_kb(stock["id"], lang),
            )
        except Exception:
            await context.bot.send_message(
                chat_id=uid, text=receipt_txt, parse_mode=ParseMode.HTML,
                reply_markup=otp_kb(stock["id"], lang),
            )
    else:
        await update.message.reply_text(
            receipt_txt, parse_mode=ParseMode.HTML,
            reply_markup=otp_kb(stock["id"], lang),
        )
    # Reset the BOTTOM keyboard to the main menu (fresh message — the
    # receipt above is never touched).
    await context.bot.send_message(
        chat_id=uid, text=menu_footer_text(lang), parse_mode=ParseMode.HTML,
        reply_markup=main_menu_kb(is_admin(uid), lang),
    )

    await forward_order_history(context, uid, ntype, country, rate, stock, order_id)
    start_otp_poller(context, uid, stock)
    # v9.27: the referral commission is NOT paid here anymore - it stays
    # pending until the buyer's OTP actually arrives (pay_pending_referral).


# --------------------------------------------------------------------------- #
#  v9.31 USER-SIDE BULK BUY
#  Menu -> pick type -> type HOW MANY -> confirm -> otphub.<n><country>.txt
#  File lines are the SAME 'phone | url' stock format. Every number gets
#  its own order row (discounted unit rate) so Refund Send matches each
#  number exactly like a normal buy. Paid from the buyer's balance only
#  (user balance ke anusar), 30+ numbers get $0.01/number off.
# --------------------------------------------------------------------------- #
USER_BULK_POLLERS = 10   # live pollers per bulk order (sweeper covers rest)


def _ubulk_type_kb(lang="en"):
    return _ikb(
        [
            [InlineKeyboardButton(t(lang, "btn_wa"), callback_data="ubulk:type:wa",
                                  style=KeyboardButtonStyle.SUCCESS),
             InlineKeyboardButton(t(lang, "btn_tg"), callback_data="ubulk:type:tg",
                                  style=KeyboardButtonStyle.PRIMARY)],
            [InlineKeyboardButton(t(lang, "btn_back"), callback_data="ubulk:back",
                                  style=KeyboardButtonStyle.DANGER)],
        ], _BIC_BUY_TYPE
    )


def _ubulk_confirm_kb(lang="en", price="0.00"):
    return _ikb(
        [
            [InlineKeyboardButton(t(lang, "btn_buy_now", price=price),
                                  callback_data="ubulk:go",
                                  style=KeyboardButtonStyle.SUCCESS),
             InlineKeyboardButton("\u274C", callback_data="ubulk:cancel",
                                  style=KeyboardButtonStyle.DANGER)],
            [InlineKeyboardButton(t(lang, "btn_back"), callback_data="ubulk:back",
                                  style=KeyboardButtonStyle.DANGER)],
        ], dict(_BIC_BUY_CONFIRM, **{"\u274C": _BIC_X})
    )


async def show_user_bulkbuy(update, context):
    """v9.31: Bulk Buy landing card - live per-type availability + rate
    + the owner-set discount rule (Bulk Manage), then the type picker."""
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    counts, _tot = await get_stock_counts()
    wa_n = sum((counts.get("whatsapp") or {}).values())
    tg_n = sum((counts.get("telegram") or {}).values())
    wa_rate = float(await get_setting("whatsapp_rate") or 0)
    tg_rate = float(await get_setting("telegram_rate") or 0)
    dmin, damt = await bulk_disc_params()   # v9.34 owner-configurable
    await clear_user_state(uid)
    context.user_data.pop("ubulk", None)
    await _send_tracked(
        update, context,
        t(lang, "ub_pick", wa_n=wa_n, tg_n=tg_n,
          wa_rate="%.2f" % wa_rate, tg_rate="%.2f" % tg_rate,
          dmin=dmin, damt="%.2f" % damt),
        _ubulk_type_kb(lang),
    )


async def show_user_bulkqty(update, context, ntype):
    """v9.31: quantity card for one type; state 'user_bulkbuy' waits for
    the typed quantity."""
    uid = update.effective_user.id
    lang = await get_user_lang(uid)
    await set_user_state(uid, "user_bulkbuy", {"ntype": ntype})
    context.user_data.pop("ubulk", None)
    db_type = "whatsapp" if ntype == "wa" else "telegram"
    counts, _tot = await get_stock_counts()
    avail = sum((counts.get(db_type) or {}).values())
    rate = float(await get_setting(
        "whatsapp_rate" if ntype == "wa" else "telegram_rate") or 0)
    u = await get_user(uid) or {}
    bal = float(u.get("balance") or 0.0)
    label = "WhatsApp" if ntype == "wa" else "Telegram"
    dmin, damt = await bulk_disc_params()   # v9.34 owner-configurable
    await _send_tracked(
        update, context,
        t(lang, "ub_qty", label=label, n=avail, rate="%.2f" % rate,
          bal="%.2f" % bal, dmin=dmin, damt="%.2f" % damt),
        _ikb([[InlineKeyboardButton(t(lang, "btn_back"),
                                    callback_data="ubulk:back",
                                    style=KeyboardButtonStyle.DANGER)]],
             _BIC_NAV),
    )


async def handle_user_bulk_qty(update, context, uid, text, sdata):
    """v9.31: the typed quantity -> strict int -> stock/balance checks
    -> confirmation card. NOTHING is charged here."""
    lang = await get_user_lang(uid)
    d = sdata or {}
    ntype = d.get("ntype")
    if ntype not in ("wa", "tg"):
        await clear_user_state(uid)
        await _send_tracked(update, context, t(lang, "ub_expired"),
                            main_menu_kb(is_admin(uid), lang))
        return
    db_type = "whatsapp" if ntype == "wa" else "telegram"
    m = re.fullmatch(r"\d{1,4}", (text or "").strip())
    n = int(m.group(0)) if m else 0
    if n <= 0 or n > USER_BULK_MAX:
        await _send_tracked(update, context,
                            t(lang, "ub_bad_qty", cap=USER_BULK_MAX))
        return
    counts, _tot = await get_stock_counts()
    avail = sum((counts.get(db_type) or {}).values())
    if n > avail:
        await _send_tracked(update, context, t(lang, "ub_stock_low", n=avail))
        return
    rate = float(await get_setting(
        "whatsapp_rate" if ntype == "wa" else "telegram_rate") or 0)
    dmin, damt = await bulk_disc_params()   # v9.34 owner-configurable
    unit = bulk_unit_rate(rate, n, dmin, damt)
    u = await get_user(uid) or {}
    bal = float(u.get("balance") or 0.0)
    total = round(unit * n, 2)
    if unit > 0:
        maxn = int((bal + _MONEY_EPS) // unit)   # v9.35: epsilon floor
    else:
        maxn = USER_BULK_MAX
    maxn = max(0, min(maxn, USER_BULK_MAX))
    if n > maxn:
        await _send_tracked(
            update, context,
            t(lang, "ub_no_bal", n=n, total="%.2f" % total,
              bal="%.2f" % bal, maxn=maxn))
        return
    label = "WhatsApp" if ntype == "wa" else "Telegram"
    disc = t(lang, "ub_disc", dmin=dmin) if n >= dmin else ""
    context.user_data["ubulk"] = {"ntype": ntype, "n": n}
    await _send_tracked(
        update, context,
        t(lang, "ub_confirm", div=DIV, label=label, n=n,
          unit="%.2f" % unit, disc=disc, total="%.2f" % total,
          after="%.2f" % (bal - total)),
        _ubulk_confirm_kb(lang, price="%.2f" % total),
    )


async def run_user_bulkbuy(update, context, uid, p):
    """v9.31: execute the confirmed bulk order - in-flight lock, atomic
    engine, .txt file delivery, receipt, owner log, pollers."""
    lock = "bulkbuying:%s" % uid
    if context.bot_data.get(lock):
        if update.callback_query:
            try:
                await update.callback_query.answer(
                    t(await get_user_lang(uid), "toast_processing"),
                    show_alert=True)
            except Exception:
                pass
        return
    context.bot_data[lock] = True
    try:
        lang = await get_user_lang(uid)
        ntype = p["ntype"]
        n = int(p["n"])
        rate = float(await get_setting(
            "whatsapp_rate" if ntype == "wa" else "telegram_rate") or 0)
        dmin, damt = await bulk_disc_params()   # v9.34 owner-set
        unit = bulk_unit_rate(rate, n, dmin, damt)
        ref_on = await ref_enabled()
        ref_rate = await get_ref_rate() if ref_on else 0.0
        res = await bulk_purchase(uid, ntype, n, unit,
                                  ref_on=ref_on, ref_rate=ref_rate)
        await clear_user_state(uid)
        context.user_data.pop("ubulk", None)
        if not res["ok"]:
            if res["err"] == "no_balance":
                bal = res.get("balance") or 0.0
                total = round(unit * n, 2)
                await _send_tracked(
                    update, context,
                    insufficient_text(total, bal, total - bal, lang),
                    insufficient_kb(lang))
            else:
                await _send_tracked(update, context, t(lang, "ub_none"),
                                    back_home_kb(lang))
            return
        rows = res["rows"]
        got = len(rows)
        country = str((rows[0].get("country") or "USA"))
        fname = "otphub.%d%s.txt" % (got, country.lower())
        content = "\n".join("%s | %s" % (r["phone_number"], r["otp_url"])
                            for r in rows)
        disc = t(lang, "ub_disc", dmin=dmin) if n >= dmin else ""
        text = t(lang, "ub_done", div=DIV, n=got,
                 total="%.2f" % res["total"], unit="%.2f" % unit,
                 disc=disc, bal="%.2f" % res["balance"], fname=fname)
        if got < n:
            text += "\n\n" + t(lang, "ub_partial", n=got)
        # the file is a receipt - sent fresh, never edited or deleted
        try:
            await context.bot.send_document(
                chat_id=uid, document=content.encode("utf-8"),
                filename=fname, caption=text, parse_mode=ParseMode.HTML)
        except Exception:
            await context.bot.send_document(
                chat_id=uid, document=content.encode("utf-8"),
                filename=fname)
            await context.bot.send_message(
                chat_id=uid, text=text, parse_mode=ParseMode.HTML)
        await context.bot.send_message(
            chat_id=uid, text=menu_footer_text(lang),
            parse_mode=ParseMode.HTML,
            reply_markup=main_menu_kb(is_admin(uid), lang))
        # instant pollers for the first few numbers; the permanent
        # sweeper (v9.28) probes every remaining one within ~2 minutes
        for r in rows[:USER_BULK_POLLERS]:
            try:
                start_otp_poller(context, uid, dict(r))
            except Exception:
                pass
        # owner awareness log (one line, guarded)
        label = "WhatsApp" if ntype == "wa" else "Telegram"
        u = await get_user(uid) or {}
        nm = str(u.get("first_name") or uid)
        for aid in sorted(ADMIN_IDS):
            try:
                await context.bot.send_message(
                    chat_id=aid,
                    text=("\U0001F4E6 <b>USER BULK BUY</b>\n"
                          f"\U0001F464 {html_escape(nm)} (<code>{uid}</code>)\n"
                          f"\U0001F4F1 {got} x {label} \u2022 ${unit:.2f}/num\n"
                          f"\U0001F4B5 ${res['total']:.2f} \u2022 {fname}"),
                    parse_mode=ParseMode.HTML)
            except Exception:
                pass
        logger.info("USER BULK BUY %s: %s x %s @ %.2f = %.2f (%s)",
                    uid, got, label, unit, res["total"], fname)
    finally:
        context.bot_data.pop(lock, None)


async def user_bulkbuy_callback(update, context):
    """v9.31 inline router: ubulk:type:<wa|tg> / ubulk:go / ubulk:back /
    ubulk:cancel - banned users + force-join gates re-checked here."""
    q = update.callback_query
    uid = q.from_user.id
    user = await get_user(uid) or {}
    if user.get("is_banned"):
        try:
            await q.answer(t(lang_of(user), "blocked"), show_alert=True)
        except Exception:
            pass
        return
    lang = lang_of(user)
    if not is_admin(uid) and await managed_channel_ids():
        pend = await pending_force_join(uid)
        if pend:
            return await show_force_join(update, context, pend, lang)
    action = q.data.split(":", 1)[1] if ":" in q.data else ""
    if action.startswith("type:"):
        ntype = action.split(":", 1)[1]
        if ntype not in ("wa", "tg"):
            try:
                await q.answer(t(lang, "ub_expired"), show_alert=True)
            except Exception:
                pass
            return
        await _safe_answer(q)
        return await show_user_bulkqty(update, context, ntype)
    if action == "back":
        await _safe_answer(q)
        return await show_user_bulkbuy(update, context)
    if action == "cancel":
        await _safe_answer(q)
        await clear_user_state(uid)
        context.user_data.pop("ubulk", None)
        await _send_tracked(update, context, menu_info_text(lang),
                            main_menu_kb(is_admin(uid), lang))
        return
    if action == "go":
        p = context.user_data.get("ubulk")
        if not p:
            await clear_user_state(uid)
            try:
                await q.answer(t(lang, "ub_expired"), show_alert=True)
            except Exception:
                pass
            return
        await _safe_answer(q)
        return await run_user_bulkbuy(update, context, uid, p)
    try:
        await q.answer(t(lang, "toast_expired"), show_alert=True)
    except Exception:
        pass


# --------------------------------------------------------------------------- #
#  BACKGROUND OTP POLLER  (polls the number's own API for 10 minutes)
# --------------------------------------------------------------------------- #
OTP_POLL_SECONDS = 600   # 10 minutes
OTP_POLL_INTERVAL = 5    # check every 5 seconds -> instant delivery


async def notify_otp(context, uid, phone, code):
    """Instant OTP notification (v9.13 design, v9.16 localized)."""
    lang = await get_user_lang(uid)
    try:
        await context.bot.send_message(
            chat_id=uid,
            text=(
                f"{t(lang, 'otp_received')}\n"
                f"\U0001F7E2 <code>{html_escape(str(phone))}</code>\n"
                f"\u2705 <code>{html_escape(str(code))}</code>"
            ),
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        logger.warning("OTP notify failed user=%s: %s", uid, e)


# --------------------------------------------------------------------------- #
#  v9.29 OTP SUCCESS CHANNEL  (@RTO_LiveUsa0tp - public proof feed)
# --------------------------------------------------------------------------- #
async def post_otp_success(bot, uid, phone, code, order_id=None):
    """v9.29: post every successfully delivered OTP to the owner's
    public channel (OTP_SUCCESS_CHANNEL, default @RTO_LiveUsa0tp) in the
    owner's EXACT fixed format, whole post BOLD:
        \U0001F389Successfully otp received
        \U0001F916User :- {name}
        \U0001F7E2Number {masked}
        \u2705OTP :- {code}
        Price :- {$0.15}
    PRIVACY: the buyer's NAME only - the @username is NEVER posted
    (strangers must not be able to DM the buyer from the channel).
    The number goes through the same mask_number() as the purchase
    log - only the last 4 digits stay visible. The price is the rate
    the buyer ACTUALLY paid (order rate_at_purchase, with
    get_order_amount_for as fallback).
    CRASH-PROOF BY CONTRACT: everything is guarded - a dead channel,
    a missing order row or a DB hiccup can only log a warning, it can
    NEVER break the buyer's delivery or the calling poller/sweeper."""
    try:
        name = ""
        try:
            u = await get_user(uid) or {}
            name = str(u.get("first_name") or "").strip()
        except Exception:
            name = ""
        if not name:
            name = "User"
        price = None
        srv = ""
        if order_id:
            try:
                async with adb() as db:
                    cur = await db.execute(
                        "SELECT rate_at_purchase, total_amount, "
                        "number_type FROM orders WHERE order_id=?",
                        (str(order_id),))
                    row = await cur.fetchone()
                    await cur.close()
                if row is not None:
                    if row[0] is not None:
                        price = float(row[0])
                    elif row[1] is not None:
                        price = float(row[1])
                    _nt = str(row[2] or "").strip().lower()
                    if _nt == "wa":
                        srv = "WhatsApp"
                    elif _nt == "tg":
                        srv = "Telegram"
            except Exception:
                price = None
        if price is None:
            try:
                amount, _oid = await get_order_amount_for(uid, str(phone))
                price = amount
            except Exception:
                price = None
        try:
            price_txt = f"${float(price):.2f}"
        except Exception:
            price_txt = "$0.00"
        if srv == "WhatsApp":
            srv_line = "\U0001F4ACService :- WhatsApp \U0001F7E2\n"
        elif srv == "Telegram":
            srv_line = "\U0001F4ACService :- Telegram \U0001F535\n"
        else:
            srv_line = ""
        text = (
            "<b>\U0001F389Successfully otp received\n"
            f"\U0001F916User :- {html_escape(name)}\n"
            f"\U0001F7E2Number {html_escape(mask_number(str(phone)))}\n"
            f"{srv_line}"
            f"\u2705OTP :- {html_escape(str(code))}\n"
            f"Price :- {price_txt}</b>"
        )
        try:
            await bot.send_message(chat_id=OTP_SUCCESS_CHANNEL, text=text,
                                   parse_mode=ParseMode.HTML)
            return
        except Exception as e:
            logger.warning("OTP success channel post failed (%s) - "
                           "retrying once", str(e)[:80])
        await asyncio.sleep(3)
        await bot.send_message(chat_id=OTP_SUCCESS_CHANNEL, text=text,
                               parse_mode=ParseMode.HTML)
    except Exception as e:
        logger.warning("OTP success channel post failed: %s", str(e)[:120])


def schedule_otp_success(bot, uid, phone, code, order_id=None):
    """v9.29: fire-and-forget channel post. The buyer's OTP delivery
    NEVER waits on (or dies with) the channel. EXACTLY-ONCE by
    construction: every caller runs only inside a WON
    update_otp_for_stock claim - and the atomic claim can be won by
    exactly one path, so no double posts, ever."""
    try:
        asyncio.get_running_loop().create_task(
            post_otp_success(bot, uid, phone, code, order_id))
    except Exception as e:
        logger.warning("OTP channel post schedule failed: %s", str(e)[:80])


async def poll_otp_task(context, uid, stock, recover=False):
    """Poll the stock number's OTP API every 5s for 10 minutes.
    v9.26: uses fetch_sms_text_smart (provider machine endpoint first -
    the /sms/ page can sit on WAITING while the code is already live at
    /api/sms/). Baseline (old SMS) is captured EXACTLY ONCE at the first
    poll and persisted - an EMPTY baseline is a real state ('[]') and
    means every code seen after it belongs to the buyer; the poller
    NEVER re-baselines. STRICT refund guard: the moment a refund is
    requested the poller dies and OTP can never be delivered for that
    number.
    v9.28 recover=True (restart recovery): the sale already happened
    LONG ago and no baseline may exist yet - an OTP that arrived while
    the process was down is the BUYER'S code, so a missing baseline is
    captured as EMPTY right away instead of swallowing the waiting
    code (the restart must never cost a delivery)."""
    stock_id = stock["id"]
    phone = stock["phone_number"]
    url = (stock.get("otp_url") or "").strip()
    if not url:
        return
    captured, baseline = await get_stock_baseline(stock_id)
    if recover and not captured:
        # v9.28: no baseline row yet -> the code that may already be
        # sitting at the provider belongs to the waiting buyer. Capture
        # an EMPTY baseline now and deliver anything that shows up.
        captured = True
        baseline = set()
        await save_stock_baseline(stock_id, [])
    loop = asyncio.get_running_loop()
    deadline = loop.time() + OTP_POLL_SECONDS
    try:
        session = await http_session()
        while loop.time() < deadline:
            st = await get_stock_item(stock_id)
            if (not st or st.get("otp_blocked")
                    or st.get("refund_state") in ("requested", "approved")
                    or st.get("otp_status") == "used"):
                logger.info("OTP poller aborted stock=%s "
                            "(refunded/blocked/delivered)", stock_id)
                return
            text = await fetch_sms_text_smart(url, session)
            codes = _otp_codes(text)
            if not captured:
                # v9.26: capture the baseline EXACTLY ONCE. The saved
                # row (even empty '[]') marks the capture moment - the
                # old code treated an empty saved list as 'not captured
                # yet' and re-baselined on the next fetch, so a fast
                # OTP swallowed itself as old SMS and was never
                # delivered.
                captured = True
                baseline = set(codes)
                await save_stock_baseline(stock_id, codes)
                logger.info("OTP poll baseline captured stock=%s "
                            "codes=%s", stock_id, codes or "-")
            else:
                fresh = [c for c in codes if c not in baseline]
                if fresh:
                    # final strict re-check right before notifying (race guard)
                    st2 = await get_stock_item(stock_id)
                    if (not st2 or st2.get("otp_blocked")
                            or st2.get("refund_state")
                            in ("requested", "approved")):
                        logger.info("OTP delivery cancelled stock=%s "
                                    "(refund in progress)", stock_id)
                        return
                    code = fresh[0]
                    if await update_otp_for_stock(stock_id, code):
                        await increment_otp_count(uid)
                        await notify_otp(context, uid, phone, code)
                        # v9.27: the OTP ARRIVED -> the referral
                        # commission becomes real money (exactly once).
                        st_row = {}
                        try:
                            st_row = await get_stock_item(stock_id) or {}
                            await pay_pending_referral(
                                context, st_row.get("order_id"))
                        except Exception:
                            logger.warning("referral payout failed "
                                           "stock=%s", stock_id, exc_info=True)
                        # v9.29: public success channel post (fire &
                        # forget, exactly-once via the won claim)
                        schedule_otp_success(
                            context.bot, uid, phone, code,
                            st_row.get("order_id"))
                        logger.info("OTP DELIVERED stock=%s user=%s code=%s",
                                    stock_id, uid, code)
                    # claim lost -> the Get OTP path already delivered
                    return
            await asyncio.sleep(OTP_POLL_INTERVAL)
    except asyncio.CancelledError:
        raise
    except Exception as e:
        logger.warning("OTP poller error stock=%s: %s", stock_id, e)
        return
    # 10 minutes over - no OTP arrived
    _lng = await get_user_lang(uid)
    try:
        await context.bot.send_message(
            chat_id=uid,
            text=(
                f"{t(_lng, 'otp_timeout')}\n"
                f"{DIV}\n"
                f"\U0001F7E2 <code>{html_escape(str(phone))}</code>\n"
                f"{DIV}\n"
                f"{t(_lng, 'otp_timeout_body')}"
            ),
            parse_mode=ParseMode.HTML,
        )
    except Exception:
        pass


def start_otp_poller(context, uid, stock, recover=False):
    """Start the 10-minute background OTP poller for a purchased number."""
    if (stock.get("otp_blocked")
            or stock.get("refund_state") in ("requested", "approved")):
        logger.info("OTP poller skipped stock=%s (refunded/blocked)",
                    stock.get("id"))
        return
    if not (stock.get("otp_url") or "").strip():
        logger.info("No OTP URL on stock %s - poller skipped", stock.get("id"))
        return
    polls = context.bot_data.setdefault("otp_polls", {})
    if len(polls) > 2000:   # v9.20: prune finished pollers (no growth)
        for _k in [_k for _k, _v in polls.items() if _v.done()]:
            polls.pop(_k, None)
    sid = stock["id"]
    old = polls.get(sid)
    if old and not old.done():
        return
    polls[sid] = context.application.create_task(
        poll_otp_task(context, uid, stock, recover=recover)
    )
    logger.info("OTP poller started stock=%s user=%s (10 min window%s)",
                sid, uid, ", recovery" if recover else "")


# --------------------------------------------------------------------------- #
#  v9.28 OTP DELIVERY SAFETY NET  (recovery + permanent sweeper worker)
#  Three INDEPENDENT paths now deliver an OTP - if one misses it, the
#  next one catches it:
#    1) FAST POLLER   - 5s checks for 10 min after the purchase (v9.26)
#    2) RECOVERY      - after a restart/reboot the pollers of every
#                       undelivered recent sale are re-armed automatically
#                       (they used to die silently with the old process)
#    3) SWEEPER       - a permanent low-rate worker; every cycle it
#                       probes sold numbers that still have no OTP and
#                       no live poller (10-min window over, poller died,
#                       process restarted, anything) and delivers the
#                       moment the provider shows a code. No time limit
#                       - exactly like the owner's rule: "koi timing
#                       nahi". Refunded/blocked/delivered rows are
#                       skipped by the DB query itself.
# --------------------------------------------------------------------------- #
OTP_SWEEP_INTERVAL = 120    # one sweep cycle every 2 minutes
OTP_SWEEP_BATCH = 300       # max numbers probed per cycle (load-safe)
OTP_SWEEP_WORKERS = 20      # concurrent probes inside a cycle
OTP_RECOVERY_HOURS = 24     # restart-recovery window for fast pollers


class _BootContext:
    """v9.28: minimal context shim so boot-time poller re-arming can
    reuse start_otp_poller exactly like a normal runtime start.
    Carries .bot / .application / .bot_data like a real PTB context."""
    def __init__(self, app):
        self.bot = app.bot
        self.application = app
        self.bot_data = app.bot_data


async def recover_otp_pollers(app):
    """v9.28 RECOVERY: a restart used to silently kill every in-flight
    OTP poller (they lived only in bot_data) - a buyer could wait
    forever. Now every undelivered sale of the last 24h gets its fast
    poller re-armed right after boot."""
    try:
        rows = await find_undelivered_sold(limit=2000,
                                           max_age_hours=OTP_RECOVERY_HOURS)
        if not rows:
            logger.info("OTP recovery (v9.28): nothing to re-arm")
            return
        bootctx = _BootContext(app)
        armed = 0
        for r in rows:
            try:
                uid = int(r["sold_to"])
            except (TypeError, ValueError):
                continue
            start_otp_poller(bootctx, uid, dict(r), recover=True)
            armed += 1
        logger.info("OTP recovery (v9.28): %d poller(s) re-armed after "
                    "restart", armed)
    except Exception:
        logger.warning("OTP recovery failed", exc_info=True)


async def _sweep_one(app, sem, session, stock_row):
    """Probe ONE undelivered sold number and deliver if the provider now
    shows a code. Baseline semantics are IDENTICAL to the fast poller:
    captured-once, persisted; a legacy missing baseline reads empty
    (buyer-safe) and is captured exactly here, once."""
    sid = stock_row["id"]
    polls = app.bot_data.setdefault("otp_polls", {})
    live = polls.get(sid)
    if live and not live.done():
        return                      # a fast poller owns this number
    st = await get_stock_item(sid)
    if (not st or st.get("otp_code")
            or st.get("otp_blocked") or st.get("otp_status") == "used"
            or st.get("refund_state") in ("requested", "approved")
            or st.get("status") != "sold"):
        return
    url = (st.get("otp_url") or "").strip()
    if not url:
        return
    async with sem:                 # cap the concurrent probes
        try:
            text = await fetch_sms_text_smart(url, session)
        except Exception:
            return                  # network hiccup -> next cycle
    codes = _otp_codes(text)
    if not codes:
        return
    captured, baseline = await get_stock_baseline(sid)
    if not captured:
        # v9.28: no baseline yet (poller died before its first fetch) -
        # any code the provider shows NOW belongs to the waiting buyer.
        # Capture an EMPTY baseline and deliver - never swallow.
        await save_stock_baseline(sid, [])
        fresh = codes
    else:
        fresh = [c for c in codes if c not in baseline]
    if not fresh:
        return
    # final strict re-check right before claiming (refund race guard)
    st2 = await get_stock_item(sid)
    if (not st2 or st2.get("otp_code") or st2.get("otp_blocked")
            or st2.get("refund_state") in ("requested", "approved")
            or st2.get("status") != "sold"):
        return
    code = fresh[0]
    try:
        uid = int(st2["sold_to"])
    except (TypeError, ValueError):
        return
    if not await update_otp_for_stock(sid, code):
        return                      # poller/Get OTP won the race
    await increment_otp_count(uid)
    await notify_otp(app, uid, st2["phone_number"], code)
    try:
        await pay_pending_referral(app, st2.get("order_id"))
    except Exception:
        logger.warning("referral payout failed stock=%s", sid,
                       exc_info=True)
    # v9.29: public success channel post (fire & forget)
    schedule_otp_success(app.bot, uid, st2["phone_number"], code,
                         st2.get("order_id"))
    logger.info("OTP SWEPT stock=%s user=%s code=%s (safety net)",
                sid, uid, code)


async def otp_sweeper_task(app):
    """v9.28 PERMANENT WORKER: the last line of defence. Every cycle it
    re-checks sold numbers without OTP that no live poller is covering
    (window over / poller crashed / process restarted) and delivers the
    moment the provider shows a code - automatically, forever, no time
    limit. DB-bounded (LIMIT), semaphore-bounded (20) and crash-proof:
    one bad cycle never kills the loop."""
    logger.info("OTP sweeper (v9.28) armed - every %ss, batch %s, "
                "%s workers", OTP_SWEEP_INTERVAL, OTP_SWEEP_BATCH,
                OTP_SWEEP_WORKERS)
    while True:
        try:
            await asyncio.sleep(OTP_SWEEP_INTERVAL)
            # v9.28 page rotation: walk the whole backlog page by page so
            # even a 20k-number queue is fully covered over time; when a
            # page comes back short (or empty) the walk restarts at the
            # newest sales.
            off = int(await get_setting("otp_sweep_offset") or 0)
            rows = await find_undelivered_sold(limit=OTP_SWEEP_BATCH,
                                               offset=off)
            if len(rows) < OTP_SWEEP_BATCH:
                await set_setting("otp_sweep_offset", "0")
            else:
                await set_setting("otp_sweep_offset", str(off + OTP_SWEEP_BATCH))
            if not rows:
                continue
            sem = asyncio.Semaphore(OTP_SWEEP_WORKERS)
            session = await http_session()
            await asyncio.gather(
                *[_sweep_one(app, sem, session, r) for r in rows],
                return_exceptions=True)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            logger.warning("OTP sweeper cycle error: %s", str(e)[:120])


# --------------------------------------------------------------------------- #
#  ORDER HISTORY GROUP FORWARD
# --------------------------------------------------------------------------- #
def mask_user_id(uid: int) -> str:
    s = str(uid)
    if len(s) <= 6:
        return s
    keep = 3
    return s[:keep] + "*" * (len(s) - keep * 2) + s[-keep:]


def mask_number(number: str) -> str:
    s = number
    if len(s) <= 6:
        return s
    keep = 5
    return s[:keep] + "*" * max(len(s) - keep - 4, 1) + s[-4:]


async def get_total_bot_balance() -> float:
    async with adb() as db:
        cur = await db.execute("SELECT COALESCE(SUM(balance),0) FROM users")
        val = (await cur.fetchone())[0]
        await cur.close()
        return float(val)


async def forward_order_history(context, uid, ntype, country, rate, stock, order_id):
    """Send a formatted purchase notification to the order-history group."""
    group_id = await get_setting("order_history_group_id")
    if not group_id:
        group_id = str(ORDER_HISTORY_GROUP_ID)
    try:
        gid = int(group_id)
    except Exception:
        return
    platform = "WhatsApp" if ntype == "wa" else "Telegram"
    masked_uid = mask_user_id(uid)
    masked_num = mask_number(stock["phone_number"])
    total_bal = await get_total_bot_balance()
    now = _utcnow().strftime("%Y-%m-%d %H:%M:%S")
    text = (
        "\U0001F525 <b>New Purchase Successful!</b>\n"
        f"Platform: {platform}\n"
        f"\U0001F464 User ID: {masked_uid}\n"
        f"\U0001F4E6 Quantity: 1 pcs\n"
        f"\U0001F4B0 Price: USDT {rate:.2f}\n"
        f"\U0001F517 Number: {masked_num}\n"
        f"\U0001F194 Order ID: {order_id}\n"
        f"\U0001F4B0 Total Bot Balance: USDT {total_bal:,.2f}\n"
        f"\u23F0 Time: {now}"
    )
    try:
        await context.bot.send_message(
            chat_id=gid, text=text, parse_mode=ParseMode.HTML
        )
    except Exception as e:
        logger.warning("forward_order_history failed: %s", e)


# --------------------------------------------------------------------------- #
#  OTP INLINE  (Get OTP action button on the receipt)
# --------------------------------------------------------------------------- #
async def _safe_answer(q, text=None, show_alert=False):
    """Answer a callback query without dying on stale queries.
    Proven live: a button pressed while the bot was down arrives
    "too old" after restart - the answer API rejects it, but the
    action behind the tap must STILL run."""
    try:
        await q.answer(text=text, show_alert=show_alert)
    except Exception as e:
        logger.info("callback answer skipped (%s)", str(e)[:60])


async def otp_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # v9.20 single-answer discipline: the callback query is answered EXACTLY
    # once (toast on guard exits, 'Fetching...' right before the fetch).
    q = update.callback_query
    uid = q.from_user.id
    _lng = await get_user_lang(uid)

    async def _reply(txt):
        # q.message can be gone/unreachable on very old messages
        try:
            if q.message is not None:
                return await q.message.reply_text(txt, parse_mode=ParseMode.HTML)
        except Exception:
            pass
        try:
            return await context.bot.send_message(
                chat_id=update.effective_chat.id, text=txt,
                parse_mode=ParseMode.HTML)
        except Exception:
            return None

    parts = q.data.split(":")
    try:
        stock_id = int(parts[1])
    except (IndexError, ValueError):
        await _safe_answer(q, t(_lng, "toast_invalid"), show_alert=True)
        return
    stock = await get_stock_item(stock_id)
    if not stock:
        await _safe_answer(q, t(_lng, "toast_not_found"), show_alert=True)
        return

    # v9.28: STRICT refund block BEFORE the ownership check - a refunded
    # buyer (sold_to was wiped) must see the clear 'refunded' card, not
    # a confusing 'not your number' toast.
    if stock.get("otp_blocked") or stock.get("refund_state") in (
            "requested", "approved", "rejected"):
        # v9.28: acknowledge the tap BEFORE the card - an unanswered
        # query keeps the button spinner spinning on the user's screen.
        await _safe_answer(q)
        await _reply(
            f"{t(_lng, 'otp_blocked')}\n"
            f"{DIV}\n"
            f"\U0001F7E2 <code>{html_escape(stock['phone_number'])}</code>\n"
            f"{DIV}\n"
            f"{t(_lng, 'otp_blocked_body')}")
        return

    if stock.get("sold_to") != uid and not is_admin(uid):
        await _safe_answer(q, t(_lng, "toast_not_yours"), show_alert=True)
        return

    if not (stock.get("otp_url") or "").strip():
        await _safe_answer(q, t(_lng, "toast_no_link"), show_alert=True)
        return

    # If already delivered -> show the SAME otp again (exact format)
    if stock.get("otp_code") and stock.get("otp_status") == "used":
        # v9.28: if the delivery-time referral payout ever failed (DB
        # busy, transient error), THIS is the recovery point - the
        # atomic pending->paid guard makes the retry exactly-once.
        try:
            await pay_pending_referral(context, stock.get("order_id"))
        except Exception:
            logger.warning("referral payout retry failed stock=%s",
                           stock_id, exc_info=True)
        await _reply(
            f"{t(_lng, 'otp_received')}\n"
            f"\U0001F7E2 <code>{html_escape(stock['phone_number'])}</code>\n"
            f"\u2705 <code>{html_escape(stock['otp_code'])}</code>")
        return

    # Fetch now - v9.26 LOSS FIX: the provider's MACHINE endpoint
    # (/api/sms/) is probed first; the JS-rendered /sms/ page is only a
    # fallback (it can say WAITING while the code is already live).
    await _safe_answer(q, "\u23F3 Fetching your OTP...")
    # v9.28: the typing indicator is COSMETIC - a transient Telegram
    # error here used to abort the whole fetch (toast said 'Fetching'
    # and then nothing). The OTP fetch must never depend on it.
    try:
        await context.bot.send_chat_action(chat_id=uid,
                                           action=ChatAction.TYPING)
    except Exception as e:
        logger.info("chat_action skipped (%s)", str(e)[:60])
    text = await fetch_sms_text_smart(stock["otp_url"], None)
    codes = _otp_codes(text)
    # v9.26: the baseline is NEVER captured or re-captured here - the
    # capture belongs to the poller's first fetch at purchase time. A
    # missing row (legacy purchase) reads as an EMPTY baseline: every
    # code the API returns now belongs to the waiting buyer. The old
    # 'current codes become the baseline' logic swallowed the buyer's
    # OTP exactly when it had ALREADY arrived - the 3-number loss.
    _captured, baseline = await get_stock_baseline(stock_id)
    fresh = [c for c in codes if c not in baseline]
    if fresh:
        code = fresh[0]
        if await update_otp_for_stock(stock_id, code):
            await increment_otp_count(uid)
            await _reply(
                f"{t(_lng, 'otp_received')}\n"
                f"\U0001F7E2 <code>{html_escape(stock['phone_number'])}</code>\n"
                f"\u2705 <code>{html_escape(str(code))}</code>")
            # v9.27: OTP ARRIVED via Get OTP -> referral pays exactly once
            # (the atomic pending->paid guard de-dupes against the poller).
            try:
                await pay_pending_referral(context, stock.get("order_id"))
            except Exception:
                logger.warning("referral payout failed stock=%s",
                               stock_id, exc_info=True)
            # v9.29: public success channel post (fire & forget,
            # exactly-once via the won claim)
            schedule_otp_success(context.bot, uid, stock["phone_number"],
                                 code, stock.get("order_id"))
        else:
            # v9.21: the poller delivered this exact OTP while we were
            # fetching - show the stored one, never double-notify/count.
            # v9.28 RACE FIX: the claim can also be lost to a refund that
            # won the race - then the number is dead and the code must
            # NEVER be shown (the buyer was already refunded).
            _st3 = await get_stock_item(stock_id) or {}
            if (_st3.get("otp_blocked")
                    or _st3.get("refund_state")
                    in ("requested", "approved", "rejected")):
                await _reply(
                    f"{t(_lng, 'otp_blocked')}\n"
                    f"{DIV}\n"
                    f"\U0001F7E2 <code>{html_escape(stock['phone_number'])}</code>\n"
                    f"{DIV}\n"
                    f"{t(_lng, 'otp_blocked_body')}")
                return
            _shown = _st3.get("otp_code") or code
            await _reply(
                f"{t(_lng, 'otp_received')}\n"
                f"\U0001F7E2 <code>{html_escape(stock['phone_number'])}</code>\n"
                f"\u2705 <code>{html_escape(str(_shown))}</code>")
    else:
        await _reply(
            f"{t(_lng, 'otp_waiting')}\n"
            f"{DIV}\n"
            f"\U0001F7E2 <code>{html_escape(stock['phone_number'])}</code>\n"
            f"{DIV}\n"
            f"{t(_lng, 'otp_waiting_body')}")


# --------------------------------------------------------------------------- #
#  MANAGE REFUND HUB (v9.27) - the old user-side refund system is GONE.
#  Three owner tools, all inside Admin Panel -> Manage Refund:
#    1) CHECK NUMBER     - upload a stock-format file (phone | url); every
#                          number is live-checked (30-way worker pool, live
#                          progress bar) and a .txt of the NO-OTP numbers
#                          comes back in the same forward-ready format.
#    2) REFUND SEND      - forward that file: every URL owned by a sold
#                          number without OTP is refunded AUTOMATICALLY
#                          (the buyer gets the success card with number +
#                          price). A second live check runs before any
#                          money moves - a URL whose OTP arrived is NEVER
#                          refunded. After the refund the stock row is
#                          WIPED (url + owner deleted) so the same file
#                          can never match again: one refund per number,
#                          ever, loot-proof by construction.
#    3) CHEK NUMBER & REFUND (v9.40) - paste numbers line-by-line
#                          (+12369693939 per line, or a .txt): owner
#                          lookup -> refund history -> DB OTP + a
#                          SECOND LIVE probe -> refund EXACTLY what
#                          the buyer paid, all in one pass (the same
#                          atomic zero-loss spine as Refund Send).
# --------------------------------------------------------------------------- #

CHECK_WORKERS = 30          # concurrent live OTP probes (load-safe)
CHECK_TIMEOUT = 10          # seconds per provider probe
CHECK_EDIT_EVERY = 2.0      # progress-bar edit cadence (seconds)
CHECKREFUND_MAX = 50000     # v9.40: max numbers per Chek & Refund run


def _progress_bar(done, total, width=12):
    if total <= 0:
        return "\u2591" * width
    filled = max(0, min(width, int(round(width * done / total))))
    return "\u2593" * filled + "\u2591" * (width - filled)


def _uniq_entries(entries):
    """Deduplicate parsed stock lines by normalized URL (first wins)."""
    seen, uniq = set(), []
    for phone, url in entries:
        k = normalize_url(url)
        if not k or k in seen:
            continue
        seen.add(k)
        uniq.append((phone, url))
    return uniq


async def show_manage_refund(update, context):
    """Admin Panel -> Manage Refund hub (v9.27)."""
    if not is_admin(update.effective_user.id):
        return
    uid = update.effective_user.id
    await set_user_state(uid, "admin_refund_menu")
    async with adb() as db:
        cur = await db.execute(
            "SELECT COUNT(*) FROM stock WHERE status='sold'")
        sold_n = (await cur.fetchone())[0]
        await cur.close()
    lines = [
        "\U0001F4B8 <b>MANAGE REFUND</b>",
        "",
        DIV,
        f"\U0001F4E6 <b>Sold numbers (all time):</b> {sold_n}",
        DIV,
        "",
        "<b>1\ufe0f\u20e3 \U0001F522 Check Number</b> \u2014 upload your stock "
        "file (<code>number | url</code>): every number is live-checked "
        "with a live progress bar; you get a <b>.txt of the numbers with "
        "NO OTP</b> (same format).",
        "",
        "<b>2\ufe0f\u20e3 \U0001F4B8 Refund Send</b> \u2014 forward that checked "
        "file: the owner of every no-OTP number is refunded automatically "
        "(buyer paid price, instant notification). A URL whose OTP "
        "arrived is never refunded. After a refund its data is wiped \u2014 "
        "the same file can never pay twice.",
        "",
        "<b>3\ufe0f\u20e3 \U0001F501 Chek Number & Refund</b> \u2014 paste "
        "numbers line-by-line (<code>+12369693939</code>): owner, refund "
        "history and OTP are checked and eligible buyers are refunded "
        "IN ONE STEP (what they actually paid - loss-proof).",
    ]
    await _send_tracked(update, context, "\n".join(lines), admin_refund_kb())


async def show_check_number(update, context):
    if not is_admin(update.effective_user.id):
        return
    await set_user_state(update.effective_user.id, "admin_check_number")
    await _send_tracked(
        update, context,
        "\U0001F522 <b>CHECK NUMBER</b>\n\n"
        f"{DIV}\n"
        "Send your stock-format file, or paste the lines here:\n"
        "\U0001F4C4 <code>+14133525884 | http://provider/sms/XXXX</code>\n"
        f"{DIV}\n"
        "\U0001F50D EVERY number is live-checked \u2014 10k / 20k+, fast "
        "worker pool, live progress bar.\n"
        "\U0001F4E5 Result: a <b>.txt with the numbers where NO OTP "
        "arrived</b> \u2014 same format, forward it straight to "
        "\U0001F4B8 Refund Send.",
        admin_input_kb())


async def show_refund_send(update, context):
    if not is_admin(update.effective_user.id):
        return
    await set_user_state(update.effective_user.id, "admin_refund_send")
    await _send_tracked(
        update, context,
        "\U0001F4B8 <b>REFUND SEND</b>\n\n"
        f"{DIV}\n"
        "Forward the <b>checked no-OTP file</b> (or paste the lines).\n"
        f"{DIV}\n"
        "\U0001F91F Every URL that belongs to a sold number WITHOUT OTP "
        "gets an <b>automatic refund</b> \u2014 the buyer is paid what he "
        "actually paid and notified instantly.\n"
        "\U0001F6AB A URL whose OTP arrived (live-checked again before "
        "any money moves) is NEVER refunded.\n"
        "\U0001F512 One refund per number, ever \u2014 refunded data is "
        "wiped, so re-sending the same file matches nothing.",
        admin_input_kb())


async def _edit_progress(status, title, counters, total, last_edit,
                         force=False):
    now = time.monotonic()
    if not force and now - last_edit["t"] < CHECK_EDIT_EVERY:
        return
    last_edit["t"] = now
    done = counters["done"]
    try:
        await status.edit_text(
            f"{title}\n"
            f"{_progress_bar(done, total)} {done}/{total} "
            f"({done * 100 // total if total else 100}%)\n"
            + counters["line"](counters),
            parse_mode=ParseMode.HTML)
    except Exception:
        pass


async def show_check_refund(update, context):
    """v9.40 CHEK NUMBER & REFUND: paste numbers line-by-line,
    one pass checks owner + refund history + OTP and refunds what
    the buyer actually paid (zero-loss spine, admin-only)."""
    if not is_admin(update.effective_user.id):
        return
    await set_user_state(update.effective_user.id, "admin_check_refund")
    await _send_tracked(
        update, context,
        "\U0001F501 <b>CHEK NUMBER & REFUND</b>\n\n"
        f"{DIV}\n"
        "Numbers line-by-line bhejo (ya .txt file):\n"
        "\U0001F4C4 <code>+12369693939</code>\n"
        "\U0001F4C4 <code>+12369693940</code>\n"
        f"{DIV}\n"
        "\U0001F50D Har number check hoga: kiska hai \u2192 pehle "
        "kabhi refund hua ya nahi \u2192 OTP aaya ya nahi.\n"
        "\U0001F91D OTP nahi aaya hoga to buyer ko UTNA HI refund "
        "milega jitna usne buy kiya tha \u2014 instant notification.\n"
        "\U0001F6AB OTP wala number kabhi refund nahi hota; jo number "
        "pehle refund ho chuka wo dubara match hi nahi karta.\n"
        "\U0001F512 Ek number ka refund sirf EK baar \u2014 atomic "
        "guard + data wipe = loss-proof.",
        admin_input_kb())


PHONE_LINE_RE = re.compile(r"^\+?\d{7,15}$")


def _phone_variants(phone):
    """v9.40: the DB may store a number with or without the '+' -
    every sane variant is tried so a real sale can never be
    missed (loss-safe matching)."""
    out = [phone]
    bare = str(phone).lstrip("+")
    for cand in ("+" + bare, bare):
        if cand not in out:
            out.append(cand)
    return out


def parse_phone_lines(text):
    """v9.40: line-by-line numbers ('+12369693939'). Bare numbers
    are the owner format; 'number | url' stock lines are accepted
    too. Returns (phones, bad_lines) - deduped, order kept."""
    phones, seen, bad = [], set(), 0
    for raw in str(text or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        head = line.split("|", 1)[0]
        hit = None
        for tok in head.replace(",", " ").split():
            tok = tok.strip()
            if PHONE_LINE_RE.match(tok):
                hit = tok
                break
        if hit is None:
            bad += 1
            continue
        if hit not in seen:
            seen.add(hit)
            phones.append(hit)
    return phones, bad


async def find_sold_stock_by_phone(phone):
    """v9.40 CHEK & REFUND match: the CURRENT owner of a phone
    number. Only a sold row with a live owner and no OTP yet can
    match; a refunded row (status refunded, data wiped, dead) can
    never match again - 'pehle kabhi refund hua' can never pay
    twice."""
    for cand in _phone_variants(phone):
        async with adb() as db:
            cur = await db.execute(
                "SELECT * FROM stock WHERE status='sold' "
                "AND sold_to IS NOT NULL "
                "AND (otp_code IS NULL OR otp_code='') "
                "AND COALESCE(otp_blocked,0)=0 "
                "AND phone_number=? ORDER BY id DESC LIMIT 1",
                (cand,))
            row = await cur.fetchone()
            await cur.close()
        if row:
            return dict(row)
    return None


async def stock_state_by_phone(phone):
    """v9.40: the newest stock row for a phone - used to EXPLAIN a
    non-refund: OTP arrived / refunded before / still in stock /
    unknown number."""
    for cand in _phone_variants(phone):
        async with adb() as db:
            cur = await db.execute(
                "SELECT id, phone_number, sold_to, status, otp_code, "
                "otp_blocked, number_type FROM stock "
                "WHERE phone_number=? ORDER BY id DESC LIMIT 1",
                (cand,))
            row = await cur.fetchone()
            await cur.close()
        if row:
            return dict(row)
    return None


async def run_check_and_refund(update, context, admin_id, text):
    """v9.40 CHEK NUMBER & REFUND engine (owner order: 'ye number
    kiske pass hai -> pahle kabhi refund hua ya nahi -> otp aaya
    hai ya nahi -> utna hi refund jitna buy kiya tha; loss na
    ho'). Same zero-loss spine as Refund Send: a SECOND live OTP
    check runs before any money moves, the refund itself is an
    atomic guard that wins only while the row is still sold AND
    OTP-free, the row is wiped on win (re-sending the same
    numbers matches nothing), and the OTP claim path refuses
    refunded rows - a buyer can never hold BOTH the OTP and the
    refund."""
    phones, bad = parse_phone_lines(text)
    if not phones:
        await update.message.reply_text(
            "\u26A0\ufe0f <b>No numbers found.</b> Ek line par ek "
            "number bhejo (<code>+12369693939</code>)",
            parse_mode=ParseMode.HTML)
        return
    if len(phones) > CHECKREFUND_MAX:
        phones = phones[:CHECKREFUND_MAX]
    total = len(phones)
    counters = {"done": 0, "refunded": 0, "otp_live": 0, "otp_db": 0,
                "already": 0, "not_sold": 0, "no_owner": 0,
                "no_price": 0, "unreach": 0}

    def _line(c):
        return (f"\u2705 Refunded: {c['refunded']}   "
                f"\U0001F6AB OTP: {c['otp_live'] + c['otp_db']}   "
                f"\U0001F501 Pehle refund: {c['already']}   "
                f"\U0001F465 Owner nahi: {c['not_sold'] + c['no_owner']}")

    status = await update.message.reply_text(
        f"\U0001F501 <b>CHEK & REFUND {total} number(s)...</b>\n"
        f"{_progress_bar(0, total)} 0/{total} (0%)\n{_line(counters)}",
        parse_mode=ParseMode.HTML)
    refunded_rows, otp_live_list = [], []
    lock = asyncio.Lock()
    sem = asyncio.Semaphore(CHECK_WORKERS)
    last_edit = {"t": time.monotonic()}

    async def _one(phone):
        row = await find_sold_stock_by_phone(phone)
        if row is None:
            st = await stock_state_by_phone(phone)
            async with lock:
                counters["done"] += 1
                if st is None:
                    counters["no_owner"] += 1
                elif st.get("otp_code"):
                    counters["otp_db"] += 1
                elif st.get("status") == "refunded" \
                        or st.get("otp_blocked"):
                    counters["already"] += 1
                else:
                    counters["not_sold"] += 1
            return
        buyer = int(row["sold_to"])
        live = await check_live_otp(row.get("otp_url") or "",
                                    timeout=CHECK_TIMEOUT)
        if live[0] == "otp":
            async with lock:
                counters["done"] += 1
                counters["otp_live"] += 1
                otp_live_list.append((row["phone_number"], live[1]))
            return
        if live[0] == "unknown":
            # no positive proof of 'no OTP' -> no money moves
            async with lock:
                counters["done"] += 1
                counters["unreach"] += 1
            return
        amount, order_id = await get_order_amount_for(
            buyer, row["phone_number"])
        if amount is None:
            rate_key = ("whatsapp_rate"
                        if row.get("number_type") == "whatsapp"
                        else "telegram_rate")
            try:
                amount = float(await get_setting(rate_key))
            except Exception:
                amount = 0.0
        if not amount or amount <= 0:
            async with lock:
                counters["done"] += 1
                counters["no_price"] += 1
            return
        # ATOMIC refund guard: wins only while still sold AND no OTP.
        if not await mark_stock_refunded(row["id"]):
            async with lock:
                counters["done"] += 1
                counters["otp_db"] += 1
            return
        await credit_refund_balance(buyer, float(amount))
        if order_id:
            try:
                await cancel_pending_referral(order_id)
            except Exception:
                logger.warning("referral cancel failed %s", order_id,
                               exc_info=True)
        try:
            await notify_user_refunded(context, buyer,
                                       row["phone_number"], float(amount))
        except Exception:
            pass
        async with lock:
            counters["done"] += 1
            counters["refunded"] += 1
            refunded_rows.append((row["phone_number"], buyer,
                                  float(amount)))
        await _edit_progress(
            status,
            f"\U0001F501 <b>CHEK & REFUND {total} number(s)...</b>",
            dict(counters, line=_line), total, last_edit)

    async def _guarded(p):
        async with sem:
            await _one(p)

    await asyncio.gather(*[_guarded(p) for p in phones])
    await _edit_progress(
        status, f"\U0001F501 <b>CHEK & REFUND {total} number(s)...</b>",
        dict(counters, line=_line), total, last_edit, force=True)

    total_paid = sum(a for _, _, a in refunded_rows)
    matched = (counters["refunded"] + counters["otp_live"]
               + counters["otp_db"])
    lines = [
        "\u2705 <b>CHEK NUMBER & REFUND COMPLETE</b>",
        "",
        DIV,
        f"\U0001F4C4 <b>Numbers in:</b> {total}"
        + (f" (\u26a0\ufe0f {bad} kachra line skip)" if bad else ""),
        f"\U0001F91D <b>Live owner mila:</b> {matched}",
        f"\u2705 <b>Refund ho gaya:</b> {counters['refunded']} user \u2014 "
        f"<b>${total_paid:.2f}</b> credited (jitna buy kiya tha, "
        "utna hi)",
        f"\U0001F6AB <b>OTP aa gaya tha (refund NAHI):</b> "
        f"{counters['otp_live'] + counters['otp_db']} \u2014 paisa bacha",
        f"\U0001F501 <b>Pehle kabhi refund ho chuka (skip):</b> "
        f"{counters['already']}",
        f"\U0001F465 <b>Owner nahi / becha hi nahi gaya:</b> "
        f"{counters['not_sold'] + counters['no_owner']}",
    ]
    if counters["unreach"]:
        lines.append(f"\u26A0\ufe0f <b>Unreachable (NOT paid \u2014 "
                     "dubara chalao):</b> " + str(counters["unreach"]))
    if counters["no_price"]:
        lines.append(f"\u2139\ufe0f <b>Price nahi mila (skip):</b> "
                     + str(counters["no_price"]))
    if refunded_rows:
        lines.append("")
        lines.append(DIV)
        lines.append("\U0001F4B0 <b>REFUND LIST</b>")
        lines.extend(
            f"  {i}. <code>{html_escape(str(p))}</code> \u2192 user "
            f"<code>{u}</code> \u2014 <b>${a:.2f}</b>"
            for i, (p, u, a) in enumerate(refunded_rows[:25], 1))
        if len(refunded_rows) > 25:
            lines.append(f"  ... +{len(refunded_rows) - 25} more")
    if otp_live_list:
        lines.append("")
        lines.append("\U0001F6AB <b>Live OTP mila in par:</b> "
                     + ", ".join(
                         f"<code>{html_escape(str(p))}</code> "
                         f"(<code>{html_escape(str(c))}</code>)"
                         for p, c in otp_live_list[:5]))
    lines.append("")
    lines.append("\U0001F512 Har refund EK hi baar \u2014 refunded "
                 "number ka data wipe, dobara bhejo to match hi nahi "
                 "hoga.")
    await update.message.reply_text("\n".join(lines),
                                    parse_mode=ParseMode.HTML)
    logger.info("CHEK&REFUND by %s: %s numbers, %s refunded $%.2f, "
                "%s otp-skip, %s already-refunded, %s no-owner",
                admin_id, total, counters["refunded"], total_paid,
                counters["otp_live"] + counters["otp_db"],
                counters["already"],
                counters["not_sold"] + counters["no_owner"])


async def run_check_number(update, context, admin_id, text):
    """CHECK NUMBER engine: live-check every line, report + dead file."""
    entries, errors = parse_stock_lines(text)
    uniq = _uniq_entries(entries)
    if not uniq:
        await update.message.reply_text(
            "\u26A0\ufe0f <b>No checkable lines found.</b> Send the stock "
            "format: <code>number | url</code>",
            parse_mode=ParseMode.HTML)
        return
    total = len(uniq)
    counters = {"done": 0, "otp": 0, "clean": 0, "err": 0}

    def _line(c):
        return (f"\u2705 OTP: {c['otp']}   \u26AB No OTP: {c['clean']}   "
                f"\u26A0\ufe0f Err: {c['err']}")

    status = await update.message.reply_text(
        f"\U0001F50D <b>CHECKING {total} number(s)...</b>\n"
        f"{_progress_bar(0, total)} 0/{total} (0%)\n{_line(counters)}",
        parse_mode=ParseMode.HTML)
    otp_found, dead = [], []
    lock = asyncio.Lock()
    sem = asyncio.Semaphore(CHECK_WORKERS)
    last_edit = {"t": time.monotonic()}

    async def _work(phone, url):
        async with sem:
            try:
                res = await check_live_otp(url, timeout=CHECK_TIMEOUT)
            except Exception:
                res = ("unknown", None)
            async with lock:
                counters["done"] += 1
                if res[0] == "otp":
                    counters["otp"] += 1
                    otp_found.append((phone, res[1]))
                elif res[0] == "waiting":
                    counters["clean"] += 1
                    dead.append((phone, url))
                else:
                    counters["err"] += 1
        await _edit_progress(status,
                             f"\U0001F50D <b>CHECKING {total} "
                             f"number(s)...</b>",
                             dict(counters, line=_line), total, last_edit)

    await asyncio.gather(*[_work(p, u) for p, u in uniq])
    await _edit_progress(status,
                         f"\U0001F50D <b>CHECKING {total} number(s)...</b>",
                         dict(counters, line=_line), total, last_edit,
                         force=True)

    lines = [
        "\u2705 <b>CHECK COMPLETE</b>",
        "",
        DIV,
        f"\U0001F50D <b>Checked:</b> {total}",
        f"\u26AB <b>No OTP (refundable):</b> {counters['clean']}",
        f"\u2705 <b>OTP arrived (keep!):</b> {counters['otp']}",
        f"\u26A0\ufe0f <b>Unreachable (not included):</b> {counters['err']}",
    ]
    if errors:
        lines.append(f"\U0001F6A9 <b>Invalid lines skipped:</b> {len(errors)}")
    lines.append(DIV)
    if otp_found:
        lines.append("\u2705 <b>OTP seen on (do NOT refund):</b>")
        for phone, code in otp_found[:8]:
            lines.append(f"\U0001F7E2 <code>{html_escape(str(phone))}</code>"
                         f" \u2192 OTP <code>{html_escape(str(code))}</code>")
        if len(otp_found) > 8:
            lines.append(f"<i>\u2026and {len(otp_found) - 8} more</i>")
        lines.append("")
    if counters["err"]:
        lines.append("\u26A0\ufe0f Unreachable numbers are excluded \u2014 "
                     "run the check again for them later.")
        lines.append("")
    if dead:
        content = "\n".join(f"{p} | {u}" for p, u in dead)
        fname = ("checked_no_otp_%s.txt"
                 % _utcnow().strftime("%Y%m%d_%H%M%S"))
        lines.append(f"\U0001F4E5 Attached: <b>{len(dead)} number(s) with "
                     "NO OTP</b> \u2014 forward this file to \U0001F4B8 "
                     "Refund Send.")
        await update.message.reply_text("\n".join(lines),
                                        parse_mode=ParseMode.HTML)
        await update.message.reply_document(
            document=content.encode("utf-8"), filename=fname,
            caption=("\U0001F4C4 <b>No-OTP numbers</b> \u2014 stock format, "
                     "forward-ready for \U0001F4B8 Refund Send"),
            parse_mode=ParseMode.HTML)
    else:
        if counters["otp"] and not counters["err"]:
            lines.append("\U0001F389 Every number already has its OTP \u2014 "
                         "nothing to refund.")
        elif not counters["err"]:
            lines.append("\u2139\ufe0f Nothing to report \u2014 no dead "
                         "numbers found.")
        await update.message.reply_text("\n".join(lines),
                                        parse_mode=ParseMode.HTML)
    await clear_user_state(admin_id)


async def notify_user_refunded(context, user_id, phone, amount):
    """The buyer's instant success card (v9.27, localized)."""
    _lng = await get_user_lang(user_id)
    amount_s = f"{float(amount):.2f}"
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text=(
                f"{t(_lng, 'rfs_title')}\n"
                f"{DIV}\n"
                f"{t(_lng, 'rfs_body', number=html_escape(str(phone)), amount=amount_s)}"
            ),
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        logger.warning("refund notify failed user=%s: %s", user_id, e)


async def run_refund_send(update, context, admin_id, text):
    """REFUND SEND engine: match the forwarded no-OTP file against LIVE
    stock, re-verify each URL, refund the owners, wipe the rows."""
    entries, errors = parse_stock_lines(text)
    uniq = _uniq_entries(entries)
    if not uniq:
        await update.message.reply_text(
            "\u26A0\ufe0f <b>No refundable lines found.</b> Forward the "
            "file from \U0001F522 Check Number "
            "(<code>number | url</code>)",
            parse_mode=ParseMode.HTML)
        return
    total = len(uniq)
    counters = {"done": 0, "refunded": 0, "otp_live": 0, "otp_db": 0,
                "no_owner": 0, "unknown": 0, "no_price": 0}

    def _line(c):
        return (f"\u2705 Refunded: {c['refunded']}   "
                f"\U0001F6AB OTP: {c['otp_live'] + c['otp_db']}   "
                f"\U0001F465 No owner: {c['no_owner']}")

    status = await update.message.reply_text(
        f"\U0001F4B8 <b>REFUNDING {total} number(s)...</b>\n"
        f"{_progress_bar(0, total)} 0/{total} (0%)\n{_line(counters)}",
        parse_mode=ParseMode.HTML)
    refunded_rows, otp_live_list = [], []
    lock = asyncio.Lock()
    sem = asyncio.Semaphore(CHECK_WORKERS)
    last_edit = {"t": time.monotonic()}

    async def _refund_one(phone, url):
        row = await find_sold_stock_by_url(url)
        if row is None:
            async with lock:
                counters["done"] += 1
                counters["no_owner"] += 1
            return
        if row.get("otp_code"):
            async with lock:
                counters["done"] += 1
                counters["otp_db"] += 1
            return
        buyer = int(row["sold_to"])
        live = await check_live_otp(url, timeout=CHECK_TIMEOUT)
        if live[0] == "otp":
            async with lock:
                counters["done"] += 1
                counters["otp_live"] += 1
                otp_live_list.append((row["phone_number"], live[1]))
            return
        if live[0] == "unknown":
            # no positive proof of 'no OTP' -> no money moves (owner-safe)
            async with lock:
                counters["done"] += 1
                counters["unknown"] += 1
            return
        amount, order_id = await get_order_amount_for(
            buyer, row["phone_number"])
        if amount is None:
            rate_key = ("whatsapp_rate"
                        if row.get("number_type") == "whatsapp"
                        else "telegram_rate")
            try:
                amount = float(await get_setting(rate_key))
            except Exception:
                amount = 0.0
        if not amount or amount <= 0:
            async with lock:
                counters["done"] += 1
                counters["no_price"] += 1
            return
        # ATOMIC refund guard: wins only while still sold AND no OTP.
        if not await mark_stock_refunded(row["id"]):
            async with lock:
                counters["done"] += 1
                counters["otp_db"] += 1
            return
        await credit_refund_balance(buyer, float(amount))
        if order_id:
            try:
                await cancel_pending_referral(order_id)
            except Exception:
                logger.warning("referral cancel failed %s", order_id,
                               exc_info=True)
        try:
            await notify_user_refunded(context, buyer,
                                       row["phone_number"], float(amount))
        except Exception:
            pass
        async with lock:
            counters["done"] += 1
            counters["refunded"] += 1
            refunded_rows.append((row["phone_number"], buyer,
                                  float(amount)))
        await _edit_progress(
            status, f"\U0001F4B8 <b>REFUNDING {total} number(s)...</b>",
            dict(counters, line=_line), total, last_edit)

    await asyncio.gather(*[_refund_one(p, u) for p, u in uniq])
    await _edit_progress(
        status, f"\U0001F4B8 <b>REFUNDING {total} number(s)...</b>",
        dict(counters, line=_line), total, last_edit, force=True)

    total_paid = sum(a for _, _, a in refunded_rows)
    lines = [
        "\u2705 <b>REFUND SEND COMPLETE</b>",
        "",
        DIV,
        f"\U0001F4C4 <b>URLs in file:</b> {total}",
        f"\U0001F91D <b>Matched to owners:</b> "
        f"{counters['refunded'] + counters['otp_live'] + counters['otp_db']}",
        f"\u2705 <b>Refunded users:</b> {counters['refunded']} \u2014 "
        f"<b>${total_paid:.2f}</b> credited",
        f"\U0001F6AB <b>Skipped (OTP arrived):</b> "
        f"{counters['otp_live'] + counters['otp_db']} \u2014 money saved",
        f"\U0001F465 <b>No active owner (already refunded / not sold):</b> "
        f"{counters['no_owner']}",
    ]
    if counters["unknown"]:
        lines.append(f"\u26A0\ufe0f <b>Unreachable (NOT paid \u2014 run "
                     "again):</b> " + str(counters["unknown"]))
    if counters["no_price"]:
        lines.append(f"\u2139\ufe0f <b>No price found (skipped):</b> "
                     + str(counters["no_price"]))
    if errors:
        lines.append(f"\U0001F6A9 <b>Invalid lines skipped:</b> "
                     + str(len(errors)))
    lines.append(DIV)
    if refunded_rows:
        lines.append("\u2705 <b>Paid:</b>")
        for phone, buyer, amt in refunded_rows[:10]:
            lines.append(
                f"\U0001F7E2 <code>{html_escape(str(phone))}</code> \u2192 "
                f"${amt:.2f} \u2192 user <code>{buyer}</code>")
        if len(refunded_rows) > 10:
            lines.append(f"<i>\u2026and {len(refunded_rows) - 10} more</i>")
        lines.append("")
    if otp_live_list:
        lines.append("\U0001F6AB <b>OTP arrived \u2014 NO refund:</b>")
        for phone, code in otp_live_list[:8]:
            lines.append(
                f"\U0001F7E2 <code>{html_escape(str(phone))}</code> \u2192 "
                f"OTP <code>{html_escape(str(code))}</code>")
        if len(otp_live_list) > 8:
            lines.append(
                f"<i>\u2026and {len(otp_live_list) - 8} more</i>")
        lines.append("")
    lines.append("\U0001F512 Refunded numbers are wiped \u2014 the same "
                 "file can never match or pay again.")
    await update.message.reply_text("\n".join(lines),
                                    parse_mode=ParseMode.HTML)
    logger.info("REFUND SEND by %s: %s urls, %s refunded $%.2f, "
                "%s otp-blocked, %s no-owner",
                admin_id, total, counters["refunded"], total_paid,
                counters["otp_live"] + counters["otp_db"],
                counters["no_owner"])
    await clear_user_state(admin_id)


# --------------------------------------------------------------------------- #
#  INLINE NAV (Main Menu button on the receipt) + fallback for old buttons
# --------------------------------------------------------------------------- #
async def nav_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inline nav: home (fresh main menu, NOTHING deleted), dep, back, close."""
    q = update.callback_query
    await _safe_answer(q)
    uid = q.from_user.id
    action = q.data.split(":")[1]
    user = await get_user(uid)
    if user and user.get("is_banned"):
        await _send_tracked(update, context,
                            t(lang_of(user), "blocked"), None)
        return
    if action == "home":
        # Send a FRESH main menu — never delete or edit the current message
        lang = await get_user_lang(uid)
        await clear_user_state(uid)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=menu_info_text(lang),
            parse_mode=ParseMode.HTML,
            reply_markup=main_menu_kb(is_admin(uid), lang),
        )
    elif action == "dep":
        await show_dep_menu(update, context)
    elif action == "back":
        state, sdata = await get_user_state(uid)
        await go_back(update, context, state, sdata)
    elif action == "close":
        # Remove ONLY the buttons — the message text stays
        try:
            await q.edit_message_reply_markup(reply_markup=None)
        except Exception:
            pass


async def buy_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inline BUY flow: buy:wa|tg|ctry|do|back_type|back_ctry"""
    q = update.callback_query
    await _safe_answer(q)
    uid = q.from_user.id
    user = await get_user(uid)
    if user and user.get("is_banned"):
        await _send_tracked(update, context,
                            t(lang_of(user), "blocked"), None)
        return
    parts = q.data.split(":")
    act = parts[1]
    if act in ("wa", "tg") and len(parts) == 2:
        # type button (buy:wa / buy:tg) -> country list
        return await show_buy_country(update, context, act)
    if act in ("wa", "tg") and len(parts) >= 3:
        # country button (buy:wa:USA) -> confirm screen
        return await show_buy_confirm(update, context, act, parts[2])
    if act == "ctry" and len(parts) >= 4:
        # legacy format kept for old inline buttons
        return await show_buy_confirm(update, context, parts[2], parts[3])
    if act == "do" and len(parts) >= 4:
        return await do_purchase(update, context, uid, parts[2], parts[3])
    if act == "back_type":
        return await show_buy_type(update, context)
    if act == "back_ctry" and len(parts) >= 3:
        return await show_buy_country(update, context, parts[2])


async def dep_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inline DEPOSIT flow: dep:new|hist|back|amt|custom|net|paid|cancel"""
    q = update.callback_query
    uid = q.from_user.id
    user = await get_user(uid)
    if user and user.get("is_banned"):
        await _send_tracked(update, context,
                            t(lang_of(user), "blocked"), None)
        return
    parts = q.data.split(":")
    act = parts[1]
    if act == "amt" and len(parts) >= 3:
        # v9.20: parse BEFORE answering - the bad-amount alert is the
        # one and only answer for this query (single-answer rule)
        try:
            amount = float(parts[2])
        except ValueError:
            amount = None
        if amount is None or not math.isfinite(amount) or amount <= 0:
            await _safe_answer(q, t(await get_user_lang(uid),
                                    "toast_bad_amount"),
                               show_alert=True)
            return
        await _safe_answer(q)
        return await show_dep_networks(update, context, amount)
    await _safe_answer(q)
    if act == "new":
        return await show_dep_amount(update, context)
    if act == "hist":
        return await show_dep_history(update, context)
    if act == "back":
        return await show_dep_menu(update, context)
    if act == "custom":
        return await prompt_custom_amount(update, context, uid)
    if act == "net" and len(parts) >= 3:
        state, sdata = await get_user_state(uid)
        if state != "dep_net" or not (sdata or {}).get("amount"):
            _lng = await get_user_lang(uid)
            return await _send_tracked(
                update, context,
                t(_lng, "dep_expired_session"),
                main_menu_kb(is_admin(uid), _lng))
        return await deposit_create(update, context, uid,
                                    float(sdata["amount"]), parts[2])
    if act == "paid" and len(parts) >= 3:
        dep_id = parts[2]
        state, sdata = await get_user_state(uid)
        if state != "awaiting_txid" or \
                (sdata or {}).get("deposit_id") != dep_id:
            _lng = await get_user_lang(uid)
            return await _send_tracked(
                update, context,
                t(_lng, "dep_no_active"),
                main_menu_kb(is_admin(uid), _lng))
        dep = await get_deposit(dep_id)
        if not dep or dep.get("status") != "pending":
            await clear_user_state(uid)
            _lng = await get_user_lang(uid)
            return await _send_tracked(
                update, context,
                t(_lng, "dep_closed"),
                main_menu_kb(is_admin(uid), _lng))
        _lng = await get_user_lang(uid)
        return await _send_tracked(
            update, context,
            txid_prompt_text(dep_id,
                             (sdata or {}).get("network") or "bep20", _lng),
            txid_input_kb(dep_id, _lng))
    if act == "cancel":
        dep_id = parts[2] if len(parts) >= 3 else None
        if not dep_id:
            state, sdata = await get_user_state(uid)
            if state == "awaiting_txid":
                dep_id = (sdata or {}).get("deposit_id")
        if dep_id:
            await cancel_pending_deposit(uid, dep_id)
        await clear_user_state(uid)
        _lng = await get_user_lang(uid)
        return await _send_tracked(update, context,
                                   t(_lng, "dep_cancelled") + "\n\n"
                                   + menu_info_text(_lng),
                                   main_menu_kb(is_admin(uid), _lng))


async def admin_flow_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin inline flows: adst:wa|tg|back, adstc:<ntype>:<country>,
    adrt:wa|tg, adbn:ban|unban"""
    q = update.callback_query
    uid = q.from_user.id
    if not is_admin(uid):
        await _safe_answer(q, "Admins only", show_alert=True)
        return
    await _safe_answer(q)
    parts = q.data.split(":")
    grp, act = parts[0], parts[1]
    if grp == "adst":
        if act in ("wa", "tg"):
            return await show_admin_add_country(update, context, act)
        if act == "back":
            return await show_admin_add_type(update, context)
    if grp == "adstc" and len(parts) >= 3:
        return await prompt_admin_add_phone(update, context, parts[1], parts[2])
    if grp == "adrt" and act in ("wa", "tg"):
        return await prompt_admin_set_rate(update, context, act)
    if grp == "adbn" and act in ("ban", "unban"):
        return await prompt_admin_ban(update, context, act)
    if grp == "admuser":
        if act == "bal" and len(parts) >= 3:
            try:
                target = int(parts[2])
            except ValueError:
                await _safe_answer(q, "Invalid user", show_alert=True)
                return
            return await prompt_admin_modbal(update, context, target)
        if act == "back":
            return await show_admin_panel(update, context)


async def fallback_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gracefully answer old inline buttons from previous bot versions."""
    q = update.callback_query
    await q.answer("\u274C This button expired \u2014 please retry", show_alert=True)


# --------------------------------------------------------------------------- #
#  v9.10.1 DEPOSIT VERIFICATION - TXID ONLY, NO AUTO-CREDIT
#  Flow: user pays -> taps I PAID -> sends the TXID -> the bot checks that
#  exact transaction on-chain (right network, right wallet, USDT contract,
#  success status, enough confirmations, amount >= order) and only then
#  credits. There is NO amount-matching poller anymore: with many users
#  paying equal amounts at the same time, an amount alone can never prove
#  which order a payment belongs to - the TXID can, and it is mandatory.
# --------------------------------------------------------------------------- #
TXID_RE = re.compile(r"^0x[0-9a-fA-F]{64}$")


def token_value_usdt(transfer: dict) -> float:
    """On-chain raw token value -> USDT float (decimals read per transfer)."""
    try:
        raw = int(transfer.get("value") or "0")
    except (TypeError, ValueError):
        return 0.0
    try:
        dec = int(transfer.get("tokenDecimal") or 18)
    except (TypeError, ValueError):
        dec = 18
    return raw / (10 ** dec)


async def _bsc_rpc(method, params):
    """One JSON-RPC call, rotating public BSC endpoints.
    Returns the result value, or None when every endpoint failed."""
    payload = {"jsonrpc": "2.0", "id": 1, "method": method,
               "params": params}
    session = await http_session()
    for url in BSC_RPC_ENDPOINTS:
        host = url.split("/")[2]
        try:
            async with session.post(
                url, json=payload,
                timeout=aiohttp.ClientTimeout(total=BSC_RPC_TIMEOUT),
            ) as resp:
                data = await resp.json(content_type=None)
        except Exception as e:
            logger.warning("BSC RPC %s %s failed: %s",
                           host, method, str(e)[:80])
            continue
        if isinstance(data, dict) and data.get("error") is None \
                and "result" in data:
            return data["result"]
        logger.warning("BSC RPC %s rejected %s: %s", host, method,
                       str(data.get("error"))[:80]
                       if isinstance(data, dict) else str(data)[:80])
    return None


def _topic_for_address(addr: str) -> str:
    """0x-address -> 32-byte event topic (left-padded)."""
    return "0x" + "0" * 24 + (addr or "").lower().replace("0x", "")


def _addr_from_topic(topic: str) -> str:
    """32-byte event topic -> 0x-address."""
    return "0x" + (topic or "0x")[-40:]


def _log_to_transfer(lg: dict, ts: int, decimals: int = 18) -> dict:
    """One eth_getLogs entry -> transfer dict (same shape the bot
    used to get from the explorer API)."""
    topics = lg.get("topics") or []
    try:
        raw = int(lg.get("data") or "0x0", 16)
    except (TypeError, ValueError):
        raw = 0
    try:
        block = int(lg.get("blockNumber"), 16)
    except (TypeError, ValueError):
        block = 0
    return {
        "hash": (lg.get("transactionHash") or "").lower(),
        "from": _addr_from_topic(topics[1] if len(topics) > 1 else "0x"),
        "to": _addr_from_topic(topics[2] if len(topics) > 2 else "0x"),
        "value": str(raw),
        "tokenDecimal": str(decimals),
        "timeStamp": str(ts),
        "confirmations": "0",
        "blockNumber": block,
    }


async def bsc_tx_usdt_transfer(txid: str, wallet: str = None):
    """Look up ONE transaction by hash via its receipt (public RPC).
    Returns (transfer_or_None, state) with state in:
      "found"           tx succeeded and carries USDT -> our wallet
      "pending"         tx not found yet (still mining / unknown hash)
      "failed"          tx exists but reverted on-chain
      "wrong_token"     no USDT transfer event in the tx
      "wrong_recipient" USDT moved, but NOT to our deposit wallet
    Only a SUCCESSFUL execution emits logs, so a found transfer is
    automatically confirmed on-chain."""
    receipt = await _bsc_rpc("eth_getTransactionReceipt",
                             [(txid or "").lower()])
    if not isinstance(receipt, dict) or not receipt:
        return None, "pending"
    if str(receipt.get("status", "")).lower() not in ("0x1", "0x01"):
        return None, "failed"
    conf = await _evm_confirmations(BSC_RPC_ENDPOINTS,
                                    receipt.get("blockNumber"))
    if conf is not None and conf < EVM_MIN_CONFIRMATIONS:
        return None, "pending"          # found but too fresh - wait
    contract = ((await get_setting("usdt_bep20_contract")
                 or USDT_BEP20_CONTRACT)).lower()
    # v9.12: use the wallet bound to THIS order first (trace-safe
    # across wallet rotations), fall back to the current setting.
    wallet = ((wallet or "").strip().lower()
              or (await get_setting("usdt_wallet_address")
                  or "").strip().lower())
    saw_usdt = False
    for lg in receipt.get("logs") or []:
        if not isinstance(lg, dict):
            continue
        if (lg.get("address") or "").lower() != contract:
            continue
        topics = lg.get("topics") or []
        if len(topics) < 3 \
                or str(topics[0]).lower() != USDT_TRANSFER_TOPIC:
            continue
        saw_usdt = True
        if _addr_from_topic(topics[2]).lower() != wallet:
            continue
        try:
            block = int(receipt.get("blockNumber") or "0x0", 16)
        except (TypeError, ValueError):
            block = 0
        bh = await _bsc_rpc("eth_getBlockByNumber",
                            [receipt.get("blockNumber") or "0x0", False])
        try:
            ts = int((bh or {}).get("timestamp"), 16)
        except (TypeError, ValueError):
            ts = 0
        return _log_to_transfer(lg, ts), "found"
    if saw_usdt:
        return None, "wrong_recipient"
    return None, "wrong_token"


async def hash_already_credited(tx_hash: str) -> bool:
    """One on-chain transaction can pay for ONE deposit only - ever."""
    h = (tx_hash or "").strip().lower()
    if not h:
        return False
    async with adb() as db:
        cur = await db.execute(
            "SELECT 1 FROM deposits WHERE LOWER(tx_hash)=? "
            "AND status='confirmed' LIMIT 1",
            (h,),
        )
        row = await cur.fetchone()
        await cur.close()
        return row is not None


async def mark_usdt_seen(tx_hash, ts, value, matched):
    """Record an incoming transfer the FIRST time we see it.
    Returns True only on the first insert (alert-once guarantee)."""
    h = (tx_hash or "").strip().lower()
    if not h:
        return False
    async with adb() as db:
        cur = await db.execute(
            "INSERT OR IGNORE INTO usdt_seen(hash,ts,value,matched) "
            "VALUES(?,?,?,?)",
            (h, int(ts or 0), float(value or 0.0), int(matched or 0)),
        )
        return cur.rowcount > 0


# --------------------------------------------------------------------------- #
#  v9.32 BINANCE PAY VERIFY ENGINE
#  Official API only (signed GET /sapi/v1/pay/transactions). Every failure
#  degrades to "pending + manual Order-ID + admin approval" - nothing here
#  can crash a handler or mis-credit a balance.
# --------------------------------------------------------------------------- #
# ===========================================================================
# vCENTRAL 1.0 — GLOBAL ONE-PAYMENT-ONE-CREDIT (BINANCE_CENTRAL integration)
# Ab Binance Pay verification LOCAL central service (127.0.0.1:8790) se hogi.
# Central service owner ki Pay history fetch karti hai, Order ID match karti
# hai aur SUCCESS hone par payment ko ATOMICALLY is bot ke liye CLAIM kar
# leti hai — manual path + 45s sweeper dono. Same payment kisi doosre bot me
# kabhi credit nahi hogi. Fail-closed: central down -> api_error (existing
# "API busy, retry later" UX — user ka fault nahi, attempts nahi badhte).
# ===========================================================================
CENTRAL_API_URL = os.getenv("CENTRAL_API_URL", "http://127.0.0.1:8790")
CENTRAL_AUTH_TOKEN = os.getenv("CENTRAL_AUTH_TOKEN", "")
CENTRAL_TIMEOUT_S = 25


async def _central_claim(order_id, expected_amount, bot, created_ts=None, tx=None):
    """POST /v1/claim on the central Binance service (localhost).
    Returns parsed dict; {"status": "central_down"} on any failure."""
    try:
        want = round(float(expected_amount or 0.0), 2)
    except (TypeError, ValueError):
        want = 0.0
    payload = {"order_id": str(order_id or ""), "expected_amount": want,
               "bot": bot, "tolerance": AMOUNT_MATCH_TOLERANCE}
    if created_ts:
        payload["created_ts"] = int(created_ts)
    if tx is not None:
        payload["tx"] = tx
    body = json.dumps(payload).encode("utf-8")
    url = "%s/v1/claim" % CENTRAL_API_URL.rstrip("/")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, data=body,
                timeout=aiohttp.ClientTimeout(total=CENTRAL_TIMEOUT_S),
                headers={"Content-Type": "application/json",
                         "X-Auth-Token": CENTRAL_AUTH_TOKEN},
            ) as resp:
                if resp.status != 200:
                    logger.warning("central claim HTTP %s", resp.status)
                    return {"status": "central_down"}
                return await resp.json(content_type=None)
    except Exception as e:
        logger.critical("BINANCE_CENTRAL unreachable: %s", str(e)[:120])
        return {"status": "central_down"}


def _binance_sign(query: str) -> str:
    """HMAC-SHA256 signature the official Binance API demands."""
    return hmac.new(BINANCE_PAY_SECRET.encode("utf-8"),
                    query.encode("utf-8"), hashlib.sha256).hexdigest()


async def binance_pay_fetch_history(limit: int = BINANCE_HISTORY_LIMIT):
    """Signed GET /sapi/v1/pay/transactions. Returns the transaction
    list ([] when empty) or None on ANY failure (network, auth,
    IP-restriction, API reject) - callers degrade gracefully."""
    if not BINANCE_PAY_API_KEY or not BINANCE_PAY_SECRET:
        return None
    try:
        ts = int(time.time() * 1000)
        query = f"timestamp={ts}&recvWindow=10000&limit={int(limit)}"
        url = (f"{BINANCE_API_BASE}/sapi/v1/pay/transactions?"
               f"{query}&signature={_binance_sign(query)}")
        session = await http_session()
        async with session.get(
            url, headers={"X-MBX-APIKEY": BINANCE_PAY_API_KEY},
            timeout=aiohttp.ClientTimeout(total=BINANCE_PAY_TIMEOUT),
        ) as resp:
            data = await resp.json(content_type=None)
    except Exception as e:
        logger.warning("Binance Pay history fetch failed: %s", str(e)[:100])
        return None
    if not isinstance(data, dict) or str(data.get("code")) != "000000":
        logger.warning("Binance Pay API rejected: %s", str(data)[:140])
        return None
    rows = data.get("data")
    return rows if isinstance(rows, list) else []


def _binance_tx_ids(tx: dict) -> list:
    """ALL id forms of ONE Pay transfer. LIVE-VERIFIED 2026-09:
    orderId = pure digits (the Order ID the Binance app shows the
    user), transactionId = P_XXXXXXXXXXXXXXXX. The same payment can be
    submitted in either form - matching and replay must cover both."""
    ids = []
    for f in ("orderId", "transactionId", "orderNo"):
        v = str(tx.get(f) or "").strip().lower()
        if v and v not in ids:
            ids.append(v)
    return ids


def _binance_tx_id(tx: dict) -> str:
    """CANONICAL replay key: orderId (app-shown) else transactionId."""
    ids = _binance_tx_ids(tx)
    return ids[0] if ids else ""


def _binance_tx_incoming(tx: dict) -> bool:
    """Funds IN to the owner's account. LIVE-VERIFIED 2026-09 with the
    owner's real keys: /sapi/v1/pay/transactions returns a SIGNED amount
    (positive = money IN, negative = money OUT) and no fundsIn /
    transactionType fields; those doc-shaped fields are still honoured
    first if a future API revision reintroduces them."""
    try:
        amt = float(tx.get("amount") or 0.0)
    except (TypeError, ValueError):
        return False
    if amt != 0:
        return amt > 0
    if tx.get("fundsIn") is not None:
        return str(tx.get("fundsIn")) == "2"
    if tx.get("transactionType") is not None:
        return str(tx.get("transactionType")) == "2"
    return False


def _binance_tx_amount(tx: dict) -> float:
    """ABSOLUTE transferred amount (the live API signs it: -1 = sent out)."""
    try:
        v = abs(float(tx.get("amount") or 0.0))
    except (TypeError, ValueError):
        return 0.0
    return v if math.isfinite(v) else 0.0


def _binance_tx_time_ms(tx: dict) -> int:
    try:
        return int(tx.get("transactionTime") or 0)
    except (TypeError, ValueError):
        return 0


def binance_tx_matches(tx: dict, order_id: str) -> bool:
    """Pasted id matches ANY id form of the transfer, exactly or by its
    trailing segment (users copy with/without the P_ / M_P_ prefix)."""
    oid = re.sub(r"\s+", "", str(order_id or "")).lower()
    if not oid:
        return False
    for tid in _binance_tx_ids(tx):
        if tid == oid or tid.rsplit("_", 1)[-1] == oid:
            return True
    return False


def binance_transfer_shape(tx: dict, pay_id: str) -> dict:
    """Map a Pay transaction onto the on-chain transfer shape the
    existing pipeline consumes (token_value_usdt reads value/decimal)."""
    amt = _binance_tx_amount(tx)
    return {
        "hash": _binance_tx_id(tx).lower(),
        "from": str(tx.get("counterpartyId")
                    or tx.get("initiatorUserId") or ""),
        "to": pay_id,
        "value": str(int(round(amt * 100_000_000))),
        "tokenDecimal": "8",       # 1e8 scaling -> exact USDT float
        "timeStamp": str(_binance_tx_time_ms(tx) // 1000),
        "confirmations": "1",
        "blockNumber": 0,
    }


async def binance_pay_order_transfer(order_id, dep=None):
    """vCENTRAL: Order-ID check + GLOBAL claim via the central Binance
    service. State mapping identical to the previous direct-API flow:
      claimed                     -> (transfer, "found")
      already_used / failed       -> (None, "failed")
      not_found / amount_mismatch -> (None, "pending")
      wrong_token                 -> (None, "wrong_token")
      wrong_recipient             -> (None, "wrong_recipient")
      central_down                -> (None, "api_error")
    On 'claimed' the payment is locked GLOBALLY for THIS bot — no other
    bot on this VPS can ever credit the same payment."""
    created = 0
    if dep:
        try:
            created = int(dep.get("created_ts") or 0)
        except (TypeError, ValueError):
            created = 0
    want = 0.0
    if dep:
        try:
            want = float(dep.get("pay_amount") or dep.get("amount") or 0.0)
        except (TypeError, ValueError):
            want = 0.0
    res = await _central_claim(order_id, want, "bdusawp",
                               created_ts=created or None)
    st = str(res.get("status") or "central_down")
    if st == "central_down":
        return None, "api_error"
    if st in ("already_used", "failed"):
        return None, "failed"
    if st in ("not_found", "amount_mismatch"):
        return None, "pending"
    if st == "wrong_token":
        return None, "wrong_token"
    if st == "wrong_recipient":
        return None, "wrong_recipient"
    if st != "claimed":
        return None, "api_error"
    tx = res.get("tx") or {}
    pay_id = (await get_setting("binance_pay_id")
              or BINANCE_PAY_ID_DEFAULT)
    return binance_transfer_shape(tx, pay_id), "found"


async def _unique_binance_amount(base: float) -> float:
    """v9.35 EXACT AMOUNT (owner order: "0.30 hi ho, koi bhi binance
    me ya kahi bhi"): the order charges EXACTLY the amount the user
    picked - the v9.32 unique-cent bump (+$0.01 steps) is RETIRED.
    Binding rides ONLY on the user-submitted Order ID (v9.44): the
    sweep just retries orders whose Order ID was submitted - no
    Order ID, no credit; the manual Order-ID path credits the
    SUBMITTER's own order - one Order ID = one credit, ever."""
    try:
        b = float(base)
    except (TypeError, ValueError):
        return 0.0
    if not math.isfinite(b) or b <= 0:
        return 0.0
    return round(b, 2)


async def get_pending_binance_deposits():
    async with adb() as db:
        cur = await db.execute(
            "SELECT * FROM deposits "
            "WHERE status='pending' AND network='binance' "
            "ORDER BY id ASC")
        rows = await cur.fetchall()
        await cur.close()
        return [dict(r) for r in rows]


async def binance_pay_probe():
    """Boot probe: is the official Binance API reachable with the
    configured keys? Returns (True, '') or (False, reason) - never raises."""
    rows = await binance_pay_fetch_history(limit=1)
    if rows is None:
        return False, ("API unreachable/rejected - check key/secret, "
                       "IP-whitelist and permissions in Binance API "
                       "Management")
    return True, ""


async def binance_pay_sweeper(app):
    """v9.44 ORDER-ID-ONLY sweep (owner order: bina Order ID ke credit
    NAHI): every 45s, pending Binance orders whose Order ID was SUBMITTED
    by the user (stored tx_hash) are re-verified via the central service
    - Order ID + amount match -> credit (identical rules to the manual
    submission path). Orders with NO submitted Order ID are NEVER
    auto-credited; they stay pending until the user submits the Order ID
    (or the owner approves manually via Pending Deposits). Central down
    -> orders stay pending, retry next cycle.
    After a credit: the SAME deposit-group forward + user DM as every
    other network (notify_deposit_verified)."""
    logger.info("Binance Pay sweeper armed: every %ss, history limit %s",
                BINANCE_SWEEP_SECONDS, BINANCE_HISTORY_LIMIT)
    while True:
        try:
            await asyncio.sleep(BINANCE_SWEEP_SECONDS)
            pend = await get_pending_binance_deposits()
            if not pend:
                continue
            # v9.44 OWNER ORDER: bina Order ID ke auto-credit BAND.
            # Sweep = RETRY engine sirf un pending orders ke liye jinme
            # user ne Order ID submit kiya (tx_hash). Order ID + amount
            # central pe match hoga TABHI credit. Amount-only matching
            # REMOVED - galat user ko galat credit ka bug dead.
            for dep in pend:
                dep_id = dep["deposit_id"]
                submitted = str(dep.get("tx_hash") or "").strip().lower()
                if not submitted:
                    continue        # NO submitted Order ID -> no credit
                transfer, tstate = await binance_pay_order_transfer(
                    submitted, dep)
                if tstate != "found" or not isinstance(transfer, dict):
                    continue
                tid = str(transfer.get("hash") or "").strip().lower()
                if not tid or await hash_already_credited(tid):
                    continue
                amt = token_value_usdt(transfer)
                if amt <= 0:
                    continue
                credited = await credit_auto_deposit(dep_id, tid, amt,
                                                     "binance_auto")
                if credited:
                    await trace_deposit(dep_id, dep["user_id"], "binance",
                                        tid, "sweep_matched",
                                        "$%.2f order-id-retry" % amt)
                    try:
                        await notify_deposit_verified(app.bot, credited,
                                                      amt, "binance_auto")
                    except Exception as e:
                        logger.warning("Binance sweep notify failed: %s",
                                       str(e)[:100])
                    logger.info("Binance Pay RETRY-CREDIT: order %s +$%.2f "
                                "(submitted id %s)", dep_id, amt, submitted)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            logger.warning("Binance sweeper cycle failed: %s", str(e)[:120])


# --------------------------------------------------------------------------- #
#  v9.12: deposit audit trail (append-only) - trace_deposit below is shared
#  by every deposit path (TXID on-chain + Binance Pay order-id + sweep).
# --------------------------------------------------------------------------- #
async def trace_deposit(deposit_id, user_id, network, txid, event,
                        detail=""):
    """v9.12: append-only audit trail. Every deposit event lands in
    deposit_trace + journalctl. Never raises - tracing must never
    break verification or crediting."""
    try:
        async with adb() as db:
            await db.execute(
                "INSERT INTO deposit_trace(ts,deposit_id,user_id,"
                "network,txid,event,detail) VALUES(?,?,?,?,?,?,?)",
                (int(_utcnow().timestamp()), deposit_id or "-",
                 user_id or 0, network or "-", (txid or "")[:80],
                 event, (detail or "")[:300]))
    except Exception as e:
        logger.warning("deposit_trace write failed: %s", e)
    try:
        logger.info("[TRACE] %s dep=%s user=%s net=%s tx=%s %s",
                    event, deposit_id, user_id, network,
                    (txid or "")[:18], detail)
    except Exception:
        pass


async def _bump_txid_attempt(deposit_id):
    """Count one more failed TXID try on this order (brute-force cap)."""
    async with adb() as db:
        await db.execute(
            "UPDATE deposits SET attempts=attempts+1 WHERE deposit_id=?",
            (deposit_id,))


async def credit_auto_deposit(deposit_id, tx_hash, credited, mode):
    """Confirm a pending deposit + credit the user. v9.21 LOOT-PROOF:
    the whole decide+mark+credit runs inside ONE BEGIN IMMEDIATE
    transaction that ALSO re-checks TXID replay - two accomplice
    accounts submitting the same valid on-chain tx on two pending
    deposits can never both win (the second sees the first's committed
    tx_hash and gets None). Double-poll / double-tap stay impossible
    via the pending-only guard. Returns the deposit row on success,
    None if it was already decided or the tx paid another deposit."""
    h = (tx_hash or "").strip().lower()
    conn = await _get_shared_db()
    async with _tx_lock():
        await conn.execute("BEGIN IMMEDIATE")
        try:
            if h:
                cur = await conn.execute(
                    "SELECT 1 FROM deposits WHERE LOWER(tx_hash)=? "
                    "AND status='confirmed' AND deposit_id<>? LIMIT 1",
                    (h, deposit_id),
                )
                replay = await cur.fetchone()
                await cur.close()
                if replay:
                    await conn.execute("ROLLBACK")
                    return None
            cur = await conn.execute(
                "SELECT * FROM deposits WHERE deposit_id=? "
                "AND status='pending'",
                (deposit_id,),
            )
            row = await cur.fetchone()
            await cur.close()
            if not row:
                await conn.execute("ROLLBACK")
                return None
            dep = dict(row)
            cur = await conn.execute(
                "UPDATE deposits SET status='confirmed', tx_hash=?, "
                "confirmed_by=0, confirmed_at=datetime('now'), "
                "verified_at=datetime('now'), match_mode=? "
                "WHERE deposit_id=? AND status='pending'",
                (tx_hash, mode, deposit_id),
            )
            if cur.rowcount == 0:    # decided between the two queries
                await cur.close()
                await conn.execute("ROLLBACK")
                return None
            await cur.close()
            await conn.execute(
                "UPDATE users SET balance=balance+?, "
                "total_deposit=total_deposit+?, updated_at=datetime('now') "
                "WHERE telegram_id=?",
                (credited, credited, dep["user_id"]),
            )
            await conn.commit()
        except Exception:
            try:
                await conn.execute("ROLLBACK")
            except Exception:
                pass
            raise
    dep["credited"] = credited
    dep["tx_hash"] = tx_hash
    return dep


async def clear_deposit_state_if_current(uid, deposit_id):
    state, sdata = await get_user_state(uid)
    if state == "awaiting_txid" and \
            (sdata or {}).get("deposit_id") == deposit_id:
        await clear_user_state(uid)


async def notify_deposit_verified(bot, dep, credited, mode):
    """User DM + FULL-DETAIL deposit-group post after a verified deposit.
    No screenshots - everything the admin needs is in the text."""
    uid = dep["user_id"]
    dep_id = dep["deposit_id"]
    txh = dep.get("tx_hash") or ""
    network = dep.get("network") or "bep20"
    meta = DEPOSIT_NETWORKS.get(network) or DEPOSIT_NETWORKS["bep20"]
    user = await get_user(uid)
    bal = (user or {}).get("balance", 0.0) or 0.0
    total_dep = (user or {}).get("total_deposit", 0.0) or 0.0
    _ulang = await get_user_lang(uid)
    try:
        await bot.send_message(
            chat_id=uid,
            text=t(_ulang, "dm_credited",
                   amount=f"{credited:.2f}", bal=f"{bal:.2f}",
                   order=dep_id),
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        logger.warning("auto-verify user DM failed: %s", e)
    name = (user.get("first_name") or "User") if user else "User"
    uname = (f"@{user['username']}"
             if user and user.get("username") else "no username")
    profile = (f'<a href="tg://user?id={uid}">'
               f'{html_escape(name)}</a>')
    group_id = await get_setting("deposit_group_id")
    txt = (
        f"\U0001F916 <b>DEPOSIT CONFIRMED</b>\n\n"
        f"{DIV}\n"
        f"\U0001F464 <b>User:</b> {profile}\n"
        f"\U0001F517 Username: {uname}\n"
        f"\U0001F194 <b>Chat ID:</b> <code>{uid}</code>\n"
        f"\U0001F4CB <b>Order:</b> <code>{html_escape(dep_id)}</code>\n"
        f"\U0001F4B5 <b>Deposit:</b> ${credited:.2f} USDT\n"
        f"\U0001F310 <b>Network:</b> {meta['short']}\n"
        f"\U0001F4CD <b>{'Binance Pay ID' if network == 'binance' else 'Wallet'}:</b> <code>{html_escape(dep.get('usdt_address') or '-')}</code>\n"
        f"\U0001F9FE <b>{'Order ID' if network == 'binance' else 'TXID'}:</b> <code>{html_escape(txh[:50])}</code>\n"
        f"\U0001F4C8 <b>Total Deposited:</b> ${total_dep:.2f}\n"
        f"\U0001F4B0 <b>Bot Balance Now:</b> ${bal:.2f}\n"
        f"{DIV}"
    )
    if meta.get("scan"):    # v9.32: on-chain nets keep the explorer link;
        txt += (f"\n\U0001F30D {meta['scan']}{html_escape(txh)}"
                )            # Binance Pay has none - Order ID is the proof
    targets = []
    if group_id:
        try:
            targets.append(int(group_id))
        except Exception:
            pass
    # v9.41: deposit notice MAIN admin ONLY (extra admins excluded)
    targets.append(ADMIN_ID)
    for tgt in dict.fromkeys(targets):
        try:
            await bot.send_message(chat_id=tgt, text=txt,
                                   parse_mode=ParseMode.HTML,
                                   disable_web_page_preview=True)
        except Exception as e:
            logger.warning("deposit notice to %s failed: %s", tgt, e)




async def _evm_rpc(endpoints, method, params):
    """One JSON-RPC call against a list of EVM endpoints (Polygon etc.).
    Returns the result value, or None when every endpoint failed."""
    payload = {"jsonrpc": "2.0", "id": 1, "method": method,
               "params": params}
    session = await http_session()
    for url in endpoints:
        host = url.split("/")[2]
        try:
            async with session.post(
                url, json=payload,
                timeout=aiohttp.ClientTimeout(total=BSC_RPC_TIMEOUT),
            ) as resp:
                data = await resp.json(content_type=None)
        except Exception as e:
            logger.warning("EVM RPC %s %s failed: %s",
                           host, method, str(e)[:80])
            continue
        if isinstance(data, dict) and data.get("error") is None \
                and "result" in data:
            return data["result"]
        logger.warning("EVM RPC %s rejected %s: %s", host, method,
                       str(data.get("error"))[:80]
                       if isinstance(data, dict) else str(data)[:80])
    return None


async def _evm_confirmations(endpoints, block_number):
    """(latest head - tx block) for an EVM receipt, or None if unknown.
    Never blocks verification on its own - only enforces depth when the
    head is readable (receipt status=1 alone already proves inclusion)."""
    try:
        block = int(block_number or "0x0", 16)
    except (TypeError, ValueError):
        return None
    if block <= 0:
        return None
    latest = await _evm_rpc(endpoints, "eth_blockNumber", [])
    try:
        head = int(latest, 16)
    except (TypeError, ValueError):
        return None
    return head - block


_TRON_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def _tron_hex_to_base58(hex_addr: str) -> str:
    """41-prefixed hex TRON address -> base58check (T...)."""
    raw = bytes.fromhex(hex_addr.replace("0x", "").lower())
    if len(raw) != 21 or raw[0] != 0x41:
        return ""
    h = hashlib.sha256(hashlib.sha256(raw).digest()).digest()
    raw += h[:4]
    n = int.from_bytes(raw, "big")
    out = ""
    while n:
        n, r = divmod(n, 58)
        out = _TRON_ALPHABET[r] + out
    return out


def _tron_to_hex_body(addr: str) -> str:
    """Any TRON address form (T... base58 or 41.. hex) -> 40-hex body."""
    a = (addr or "").strip()
    if a.startswith("T") and len(a) == 34:
        try:
            raw = bytearray()
            n = 0
            for ch in a:
                n = n * 58 + _TRON_ALPHABET.index(ch)
            raw = n.to_bytes(25, "big")
            h = hashlib.sha256(hashlib.sha256(raw[:21]).digest()).digest()
            if raw[21:] != h[:4] or raw[0] != 0x41:
                return ""
            return raw[1:21].hex()
        except Exception:
            return ""
    a = a.lower().replace("0x", "")
    return a[2:42] if a.startswith("41") and len(a) >= 42 else a[:40]


async def trc20_tx_transfer(txid: str, wallet: str):
    """TRC-20 (Tron) USDT transfer lookup via public Trongrid events API.
    Returns (transfer_dict, state) - same states as the EVM path."""
    url = f"{TRONGRID_BASE}/v1/transactions/{txid}/events"
    want = _tron_to_hex_body(wallet)
    try:
        session = await http_session()
        async with session.get(
            url, timeout=aiohttp.ClientTimeout(total=BSC_RPC_TIMEOUT)
        ) as resp:
            data = await resp.json(content_type=None)
    except Exception as e:
        logger.warning("Trongrid events failed: %s", str(e)[:80])
        return None, "pending"
    if not isinstance(data, dict) or data.get("success") is not True:
        return None, "pending"          # unknown hash = not indexed yet
    events = data.get("data") or []
    saw_usdt = False
    for ev in events:
        if not isinstance(ev, dict):
            continue
        ca = (ev.get("contract_address") or "")
        if ca.replace("0x", "").lower() != \
                _tron_to_hex_body(TRC20_USDT_CONTRACT):
            continue
        if (ev.get("event_name") or "") != "Transfer" and \
                len(ev.get("result", {}) or {}) < 3:
            continue
        res = ev.get("result") or {}
        to = res.get("to") or ""
        saw_usdt = True
        if _tron_to_hex_body(to) != want:
            continue
        try:
            raw = int(str(res.get("value") or "0"))
        except (TypeError, ValueError):
            raw = 0
        block = ev.get("block") or ev.get("block_number") or 0
        return ({"hash": txid.lower(), "to": wallet,
                 "value": str(raw), "tokenDecimal": "6",
                 "timeStamp": "0", "confirmations": "1",
                 "blockNumber": block}), "found"
    if saw_usdt:
        return None, "wrong_recipient"
    return None, "wrong_token"


async def polygon_tx_usdt_transfer(txid: str, wallet: str):
    """Polygon USDT (6 decimals) transfer lookup via public EVM RPCs."""
    receipt = await _evm_rpc(POLYGON_RPC_ENDPOINTS,
                             "eth_getTransactionReceipt",
                             [(txid or "").lower()])
    if not isinstance(receipt, dict) or not receipt:
        return None, "pending"
    if str(receipt.get("status", "")).lower() not in ("0x1", "0x01"):
        return None, "failed"
    conf = await _evm_confirmations(POLYGON_RPC_ENDPOINTS,
                                    receipt.get("blockNumber"))
    if conf is not None and conf < EVM_MIN_CONFIRMATIONS:
        return None, "pending"          # found but too fresh - wait
    contract = POLYGON_USDT_CONTRACT.lower()
    saw_usdt = False
    for lg in receipt.get("logs") or []:
        if not isinstance(lg, dict):
            continue
        if (lg.get("address") or "").lower() != contract:
            continue
        topics = lg.get("topics") or []
        if len(topics) < 3 \
                or str(topics[0]).lower() != USDT_TRANSFER_TOPIC:
            continue
        saw_usdt = True
        if _addr_from_topic(topics[2]).lower() != wallet.lower():
            continue
        return _log_to_transfer(lg, 0, decimals=6), "found"
    if saw_usdt:
        return None, "wrong_recipient"
    return None, "wrong_token"


def txid_ok_for(network: str, txid: str) -> bool:
    t = (txid or "").strip()
    if network == "binance":
        # v9.32: Binance Pay Order ID - alnum/underscore, e.g.
        # M_P_123456789012345678 or the bare digit tail
        return bool(BINANCE_ORDER_ID_RE.fullmatch(t))
    if network == "trc20":
        return bool(re.fullmatch(r"[0-9a-fA-F]{64}", t))
    return bool(TXID_RE.match(t))


async def verify_tx_on_network(network, txid, wallet):
    """Unified on-chain check. Returns (transfer, state) with state in
    found / pending / failed / wrong_token / wrong_recipient."""
    if network == "trc20":
        return await trc20_tx_transfer(txid, wallet)
    if network == "polygon":
        return await polygon_tx_usdt_transfer(txid, wallet)
    return await bsc_tx_usdt_transfer(txid, wallet)


def deposit_decline_text(tstate: str, network: str,
                         lang: str = "en") -> str:
    meta = DEPOSIT_NETWORKS.get(network) or DEPOSIT_NETWORKS["bep20"]
    if tstate == "pending":
        return t(lang, "decline_pending", net=meta['short'])
    if tstate == "failed":
        return t(lang, "decline_failed")
    if tstate == "wrong_token":
        return t(lang, "decline_token", net=meta['short'])
    return t(lang, "decline_recipient", net=meta['short'])


async def handle_txid_submission(update, context, uid, d, text):
    """User pasted the TXID after tapping I PAID -> loading -> verify."""
    lang = await get_user_lang(uid)
    dep_id = (d or {}).get("deposit_id")
    network = (d or {}).get("network") or "bep20"
    meta = DEPOSIT_NETWORKS.get(network) or DEPOSIT_NETWORKS["bep20"]
    txid = text.strip()
    if network == "binance":
        # v9.32 ANTI-TRICK: strip ALL whitespace (spaces/newlines anywhere)
        # plus wrapping junk so "M_P_ 123", " M_P_123 ", copied-with-quotes
        # or multi-line pastes still resolve to the same clean Order ID.
        txid = re.sub(r"\s+", "", text or "")
        txid = txid.strip("\"'`<>|,;:.")
    if not txid_ok_for(network, txid):
        if network == "binance":
            await trace_deposit(dep_id, uid, network, txid,
                                "txid_bad_format")
            await _send_tracked(update, context,
                                t(lang, "bin_bad_fmt"),
                                txid_input_kb(dep_id, lang))
            return
        fmt = ("64 hex characters (no 0x)" if network == "trc20"
               else "0x + 64 hex characters")
        await trace_deposit(dep_id, uid, network, txid,
                            "txid_bad_format")
        await _send_tracked(
            update, context,
            t(lang, "txid_bad_fmt", net=meta['short'], fmt=fmt),
            txid_input_kb(dep_id, lang))
        return
    dep = await get_deposit(dep_id)
    if not dep or dep.get("status") != "pending":
        await trace_deposit(dep_id, uid, network, txid,
                            "closed_order")
        await clear_user_state(uid)
        await _send_tracked(update, context,
                            t(lang, "dep_closed"),
                            main_menu_kb(is_admin(uid), lang))
        return
    try:
        tried = int(dep.get("attempts") or 0)
    except (TypeError, ValueError):
        tried = 0
    if tried >= MAX_TXID_ATTEMPTS:
        await trace_deposit(dep_id, uid, network, txid, "locked",
                            "attempts=%s" % tried)
        await clear_user_state(uid)
        await _send_tracked(update, context,
                            t(lang, "dep_locked", order=dep_id),
                            main_menu_kb(is_admin(uid), lang))
        return
    # LOADING step (required UX), then the real answer
    await _send_tracked(update, context,
                        t(lang, "dep_checking", net=meta['short']), None)
    txl = txid.lower()
    # v9.12: verify against the wallet THIS order was shown (bound
    # at creation) - wallet rotations never break pending orders.
    wallet = ((dep.get("usdt_address") or "").strip()
              or (await network_wallet(network)))
    if network == "binance":     # v9.32: official Binance Pay API check
        transfer, tstate = await binance_pay_order_transfer(txl, dep)
    else:
        transfer, tstate = await verify_tx_on_network(network, txl,
                                                      wallet)
    if tstate == "api_error":
        # v9.32: the Binance API itself is down/rejecting - NOT the
        # user's fault: no attempt bump, nothing stored, the order
        # stays pending and can be retried in a minute (or the owner
        # can approve manually from Pending Deposits).
        await trace_deposit(dep_id, uid, network, txl, "api_busy")
        await _send_tracked(update, context,
                            t(lang, "dep_api_busy"),
                            txid_input_kb(dep_id, lang))
        return
    if tstate != "found":
        # v9.28 WIRE-UP: update_deposit_tx existed but was NEVER called,
        # so a pending order could never carry a tx hash and the admin
        # Pending Deposits list (admdep:ok / admdep:no buttons) stayed
        # EMPTY forever - a dead feature. A declined submission now
        # stores its hash: the order appears in Pending Deposits and the
        # owner can manually verify + approve it (edge cases the RPC
        # nodes reject: fresh tx, node lag, wrong list state...).
        await update_deposit_tx(dep_id, txl, None)
        await trace_deposit(dep_id, uid, network, txl,
                            "declined_%s" % tstate)
        await _bump_txid_attempt(dep_id)
        if network == "binance":
            _btxt = {"pending": t(lang, "bin_decline_pending"),
                     "failed": t(lang, "bin_decline_stale"),
                     "wrong_token": t(lang, "decline_token",
                                      net=meta['short']),
                     "wrong_recipient": t(lang, "bin_decline_out"),
                     }.get(tstate) or \
                deposit_decline_text(tstate, network, lang)
        else:
            _btxt = deposit_decline_text(tstate, network, lang)
        await _send_tracked(update, context, _btxt,
                            txid_input_kb(dep_id, lang))
        return
    if network == "binance" and isinstance(transfer, dict) \
            and transfer.get("hash"):
        # v9.32 LOOT GUARD: one Pay transfer carries TWO id forms
        # (orderId digits + transactionId). Replay-protect and store the
        # CANONICAL id returned by the verified transfer - submitting
        # the other form of the same payment later can never win.
        txl = str(transfer["hash"]).lower()
    if await hash_already_credited(txl):
        await trace_deposit(dep_id, uid, network, txl,
                            "txid_replay")
        await _send_tracked(
            update, context,
            t(lang, "txid_replay"),
            txid_input_kb(dep_id, lang))
        await _bump_txid_attempt(dep_id)
        return
    val = token_value_usdt(transfer)
    try:
        want = float(dep.get("amount") or 0.0)
    except (TypeError, ValueError):
        want = 0.0
    if network == "binance":
        # v9.35: the order charges its EXACT picked amount
        try:
            want = float(dep.get("pay_amount") or want)
        except (TypeError, ValueError):
            pass
    if want <= 0 or val < want - AMOUNT_MATCH_TOLERANCE:
        # v9.28: same wire-up for amount mismatches - the owner sees the
        # order (with its tx) in Pending Deposits and can approve it
        # after a manual chain check.
        await update_deposit_tx(dep_id, txl, None)
        await trace_deposit(dep_id, uid, network, txl,
                            "amount_mismatch",
                            "got=$%.2f want=$%.2f" % (val, want))
        await _send_tracked(
            update, context,
            t(lang, "bin_amt_mismatch" if network == "binance"
              else "amt_mismatch",
              got=f"{val:.2f}", want=f"{want:.2f}"),
            txid_input_kb(dep_id, lang))
        await _bump_txid_attempt(dep_id)
        return
    credited = await credit_auto_deposit(
        dep_id, txl, val,
        "binance" if network == "binance" else "txid")
    await clear_user_state(uid)
    if not credited:
        await trace_deposit(dep_id, uid, network, txl,
                            "already_credited")
        await _send_tracked(update, context,
                            t(lang, "dep_already"),
                            main_menu_kb(is_admin(uid), lang))
        return
    await trace_deposit(dep_id, uid, network, txl, "credited",
                        "$%.2f wallet=%s" % (val, wallet))
    user = await get_user(uid)
    bal = (user or {}).get("balance", 0.0) or 0.0
    await _send_tracked(
        update, context,
        f"{t(lang, 'dep_ok_title')}\n"
        f"{DIV}\n"
        f"{t(lang, 'dep_ok_credited', amount=f'{val:.2f}')}\n"
        f"{t(lang, 'dep_ok_balance', bal=f'{bal:.2f}')}\n"
        f"{DIV}\n"
        f"{t(lang, 'dep_ok_cta')}",
        main_menu_kb(is_admin(uid), lang))
    await notify_deposit_verified(context.bot, credited, val, "txid")


# --------------------------------------------------------------------------- #
#  DEPOSIT FLOW
# --------------------------------------------------------------------------- #
async def deposit_create(update, context, uid, amount, network):
    lang = await get_user_lang(uid)
    min_dep = float(await get_setting("min_deposit"))
    if not math.isfinite(amount) or amount < min_dep:   # v9.20: nan-proof
        await set_user_state(uid, "dep_amount")
        await _send_tracked(
            update, context,
            t(lang, "dep_min_warn", min=f"{min_dep:.2f}"),
            deposit_amount_kb(lang))
        return
    if network not in DEPOSIT_NETWORKS:
        network = "bep20"
    pay_amt = None
    if network == "binance":
        # v9.35: EXACT amount - the card shows exactly what the user
        # picked; shared amounts go through the Order-ID path
        pay_amt = await _unique_binance_amount(amount)
    deposit_id, expires = await create_deposit(uid, amount, network,
                                               pay_amt)
    wallet = await network_wallet(network)
    await set_user_state(uid, "awaiting_txid",
                         {"deposit_id": deposit_id, "amount": amount,
                          "network": network, "pay_amount": pay_amt})
    await _send_tracked(update, context,
                        deposit_card_text(network, pay_amt or amount,
                                          wallet,
                                          deposit_id, expires, lang),
                        deposit_wait_kb(deposit_id, lang))


async def prompt_custom_amount(update, context, uid, error=False):
    lang = await get_user_lang(uid)
    await set_user_state(uid, "dep_custom")
    min_dep = float(await get_setting("min_deposit"))
    key = "custom_err" if error else "custom_title"
    head = t(lang, key, min=f"{min_dep:.2f}")
    await _send_tracked(update, context, head, deposit_custom_kb(lang))


def stock_format_hint() -> str:
    return (
        f"{DIV}\n"
        "\U0001F4F1 <b>Send numbers \u2014 one per line:</b>\n"
        "<code>+14133525884 | http://otp-api-link/xyz</code>\n\n"
        "\U0001F4C4 <b>Or upload a .txt file</b> with the same format.\n"
        "\U0001F527 <i>Small format mistakes are fixed automatically "
        "(missing +, extra spaces, commas, missing http://).</i>\n"
        f"{DIV}\n"
        "\u274C <b>Cancel</b> to stop."
    )


BROADCAST_RATE = 25   # msgs/sec steady pace (Telegram bot cap ~30/s)


async def _broadcast_copy_one(bot, target, src_chat, src_msg):
    """v9.23: one broadcast send as an EXACT COPY (copy_message).
    Text, photo, video, file (APK), audio, GIF, buttons and PREMIUM
    custom emojis all arrive same-to-same - the old send_message re-type
    flattened premium emojis to normal ones. Respects 429. Never raises."""
    for _try in (1, 2):
        try:
            await bot.copy_message(chat_id=target,
                                   from_chat_id=src_chat,
                                   message_id=src_msg)
            return True
        except RetryAfter as e:
            await asyncio.sleep(min(float(getattr(e, "retry_after", 1) or 1)
                                    + 0.5, 60))
        except Exception:
            return False
    return False


async def run_broadcast_copy(update, context, uid):
    """v9.23 SAME-TO-SAME broadcast engine. The admin sends ANY message
    (text / photo / video / file / APK / audio / GIF) in Broadcast state;
    every non-banned user AND every managed channel/group receives an
    exact copy_message of it. 40k-safe: id-only query, ~25/s chunks,
    429 backoff, live progress, banned users never receive."""
    msg = update.message
    src_chat = update.effective_chat.id
    src_msg = getattr(msg, "message_id", None)
    if src_msg is None:
        return
    # v9.36 DIAGNOSTIC (premium emoji flattening): log once when the
    # source carries premium custom-emoji entities. copy_message forwards
    # them entity-faithful; if recipients STILL see normal emojis then
    # Telegram itself is stripping bot-sent custom emoji (bot eligibility:
    # Fragment username / owner Premium) - the v9.36 strip-detector log
    # line in _pem_send names it on the next menu send. Nothing to re-type:
    # a copy is the maximum-fidelity tool that exists.
    try:
        _n_ce = sum(1 for _e in (getattr(msg, "entities", None) or [])
                    if getattr(_e, "type", "") == "custom_emoji")
        _n_ce += sum(1 for _e in (getattr(msg, "caption_entities", None)
                                  or [])
                     if getattr(_e, "type", "") == "custom_emoji")
        if _n_ce:
            logger.info("broadcast: source carries %d premium custom-emoji "
                        "entities - copies go out entity-faithful via "
                        "copy_message", _n_ce)
    except Exception:
        pass
    targets = await get_broadcast_targets()   # banned users never receive broadcasts
    ch_ids = [c for c in (await managed_channel_ids())
              if c not in set(targets)]
    total_u, total_c = len(targets), len(ch_ids)
    chat_id = update.effective_chat.id
    head = (f"\U0001F4E3 <b>BROADCAST RUNNING</b>\n\n"
            f"{DIV}\n"
            f"\U0001F465 Users: <b>{total_u}</b> \u2022 "
            f"\U0001F4E1 Chats: <b>{total_c}</b>\n"
            f"\U0001F4CB Same-to-same copy (premium emoji included)\n"
            f"\u2705 Sent: 0   \u274C Failed: 0")
    prog = await msg.reply_text(head, parse_mode=ParseMode.HTML)
    prog_msg_id = getattr(prog, "message_id", None)
    sent = failed = 0
    done_ct = 0
    grand = total_u + total_c
    last_edit = time.monotonic()

    async def _pump(final=False):
        nonlocal last_edit
        if final or time.monotonic() - last_edit >= 10.0:
            last_edit = time.monotonic()
            pct = int(min(100, done_ct * 100 / max(grand, 1)))
            await _broadcast_progress_edit(
                context.bot, chat_id, prog_msg_id,
                f"\U0001F4E3 <b>BROADCAST RUNNING</b>\n\n"
                f"{DIV}\n"
                f"\U0001F465 Users: <b>{total_u}</b> \u2022 "
                f"\U0001F4E1 Chats: <b>{total_c}</b>\n"
                f"\u2705 Sent: {sent}   \u274C Failed: {failed}\n"
                f"{pct}% done")

    for tgt_list in (targets, ch_ids):
        for i in range(0, len(tgt_list), BROADCAST_RATE):
            chunk = tgt_list[i:i + BROADCAST_RATE]
            res = await asyncio.gather(
                *(_broadcast_copy_one(context.bot, u, src_chat, src_msg)
                  for u in chunk))
            sent += sum(1 for r in res if r)
            failed += sum(1 for r in res if not r)
            done_ct += len(chunk)
            await _pump()
            if i + BROADCAST_RATE < len(tgt_list):
                await asyncio.sleep(1.0)   # steady ~25 msgs/sec pace
    await clear_user_state(uid)
    done = (f"\u2705 <b>BROADCAST DONE</b>\n\n"
            f"{DIV}\n"
            f"\U0001F465 Users: {total_u} \u2022 "
            f"\U0001F4E1 Chats: {total_c}\n"
            f"\U0001F4EC <b>Sent:</b> {sent}\n"
            f"\u274C <b>Failed:</b> {failed}\n"
            f"{DIV}")
    if prog_msg_id:
        await _broadcast_progress_edit(context.bot, chat_id, prog_msg_id,
                                       done)
    else:
        await _send_tracked(update, context, done, admin_panel_kb())


async def _broadcast_progress_edit(bot, chat_id, message_id, text):
    try:
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                    text=text, parse_mode=ParseMode.HTML)
    except Exception:
        pass


async def process_bulk_stock(update, context, uid, sdata, text):
    """Parse a bulk stock dump (pasted text or .txt file) and add every
    valid number.  Format per line:  +14133525884 | http://otp-api-link"""
    d = sdata or {}
    ntype = d.get("ntype", "wa")
    country = d.get("country", "USA")
    db_type = "whatsapp" if ntype == "wa" else "telegram"
    label = "WhatsApp" if ntype == "wa" else "Telegram"

    entries, errors = parse_stock_lines(text)
    if not entries and not errors:
        await _send_tracked(
            update, context,
            "\u26A0\uFE0F <b>NO NUMBERS FOUND</b> \u2014 try again:\n\n"
            + stock_format_hint(),
            admin_input_kb(),
        )
        return  # stay in the add-stock state

    # v9.20: batch checks + ONE bulk insert. A 10k-line dump used to run
    # 3 queries + a commit PER LINE; now it is 2 queries + 1 commit total.
    avail = await phones_in_stock_set([p for p, _u in entries],
                                      only_available=True)
    any_set = await phones_in_stock_set([p for p, _u in entries])
    fresh_entries = []
    dup = 0
    seen = set()
    for phone, url in entries:
        if phone in avail or phone in seen:
            dup += 1
            continue
        seen.add(phone)
        fresh_entries.append((phone, url))
    added = len(fresh_entries)
    readded = sum(1 for p, _u in fresh_entries if p in any_set)
    no_link = sum(1 for _p, u in fresh_entries if not u)
    await add_stock_many(fresh_entries, ntype, country, uid)

    if added == 0:
        lines = ["\u274C <b>NOTHING ADDED</b>\n\n" + DIV]
        if dup:
            lines.append(f"\U0001F501 <b>{dup}</b> number(s) already in stock")
        if errors:
            lines.append(f"\u274C <b>{len(errors)}</b> bad line(s):")
            for ln, sample, why in errors[:5]:
                lines.append(f"   \u2022 <code>{html_escape(sample)}</code> \u2014 {why}")
        lines.append("\n" + stock_format_hint())
        await _send_tracked(update, context, "\n".join(lines), admin_input_kb())
        return  # stay in the add-stock state

    await clear_user_state(uid)
    lines = [
        f"\u2705 <b>STOCK ADDED \u2014 {label.upper()} "
        f"{flag_of(country)} {country}</b>\n",
        DIV,
        f"\U0001F4F1 <b>Numbers added:</b> {added}",
    ]
    if dup:
        lines.append(f"\U0001F501 <b>Duplicates skipped:</b> {dup}")
    if errors:
        lines.append(f"\u274C <b>Bad lines skipped:</b> {len(errors)}")
        for ln, sample, why in errors[:3]:
            lines.append(f"   \u2022 <code>{html_escape(sample)}</code> \u2014 {why}")
    if no_link:
        lines.append(
            f"\n\u26A0\uFE0F <b>{no_link}</b> number(s) have NO OTP link \u2014 "
            "they can be sold but OTP auto-check won't work for them."
        )
    if readded:
        lines.append(
            f"\n\u26A0\uFE0F <b>{readded}</b> number(s) were sold/refunded "
            "before \u2014 double-check they are not live duplicates, "
            "or you may sell the same number twice!"
        )
    lines.append(DIV)
    await _send_tracked(update, context, "\n".join(lines), admin_panel_kb())


# --------------------------------------------------------------------------- #
#  STATE TEXT HANDLER  (awaiting_tx + admin input states)
# --------------------------------------------------------------------------- #
async def handle_state_text(update, context, state, sdata, text):
    uid = update.effective_user.id
    d = sdata or {}

    # v9.21 defense-in-depth: admin input states re-verify the caller.
    # These states are only ever SET by admin-gated flows, but rates,
    # balances, the wallet and the ledger must never depend on that
    # promise alone - a leaked/forged state dies right here.
    if state and state.startswith("admin") and not is_admin(uid):
        await clear_user_state(uid)
        _lng0 = await get_user_lang(uid)
        await _send_tracked(update, context, menu_info_text(_lng0),
                            main_menu_kb(False, _lng0))
        return

    # v9.41 MANAGE ADMIN: submenu buttons + add/remove ID inputs
    if state == "admin_adm":
        if btn_eq(text, BTN_ADMA_ADD):
            return await prompt_admin_add(update, context)
        if btn_eq(text, BTN_ADMA_REM):
            return await prompt_admin_remove(update, context)
        if btn_eq(text, BTN_ADMA_LIST):
            return await show_admin_list(update, context)
        return await show_admin_manage(update, context)

    if state in ("admin_adm_add", "admin_adm_rm"):
        return await handle_admin_manage_input(update, context, uid, state,
                                               text)

    if state == "awaiting_txid":
        return await handle_txid_submission(update, context, uid, d, text)

    if state == "dep_custom":
        try:
            amount = float(text.strip().replace("$", ""))
        except ValueError:
            amount = None
        min_dep = float(await get_setting("min_deposit"))
        # v9.20: isfinite - "nan"/"inf" skip every < check (NaN-proof)
        if amount is None or not math.isfinite(amount) or amount < min_dep:
            return await prompt_custom_amount(update, context, uid, error=True)
        return await show_dep_networks(update, context, amount)

    if state == "user_bulkbuy":
        # v9.31 USER BULK BUY: the typed quantity -> checks -> confirm card
        return await handle_user_bulk_qty(update, context, uid, text, d)

    if state in ("admin_add_phone", "admin_add_url"):
        # BULK stock add: one "+1phone | otp-url" per line (or .txt content)
        await process_bulk_stock(update, context, uid, d, text)
        return

    if state == "admin_bulkmanage_min" and is_admin(uid):
        # v9.34 BULK MANAGE: the typed minimum quantity -> settings
        m = re.fullmatch(r"\d{1,5}", (text or "").strip())
        if not m or int(m.group(0)) < 2:
            await _send_tracked(
                update, context,
                "\u274C <b>Invalid quantity.</b> Type the MINIMUM "
                "numbers for the discount (2 or more, e.g. 30):",
                admin_input_kb())
            return
        val = int(m.group(0))
        if val > 100000:
            await _send_tracked(
                update, context,
                "\u26A0\uFE0F <b>Too big.</b> Type a minimum quantity "
                "up to 100,000:",
                admin_input_kb())
            return
        await set_setting("bulk_disc_min", str(val))
        await clear_user_state(uid)
        return await show_admin_bulkmanage(update, context)

    if state == "admin_bulkmanage_disc" and is_admin(uid):
        # v9.34 BULK MANAGE: the typed per-number discount -> settings
        s = (text or "").strip().lstrip("$").replace(",", ".")
        if not re.fullmatch(r"\d{1,2}(?:\.\d{1,4})?", s):
            await _send_tracked(
                update, context,
                "\u274C <b>Invalid amount.</b> Type the per-number "
                "discount in $ (e.g. 0.02, or 0 to switch OFF):",
                admin_input_kb())
            return
        val = round(float(s), 4)
        if val > 10:
            await _send_tracked(
                update, context,
                "\u26A0\uFE0F <b>Too big.</b> Max discount is $10 per "
                "number:",
                admin_input_kb())
            return
        await set_setting("bulk_disc_per", "%.4f" % val)
        await clear_user_state(uid)
        return await show_admin_bulkmanage(update, context)

    if state == "admin_set_rate":
        try:
            val = float(text)
            if not math.isfinite(val) or val <= 0:
                raise ValueError
        except ValueError:
            await _send_tracked(update, context,
                                "\u274C <b>Invalid number.</b> Send a price like 2.50:",
                                admin_input_kb())
            return
        ntype = d.get("ntype", "wa")
        key = "whatsapp_rate" if ntype == "wa" else "telegram_rate"
        old = float(await get_setting(key))
        await set_setting(key, f"{val:.2f}")
        async with adb() as db:
            await db.execute(
                "INSERT INTO rate_history(rate_type,old_rate,new_rate,changed_by) "
                "VALUES(?,?,?,?)",
                (key, old, val, uid),
            )
        await clear_user_state(uid)
        label = "WhatsApp" if ntype == "wa" else "Telegram"
        await _send_tracked(update, context,
                            f"\u2705 <b>{label.upper()} RATE UPDATED</b>\n\n"
                            f"{DIV}\n"
                            f"\U0001F4C9 <b>${old:.2f} \u2192 ${val:.2f}</b>\n"
                            f"{DIV}",
                            admin_panel_kb())
        return

    if state == "admin_ch_add":
        return await resolve_and_add_channel(update, context, uid, text, d)

    if state == "admin_ref_price":
        # v9.24: new per-buy referral commission (validated, 0 < x <= 1000)
        raw = text.strip().replace("$", "").replace(",", "")
        try:
            val = float(raw)
            if not math.isfinite(val) or val <= 0 or val > 1000:
                raise ValueError
        except ValueError:
            await _send_tracked(update, context,
                                "\u274C <b>Invalid amount.</b> Send a commission "
                                "like <code>0.005</code>:",
                                admin_input_kb())
            return
        old = await get_ref_rate()
        await set_setting("ref_rate", f"{val:.4f}")
        await clear_user_state(uid)
        await _send_tracked(
            update, context,
            f"\u2705 <b>REFFER PRICE UPDATED</b>\n\n"
            f"{DIV}\n"
            f"\U0001F4C8 <b>${_fmt_amt(old)} \u2192 ${_fmt_amt(val)}</b> "
            f"per buy\n"
            f"{DIV}\n"
            f"\u2139\uFE0F Every referred purchase now pays the referrer "
            f"<b>${_fmt_amt(val)}</b> (VIP rates stay separate).",
            admin_refer_kb(ref_is_on()))
        return

    if state == "admin_ref_vip_add_id":
        # v9.24: VIP referrer chat ID -> must be an existing user
        try:
            target = int(text.strip())
        except ValueError:
            await _send_tracked(update, context,
                                "\u274C <b>Invalid ID.</b> Send a numeric chat ID:",
                                admin_input_kb())
            return
        tu = await get_user(target)
        if tu is None:
            await _send_tracked(update, context,
                                "\u26A0\uFE0F <b>User not found.</b> The user must "
                                "/start the bot first. Send another ID:",
                                admin_input_kb())
            return
        return await prompt_admin_vip_rate(update, context, target)

    if state == "admin_ref_vip_add_rate":
        # v9.24: VIP special rate -> save + confirm + notify the VIP
        target = (d or {}).get("target")
        if not target:
            await clear_user_state(uid)
            return await show_admin_ref_vip(update, context)
        raw = text.strip().replace("$", "").replace(",", "")
        try:
            val = float(raw)
            if not math.isfinite(val) or val <= 0 or val > 1000:
                raise ValueError
        except ValueError:
            await _send_tracked(update, context,
                                "\u274C <b>Invalid rate.</b> Send a commission like "
                                "<code>0.010</code>:",
                                admin_input_kb())
            return
        await ref_vip_set(int(target), val)
        await clear_user_state(uid)
        try:
            _tl = await get_user_lang(int(target))
            await context.bot.send_message(
                chat_id=int(target),
                text=t(_tl, "ref_vip_line", rate=_fmt_amt(val)),
                parse_mode=ParseMode.HTML)
        except Exception:
            pass   # VIP blocked the bot - rate still saved
        await _send_tracked(
            update, context,
            f"\u2705 <b>VIP ADDED</b>\n\n"
            f"{DIV}\n"
            f"\U0001F194 <code>{int(target)}</code>\n"
            f"\U0001F4B5 VIP rate: <b>${_fmt_amt(val)}</b> per buy\n"
            f"{DIV}\n"
            f"\u2139\uFE0F Every buy from their referrals now pays "
            f"<b>${_fmt_amt(val)}</b> \u2014 the normal rate is ignored "
            f"for this user.",
            admin_ref_vip_kb())
        return

    if state == "admin_broadcast":
        # v9.23: SAME-TO-SAME broadcast - copy_message keeps text, media,
        # files, buttons and premium custom emojis pixel-identical.
        return await run_broadcast_copy(update, context, uid)

    if state == "admin_ban":
        try:
            target = int(text)
        except ValueError:
            await _send_tracked(update, context,
                                "\u274C <b>Invalid ID.</b> Send a numeric Telegram user ID:",
                                admin_input_kb())
            return
        # v9.25: NO owner-admin can ever be banned (owner OR second admin)
        if target in ADMIN_IDS:
            await _send_tracked(update, context,
                                "\u26A0\uFE0F <b>You can't ban an owner-"
                                "admin.</b> Send another ID:",
                                admin_input_kb())
            return
        action = d.get("action", "ban")
        banned = action == "ban"
        await set_ban(target, banned)
        await clear_user_state(uid)
        label = "BANNED" if banned else "UNBANNED"
        await _send_tracked(update, context,
                            f"\u2705 <b>USER {label}</b>\n\n"
                            f"{DIV}\n\U0001F194 <code>{target}</code>\n{DIV}",
                            admin_panel_kb())
        return

    if state == "admin_modify_user":
        try:
            target = int(text.strip())
        except ValueError:
            await _send_tracked(update, context,
                                "\u274c <b>Invalid ID.</b> Send a numeric chat ID:",
                                admin_input_kb())
            return
        return await admin_user_details(update, context, target)

    if state == "admin_modbal":
        target = d.get("target")
        raw = text.strip().replace("$", "").replace(",", "")
        try:
            if raw.startswith("+"):
                mode, val = "add", float(raw[1:])
            elif raw.startswith("-"):
                mode, val = "deduct", float(raw[1:])
            else:
                mode, val = "set", float(raw)
            if not math.isfinite(val):   # v9.20: nan/inf can never be a balance
                raise ValueError
        except ValueError:
            await _send_tracked(update, context,
                                "\u274c <b>Invalid amount.</b> e.g. 10.50 / +5 / -2:",
                                admin_input_kb())
            return
        u = await get_user(target)
        if not u:
            await clear_user_state(uid)
            await _send_tracked(update, context,
                                "\u26a0\ufe0f <b>User not found.</b>",
                                admin_panel_kb())
            return
        old = u.get("balance", 0.0) or 0.0
        if mode == "add":
            new = old + val
        elif mode == "deduct":
            new = old - val
        else:
            new = val
        clamp = ""
        if new < 0:
            new = 0.0
            clamp = "\n\u26a0\ufe0f <i>Balance can't be negative \u2014 set to $0.00</i>"
        await set_balance(target, new)
        label = {"add": "ADDED", "deduct": "DEDUCTED", "set": "SET"}[mode]
        note = (f"\u2705 <b>BALANCE {label}</b>\n"
                f"\U0001F4B0 <code>${old:.2f} \u2192 ${new:.2f}</code>{clamp}")
        await clear_user_state(uid)
        return await admin_user_details(update, context, target, note=note)

    if state == "admin_set_wallet":
        if len(text) < 10:
            await _send_tracked(update, context,
                                "\u26A0\uFE0F <b>Wallet address looks too short.</b> "
                                "Send the full address:",
                                admin_input_kb())
            return
        old_addr = await get_setting("usdt_wallet_address")
        addr = text.strip()
        await set_setting("usdt_wallet_address", addr)
        await trace_deposit("-", uid, "bep20", "-",
                            "wallet_changed",
                            "old=%s new=%s" % (old_addr, addr))
        if addr.lower().startswith("0x"):
            await set_setting("usdt_network", "BEP20")
            net_note = ("\U0001F916 <b>AUTO-VERIFY ON</b> \u2014 BEP20 "
                        "deposits confirm themselves on-chain.")
        else:
            net_note = ("\u26A0\uFE0F Not a 0x address \u2014 deposits "
                        "here need manual admin approval "
                        "(auto-verify off).")
        await clear_user_state(uid)
        await _send_tracked(update, context,
                            f"\u2705 <b>WALLET UPDATED</b>\n\n"
                            f"{DIV}\n<code>{html_escape(addr)}</code>\n{DIV}\n"
                            f"{net_note}",
                            admin_panel_kb())
        return

    # Unknown state — clean up and go home
    _lng = await get_user_lang(uid)
    await clear_user_state(uid)
    await _send_tracked(update, context, menu_info_text(_lng),
                        main_menu_kb(is_admin(uid), _lng))


# --------------------------------------------------------------------------- #
#  PHOTO / DOCUMENT  (deposit screenshots)
# --------------------------------------------------------------------------- #
_MEDIA_FILTER = (filters.VIDEO | filters.ANIMATION | filters.AUDIO |
                 filters.VOICE | filters.VIDEO_NOTE |
                 filters.Sticker.ALL)


async def on_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """v9.23: video / audio / voice / GIF / sticker. In Broadcast state
    the admin's media is broadcast same-to-same; everywhere else it is
    silently ignored (group silence included)."""
    if not _is_private(update):
        return          # v9.23 group silence
    if update.message is None:
        return
    uid = update.effective_user.id
    state, _sd = await get_user_state(uid)
    if state == "admin_broadcast" and is_admin(uid):
        return await run_broadcast_copy(update, context, uid)


async def on_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_private(update):
        return          # v9.23 group silence
    uid = update.effective_user.id
    if update.message is None or not update.message.photo:
        return          # stale/queued update guard
    state, sdata = await get_user_state(uid)
    if state == "admin_broadcast" and is_admin(uid):
        return await run_broadcast_copy(update, context, uid)
    if state != "awaiting_txid":
        return
    _lng = await get_user_lang(uid)
    await update.message.reply_text(
        t(_lng, "scr_needed"),
        parse_mode=ParseMode.HTML,
    )


async def on_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_private(update):
        return          # v9.23 group silence
    uid = update.effective_user.id
    if update.message is None or not update.message.document:
        return          # stale/queued update guard
    state, sdata = await get_user_state(uid)
    if state == "admin_broadcast" and is_admin(uid):
        return await run_broadcast_copy(update, context, uid)

    if state == "awaiting_txid":
        _lng = await get_user_lang(uid)
        await update.message.reply_text(
            t(_lng, "scr_needed"),
            parse_mode=ParseMode.HTML,
        )
        return

    # Admin: refund hub uploads (Check Number / Refund Send, v9.27)
    if state in ("admin_check_number", "admin_refund_send",
                 "admin_check_refund") and is_admin(uid):
        doc = update.message.document
        name = (doc.file_name or "").lower()
        mime = (doc.mime_type or "")
        ok_type = (name.endswith((".txt", ".text", ".csv"))
                   or mime.startswith("text/"))
        if not ok_type:
            await update.message.reply_text(
                "\u26A0\uFE0F <b>Please send a <code>.txt</code></b> file.",
                parse_mode=ParseMode.HTML,
            )
            return
        if (doc.file_size or 0) > 10_000_000:
            await update.message.reply_text(
                "\u26A0\uFE0F <b>File too big (max 10 MB).</b>",
                parse_mode=ParseMode.HTML,
            )
            return
        tg_file = await context.bot.get_file(doc.file_id)
        raw = await tg_file.download_as_bytearray()
        text = bytes(raw).decode("utf-8", errors="replace")
        await update.message.reply_text(
            "\u23F3 <b>Processing...</b>", parse_mode=ParseMode.HTML
        )
        if state == "admin_check_number":
            await run_check_number(update, context, uid, text)
        elif state == "admin_refund_send":
            await run_refund_send(update, context, uid, text)
        else:
            await run_check_and_refund(update, context, uid, text)
        return

    # v9.34: a file means nothing in the BULK MANAGE input states
    if state in ("admin_bulkmanage_min", "admin_bulkmanage_disc") \
            and is_admin(uid):
        await update.message.reply_text(
            "\u26A0\uFE0F <b>That is a file - here I need a typed "
            "value.</b>\nUse \u274C Cancel and start again.",
            parse_mode=ParseMode.HTML,
        )
        return

    # v9.31: same guard for the USER Bulk Buy quantity state
    if state == "user_bulkbuy":
        await update.message.reply_text(
            t(await get_user_lang(uid), "ub_hint_file"),
            parse_mode=ParseMode.HTML,
        )
        return

    # Admin: bulk stock upload via .txt file
    if state in ("admin_add_phone", "admin_add_url") and is_admin(uid):
        doc = update.message.document
        name = (doc.file_name or "").lower()
        mime = (doc.mime_type or "")
        ok_type = (name.endswith((".txt", ".text", ".csv"))
                   or mime.startswith("text/"))
        if not ok_type:
            await update.message.reply_text(
                "\u26A0\uFE0F <b>Please send a <code>.txt</code> file</b> "
                "with the numbers.",
                parse_mode=ParseMode.HTML,
            )
            return
        if (doc.file_size or 0) > 2_000_000:
            await update.message.reply_text(
                "\u26A0\uFE0F <b>File too big (max 2 MB).</b>\n"
                "Split it or paste the lines directly.",
                parse_mode=ParseMode.HTML,
            )
            return
        tg_file = await context.bot.get_file(doc.file_id)
        raw = await tg_file.download_as_bytearray()
        text = bytes(raw).decode("utf-8", errors="replace")
        await update.message.reply_text(
            "\u23F3 <b>Processing file...</b>", parse_mode=ParseMode.HTML
        )
        await process_bulk_stock(update, context, uid, sdata, text)
        return


# --------------------------------------------------------------------------- #
#  ADMIN INFO SCREENS
# --------------------------------------------------------------------------- #
async def admin_stock_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    counts, total = await get_stock_counts()
    lines = [
        f"\U0001F4CA <b>STOCK STATS</b>\n",
        f"{DIV}",
        f"\U0001F4E6 <b>Total available:</b> {total}",
        f"{DIV}",
    ]
    for nt, label, icon in (("whatsapp", "WhatsApp", "\U0001F7E2"),
                            ("telegram", "Telegram", "\U0001F535")):
        c = counts.get(nt, {})
        if c:
            lines.append(f"\n{icon} <b>{label}:</b>")
            for ctry, n in c.items():
                lines.append(f"  {flag_of(ctry)} {ctry} \u2014 {n}")
        else:
            lines.append(f"\n{icon} <b>{label}:</b> 0")
    lines.append(DIV)
    await _send_tracked(update, context, "\n".join(lines), admin_panel_kb())


async def admin_pending_deposits(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    deps = await get_pending_deposits()
    if not deps:
        await _send_tracked(update, context,
                            f"\u2705 <b>NO PENDING DEPOSITS</b>\n\n{DIV}\nAll caught up! \U0001F389",
                            admin_panel_kb())
        return
    await _send_tracked(update, context,
                        f"\U0001F4B0 <b>PENDING DEPOSITS</b>\n\n"
                        f"{DIV}\n\U0001F4E8 Sending {min(len(deps), 15)} request(s) below...",
                        admin_panel_kb())
    for d in deps[:15]:
        u = await get_user(d["user_id"])
        uname = f"@{u['username']}" if u and u.get("username") else "\u2014"
        txt = (
            f"\U0001F4B0 <b>PENDING DEPOSIT</b>\n\n"
            f"{DIV}\n"
            f"\U0001F464 <b>User:</b> {html_escape((u or {}).get('first_name') or '?')} {uname}\n"
            f"\U0001F194 <b>ID:</b> <code>{d['user_id']}</code>\n"
            f"\U0001F4B5 <b>Amount:</b> ${d['amount']:.2f}\n"
            f"\U0001F9FE <b>Order:</b> <code>{d['deposit_id']}</code>\n"
            f"\U0001F517 <b>TX:</b> <code>{html_escape(str(d['tx_hash'])[:80])}</code>\n"
            f"{DIV}"
        )
        try:
            if d.get("screenshot_file_id"):
                await update.message.reply_photo(
                    photo=d["screenshot_file_id"], caption=txt,
                    parse_mode=ParseMode.HTML,
                    reply_markup=admin_deposit_approve_kb(d["deposit_id"]),
                )
            else:
                await update.message.reply_text(
                    txt, parse_mode=ParseMode.HTML,
                    reply_markup=admin_deposit_approve_kb(d["deposit_id"]),
                )
        except Exception as e:
            logger.warning("send pending dep failed: %s", e)


async def admin_statistics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    s = await get_statistics()
    txt = (
        f"\U0001F4C8 <b>STATISTICS</b>\n\n"
        f"{DIV}\n"
        f"\U0001F465 <b>Users:</b> {s['users']}\n"
        f"\U0001F4E6 <b>Available stock:</b> {s['available']}\n"
        f"\U0001F6D2 <b>Sold:</b> {s['sold']}\n"
        f"\u23F3 <b>Pending deposits:</b> {s['pending_deposits']}\n"
        f"{DIV}\n"
        f"\U0001F3E6 <b>Total deposited:</b> ${s['total_deposit']:.2f}\n"
        f"\U0001F4B8 <b>Total spent:</b> ${s['total_spent']:.2f}\n"
        f"{DIV}"
    )
    await _send_tracked(update, context, txt, admin_panel_kb())


# --------------------------------------------------------------------------- #
#  ADMIN DEPOSIT APPROVE/REJECT  (inline in group / private)
# --------------------------------------------------------------------------- #
async def admin_deposit_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    admin_id = q.from_user.id
    if not is_admin(admin_id):
        # v9.20: admin gate BEFORE answering (was a double-answer crash)
        await _safe_answer(q, "Admins only", show_alert=True)
        return
    await _safe_answer(q)
    parts = q.data.split(":")
    action = parts[1] if len(parts) >= 2 else ""
    dep_id = parts[2] if len(parts) >= 3 else ""
    if not action or not dep_id:
        return

    if action == "ok":
        dep = await confirm_deposit(dep_id, admin_id)
        if dep:
            try:
                _ulang = await get_user_lang(dep["user_id"])
                await context.bot.send_message(
                    chat_id=dep["user_id"],
                    text=t(_ulang, "dm_dep_confirmed",
                           div=DIV, amount=f"{dep['amount']:.2f}",
                           order=dep_id),
                    parse_mode=ParseMode.HTML,
                )
            except Exception:
                pass
            approved = (
                f"\u2705 <b>APPROVED</b>\n\n"
                f"\U0001F194 User: <code>{dep['user_id']}</code>\n"
                f"\U0001F4B5 Amount: ${dep['amount']:.2f}\n"
                f"\U0001F9FE Order: <code>{dep_id}</code>"
            )
            try:
                if q.message.photo:
                    await q.edit_message_caption(caption=approved,
                                                 parse_mode=ParseMode.HTML)
                else:
                    await q.edit_message_text(approved,
                                              parse_mode=ParseMode.HTML)
            except Exception:
                pass   # v9.20: stale/undeletable message - approval saved
        else:
            await _safe_answer(q, "Already processed or not found",
                               show_alert=True)
    elif action == "no":
        if not await reject_deposit(dep_id, admin_id):
            await _safe_answer(q, "Already processed or not found",
                               show_alert=True)
            return
        dep = await get_deposit(dep_id)
        uid = dep["user_id"] if dep else None
        if uid:
            try:
                _ulang = await get_user_lang(uid)
                await context.bot.send_message(
                    chat_id=uid,
                    text=t(_ulang, "dm_dep_rejected",
                           div=DIV, order=dep_id),
                    parse_mode=ParseMode.HTML,
                )
            except Exception:
                pass
        rejected = f"\u274C <b>REJECTED</b> \u2014 <code>{dep_id}</code>"
        try:
            if q.message.photo:
                await q.edit_message_caption(caption=rejected,
                                             parse_mode=ParseMode.HTML)
            else:
                await q.edit_message_text(rejected, parse_mode=ParseMode.HTML)
        except Exception:
            pass   # v9.20: stale/undeletable message - rejection saved


# --------------------------------------------------------------------------- #
#  ERROR HANDLER
# --------------------------------------------------------------------------- #
async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Unhandled exception: %s", context.error, exc_info=context.error)
    # Never fail silently - tell the user something went wrong.
    # v9.36: the card itself must NEVER fail (the old premium-tagged HTML
    # card could be rejected for the very same reason as the original
    # send -> user saw NOTHING). HTML first, then a stripped, plain-text
    # retry that Telegram's parser cannot reject.
    try:
        chat_id = None
        eff = getattr(update, "effective_chat", None)
        if eff is not None:
            chat_id = getattr(eff, "id", None)
        if chat_id:
            try:
                _uu = getattr(update, "effective_user", None)
                _lng = (await get_user_lang(_uu.id)) if _uu else "en"
            except Exception:
                _lng = "en"
            _card = t(_lng, "err_generic")
            try:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=_card,
                    parse_mode=ParseMode.HTML,
                )
            except Exception:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=pem_strip(_card),
                    parse_mode=None,
                )
    except Exception:
        pass


# --------------------------------------------------------------------------- #
#  v9.36 FAILSAFE - a user-facing handler can NEVER leave a user hanging
#  Owner bug: ~40% of users pressed /start and got NOTHING. Whatever the
#  root cause (a Telegram rejection nobody matched, a dead emoji ID, a
#  DB hiccup), the old chain was: handler raises -> on_error card ALSO
#  fails -> total silence for that user. Now every user-facing entry
#  point is wrapped: if the real screen dies for ANY reason, the user
#  still gets a plain-text menu (no HTML, no premium tags, no button
#  icons - a message Telegram's parser cannot reject). The bot can
#  never again go silent on a user.
# --------------------------------------------------------------------------- #
def _failsafe_menu_text(lang: str = DEFAULT_LANG) -> str:
    """Plain menu text built WITHOUT any risky markup."""
    try:
        return pem_strip("%s\n%s\n%s" % (t(lang, "menu_title"), DIV,
                                         t(lang, "menu_where")))
    except Exception:
        return "OTPHUB - main menu"


async def _failsafe_reply(update, context):
    """Last-resort screen: plain text + icon-free reply keyboard."""
    lang = DEFAULT_LANG
    try:
        _uu = getattr(update, "effective_user", None)
        if _uu:
            lang = lang_of(await get_user(_uu.id))
    except Exception:
        lang = DEFAULT_LANG
    try:
        kb = strip_button_icons(main_menu_kb(False, lang))
    except Exception:
        kb = None
    chat_id = getattr(getattr(update, "effective_chat", None), "id", None)
    if chat_id is None:
        return
    await context.bot.send_message(
        chat_id=chat_id,
        text=_failsafe_menu_text(lang),
        parse_mode=None,            # plain text - can never fail parsing
        reply_markup=kb,
        disable_web_page_preview=True,
    )


def _failsafe(fn):
    """Wrap a user-facing handler: original first; on ANY exception log
    it and push the plain failsafe screen. Never re-raises."""
    @functools.wraps(fn)
    async def _wrap(update, context, *a, **kw):
        try:
            return await fn(update, context, *a, **kw)
        except Exception:
            logger.error("handler %s failed - failsafe screen sent",
                         fn.__name__, exc_info=True)
            try:
                await _failsafe_reply(update, context)
            except Exception:
                logger.error("failsafe reply failed too (user offline?)",
                             exc_info=True)
    return _wrap


# --------------------------------------------------------------------------- #
#  MAIN
# --------------------------------------------------------------------------- #
async def post_shutdown(app: Application):
    """v9.14: release the shared HTTP session + DB connection."""
    await close_http_session()
    if _DB_CONN is not None:
        try:
            await _DB_CONN.close()
        except Exception:
            pass


async def post_init(app: Application):
    await init_db()
    global _BOT_USERNAME, _REF_ON
    # v9.28 OTP SAFETY NET: re-arm the pollers a restart killed, then
    # arm the permanent sweeper worker (deliver-without-limit net).
    await recover_otp_pollers(app)
    if (not app.bot_data.get("otp_sweeper_task")
            or app.bot_data["otp_sweeper_task"].done()):
        app.bot_data["otp_sweeper_task"] = app.create_task(
            otp_sweeper_task(app))
    # v9.32 BINANCE PAY: arm the 45s auto-verify sweep. Always armed -
    # every cycle no-ops instantly when no Binance orders are pending,
    # and an API outage just skips (manual Order-ID path still works).
    if (not app.bot_data.get("binance_sweeper_task")
            or app.bot_data["binance_sweeper_task"].done()):
        app.bot_data["binance_sweeper_task"] = app.create_task(
            binance_pay_sweeper(app))
    # v9.36 EMOJI SELF-HEAL: periodic READ-ONLY re-probe of every
    # premium ID (no messages ever) - dead IDs get pruned/revived while
    # the bot runs, so the premium layer recovers WITHOUT a restart.
    if (not app.bot_data.get("pem_heal_task")
            or app.bot_data["pem_heal_task"].done()):
        app.bot_data["pem_heal_task"] = app.create_task(_pem_heal_loop(app))
    # v9.36 FORCE-JOIN SANITY: read-only probe - a managed chat the bot
    # can no longer see must never trap users behind the join gate.
    await probe_managed_chats(app.bot)
    try:
        me = await app.bot.get_me()
        _BOT_USERNAME = me.username or ""
    except Exception:
        pass
    _REF_ON = (await get_setting("ref_enabled")) == "1"
    try:
        await app.bot.set_my_commands([
            ("start", "Open main menu"),
            ("menu", "Show menu"),
            ("language", "Change language"),
            ("admin", "Admin panel"),
            ("help", "Help"),
        ])
    except Exception as e:
        logger.warning("set_my_commands failed: %s", e)
    logger.info("Bot started as @%s", _BOT_USERNAME
                or (await app.bot.get_me()).username)
    logger.info("Deposit verification: TXID-ONLY on-chain + Binance Pay "
                "Order-ID auto-verify (v9.40, %ss sweep)",
                BINANCE_SWEEP_SECONDS)
    _w = {k: await get_setting(k) for k in
          ("usdt_wallet_address", "trc20_wallet_address",
           "polygon_wallet_address")}
    logger.info("Wallets (v9.23): BEP20=%s TRC20=%s Polygon=%s",
                _mask_addr(_w["usdt_wallet_address"]),
                _mask_addr(_w["trc20_wallet_address"]),
                _mask_addr(_w["polygon_wallet_address"]))
    _pem_ok = await _pemoji_selftest(app.bot)
    logger.info("Premium emojis (v9.40): %s (%d ids, user-side only)",
                "ACTIVE" if _pem_ok else "OFF", len(_PEMO_ORDER))
    _bicon_ok = await _bicons_selftest(app.bot)
    logger.info("Button icons (v9.40): %s (%d icon ids, all keyboards, "
                "PTB %s) - icon needs a recent Telegram app + PTB>=22.8",
                "ACTIVE" if _bicon_ok else "OFF", len(_BICON),
                _ptb_version())
    _dmin, _damt = await bulk_disc_params()
    logger.info("User Bulk Buy (v9.40): %s (%s+ numbers = $%.2f off per "
                "number, owner-set via Bulk Manage, cap %s)",
                "ON", _dmin, _damt, USER_BULK_MAX)
    logger.info("Referral system (v9.40): %s (commission $%s, PENDING at "
                "buy, pays the moment the buyer's OTP arrives)",
                "ON" if _REF_ON else "OFF", _fmt_amt(await get_ref_rate()))
    logger.info("Owner-admins (v9.41): %d MAIN %s (extra: Manage Admin "
                "panel; deposit notice MAIN-only)", len(ADMIN_IDS),
                sorted(ADMIN_IDS))
    logger.info("OTP success channel (v9.41): %s (every delivered OTP "
                "is posted - name, masked number, OTP, service, price)",
                OTP_SUCCESS_CHANNEL)
    _bp_ok, _bp_err = await binance_pay_probe()
    logger.info("Binance Pay deposits (v9.40): %s (Pay ID %s)%s",
                "ACTIVE" if _bp_ok else "OFF",
                (await get_setting("binance_pay_id"))
                or BINANCE_PAY_ID_DEFAULT,
                "" if _bp_ok else " - %s" % _bp_err)


def build_app() -> Application:
    # v9.14: handlers of different users run in parallel (no queueing
    # behind one slow screen / RPC call); shared DB+HTTP are safe for it.
    app = (Application.builder()
           .token(BOT_TOKEN)
           .concurrent_updates(True)
           .post_init(post_init)
           .post_shutdown(post_shutdown)
           .build())

    # Debug: log every incoming update (enable with LOG_UPDATES=1)
    if os.getenv("LOG_UPDATES"):
        async def _log_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
            try:
                if update.message:
                    u = update.message.from_user
                    logger.info("MSG  user=%s (%s) chat=%s text=%r",
                                u.id, u.username, update.message.chat_id,
                                (update.message.text or "")[:60])
                elif update.callback_query:
                    u = update.callback_query.from_user
                    logger.info("CALL user=%s (%s) data=%r",
                                u.id, u.username, update.callback_query.data)
            except Exception:
                pass
        app.add_handler(TypeHandler(Update, _log_update), group=-1)

    # Commands (v9.36: user-facing entry points run inside _failsafe -
    # a crashed screen can never again leave a user with nothing)
    app.add_handler(CommandHandler("start", _failsafe(start_cmd)))
    app.add_handler(CommandHandler("menu", _failsafe(menu_cmd)))
    app.add_handler(CommandHandler("language", _failsafe(language_cmd)))
    app.add_handler(CommandHandler("help", _failsafe(help_cmd)))
    app.add_handler(CommandHandler("admin", _failsafe(admin_cmd)))
    app.add_handler(CommandHandler("trace", trace_cmd))

    # Text router (ALL navigation happens through the bottom keyboard)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
                                   _failsafe(on_text)))

    # Photo / Document (deposit screenshots) + v9.23 broadcast media
    app.add_handler(MessageHandler(filters.PHOTO, _failsafe(on_photo)))
    app.add_handler(MessageHandler(filters.Document.ALL,
                                   _failsafe(on_document)))
    app.add_handler(MessageHandler(_MEDIA_FILTER, _failsafe(on_media)))

    # Callback queries (specific first, fallback LAST for old-version buttons)
    app.add_handler(CallbackQueryHandler(_failsafe(otp_callback),
                                         pattern=r"^otp:"))
    app.add_handler(CallbackQueryHandler(admin_deposit_callback,
                                         pattern=r"^admdep:"))
    app.add_handler(CallbackQueryHandler(_failsafe(buy_callback),
                                         pattern=r"^buy:"))
    app.add_handler(CallbackQueryHandler(_failsafe(dep_callback),
                                         pattern=r"^dep:"))
    app.add_handler(CallbackQueryHandler(admin_flow_callback,
                                         pattern=r"^(adst|adstc|adrt|adbn|admuser):"))
    app.add_handler(CallbackQueryHandler(_failsafe(lang_callback), pattern=r"^lang:"))
    # v9.23: force-join verify + manage-channels + join tracking
    app.add_handler(CallbackQueryHandler(_failsafe(fj_verify_callback), pattern=r"^fjv:"))
    # v9.28 FIX: pattern "^adch:" never matched the REMOVE buttons
    # (callback "adchr:<id>") - channel removal has been dead since
    # v9.23: the tap fell through to the expired-button fallback. The
    # pattern now covers both prefixes (adch: + adchr:).
    app.add_handler(CallbackQueryHandler(channels_callback,
                                         pattern=r"^adch"))
    # v9.24: Manage Reffer inline (VIP remove list)
    app.add_handler(CallbackQueryHandler(admin_refer_callback,
                                         pattern=r"^adrfr:"))
    # v9.31: user-side Bulk Buy (type pick / confirm / cancel)
    # v9.34: admin BULK MANAGE (live bulk-discount config)
    app.add_handler(CallbackQueryHandler(admin_bulkmanage_callback,
                                         pattern=r"^bulkm:"))
    app.add_handler(CallbackQueryHandler(_failsafe(user_bulkbuy_callback),
                                         pattern=r"^ubulk:"))
    app.add_handler(ChatJoinRequestHandler(on_join_request))
    app.add_handler(ChatMemberHandler(on_chat_member,
                                      ChatMemberHandler.CHAT_MEMBER))
    app.add_handler(CallbackQueryHandler(_failsafe(nav_callback),
                                         pattern=r"^nav:"))
    app.add_handler(CallbackQueryHandler(_failsafe(fallback_callback)))

    app.add_error_handler(on_error)
    return app


def main():
    # Startup/runtime supervisor: transient Telegram-API or network
    # failures (proven live: TimedOut in get_me) must not leave the
    # bot dead. Restart with capped backoff; a CLEAN shutdown (SIGTERM
    # from timeout/systemd, Ctrl-C) exits without restarting.
    attempt = 0
    while True:
        attempt += 1
        try:
            logger.info("Starting bot v9.40 (SILENT BOOT: zero test "
                        "messages - emoji/icon checks are read-only API "
                        "probes; BINANCE PAY: 4th deposit network "
                        "\U0001F3E6 Binance Pay - pay the order's EXACT amount to "
                        "Pay ID %s, auto-verifies by ORDER ID via the official Binance API "
                        "+ 45s order-id retry sweep; one Order ID = one credit ever; "
                        "USER BULK BUY: menu button "
                        "-> type how many -> balance-verified purchase "
                        "with the owner-set bulk discount -> otphub.<n><country>.txt "
                        "file, per-number order rows so Refund Send "
                        "matches each number; admin Bulk Buy v9.30 "
                        "intact; NEW TOKEN + OTP success channel %s: "
                        "every delivered OTP posted with name, masked "
                        "number, OTP, price; OTP 100%% delivery net: "
                        "restart recovery + permanent sweeper worker + "
                        "refund/OTP race guard, three independent "
                        "delivery paths; refund hub - Check Number / "
                        "Refund Send with data wipe / Chek Number & "
                        "Refund one-tap bulk; Active Numbers menu; referral "
                        "commission pays on OTP arrival; second admin %s "
                        "FULL access; OTP delivery v9.26 machine-endpoint "
                        "fetch intact; 13 languages, loot-proof core: "
                        "atomic buy, TXID verify, trace)... attempt %s",
                        BINANCE_PAY_ID_DEFAULT,
                        OTP_SUCCESS_CHANNEL,
                        ADMIN_ID_2, attempt)
            app = build_app()
            app.run_polling(allowed_updates=Update.ALL_TYPES)
            logger.info("Clean shutdown - supervisor exiting.")
            break
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception as e:
            wait = min(30, 3 * attempt)
            logger.warning("Bot failure (%s: %s) - auto-restart in %ss",
                           type(e).__name__, str(e)[:100], wait)
            try:
                asyncio.run(_release_shared_resources())
            except Exception:
                pass
            time.sleep(wait)


if __name__ == "__main__":
    main()
