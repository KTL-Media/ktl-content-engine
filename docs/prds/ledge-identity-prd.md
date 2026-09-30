# PRD: Persistent AI Visual Identity Platform

**Working product name:** Ledge Identity\
**Product type:** Consumer/prosumer AI visual-creation SaaS\
**Status:** Draft\
**Version:** 0.1\
**Primary platform:** Responsive web application, with mobile-first capture support\
**Primary user:** Creators, artists, musicians, influencers, entrepreneurs, and marketers who want recognizable, reusable AI representations of themselves across visual media.

## 1. Product summary

Ledge Identity transforms a user’s photographs into a persistent, user-controlled multidimensional AI identity that can appear consistently across images, avatars, cinematic scenes, stylized worlds, UGC-style ads, commercials, trailers, and music-video concepts.

The platform’s core promise is:

> **Create once. Be visually recognizable anywhere.**

Unlike a general image generator where each prompt starts from scratch, the product creates a reusable **Identity Profile**: a secure, consent-based representation of a user’s distinctive visual characteristics, preferences, approved likeness settings, and stylistic boundaries. That identity can then power a guided creation pipeline across multiple formats and model providers.

The core flywheel is:

$$
\text{Capture} \rightarrow \text{Create Identity} \rightarrow \text{Explore Worlds} \rightarrow \text{Generate} \rightarrow \text{Animate} \rightarrow \text{Publish} \rightarrow \text{Share} \rightarrow \text{Earn/Bonus} \rightarrow \text{Create More}
$$

The commercial model combines free promotional credits, subscriptions, one-time credit packs, and usage-based pricing for higher-cost generations such as high-resolution images, multi-scene video, character animation, and premium model workflows.

______________________________________________________________________

## 2. Problem and opportunity

### Problem

People want to create professional visual content featuring themselves, but traditional production is slow, expensive, and limited by location, scheduling, wardrobe, crews, cameras, editing, and post-production.

Existing AI image tools can generate attractive visuals, but they often fail on the most important requirement: **the person does not consistently look like themselves across outputs.** Users may get inconsistent facial structure, body proportions, hair, skin tone, styling, age, or recognizable features from one generation to the next.

Creators also face fragmented workflows:

- One tool for headshots and avatars.
- A separate tool for AI images.
- Another for video animation.
- Another for editing, captions, and publishing.
- No durable identity layer that persists across those tools and outputs.
- No clear mechanism to monetize or earn usage credits from published content.


### Opportunity

A persistent identity layer can become the user’s creative infrastructure: a personal digital actor, avatar system, and visual-production workspace.

For independent creators and small businesses, this platform can make high-volume visual production possible without replacing the user’s authorship. The user remains the owner, director, reviewer, and publisher; AI accelerates creation and production.

Because the product processes photographs and may derive information associated with a person’s appearance, it must be designed as a consent-first, privacy-first product. Privacy guidance for biometric systems emphasizes explicit knowledge and agreement, minimal collection, privacy-by-design, documented consent, security controls, and a clear retention/deletion approach.[^2_1][^2_2][^2_3]

______________________________________________________________________

## 3. Product vision

### Vision statement

Build the most trusted personal AI identity platform for creating recognizable, expressive, commercially useful visual media across images and video.

### Product principles

- **Identity continuity:** The person should remain recognizable across styles, environments, poses, formats, and time.
- **Creator control:** Users decide what their identity can generate, where it can be used, and whether it is private, shareable, or commercially licensable.
- **Consent by design:** The platform supports only self-owned identities by default, with enhanced authorization requirements for third-party likenesses.
- **Creation before configuration:** Users should reach a compelling first output quickly without learning complex prompt engineering.
- **Model-agnostic orchestration:** The platform can route work across identity-consistency, image-generation, upscaling, editing, lip-sync, and image-to-video services.
- **Transparent economics:** Every workflow displays its credit cost before execution.
- **Safe publishing:** Generated media should carry provenance and disclosure mechanisms where technically and commercially appropriate.

______________________________________________________________________

## 4. Goals and non-goals

### Product goals

| Goal | Definition of success |
| :-- | :-- |
| Establish a high-quality identity profile | Users can create a reusable identity from guided photo capture or uploads |
| Deliver recognizable outputs | Users perceive generated people as consistently resembling their approved identity |
| Reduce time to professional content | A user can produce a usable image in minutes and a short animated asset in a single session |
| Support varied creative expression | Users can render their identity across realistic, cinematic, cartoon, editorial, commercial, and music-video formats |
| Build a sustainable credit economy | Users understand credits, use them intentionally, and can upgrade or replenish without confusion |
| Create a sharing flywheel | Finished content drives referrals, engagement, and earned promotional credits |
| Preserve user trust | Users can control, export, delete, or revoke their identity and associated media |

### Non-goals for MVP

- Full Hollywood-grade feature-film production.
- Fully autonomous publishing to every social network.
- Open marketplace for selling another person’s likeness.
- Public generation using celebrity, public-figure, or non-consenting third-party identities.
- Voice cloning, real-time face swapping, and live-stream impersonation.
- Enterprise-grade team administration, SSO, rights-management workflows, and agency multi-seat controls.
- Native mobile applications at initial launch; mobile web capture is sufficient for MVP.
- General-purpose AI editing software intended to replace professional video editors.

______________________________________________________________________

## 5. Users and jobs to be done

### Primary persona: Independent visual creator

**Profile:** Musicians, video creators, influencers, podcasters, educators, streamers, artists, and solo entrepreneurs.

**Need:** Produce distinctive content at a pace and budget that supports frequent publishing.

**Job to be done:**

> When I need fresh visual content for my audience or brand, I want to create consistent images and videos that visibly look like me, so I can publish more often without organizing a traditional photo or video shoot.

### Secondary persona: Brand operator or small business owner

**Profile:** Founders, coaches, local brands, e-commerce sellers, realtors, consultants, and marketing freelancers.

**Need:** Generate ad-ready visual assets using a recognizable representative or spokesperson.

**Job to be done:**

> When I need marketing creative, I want to place my approved identity into campaigns, scenes, and formats, so I can test content quickly while maintaining a recognizable personal brand.

### Tertiary persona: Creative director or production collaborator

**Profile:** Social-media manager, editor, agency contractor, designer, producer, or collaborator working for the identity owner.

**Need:** Produce assets from an approved identity without receiving unrestricted account access.

**Job to be done:**

> When I create assets for a client, I want permissioned access to their approved identity and brand rules, so I can produce content while the identity owner keeps control over their likeness.

______________________________________________________________________

## 6. Product flywheel

| Stage | User action | Product outcome | Flywheel effect |
| :-- | :-- | :-- | :-- |
| Capture | Upload or capture guided photographs | Sufficient, high-quality identity inputs | Better source material improves output quality |
| Create Identity | Train/configure an Identity Profile | Persistent, reusable likeness layer | Identity becomes a retained product asset |
| Explore Worlds | Browse styles, templates, characters, and scenes | Creative inspiration without prompt expertise | More discovery increases generation intent |
| Generate | Create images from an identity + world + prompt | High-value visual outputs | Successful results build trust and habit |
| Animate | Turn images into motion or video sequences | More shareable, premium output | Animation creates higher-value credit use |
| Publish | Export, download, schedule, or share assets | Content enters the user’s channels | Published output becomes acquisition surface |
| Share | Share branded links, results, or referral invites | New user discovery and social proof | Referrals reduce acquisition cost |
| Earn/Bonus | Receive referral, challenge, launch, or campaign credits | Incentive to return | Credits trigger repeat creation |
| Create More | Reuse identity, saved worlds, templates, and projects | Ongoing content production | Retention and subscription value increase |

### Core loop metric

$$
\text{Activated Creator} =
\text{Identity Approved}
\land
\text{First Generation Completed}
\land
\text{First Asset Saved or Shared}
$$

### North-star metric

**Weekly Identity-Powered Creations:** the number of completed image or video assets generated using a verified Identity Profile during a seven-day period.

______________________________________________________________________

## 7. MVP scope

### Must-have capabilities

| Capability | MVP requirement | Priority |
| :-- | :-- | :-- |
| Account and age gate | Email/OAuth sign-up, terms acceptance, age confirmation | Must |
| Identity consent | Explicit consent and self-ownership attestation before identity creation | Must |
| Guided capture/upload | Upload 10–25 photos with quality guidance and validation | Must |
| Identity Profile | Create one persistent identity per user, with preview and approval state | Must |
| Identity quality review | Automated quality checks plus fallback/manual-review queue | Must |
| World explorer | Browse presets for styles, scenes, wardrobe, poses, and creative formats | Must |
| Image generation | Generate identity-consistent images from templates and prompts | Must |
| Image variations | Re-run, remix, change pose/style/background, and upscale | Must |
| Generation history | Save prompts, settings, outputs, costs, and job status | Must |
| Credit wallet | Display balance, per-action cost, ledger, and promotional credits | Must |
| Subscription and packs | Free tier, paid subscriptions, and one-time credit purchases | Must |
| Basic video animation | Convert approved image outputs into short image-to-video clips | Should |
| Export and share | Download approved files and share a public gallery link | Should |
| Referral rewards | Invite link, attribution, and bonus-credit issuance | Should |
| Brand kits | Save preferred colors, mood, references, and recurring worlds | Could |
| Collaboration | Invite a limited collaborator to a project | Could |
| Social scheduling | Publish or schedule directly to social platforms | Post-MVP |
| Advanced multi-scene video editor | Timeline, audio sync, transitions, sequencing | Post-MVP |
| Voice cloning | Voice identity, lip sync, dubbing | Post-MVP / separate risk review |


______________________________________________________________________

## 8. User experience

### Primary onboarding flow

1. User lands on a clear value proposition: “Create your AI visual identity.”
2. User creates an account and completes age confirmation.
3. User reads and accepts a specific likeness, consent, retention, and acceptable-use disclosure.
4. User chooses **Create My Identity**.
5. The app explains photo requirements: lighting, angles, facial visibility, expression variation, no other people, no sunglasses, no heavy filters.
6. User uploads or captures 10–25 photos.
7. The system validates image quality and identifies unusable photos.
8. User confirms: “I own or have legal authority to use these images and authorize creation of this identity.”
9. The system creates an Identity Profile and displays a training/processing status.
10. User receives a first “identity check” output.
11. User approves, retries, or improves their source set.
12. User enters the World Explorer and receives a starter credit grant.
13. User selects a world/template, adjusts optional creative controls, and generates a first image.
14. User downloads, saves, remixes, animates, or shares the result.

### First-value target

A new user should receive an identity-based image they consider recognizable within 15 minutes of completing a successful upload flow, excluding exceptional review cases.

### Core creation flow

1. User selects an approved Identity Profile.
2. User selects a world, template, or style.
3. User optionally specifies a prompt, wardrobe, mood, camera angle, setting, and aspect ratio.
4. The app presents a visual preview of the request and exact credit cost.
5. User confirms generation.
6. The system deducts or reserves credits and queues the job.
7. The user sees progress states: `Queued`, `Preparing identity`, `Generating`, `Enhancing`, `Complete`, or `Failed`.
8. On completion, the user can compare variants, save a favorite, remix, upscale, animate, or export.
9. The system stores lineage: identity version, world/template, prompt, generation model, settings, cost, and output source.

### Animation flow

1. User selects a generated image or an image from their approved identity library.
2. User chooses a motion template or provides a concise movement prompt.
3. User sets aspect ratio, duration, and output quality.
4. The app displays credit cost and expected completion range.
5. User confirms generation.
6. The platform sends the asset through an image-to-video workflow.
7. The user receives a video preview and can download, regenerate, or publish.

______________________________________________________________________

## 9. Functional requirements

### 9.1 Accounts and authentication

- Users can sign up through email/password and supported OAuth providers.
- The platform requires confirmation that users meet the service’s minimum age requirement before identity creation.
- Users can sign in, sign out, reset credentials, manage payment methods, and request account deletion.
- Each account has a private default workspace.
- A user cannot access another user’s identity, generations, credit balance, or source photographs without explicit authorization.


### 9.2 Identity capture and creation

- A user can upload JPG, JPEG, PNG, HEIC, and WEBP images.
- The system validates file size, resolution, face visibility, image sharpness, duplicate images, presence of multiple people, and excessive filtering.
- The platform provides a minimum and recommended photo count.
- The upload experience explains why an image fails validation and suggests a correction.
- The user must affirm that they are the depicted person or have documented authorization to create the identity.
- The system records the consent event, policy version, timestamp, account ID, and supplied attestation.
- The system creates an immutable Identity Profile ID and versioned Identity Model records.
- Users can rename, archive, regenerate, or permanently delete their identities.
- The default maximum for MVP is one active verified identity per account, with additional identities enabled only under reviewed conditions.


### 9.3 Identity Profile

An Identity Profile includes:


| Attribute | Description |
| :-- | :-- |
| Identity ID | Internal persistent identifier |
| Display name | User-selected private label |
| Identity status | Draft, processing, review required, approved, suspended, deleted |
| Source set | Original images and quality metadata |
| Identity embedding/model reference | Encrypted or provider-safe representation needed for consistency workflows |
| Visual traits profile | System-derived identity controls, not exposed as an identity-verification product |
| Identity version | Versioned changes from new or improved source images |
| Consent record | Timestamped consent and policy version |
| Allowed uses | Personal, commercial, collaboration, public sharing settings |
| Restrictions | Disallowed content categories, visibility rules, or account-level safety limits |
| Creation lineage | Workflow/model versions used to establish the identity |

### 9.4 World Explorer

The World Explorer lets users select prebuilt creative contexts without needing advanced prompt skills.

World categories include:

- Professional headshots and personal branding.
- Editorial fashion and luxury campaigns.
- Film stills and cinematic characters.
- Sci-fi, fantasy, noir, cyberpunk, and surreal environments.
- Cartoon, anime-inspired, illustrated, clay, comic, and 3D-avatar treatments.
- Music-video scenes and album-cover concepts.
- UGC testimonials, creator ads, product demonstrations, and promotional imagery.
- Travel, sports, nightlife, business, education, and lifestyle settings.
- Seasonal, cultural, event, and campaign-based creative packs.

Each world includes:

- A title and thumbnail.
- A creative prompt template.
- Supported aspect ratios.
- Supported identity strength range.
- Required or optional variables.
- Content rating and safety constraints.
- Credit estimate by output type.
- Model/workflow compatibility.
- A recommended “starter prompt” for fast creation.


### 9.5 Image generation

- Users can generate 1, 2, or 4 image variations per request.
- Users can select format: portrait, square, landscape, vertical short-form, wide cinematic, or custom supported dimensions.
- Users can set creative controls such as identity strength, realism, style intensity, lighting, setting, wardrobe, camera framing, and mood.
- The platform must preserve the selected identity as the primary subject unless the user explicitly requests a non-personal output.
- The system must prevent or block disallowed prompts and unsafe content requests.
- Users can save outputs to a private library.
- Users can remix previous outputs while preserving reference lineage.
- Users can use an output as an image reference for later generations.
- Users can upscale or enhance a completed output when supported.
- Every generation creates a Job record, output record, cost entry, and audit event.


### 9.6 Video and animation

- Users can animate an approved identity-based image into a short video.
- MVP supports predefined duration options such as 5, 8, or 10 seconds, subject to provider availability.
- Users can choose motion templates: subtle portrait movement, camera push-in, turn, walk, performance energy, ambient scene, product presentation, and cinematic motion.
- The system shows credit cost and expected processing status before execution.
- The resulting video retains the originating image, identity version, generation workflow, and safety metadata.
- The platform rejects video requests that violate likeness, safety, or deceptive-use rules.
- Users can download or share watermarked or provenance-enabled outputs according to plan and policy.


### 9.7 Projects and content library

- Users can create projects such as “Album Visuals,” “Fall Campaign,” “Podcast Promo,” or “Personal Brand.”
- Projects contain identities, references, prompts, worlds, image outputs, video outputs, and exports.
- Users can search and filter the library by date, project, content type, world, status, and favorites.
- Users can duplicate a project to create a new campaign.
- Users can delete assets individually or in bulk.
- Users can export selected items as image or video files, subject to plan limitations.


### 9.8 Publishing and sharing

- Users can download images and video outputs in supported formats.
- Users can create an optional share page for selected assets.
- Share pages can be private link-only, unlisted, or public.
- Users can revoke a share page at any time.
- The platform includes a configurable generated-media disclosure or provenance indicator where supported.
- Users can copy a share link and referral link from the asset or project view.
- Direct social publishing is post-MVP; MVP focuses on optimized downloads and sharing links.


### 9.9 Credits, subscriptions, and bonuses

- Every credit-consuming action displays cost before the user confirms.
- The platform supports:
    - Free sign-up credits.
    - Subscription-issued recurring credits.
    - One-time purchased credit packs.
    - Promotional credits.
    - Referral credits.
    - Campaign or challenge rewards.
- Credits must distinguish expiration rules by credit type.
- The wallet displays available balance, pending/reserved balance, recent usage, bonus credits, purchased credits, and expiration date where applicable.
- Failed jobs automatically refund reserved credits unless the job produced a usable partial result and the policy clearly states otherwise.
- The system records an immutable ledger entry for grants, reservations, deductions, refunds, expirations, purchases, and adjustments.
- High-cost video and premium workflows require explicit confirmation before execution.


### 9.10 Referral and reward system

- Each user receives a unique referral link.
- A referral reward is issued only after the referred account completes defined activation criteria, such as identity approval and first successful generation.
- The system detects and limits self-referral, duplicate-account abuse, and fraud.
- Credits earned through referrals have a clear amount, expiration rule, and usage scope.
- Promotional challenges can reward users for eligible public sharing, subject to clear terms and anti-fraud review.
- Rewards should not require users to make their identity public by default.

______________________________________________________________________

## 10. Safety, consent, and trust requirements

A visual-identity product must treat a person’s likeness as a high-trust asset, not merely as an image prompt. Guidance on biometric data and AI emphasizes explicit consent, informed disclosure, data minimization, protection against unauthorized access, meaningful retention and deletion controls, and assessment of foreseeable harms.[^2_3][^2_4][^2_1]

### Consent requirements

- The user must explicitly confirm they own the images or possess legal authority to use them.
- Consent must be separate from general terms of service and describe the purpose of identity creation, processing, storage, generation, sharing, and deletion.
- The system records consent version, date/time, identity ID, and account ID.
- The user can withdraw consent and request deletion of the Identity Profile and associated identity-training artifacts, subject to lawful retention requirements.
- The system must clearly state whether uploaded images or derived identity representations are used to train general models. The MVP default should be: **not used for generalized model training without separate opt-in consent.**
- Users must be able to opt out of promotional use of their generated content and likeness.


### Likeness protection

- MVP supports self-identity only.
- Users may not create identities for celebrities, public figures, minors, acquaintances, partners, clients, or any third party without verified authorization.
- The product blocks non-consensual sexual, exploitative, defamatory, fraudulent, or deceptive likeness content.
- The system must not position outputs as authentic recordings, evidence, or endorsements.
- The platform includes reporting and rapid review paths for impersonation, unauthorized likeness use, and harmful content.
- Account suspension and asset removal tools must be available to trust-and-safety operators.


### Privacy and data minimization

- Collect only the images, account data, and derived information necessary to create and operate the Identity Profile.
- Encrypt source photographs, identity artifacts, credentials, and access tokens in transit and at rest.
- Separate identity data from analytics identifiers where feasible.
- Restrict internal access through least-privilege controls and audit logging.
- Provide self-service identity deletion and account deletion flows.
- Publish retention periods for source images, generated outputs, identity artifacts, backups, and logs.
- Require a privacy impact assessment and jurisdiction-specific legal review before launch in markets with biometric privacy laws.


### Content safeguards

- Prompt and image moderation occurs before and after generation as appropriate.
- Users receive a clear explanation when content is blocked, with a safe alternative where possible.
- The system flags potentially misleading public-facing content that depicts realistic events, endorsements, or news-like imagery.
- Exports can include metadata or visible disclosures when required by policy, platform rules, or applicable law.
- The user can mark content as personal, commercial, or public-shareable, but cannot override safety restrictions.

______________________________________________________________________

## 11. Non-functional requirements

### Performance

| Workflow | Target |
| :-- | :-- |
| Standard web page load | Under 3 seconds on typical broadband |
| Photo validation feedback | Under 5 seconds after upload completion |
| Identity processing acknowledgment | Immediate status confirmation |
| Identity creation | Target under 15 minutes for normal queue conditions |
| Standard image generation | Target under 90 seconds |
| Image variation/retry | Target under 90 seconds |
| Short image-to-video generation | Target under 10 minutes, provider-dependent |
| Library search/filter response | Under 2 seconds for typical user library size |

### Reliability

- Target 99.5% monthly application availability for MVP.
- Generation jobs must be asynchronous, fault-tolerant, retryable, and idempotent.
- Every job must expose a user-visible status.
- Failed provider jobs must either retry safely, route to an approved fallback workflow, or return a clear failure result.
- Credit deductions must be transactionally linked to job state to prevent double charging.
- Source images and identity artifacts require backup and recovery policies consistent with user deletion rights.


### Security

- Use TLS for all data in transit.
- Encrypt sensitive data at rest.
- Do not expose model-provider API keys, payment credentials, or internal identity references in the client.
- Require server-side authorization checks for every identity, project, asset, export, and wallet action.
- Log authentication, consent, identity creation, identity deletion, sharing, export, referral, and credit events.
- Rate-limit uploads, generation requests, login attempts, password resets, and referral actions.
- Perform vulnerability testing, abuse testing, and access-control testing before launch.


### Accessibility

- Core capture, upload, creation, export, account, and deletion flows support keyboard navigation.
- All form controls have accessible labels and actionable validation errors.
- Progress states are available to screen readers.
- Color is not the only mechanism used to communicate job status or safety warnings.
- The platform targets WCAG 2.1 AA for core workflows.

______________________________________________________________________

## 12. Technical architecture

### High-level system components

| Component | Responsibility |
| :-- | :-- |
| Web client | Onboarding, capture, World Explorer, generation controls, library, wallet, share pages |
| API gateway | Authentication, authorization, request validation, rate limiting |
| Identity service | Upload intake, quality checks, consent binding, identity creation, version management |
| Orchestration service | Routes jobs to approved generation, enhancement, animation, and moderation providers |
| Job queue | Asynchronous processing, retry rules, status propagation, provider fallback |
| Prompt/template service | World templates, prompt construction, safety constraints, version control |
| Asset service | Secure image/video storage, transformations, CDN delivery, deletion workflows |
| Credit service | Wallet, ledger, reservations, deductions, refunds, entitlements, promotions |
| Payments service | Subscription status, purchases, invoices, webhook reconciliation |
| Moderation service | Prompt moderation, input-image checks, output review, abuse reporting |
| Analytics service | Activation, funnel, generation, cost, retention, referral, and safety events |
| Admin console | Support, moderation, refunds, identity review, content takedowns, audit review |

### AI orchestration requirements

- The system must abstract underlying providers so the product is not coupled to one image or video model.
- Each job stores provider, model version, workflow version, latency, cost, retry count, safety result, and output lineage.
- Model routing rules may vary by task type, quality tier, available credit balance, geography, safety classification, and provider health.
- Prompt templates must be versioned and reversible.
- The system should support identity-consistency methods appropriate to each model provider without exposing proprietary implementation details to the end user.
- Evaluation tooling must compare identity fidelity, prompt adherence, visual quality, safety outcomes, latency, and cost.


### Core entities

| Entity | Core fields |
| :-- | :-- |
| User | `id`, `email`, `display_name`, `age_gate_status`, `account_status`, `created_at` |
| Workspace | `id`, `owner_id`, `name`, `plan_id`, `settings` |
| Identity Profile | `id`, `workspace_id`, `name`, `status`, `identity_version`, `consent_id`, `created_at` |
| Identity Source | `id`, `identity_id`, `asset_id`, `quality_score`, `validation_status`, `metadata` |
| Consent Record | `id`, `user_id`, `identity_id`, `policy_version`, `attestation`, `timestamp` |
| World Template | `id`, `category`, `title`, `prompt_template`, `settings_schema`, `safety_policy` |
| Project | `id`, `workspace_id`, `name`, `identity_id`, `visibility`, `created_at` |
| Generation Job | `id`, `project_id`, `identity_id`, `type`, `status`, `provider`, `model_version`, `credit_cost` |
| Media Asset | `id`, `job_id`, `type`, `storage_key`, `visibility`, `provenance`, `created_at` |
| Credit Wallet | `id`, `workspace_id`, `available_credits`, `reserved_credits` |
| Credit Ledger Entry | `id`, `wallet_id`, `type`, `amount`, `source`, `expiration_at`, `reference_id` |
| Referral | `id`, `referrer_id`, `referred_user_id`, `status`, `reward_entry_id` |
| Safety Case | `id`, `asset_id`, `reporter_id`, `category`, `status`, `resolution` |


______________________________________________________________________

## 13. Credit economy

### Example credit actions

Credit costs must be configurable and may change by provider cost, plan, output quality, and promotional policy.


| Action | Illustrative cost | Notes |
| :-- | --: | :-- |
| Standard image, one variation | 5 credits | Standard resolution and queue |
| Standard image, four variations | 16 credits | Discounted bundle versus four individual runs |
| High-quality image | 12 credits | Higher-cost model or enhanced workflow |
| Upscale/enhance | 3 credits | Applies to an existing output |
| Identity reprocessing | 25 credits | Free or discounted retry when platform quality checks fail |
| 5-second animation | 30 credits | Cost depends on motion model |
| 10-second premium animation | 60 credits | Higher compute cost |
| Commercial/UGC template pack | Variable | Template may carry a workflow multiplier |

### Subscription tiers

| Plan | Intended user | Included benefits |
| :-- | :-- | :-- |
| Free | Evaluators and new users | Starter credits, one identity, standard queue, limited export |
| Creator | Frequent individuals | Monthly credits, higher-resolution output, faster queue, more saved projects |
| Pro | Professional creators | Larger credit allocation, premium workflows, commercial-use tools, expanded library |
| Studio | Teams/agencies, post-MVP | Multiple identities with authorization, collaboration, brand kits, admin controls |

### Credit policy requirements

- Display exact credit cost before a user starts a generation.
- Reserve credits when a job begins; settle the charge only according to clear success/failure rules.
- Automatically refund the correct amount when an eligible job fails.
- Identify bonus, subscription, and purchased credits separately.
- Apply the user-visible credit-expiration rule deterministically.
- Prevent negative balances unless a separate, explicit policy supports it.
- Provide receipt and ledger records for every payment and credit event.
- Protect the system from unauthorized credit issuance, referral fraud, payment fraud, and replayed provider webhooks.

______________________________________________________________________

## 14. Analytics and KPIs

### Product funnel

| Funnel stage | Event | Metric |
| :-- | :-- | :-- |
| Acquisition | `landing_viewed` | Visitor-to-signup conversion |
| Registration | `signup_completed` | Signup completion rate |
| Consent | `identity_consent_accepted` | Consent acceptance rate |
| Capture | `identity_upload_started` / `identity_upload_completed` | Upload completion rate |
| Identity | `identity_creation_completed` | Approved identity rate |
| First creation | `generation_started` / `generation_completed` | First-generation completion rate |
| Value realization | `asset_saved` / `asset_downloaded` / `asset_shared` | First-value rate |
| Animation | `animation_started` / `animation_completed` | Image-to-video adoption |
| Monetization | `checkout_started` / `purchase_completed` | Credit purchase conversion |
| Retention | `generation_completed` in later period | D7, D30, and weekly creator retention |
| Virality | `referral_link_shared` / `referral_activated` | Referral activation rate |

### Key product metrics

- Identity approval rate.
- Median time from signup to first successful identity-based creation.
- First-generation completion rate.
- Identity fidelity rating from user feedback and internal evaluation.
- Generation success rate by provider, workflow, and world template.
- Average credits consumed per active creator.
- Credit-purchase conversion rate.
- Subscription conversion rate.
- Cost of goods sold per generated image and per video second.
- Download/share rate per completed asset.
- Referral activation rate.
- D7 and D30 creator retention.
- Trust-and-safety report rate.
- Identity deletion and consent withdrawal rate.
- Refund rate and failed-job credit refund rate.


### Event examples

```text
signup_completed
age_gate_confirmed
identity_consent_accepted
identity_upload_started
identity_photo_rejected
identity_creation_started
identity_creation_completed
identity_approved
world_viewed
template_selected
generation_cost_viewed
generation_started
generation_completed
generation_failed
asset_saved
asset_downloaded
asset_shared
animation_started
animation_completed
credit_pack_purchased
subscription_started
referral_link_shared
referral_activated
bonus_credits_granted
identity_deleted
consent_withdrawn
content_reported
```


______________________________________________________________________

## 15. Acceptance criteria

### Identity creation

- Given a signed-in eligible user, when they upload the required number of valid photos and accept the identity consent flow, then the system creates an Identity Profile in `processing` state.
- Given an upload containing insufficient quality, multiple people, or unsupported content, when validation runs, then the user sees specific rejected images and remediation guidance.
- Given a successful identity workflow, when the identity passes quality checks, then the user receives an `approved` identity with a generated identity-check preview.
- Given an identity-quality failure caused by the platform workflow, when no usable identity is produced, then the user receives a retry path and eligible credit refund or reprocessing entitlement.
- Given a user requests identity deletion, when they confirm the request, then new generation using that identity is immediately disabled and deletion processing begins according to the published retention policy.


### Image generation

- Given an approved identity and enough available credits, when a user chooses a world and confirms a generation, then the system creates a job, displays the credit cost, and shows a non-blocking progress state.
- Given a completed image job, when the user opens the output, then they can save, download, remix, upscale, or use the asset as an animation source.
- Given a failed image job, when failure is confirmed, then the user receives an intelligible error message, a retry option where appropriate, and correct credit settlement.
- Given a blocked prompt or output, when safety controls detect prohibited content, then no unsafe asset is released and the user receives a policy-aligned explanation.


### Animation

- Given a completed and eligible image asset, when a user selects an animation template and confirms cost, then the system starts an asynchronous video-generation job.
- Given a completed animation, when the user views it, then they can preview, download, regenerate, or share it.
- Given an animation-provider failure, when retries are exhausted, then the user sees the failed state and receives the applicable credit refund.


### Credits and rewards

- Given a paid or bonus credit grant, when the transaction is completed, then the wallet balance and immutable ledger update exactly once.
- Given a job begins, when credits are reserved, then the user cannot spend those same credits on another job.
- Given a qualifying referral activation, when anti-fraud checks pass, then referrer and/or referred-user bonuses are issued according to the active campaign rules.
- Given a job does not produce a completed eligible output, when the platform determines the job failed, then the reserved credits are released or refunded according to policy.

______________________________________________________________________

## 16. Risks and mitigations

| Risk | Impact | Mitigation |
| :-- | :-- | :-- |
| Identity inconsistency reduces trust | High | Curated source-photo guidance, quality scoring, model evaluations, user feedback loops, identity versioning |
| Non-consensual likeness misuse | Critical | Self-identity default, explicit attestation, reporting, moderation, rapid takedown, account enforcement |
| Biometric/privacy regulatory exposure | Critical | Privacy-by-design, explicit consent, minimization, retention policy, deletion controls, legal review by jurisdiction |
| AI-generated deception or impersonation | High | Use restrictions, public-share safeguards, disclosures/provenance, policy enforcement, abuse monitoring |
| High video-generation costs | High | Clear cost previews, tiering, queues, provider routing, cost caps, credit reservations |
| Provider outages or performance volatility | Medium/High | Multi-provider abstraction, retries, fallbacks, status transparency, refund automation |
| Referral or promotion abuse | Medium | Device/account/risk signals, delayed payouts, activation thresholds, manual review |
| Copyright or commercial-use disputes | High | Clear user warranties, asset/source policies, world-template rights review, legal escalation process |
| Users expect perfect identity reproduction | Medium/High | Honest onboarding, preview testing, quality feedback, controlled identity-strength settings, regenerate options |
| Content moderation over-blocks valid creative work | Medium | Explainable blocks, appeals, template-level safety tuning, human review for edge cases |


______________________________________________________________________

## 17. Release plan

### Phase 0: Foundations

- Define policies for consent, identity ownership, prohibited uses, data retention, deletion, and commercial usage.
- Build secure account, storage, consent, wallet, and job-orchestration foundations.
- Select initial image, identity-consistency, moderation, and image-to-video providers.
- Establish model evaluation datasets using properly authorized test data.
- Build admin tooling for support, refunds, and safety incidents.


### Phase 1: Closed alpha

- Self-identity onboarding.
- Photo upload and quality validation.
- One persistent identity profile.
- Limited World Explorer.
- Image generation with saved history.
- Basic credit wallet and promotional credits.
- Internal human review for identity-quality and safety edge cases.
- Invite-only user group with close qualitative feedback.


### Phase 2: Public beta

- Subscription plans and purchased credit packs.
- Expanded world/template catalog.
- Image remix, enhancement, and project organization.
- Short-form image-to-video animation.
- Share links and referral bonus system.
- In-product feedback on likeness quality and output usefulness.
- Automated refunds for qualifying failed jobs.


### Phase 3: Growth and creator tools

- Brand kits and saved creative presets.
- Advanced commercial, UGC, trailer, and music-video templates.
- Collaboration with owner-controlled permissions.
- Social export optimization and optional publishing integrations.
- Higher-quality video workflows.
- Creator challenges, template marketplace exploration, and approved partner workflows.

______________________________________________________________________

## 18. Open questions

1. Will the initial launch serve only adult users in the United States, or support multiple jurisdictions from day one?
2. What level of identity verification is appropriate before allowing an identity to generate commercially usable content?
3. Will users own all generated assets, receive a broad license, or face plan-specific commercial-use restrictions?
4. Are source photos retained after identity creation, or can users choose “train then delete originals”?
5. Can a user create multiple identities, such as “professional,” “performance,” “animated,” or “character” versions of themselves?
6. What objective and subjective standard defines acceptable identity fidelity?
7. Which image and video model providers meet the required cost, quality, commercial-use, safety, and privacy standards?
8. Will commercial templates require stronger disclosure, review, or provenance controls than personal creative outputs?
9. What specific actions qualify for promotional or referral credits without creating incentives for spam?
10. Which share settings should be the default: private, unlisted, or public?
11. Should the product support authorized client identities for agencies in a later phase, and what proof-of-consent process would be required?
12. What is the maximum acceptable generation cost per active subscriber and per video job?

______________________________________________________________________

## 19. Launch criteria

The MVP is ready for closed-alpha release when:

- Users can create a secure account and complete explicit identity consent.
- Users can upload, validate, and process a source-photo set.
- Users can create and approve one persistent Identity Profile.
- Users can generate recognizable image outputs using a minimum viable set of worlds/templates.
- Users can view job progress, failed states, generation history, and credit use.
- Users can save, download, and delete generated assets.
- Users can view wallet balance, receive starter credits, and understand credit cost before generation.
- The platform supports basic moderation, reporting, account suspension, asset takedown, and identity deletion.
- Security controls, authorization tests, backup/recovery behavior, and deletion workflows have been validated.
- Generation cost, success rate, image quality, and identity fidelity meet the predefined alpha thresholds.
- Privacy, consent, acceptable-use, retention, and refund policies are complete and visible in product flows.

The critical strategic decision is to make the **Identity Profile** the durable asset—not the prompt, not the individual image, and not the specific generation model. If the identity remains trusted, portable across workflows, visibly consistent, and entirely under user control, the platform can expand from images into video, brand content, entertainment, digital avatars, and creator commerce without losing its central product value.



[^2_1]: https://www.priv.gc.ca/en/privacy-topics/health-information-genetics-biometrics/biometrics/gd_bio_fed-final/

[^2_2]: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/biometric-data-guidance-biometric-recognition/

[^2_3]: https://kpmg.com/us/en/articles/2025/ai-and-privacy-a-look-at-biometric-tech-and-data-reg-alert.html

[^2_4]: https://liminal.co/articles/navigating-biometric-data-regulations/

[^2_5]: https://documentation.identity.entrust.com/guide/onfido-privacy-notices-and-consent

[^2_6]: https://duncancotterill.com/insights/your-face-their-data-who-owns-ai-generated-images-of-you/

[^2_7]: https://www.biometricsinstitute.org/privacy-guidelines-for-the-ai-era/

[^2_8]: https://news.crunchbase.com/ai/personal-identity-legal-fight-solomon-amplify/

[^2_9]: https://www.humanrightsresearch.org/post/the-cost-of-convenience-biometric-data-collection-and-privacy

[^2_10]: https://www.pepelwerk.com/pepelwerk_terms/biometric-data-consent/
