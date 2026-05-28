# Macro Tracker MVP 🚀

A high-performance nutritional management dashboard engineered for real-time macronutrient tracking. This application empowers users to maintain their dietary objectives through a streamlined, data-driven interface.

## 🖥️ Product Interface
As seen in **image_ca7b67.png**, the dashboard is designed for high-signal, low-friction user interaction:
*   **Intuitive Meal Logging**: A clean, centralized input control allows for rapid meal selection and submission.
*   **Real-time Analytics**: A visual progress bar provides immediate feedback on daily caloric intake, complemented by high-visibility summary cards for Carbs, Fats, and Proteins.
*   **Structured Consumption Logs**: A dynamic table view enables users to review their historical food entries with clear metric breakdowns.

## 🏗️ Technical Architecture
This project is built using a robust Django MVT (Model-View-Template) architecture, emphasizing efficient data handling and server-side integrity.

*   **Server-Side Rendering (SSR)**: Optimizes initial load times and provides a responsive user experience.
*   **Relational Database Strategy**: Utilizes the Django ORM to maintain strict schema integrity between User accounts, Food catalogs, and Consumption logs.
*   **Client-Side DOM Optimization**: Leverages vanilla JavaScript to compute and display metabolic totals without redundant server overhead.
##project overview :



<img width="1866" height="881" alt="Screenshot 2026-05-28 190553" src="https://github.com/user-attachments/assets/1037a2ec-2576-4c29-b82a-ffa20152f6b6" />


<img width="1700" height="869" alt="image" src="https://github.com/user-attachments/assets/6aa0d42c-9b61-4e90-9262-685d346b78e6" />


## 🛠️ Tech Stack
*   **Backend**: Django (Python)
*   **Frontend**: HTML5, Modern CSS (Flexbox/Grid), Vanilla ES6+ JavaScript
*   **Storage**: SQLite3 (Production-ready for PostgreSQL/MySQL)
*   **Version Control**: Git

## 📈 Roadmap & Scalability
While currently optimized as a high-performance monolithic MVP, the architecture supports seamless evolution:
1.  **Headless API Transition**: Refactoring views into a decoupled Django REST Framework (DRF) engine.
2.  **State Management**: Porting the frontend to React or Vue.js for enhanced interactivity.
3.  **Authentication**: Expanding user-specific dietary profiles and history tracking.

---
*Developed for performance, scalability, and clean nutrition tracking.*
