-- Create
--create user hr_user with password 'user1234';

-- Grant
--grant select on public.Employees to hr_user;

-- Grand 2
grant insert, update on public.Employees to hr_user;

-- Проблема с доступом к sequence
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO hr_user;
