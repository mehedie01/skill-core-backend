-- Seed data for Skill Core Solution

INSERT INTO api_service (title, short_desc, full_desc, icon, features, "order", is_active, created_at) 
VALUES 
('Custom Web Development', 'Fast, secure, and scalable websites.', 'We build modern web applications...', 'code', 'React, Django, PostgreSQL', 1, true, NOW());

INSERT INTO api_project (title, client, category, year, description, tags, image_url, is_featured, "order", is_active, created_at)
VALUES
('Apon Accessories', 'Apon', 'Web Development', '2025', 'Premium e-commerce platform...', 'React, Django', 'https://images.unsplash.com/...', true, 1, true, NOW());