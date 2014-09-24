json.array!(@users) do |user|
  json.extract! user, :id, :username, :password, :count
  json.url user_url(user, format: :json)
end
