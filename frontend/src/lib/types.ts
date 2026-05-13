export type Priority = 'low' | 'medium' | 'high' | 'critical';
export type TaskStatus = 'todo' | 'in_progress' | 'blocked' | 'done';

export interface User {
  id: string;
  email: string;
  full_name: string;
  role: 'admin' | 'user';
  created_at: string;
}

export interface Tag {
  id: string;
  name: string;
  color: string;
}

export interface ProjectFolder {
  id: string;
  name: string;
  color: string;
  task_count: number;
}

export interface Task {
  id: string;
  title: string;
  description: string | null;
  status: TaskStatus;
  priority: Priority;
  due_date: string | null;
  tags: Tag[];
  project_folder: ProjectFolder | null;
  owner_id: string;
  parent_id: string | null;
  sub_tasks: Task[];
  archived: boolean;
  created_at: string;
  updated_at: string;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  page_size: number;
  pages: number;
}

export interface AuthTokens {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export interface TaskFilters {
  q?: string;
  status?: TaskStatus;
  priority?: Priority;
  tag_ids?: string[];
  folder_id?: string;
  due_before?: string;
  due_after?: string;
  page?: number;
  page_size?: number;
}
